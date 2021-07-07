from rest_framework import serializers

import decimal

import re

import string

# https://gist.github.com/dreispt/024dd11c160af58268e2b44019080bbf#file-validators_pt-py-L128
def _toIntList(numstr, acceptX=0):
	res = []
	for i in numstr:
		if i in string.digits:
			res.append(int(i))
	if acceptX and (numstr[-1] in 'Xx'):
		res.append(10)
	return res

class FieldValidator:

	def date_duration_now(value):
		return datetime.date(datetime.now()) - value

	def date_validator(value, properties):
		if "begin" in properties:
			if value < properties["begin"]:
				raise serializers.ValidationError({"error" : "Date not in range", "detail" : "Begin: {}, Date: {}".format(properties["begin"], value)})
		
		if "end" in properties:
			if end > properties["end"]:
				raise serializers.ValidationError({"error" : "Date not in range", "detail" : "End: {}, Date: {}".format(properties["end"], value)})

		# if "min_duration" in properties:
		# 	if date_duration_now(value) < properties["min_duration"]:
		# 		raise serializers.ValidationError({"error" : "Duration too short", "detail" : "Duration: {}, Date: {}, Min duration: {}".format(date_duration_now(value), value, properties["min_duration"])})

		# if "max_duration" in properties:
		# 	if date_duration_now(value) > properties["max_duration"]:
		# 		raise serializers.ValidationError({"error" : "Duration too long", "detail" : "Duration: {}, Date: {}, Max duration: {}".format(date_duration_now(value), value, properties["max_duration"])})

		return True;

	def date_duration_now(value):
		return datetime.now() - value

	def datetime_validator(value, properties):
		if "begin" in properties:
			if value < properties["begin"]:
				raise serializers.ValidationError({"error" : "Datetime not in range", "detail" : "Begin: {}, Date: {}".format(properties["begin"], value)})
		
		if "end" in properties:
			if value > properties["end"]:
				raise serializers.ValidationError({"error" : "Datetime not in range", "detail" : "End: {}, Date: {}".format(properties["end"], value)})

		# if "min_duration" in properties:
		# 	if datetime_duration_now(value) < properties["min_duration"]:
		# 		raise serializers.ValidationError({"error" : "Duration too short", "detail" : "Duration: {}, Date: {}, Min duration: {}".format(datetime_duration_now(value), value, properties["min_duration"])})

		# if "max_duration" in properties:
		# 	if datetime_duration_now(value) > properties["max_duration"]:
		# 		raise serializers.ValidationError({"error" : "Duration too long", "detail" : "Duration: {}, Date: {}, Max duration: {}".format(datetime_duration_now(value), value, properties["max_duration"])})

		return True;

	def text_validator(value, properties):
		if "min_length" in properties:
			if len(value) < properties["min_length"]:
				raise serializers.ValidationError({"error" : "Answer too short", "detail" : "Min length: {}, Length: {}".format(properties["min_length"], len(value))})
		
		if "max_length" in properties:
			if len(value) > properties["max_length"]:
				raise serializers.ValidationError({"error" : "Answer too long", "detail" : "Max length: {}, Length: {}".format(properties["max_length"], len(value))})

		return True;

	def shorttext_validator(value, properties):
		return FieldValidator.text_validator(value, properties)

	def longtext_validator(value, properties):
		return FieldValidator.text_validator(value, properties)

	def multiplechoice_validator(value, properties):
		if isinstance(value, str):
			if not "allowed_other" in properties or properties["allowed_other"] == False:
				raise serializers.ValidationError({"error" : "\"Other\" option not allowed"})
			FieldValidator.text_validator(value, properties)
		elif not any(option["id"] == value for option in properties['options']):
				raise serializers.ValidationError({"error" : "Invalid option", "detail" : "Answer {} is not an option in {}".format(v, properties["options"])})

		return True;

	def selectboxes_validator(value, properties):
		if "min_selected" in properties:
			if len(value) < properties["min_selected"]:
				raise serializers.ValidationError({"error" : "Not enough options selected", "detail" : "Minimum: {}, Selected: {}".format(properties["min_selected"], len(value))})

		if "max_selected" in properties:
			if len(value) > properties["max_selected"]:
				raise serializers.ValidationError({"error" : "Too many options selected", "detail" : "Maxmium: {}, Selected: {}".format(properties["max_selected"], len(value))})

		if len(value) != len(set(value)):
			raise serializers.ValidationError({"error" : "Repeated values in selection"})

		other_count = 0

		for v in value:
			if isinstance(v, str):
				if not "allowed_other" in properties or properties["allowed_other"] == False:
					raise serializers.ValidationError({"error" : "\"Other\" option not allowed"})
				other_count+=1
				FieldValidator.text_validator(v, properties)
				if "max_other" in properties and other_count > properties["max_other"]:
					raise serializers.ValidationError({"error" : "Too many field with \"Other\" option."})
			elif not any(option["id"] == v for option in properties['options']):
				raise serializers.ValidationError({"error" : "Invalid option", "detail" : "Answer {} is not an option in {}".format(v, properties["options"])})

		return True;

	def number_validator(value, properties):
		if "min" in properties:
			if value < properties["min"]:
				raise serializers.ValidationError({"error" : "Number too small", "detail" : "Minimum: {}, Number: {}".format(properties["min"], value)})

		if "max" in properties:
			if value > properties["max"]:
				raise serializers.ValidationError({"error" : "Number too large", "detail" : "Maximum: {}, Number: {}".format(properties["max"], value)})

		if properties["style"] == "slider":
			if not "min" in properties:
				raise serializers.ValidationError({"error" : "A slider requires a minimum value."})
			if not "max" in properties:
				raise serializers.ValidationError({"error" : "A slider requires a maximum value."})

		if "decimal_places" in properties:
			if -decimal.Decimal(str(value)).as_tuple().exponent > properties["decimal_places"]:
				raise serializers.ValidationError({"error" : "Too many decimal places", "detail" : "Maximum: {}".format(properties["decimal_places"])})

		return True;

	def email_validator(value, properties):
		return re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+$)", value) is True

	def nif_validator(value, properties):
		nif = str(value)
		if len(nif) != 9:
			return False
		if nif[0] not in "125689":
			return False
		num = _toIntList(nif)
		sum = 0
		for pos, dig in enumerate(num[:-1]):
			sum += dig * (9 - pos)

		return (sum % 11 and (11 - sum % 11) % 10) == num[-1]

	def phone_validator(value, properties):
		return re.match("(?:9[1-36][0-9]|2[12][0-9]|2[35][1-689]|24[1-59]|26[1-35689]|27[1-9]|28[1-69]|29[1256]|3[0-9]{2})[0-9]{6}", str(value)) is True
	
	def validateField(value, properties):
		return getattr(FieldValidator, "{}_validator".format(properties["field_type"]))(value, properties)