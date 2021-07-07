from cerberus import Validator

class FormsValidator(Validator):
	def _validate_greater_than_equal(self, other, field, value):

		"{'type': 'string'}"
		if other not in self.document:
			return True
		if value < self.document[other]:
			self._error(field, "Value is lesser than %s." % other)

	def _validate_bounds(self, other, field, value):

		"{'type': 'string'}"
		if self.document['field_type'] == 'multiplechoice' or self.document['field_type'] == 'selectboxes':
			if isinstance(value, list):
				for v in value:
					if v >= len(self.document[other]):
						self._error(field, "Value out of bounds. (%s)" % other)
			else:
				if value >= len(self.document[other]):
					self._error(field, "Value out of bounds. (%s)" % other)
		return False