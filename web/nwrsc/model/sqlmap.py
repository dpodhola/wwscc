### AUTOGENERATED CODE, DO NOT MODIFY ###
sqlmap = {
'DELETECAR':'delete from cars where id=:h1',
'DELETECLASSGROUPMAPPING':'delete from rungroups where eventid=:h1',
'DELETECLASSRESULTS':'delete from eventresults where classcode=:h1 and eventid=:h2',
'DELETEDRIVER':'delete from drivers where id=:h1',
'DELETERUN':'delete from runs where id=:h1',
'DELETERUNORDER':'delete from runorder where eventid=:h1 and course=:h2 and rungroup=:h3',
'DELETERUNSBYCOURSE':'delete from runs where carid=:h1 AND course=:h2 AND eventid=:h3',
'GETALLCARS':'select * from cars',
'GETALLDRIVERS':'select * from drivers',
'GETALLRUNS':'select * from runs',
'GETCARIDSBYCHALLENGE':'select car1id,car2id from challengerounds where challengeid=:h1',
'GETCARIDSFORCOURSE':'select carid from runorder where eventid=:h1 AND course=:h2',
'GETCARIDSFORGROUP':'select carid from runorder where eventid=:h1 AND course=:h2 AND rungroup=:h3 order by row',
'GETCHALLENGESFOREVENT':'select * from challenges where eventid = :h1',
'GETCHANGES':'select * from changes',
'GETCLASSES':'select * from classlist',
'GETCLASSRESULTS':'select r.carid as carid,SUM(r.net) as sum, COUNT(r.net) as coursecnt from runs as r, cars as c where r.norder=1 and r.carid=c.id and c.classcode=:h1 and r.eventid=:h2 group by r.carid order by coursecnt DESC,sum',
'GETDIALINS':'select d.firstname as firstname, d.lastname as lastname, c.classcode as classcode, c.indexcode as indexcode, c.id as carid, SUM(r.raw) as myraw, f.position as position, f.sum as mynet from runs as r, cars as c, drivers as d, eventresults as f where r.carid=c.id and c.driverid=d.id and r.eventid=:h1 and r.rorder=1 and f.eventid=:h2 and f.carid=c.id group by d.id order by position',
'GETDRIVERSBY':'select * from drivers where firstname like :h1 and lastname like :h2 order by firstname,lastname',
'GETDRIVERSBYFIRST':'select * from drivers where firstname like :h1 order by firstname,lastname',
'GETDRIVERSBYLAST':'select * from drivers where lastname like :h1 order by firstname,lastname',
'GETEVENTENTRANTS':'select distinct d.firstname as firstname,d.lastname as lastname,c.* from runs as r, cars as c, drivers as d where r.carid=c.id AND c.driverid=d.id and r.eventid=:h1',
'GETEVENTRESULTSBYCLASS':'select d.firstname,d.lastname,r.position,r.courses,r.sum,r.diff,r.points,r.ppoints,r.updated from eventresults as r, cars as c, drivers as d where r.carid=c.id and c.driverid=d.id and r.classcode=:h1 and r.eventid=:h2 order by position',
'GETEVENTS':'select * from events order by date',
'GETINDEXES':'select * from indexlist',
'GETREGISTEREDENTRANTS':'select distinct d.firstname as firstname,d.lastname as lastname,c.* from registered as x, cars as c, drivers as d where x.carid=c.id AND c.driverid=d.id and x.eventid=:h1',
'GETROUNDSFORCHALLENGE':'select * from challengerounds where challengeid=:h1',
'GETRUNCOUNT':'select count(run) as count from runs where carid=:h1 and eventid=:h2 and course=:h3',
'GETRUNGROUPMAPPING':'select classcode from rungroups where eventid=:h1 and rungroup=:h2 order by gorder',
'GETRUNORDERENTRANTS':'select d.firstname,d.lastname,c.* from runorder as r, cars as c, drivers as d where r.carid=c.id AND c.driverid=d.id and r.eventid=:h1 AND r.course=:h2 AND r.rungroup=:h3 order by r.row',
'GETRUNORDERROWS':'select row from runorder where eventid=:h1 AND course=:h2 AND carid=:h3',
'GETRUNSBYCARID':'select * from runs where carid=:h1 and eventid=:h2 and course=:h3',
'GETRUNSBYGROUP':'select * from runs where eventid=:h1 and course=:h2 and carid in (select carid from runorder where eventid=:h3 AND course=:h4 AND rungroup=:h5)',
'GETRUNSFORCHALLENGE':'select * from runs where (eventid>>16)=:h1',
'GETSETTING':'select val from settings where name=:h1',
'GETUPDATED':'select carid, updated from eventresults where classcode=:h1 and eventid=:h2',
'INSERTBLANKCHALLENGEROUND':'insert into challengerounds (challengeid,round,swappedstart,car1id,car2id) values (:h1,:h2,:h3,:h4,:h5)',
'INSERTCAR':'insert or ignore into cars (driverid,year,make,model,color,number,classcode,indexcode) values (:h1,:h2,:h3,:h4,:h5,:h6,:h7,:h8)',
'INSERTCHALLENGE':'insert into challenges (eventid, name, depth, bonus) values (:h1,:h2,:h3,:h4)',
'INSERTCLASSGROUPMAPPING':'insert into rungroups (eventid, classcode, rungroup) values (:h1,:h2,:h3)',
'INSERTCLASSRESULTS':'insert into eventresults VALUES (NULL, :h1,:h2,:h3,:h4,:h5,:h6,:h7,:h8,:h9,:h10)',
'INSERTDRIVER':'insert or ignore into drivers (firstname,lastname,email,address,city,state,zip,homephone,workphone,clubs,brag,sponsor,membership) values (:h1,:h2,:h3,:h4,:h5,:h6,:h7,:h8,:h9,:h10,:h11,:h12,:h13)',
'INSERTRUN':'insert into runs (carid,eventid,course,run,cones,gates,status,rorder,norder,brorder,bnorder,reaction,sixty,seg1,seg2,seg3,seg4,seg5,raw,net) values (:h1,:h2,:h3,:h4,:h5,:h6,:h7,:h8,:h9,:h10,:h11,:h12,:h13,:h14,:h15,:h16,:h17,:h18,:h19,:h20)',
'INSERTRUNORDER':'insert into runorder values (NULL, :h1,:h2,:h3,:h4,:h5)',
'ISREGISTERED':'select id from registered where carid=:h1 and eventid=:h2',
'LOADDRIVERCARS':'select * from cars where driverid = :h1 order by classcode, number',
'LOADENTRANT':'select d.firstname,d.lastname,c.* from cars as c, drivers as d where c.driverid=d.id and c.id=:h1',
'LOADRUNORDER':'select carid from runorder where eventid=:h1 and course=:h2 and rungroup=:h3 order by row',
'REGISTERCAR':'insert or ignore into registered (eventid, carid) values (:h1,:h2)',
'SWAPRUNORDER':'update runorder set carid=:h1 where eventid=:h2 and course=:h3 and rungroup=:h4 and carid=:h5',
'SWAPRUNS':'update runs set carid=:h1 where eventid=:h2 and course=:h3 and carid=:h4',
'TRACK':'insert into changes (type, args) values (:h1,:h2)',
'TRACKCLEAR':'delete from changes',
'UNREGISTERCAR':'delete from registered where eventid=:h1 and carid=:h2',
'UPDATECAR':'update cars set driverid=:h1,year=:h2,make=:h3,model=:h4,color=:h5,number=:h6,classcode=:h7,indexcode=:h8 where id=:h9',
'UPDATECHALLENGEROUND':'update challengerounds set challengeid=:h1,round=:h2,swappedstart=:h3,car1id=:h4,car1dial=:h5,car1result=:h6,car1newdial=:h7,car2id=:h8,car2dial=:h9,car2result=:h10,car2newdial=:h11 where id=:h12',
'UPDATEDRIVER':'update drivers set firstname=:h1,lastname=:h2,email=:h3,address=:h4,city=:h5,state=:h6,zip=:h7,homephone=:h8,workphone=:h9,clubs=:h10,brag=:h11,sponsor=:h12,membership=:h13 where id=:h14',
'UPDATEEVENTS':'update events set ispro=:h1,courses=:h2,runs=:h3,countedruns=:h4,conepen=:h5,gatepen=:h6,segments=:h7,password=:h8,name=:h9,date=:h10,location=:h11,sponsor=:h12,host=:h13,designer=:h14,regopened=:h15,regclosed=:h16,perlimit=:h17,totlimit=:h18,cost=:h19,paypal=:h20,snail=:h21,notes=:h22 where id=:h23',
'UPDATERUN':'update runs set carid=:h1,eventid=:h2,course=:h3,run=:h4,cones=:h5,gates=:h6,status=:h7,rorder=:h8,norder=:h9,brorder=:h10,bnorder=:h11,reaction=:h12,sixty=:h13,seg1=:h14,seg2=:h15,seg3=:h16,seg4=:h17,seg5=:h18,raw=:h19,net=:h20 where id=:h21',
}
