from FileLoader import FileLoader as fl

df = fl.load("athlete_events.csv")
fl.display(df, 5)
