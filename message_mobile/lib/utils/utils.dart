import 'package:message_mobile/models/signInPageModel.dart';

List<Map<String, dynamic>> getSchema(LoginPageSelection selection) {
  switch (selection) {
    case LoginPageSelection.signUp:
      return [
        {
          "label": "User Name",
          "readonly": false,
          "extra": {},
          "name": "userName",
          "widget": "text",
          "required": true,
          "translated": false,
          "validations": {}
        },
        {
          "label": "Password",
          "readonly": false,
          "extra": {"help": "Please Enter your password", "default": ""},
          "name": "password",
          "widget": "text",
          "required": true,
          "translated": false,
          "validations": {
            "length": {"maximum": 1024}
          }
        },
        {
          "label": "sex",
          "readonly": false,
          "extra": {
            "choices": [
              {"label": "Male", "value": "male"},
              {"label": "Female", "value": "female"},
            ],
            "default": "male"
          },
          "name": "sex",
          "widget": "select",
          "required": false,
          "translated": false,
          "validations": {}
        },
        {
          "label": "Birthday",
          "readonly": false,
          "extra": {"help": "Please enter your birthday"},
          "name": "dateOfBirth",
          "widget": "datetime",
          "required": true,
          "translated": false,
          "validations": {}
        },
      ];

    case LoginPageSelection.login:
      return [
        {
          "label": "User Name",
          "readonly": false,
          "extra": {},
          "name": "userName",
          "widget": "text",
          "required": true,
          "translated": false,
          "validations": {}
        },
        {
          "label": "Password",
          "readonly": false,
          "extra": {"help": "Please Enter your password", "default": ""},
          "name": "password",
          "widget": "text",
          "required": true,
          "translated": false,
          "validations": {
            "length": {"maximum": 1024}
          }
        },
      ];
      break;
    case LoginPageSelection.setting:
      return [
        {
          "label": "ID",
          "readonly": true,
          "extra": {},
          "name": "id",
          "widget": "number",
          "required": false,
          "translated": false,
          "validations": {}
        },
        {
          "label": "Item Name",
          "readonly": false,
          "extra": {"help": "Please Enter your item name", "default": ""},
          "name": "name",
          "widget": "text",
          "required": true,
          "translated": false,
          "validations": {
            "length": {"maximum": 1024}
          }
        }
      ];
  }
}