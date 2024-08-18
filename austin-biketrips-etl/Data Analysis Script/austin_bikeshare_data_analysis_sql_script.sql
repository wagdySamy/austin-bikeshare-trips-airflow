--1. Find the total number of trips for each day.
SELECT
  day_partition AS trip_day
  , COUNT(day_partition) AS total_trips
FROM de-project-432716.general_dataset.ext_bikeshare_trips
GROUP BY day_partition;


--2. Calculate the average trip duration for each day.
SELECT
  day_partition AS trip_day
  , AVG(duration_minutes) AS avg_trips_duration
FROM de-project-432716.general_dataset.ext_bikeshare_trips
GROUP BY day_partition;


--3. Identify the top 5 stations with the highest number of trip starts.
WITH cte_data AS (
  SELECT
    start_station_name
    , COUNT(start_station_name) total_trips
  FROM de-project-432716.general_dataset.ext_bikeshare_trips
  GROUP BY start_station_name
)
SELECT start_station_name
FROM cte_data
ORDER BY total_trips DESC
LIMIT 5;


--4. Find the average number of trips per hour of the day.
SELECT
  hour_partition AS trip_hour
  , COUNT(trip_id) / COUNT(DISTINCT day_partition) AS avg_trips_number
FROM de-project-432716.general_dataset.ext_bikeshare_trips
GROUP BY hour_partition
ORDER BY 1;


--5. Determine the most common trip route (start station to end station).
SELECT
  start_station_name
  , end_station_name
  , COUNT(trip_id) trips_count
FROM de-project-432716.general_dataset.ext_bikeshare_trips
WHERE start_station_name <> end_station_name
GROUP BY start_station_name, end_station_name
ORDER BY trips_count desc
LIMIT 10;


--6. Calculate the number of trips each month.
SELECT EXTRACT(month FROM day_partition) month
  , COUNT(trip_id)
FROM de-project-432716.general_dataset.ext_bikeshare_trips
GROUP BY EXTRACT(month FROM day_partition);


--7. Find the station with the longest average trip duration.
SELECT
  start_station_name
  , AVG(duration_minutes) avg_trips_duration
FROM de-project-432716.general_dataset.ext_bikeshare_trips
GROUP BY start_station_name
ORDER BY avg_trips_duration DESC
LIMIT 1;


--8. Find the busiest hour of the day (most trips started).
SELECT
  hour_partition
  , COUNT(trip_id) trips_count
FROM de-project-432716.general_dataset.ext_bikeshare_trips
GROUP BY hour_partition
ORDER BY trips_count DESC
LIMIT 1;


--9. Identify the day with the highest number of trips.
SELECT
  day_partition trip_day
  , COUNT(trip_id) total_trips
FROM de-project-432716.general_dataset.ext_bikeshare_trips
GROUP BY day_partition
ORDER BY total_trips DESC
LIMIT 1;

