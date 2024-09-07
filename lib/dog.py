from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)


def save(session, dog):
    session.add(dog)
    session.commit()
    pass

def get_all(session):
    dogs = session.query(Dog).all()
    return dogs

def find_by_name(session, name):
    dog_name = session.query(Dog).filter(Dog.name == name).first()
    return dog_name

def find_by_id(session, id):
    dog_id = session.query(Dog).filter(Dog.id == id).first()
    return dog_id

def find_by_name_and_breed(session, name, breed):
    dog_name_and_breed = session.query(Dog).filter((Dog.name == name),(Dog.breed == breed)).first()
    return dog_name_and_breed

def update_breed(session, dog, breed):
    # Find the specific Dog table in the database
    
    dog_updates = session.query(Dog).filter(Dog.id == dog.id).first()
    
    if dog_updates:
        # Update the breed
        dog_updates.breed = breed
        # Commit the changes
        session.commit()
    else:
        print(f"No dog found with id {dog.id}")
