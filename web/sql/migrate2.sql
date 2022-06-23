CREATE TABLE "bus" (
  "bus_id" TEXT PRIMARY KEY,
  "number" INT
);

CREATE INDEX "UQBUS" ON  "bus" ("number");

CREATE TABLE "stop" (
  "stop_id" INTEGER PRIMARY KEY,
  "name" VARCHAR(32)
);

CREATE INDEX "UQSTOP" ON  "stop" ("name");

CREATE TABLE "bus_stop" (
  "bus_stop_id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "bus_id" TEXT,
  "stop_id" INT,
  CONSTRAINT "FK_bus_stop.bus_id"
    FOREIGN KEY ("bus_id")
      REFERENCES "bus"("bus_id"),
  CONSTRAINT "FK_bus_stop.stop_id"
    FOREIGN KEY ("stop_id")
      REFERENCES "stop"("stop_id")
);

CREATE TABLE "arriving_time" (
  "bus_stop_id" INT,
  "is_weekday" BOOL,
  "arriving_time" INT,
  PRIMARY KEY ("bus_stop_id", "is_weekday", "arriving_time"),
  CONSTRAINT "FK_arriving_time.bus_stop_id"
    FOREIGN KEY ("bus_stop_id")
      REFERENCES "bus_stop"("bus_stop_id")
);

CREATE TABLE "route" (
  "route_id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "departure_stop_id" INT,
  "arrival_stop_id" INT,
  CONSTRAINT "FK_route.arrival_stop_id"
    FOREIGN KEY ("arrival_stop_id")
      REFERENCES "stop"("stop_id"),
  CONSTRAINT "FK_route.departure_stop_id"
    FOREIGN KEY ("departure_stop_id")
      REFERENCES "stop"("stop_id")
);

CREATE TABLE "user_route" (
  "user_id" INT,
  "route_id" INT,
  "name" VARCHAR(32),
  PRIMARY KEY ("user_id", "route_id"),
  CONSTRAINT "FK_user_route.user_id"
    FOREIGN KEY ("user_id")
      REFERENCES "user"("user_id"),
  CONSTRAINT "FK_user_route.route_id"
    FOREIGN KEY ("route_id")
      REFERENCES "route"("route_id")
);
