CREATE DATABASE name;

CREATE TABLE crime_scene_report (
date int,
type text,
description text,
city text
);

CREATE TABLE drivers_licence (
date int,
type text,
description text,
city text
);

SELECT name 
  FROM sqlite_master
 where type = 'table'