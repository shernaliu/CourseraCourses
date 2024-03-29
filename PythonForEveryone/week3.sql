CREATE TABLE "Artist" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "Genre" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "Album" (
	"id"	INTEGER NOT NULL UNIQUE,
	"artist_id"	INTEGER,
	"title"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "Track" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT,
	"album_id"	INTEGER,
	"genre_id"	INTEGER,
	"len"	INTEGER,
	"rating"	INTEGER,
	"count"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);

insert into Artist (name) values ('Led Zepplin');
insert into Artist (name) values ('AC/DC');

insert into Genre (name) values ('Rock');
insert into Genre(name) values ('Metal');

insert into Album (title, artist_id) values ('Who Made Who', 2);
insert into Album (title, artist_id) values ('IV', 1);

insert into Track(title, rating, len, count, album_id, genre_id)
values ('Black Dog', 5, 297, 0, 2, 1);

insert into Track(title, rating, len, count, album_id, genre_id)
values ('Stairway', 5, 482, 0, 2, 1);

insert into Track(title, rating, len, count, album_id, genre_id)
values ('About To Rock', 5, 313, 0, 1, 2);

insert into Track(title, rating, len, count, album_id, genre_id)
values ('Who Made Who', 5, 207, 0, 2, 1);

select Album.title, Artist.name 
from Album join Artist on Album.artist_id = artist_id;

select Track.title, Genre.name
from Track join Genre on Track.genre_id = Genre.id;

select Track.title, Genre.name
from Track join Genre;

select Track.title, Artist.name, Album.title, Genre.name
from Track join Genre join Album join Artist
on 
Track.genre_id = Genre.id and 
Track.album_id = Album.id and
Album.artist_id = Artist.id;