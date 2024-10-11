from models import QA, db

def add_question_answer(question, answer):
    try:
        new_qa = QA(question=question, answer=answer)
        db.session.add(new_qa)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {e}")