from strava_controller import StravaController

def main():
    print("Starting strava-auto-kudos...")
    sc = StravaController()
    sc.give_kudos_by_activity_id(activity_id=10534438994)
    sc.driver.close()

if __name__ == "__main__":
    main()
    