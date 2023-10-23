import json

class Education:
    # Constructor (w/ default values)
    def __init__(
        self,
        school_name: str = "UNDEFINED",
        degree: str = "UNDEFINED",
        years_attended: str = "UNDEFINED",
    ):
        self.school_name = school_name
        self.degree = degree
        self.years_attended = years_attended

    # Copy values from another Education instance
    def copyValues(self, otherEducation):
        self.school_name = otherEducation.school_name
        self.degree = otherEducation.degree
        self.years_attended = otherEducation.years_attended

    # Convert to string
    def __str__(self):
        return json.dumps(self.toDict(), indent=4)

    # Check equality
    def __eq__(self, otherEducation) -> bool:
        if not isinstance(otherEducation, Education):
            return False
        else:
            return self.degree == otherEducation.degree

    # Convert to dictionary
    def toDict(self):
        return {
            "school_name": self.school_name,
            "degree": self.degree,
            "years_attended": self.years_attended,
        }

    # Convert dictionary to Education object
    @classmethod
    def dictToEducation(cls, userEducation):
        return cls(
            school_name=userEducation.get("school_name", "UNDEFINED"),
            degree=userEducation.get("degree", "UNDEFINED"),
            years_attended=userEducation.get("years_attended", "UNDEFINED"),
        )

    # Update methods
    def update_school_name(self, new_school_name):
        self.school_name = new_school_name

    def update_degree(self, new_degree):
        self.degree = new_degree

    def update_years_attended(self, new_years_attended):
        self.years_attended = new_years_attended
