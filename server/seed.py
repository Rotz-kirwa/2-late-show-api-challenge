from server.app import app
from server.models import db, Guest, Episode, Appearance
from faker import Faker
from random import choice
from datetime import date

print("🌱 Seeding data...")

with app.app_context():
    # Clear existing data
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()

    # Create a Faker instance
    faker = Faker()

    # Create episodes
    episodes = []
    for i in range(10):
        ep = Episode(
            date=faker.date_between(start_date='-1y', end_date='today'),
            number=i + 1
        )
        episodes.append(ep)
        db.session.add(ep)

    # Create guests
    guests = []
    for i in range(5):
        guest = Guest(
            name=faker.name(),
            occupation=faker.job(),
            email=faker.unique.email()
        )
        guests.append(guest)
        db.session.add(guest)

    db.session.commit()  # Commit episodes and guests before creating appearances

    # Re-query episodes and guests to ensure they have IDs
    episodes = Episode.query.all()
    guests = Guest.query.all()

    # Create appearances
    for guest in guests:
        for _ in range(2):
            episode = choice(episodes)
            appearance = Appearance(
                rating=choice([1, 2, 3, 4, 5]),
                episode_id=episode.id,
                guest_id=guest.id
            )
            db.session.add(appearance)

    db.session.commit()

print("✅ Done seeding!")
