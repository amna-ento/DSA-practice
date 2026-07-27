class Candidate:

    def __init__(
        self,
        candidate_id,
        name,
        degree,
        experience,
        technical_score,
        communication_score,
        projects,
        background_verified,
    ):

        self.candidate_id = candidate_id
        self.name = name
        self.degree = degree
        self.experience = experience
        self.technical_score = technical_score
        self.communication_score = communication_score
        self.projects = projects
        self.background_verified = background_verified

       
        self.status = "Not Evaluated"
        self.decision_path = []

    def __str__(self):
        return f"{self.candidate_id} | {self.name} | {self.status}"


class DecisionNode:

    def __init__(
        self,
        question=None,
        attribute=None,
        operator=None,
        value=None,
        decision=None
    ):

        self.question = question

        
        self.attribute = attribute

       
        self.operator = operator


        self.value = value


        self.yes = None
        self.no = None

       
        self.decision = decision   



experience = DecisionNode(
    question="Experience >= 3 Years?",
    attribute="experience",
    operator=">=",
    value=3
)

class DecisionTree:

    def __init__(self):
        self.root = None

    def compare(self, candidate_value, operator, required_value):

        if operator == "==":
            return candidate_value == required_value

        elif operator == "!=":
            return candidate_value != required_value

        elif operator == ">":
            return candidate_value > required_value

        elif operator == "<":
            return candidate_value < required_value

        elif operator == ">=":
            return candidate_value >= required_value

        elif operator == "<=":
            return candidate_value <= required_value

        else:
            raise ValueError("Invalid Operator")

    def evaluate(self, candidate):

        current = self.root

        # Clear previous evaluation path
        candidate.decision_path = []

        # Traverse until a leaf node is reached
        while current.decision is None:

            # Get candidate attribute dynamically
            candidate_value = getattr(
                candidate,
                current.attribute
            )

            # Compare candidate value with rule
            result = self.compare(
                candidate_value,
                current.operator,
                current.value
            )

          

            if result:

                candidate.decision_path.append(
                    f"✔ {current.question}"
                )

                current = current.yes

            else:

                candidate.decision_path.append(
                    f"✖ {current.question}"
                )

                current = current.no

      

        candidate.status = current.decision

        candidate.decision_path.append(
            f"FINAL DECISION : {current.decision}"
        )

        return current.decision


def build_recruitment_tree():

   
    hire = DecisionNode(decision="HIRE")
    reject = DecisionNode(decision="REJECT")

   

    background = DecisionNode(
        question="Background Verified?",
        attribute="background_verified",
        operator="==",
        value=True
    )

    projects = DecisionNode(
        question="Projects >= 5?",
        attribute="projects",
        operator=">=",
        value=5
    )

    communication = DecisionNode(
        question="Communication Score >= 70?",
        attribute="communication_score",
        operator=">=",
        value=70
    )

    technical = DecisionNode(
        question="Technical Score >= 80?",
        attribute="technical_score",
        operator=">=",
        value=80
    )

    experience = DecisionNode(
        question="Experience >= 3 Years?",
        attribute="experience",
        operator=">=",
        value=3
    )

    degree = DecisionNode(
        question="Has Bachelor's Degree?",
        attribute="degree",
        operator="==",
        value=True
    )



    degree.yes = experience
    degree.no = reject

    experience.yes = technical
    experience.no = reject

    technical.yes = communication
    technical.no = reject

    communication.yes = projects
    communication.no = reject

    projects.yes = background
    projects.no = reject

    background.yes = hire
    background.no = reject

   

    tree = DecisionTree()
    tree.root = degree

    return tree




tree = build_recruitment_tree()



print("=" * 50)
print("Recruitment Decision System")
print("=" * 50)

candidate_id = int(input("Enter Candidate ID: "))
name = input("Enter Candidate Name: ")

degree = input("Has Bachelor's Degree? (yes/no): ").lower() == "yes"

experience = int(input("Years of Experience: "))

technical_score = int(input("Technical Score: "))

communication_score = int(input("Communication Score: "))

projects = int(input("Number of Projects: "))

background_verified = (
    input("Background Verified? (yes/no): ").lower() == "yes"
)





candidate = Candidate(
    candidate_id,
    name,
    degree,
    experience,
    technical_score,
    communication_score,
    projects,
    background_verified
)

tree.evaluate(candidate)

print("\n" + "=" * 50)
print(f"Candidate ID : {candidate.candidate_id}")
print(f"Name         : {candidate.name}")
print(f"Status       : {candidate.status}")

print("\nDecision Path")

for step in candidate.decision_path:
    print(step)

print("=" * 50)

