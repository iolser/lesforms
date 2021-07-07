from forms.schema.FormsFields import field_schemas

schema = {
	'hide_section_numbers' : {'type' : 'boolean', 'default' : False},
	'hide_question_numbers' : {'type' : 'boolean', 'default' : False},
	'hidden_elements' : {'type' : 'dict', 'keysrules': {'type': 'string'}, 'valuesrules' : {'type' : 'boolean'}},
	'sections' : {
		'type' : 'list',
		'required' : True,
		'schema' : {
			'type' : 'dict',
			'required' : True,
			'schema' : {
				'id' : {
					'type' : 'integer',
					'required' : True
				},
				'section_name' : {
					'type' : 'string',
					'required' : True
				},
				"depends_on" : {
					'type' : 'dict', 
					'schema' : {
						'section' : {'type' : 'integer', 'required' : True},
						'question' : {'type' : 'integer', 'required' : True}
					}
				},
				'hidden_elements' : {'type' : 'dict', 'keysrules': {'type': 'string'}, 'valuesrules' : {'type' : 'boolean'}},
				'hide_question_numbers' : {'type' : 'boolean', 'default' : False},
				'questions' : {
					'type' : 'list',
					'required' : True,
					'schema' : {
						'type' : 'dict',
						'schema' : {
							'id' : {
								'type' : 'integer',
								'required' : True
							},
							'question' : {
								'type' : 'string', 
								'maxlength' : 1024, 
								'required' : True
							},
							'required' : {
								'type' : 'boolean',
								'default' : False
							},
							'properties' : {
								'type' : 'dict',
								'required' : True,
								'anyof_schema' : field_schemas
							},
							"depends_on" : {
								'type' : 'dict', 
								'schema' : {
									'section' : {'type' : 'integer', 'required' : True},
									'question' : {'type' : 'integer', 'required' : True}
								}
							}
						}
					}
				}
			}
		}
	}
}