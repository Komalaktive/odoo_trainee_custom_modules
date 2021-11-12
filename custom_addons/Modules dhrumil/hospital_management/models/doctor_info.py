from odoo import api, fields, models


class DoctorInfo(models.Model):
    _name = "doctor.info"
    _description = "Doctor Information"

    name = fields.Char(string="Name")
    specialist = fields.Char(string="Specialist")
    email = fields.Char(string="Email")

    patient_ids = fields.One2many("patient.info", "doctor_select")

    # def action_patient(self):
    #     print("\n\n\n0,0 work\n\n\n")
    #     self.create({"name": "Naresh", "patient_ids": [
    #             (0, 0, {"name": "Jeet", "problem": "xyz"}),
    #             (0, 0, {"name": "Vedant", "problem": "abc"})
    #             ]})

    """Special Command Button Action"""

    def special_command_action(self):

        """Below code is used for (0,0,vals), that create records"""

        # self.write({"patient_ids": [
        #         (0, 0, {"name": "Jeet", "problem": "xyz"}),
        #         (0, 0, {"name": "Vedant", "problem": "abc"})
        #         ]})

        """Below code is used for (1,id,vals), that update existing record"""

        # vals = {"patient_ids": []}
        # for patient in self.patient_ids:
        #     vals["patient_ids"].append([1, patient.id, {'problem': 'born injury'}])
        # self.write(vals)

        """Below code is used for (2,id,vals), that hard delete records of given id"""

        # self.write({"patient_ids": [(2, 4, 0), (2, 13, 0)]})

        """Below code is used for (3,id,vals), that soft delete in profile but record is
            available in database. In this odoo remove doctor field from this patient and 
            set as a none.
        """

        # self.write({"patient_ids": [(3, 15, False), (3, 17, False)]})

        """Below code is used for (4,id,0), that retrived soft deleted records"""

        # self.write({"patient_ids": [(4, 15, 0), (4, 17, 0)]})

        """Below code is used for (5,0,0), that soft deleted all records present in self profile"""

        # self.write({"patient_ids": [(5, 0, 0)]})
