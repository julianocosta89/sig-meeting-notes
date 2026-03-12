SIG: Browser SIG
Date: 2025-07-10
Duration: 39 minutes
============================================================

## Zoom Recording Transcript

**Jared Freeze (embrace)** 00:18 It does.
**Ted Young** 00:19 Hey? How's it going? Jared?
**Jared Freeze (embrace)** 00:21 Good! How are you?
**Ted Young** 00:23 Doing? Well, yeah, funny, you know, it was like a big holiday weekend last week. But it's like.
you know, whatever generates work in my life, was not aware that there were fewer days in the week.
**Jared Freeze (embrace)** 00:41 Yeah, right?
Yeah. Our our company is split up in Canada and Argentina as well. And it's just been like we have. We haven't really had like 5 days in a row where, like everyone's there, you know.
**Ted Young** 00:54 Yeah, yeah.
that's cool. You have people in Argentina, though.
**Jared Freeze (embrace)** 01:07 Yeah, it's great. Actually, Joaquin, who I so I just got here. I think I slacked you that I've been embraced like 3 weeks. But yeah, he's been coming to Node and Javascript stuff for a while. So with Hanson, just I guess he's moving more back end from the SDK, and I'm working on the SDK with one other person. So yeah, we're running the the web stuff.
**Ted Young** 01:33 Nice.
**Jared Freeze (embrace)** 01:34 But yeah, he's like half of our team's Argentina. That's what I was trying to say.
**Ted Young** 01:40 Cool.
**Jared Freeze (embrace)** 01:41 Yeah.
**Ted Young** 02:52 And so Martin just started at Grafana Labs, and I think he has an in-person onboarding this week, so I don't think he'll be able to join us.
but he was doing some great work.
So if he's not here, I'll I'll try to lead us through the doc that he posted.
and after that we can jump into some having a look at some of the project management stuff I've been putting together to help kind of figure out how to keep us organized.
but I think we've got a good mix of people so we could just go ahead and kick it off. Since we have a 30 min meeting.
Dan, do you wanna kick us off.
**Daniel Dyla (Dynatrace)** 04:13 Yeah, sure. So, I added, I think the 1st 2 topics here. They're both kind of questions for the group. During our issue triage in the regular Js meeting.
There. There's a few instrumentations in Js Contrib which are browser related that are.
I mean, unmaintained, is probably the accurate term for them. But people create issues and Prs on them. We never know how to handle them exactly, because there's no semantic convention around them, but they are in use, so we don't want them to be completely forgotten.
And I guess my question for this group is, what do we wanna do about those?
Should we continue to just main like half maintain them the way we are now? Should we deprecate them and say like something better is coming in the future, which would probably not mean like completely removing them and deleting them. But it would mean closing all of these issues and Prs saying like this is not the way forward. Something new is coming.
or should we do something else?
**Ted Young** 05:29 So my suggestion is that we carry on half maintaining them until we've reached a point that we're actually released. All of the the new Api, or whatever new structure for all of our browser stuff. At which point, we update these to use the new stuff we have to figure out. You know, what is the set of like core instrumentation? That kind of we as a Sig want to maintain like, what's the minimal set of stuff hotel has to provide to have a good browser experience, and that includes some libraries. But I think it might be fair to say, I don't think there's so many things already in contrib that just to say, like whatever we already offered the community we're going to continue to support. So there's in some scenario where we roll out all this new stuff. But you have people gated on the old way of doing things because we haven't updated some instrumentation. They're depending on.
**Daniel Dyla (Dynatrace)** 06:37 Yeah, okay, I guess that's fine. I just wanted to call it out here.
**Ted Young** 06:43 Yeah, I do think it's okay to have like breaking changes in the semantics and everything else. When we bump those things up. Also, I think it's a big enough.
**Daniel Dyla (Dynatrace)** 06:52 It's gonna have to be okay.
**Ted Young** 06:54 Right? Yeah, I just want to clarify that.
**Daniel Dyla (Dynatrace)** 06:57 Locations.
**Ted Young** 06:58 Yeah, that we aren't. We aren't, you know, gonna.
**Daniel Dyla (Dynatrace)** 07:02 This does not include, like the Xhr and fetch instrumentations which right now we're just using, like the Http semantic convention, which I assume will continue to be the case. But it's more about like user interaction type stuff.
And all of these instrumentations.
We're essentially written by one person a long time ago without very much outside input.
**Ted Young** 07:29 But but even those Xhr instrumentations, are they using the new stable and breaking Http conventions, or are they unmaintained enough that they're still using the old unstable Http. Conventions.
**Daniel Dyla (Dynatrace)** 07:47 I think they're currently duplicate emitting. Maybe they're using the old stuff.
**Trent Mick** 07:53 So we added the opt in support only recently to those ones.
**Daniel Dyla (Dynatrace)** 07:58 Yeah.
**Ted Young** 07:59 Great.
**Trent Mick** 07:59 So we're in the 6 month window right now.
**Ted Young** 08:02 Nice. Okay.
Good.
**Daniel Dyla (Dynatrace)** 08:10 Okay. The next item that I had here is just to we had a change proposed in the Js SDK, which affects the way that bundlers interpret the package. Jason And I am not a bundler ex like a bundling expert, and neither are any of the other Js Maintainers, really. So we hope that maybe somebody in this group could take a look at this Pr and let us know what they think.
because I don't fully I. I'm not confident that I fully understand the implications of this Pr. Even though it's only like 3 lines.
**Jared Freeze (embrace)** 08:55 I can do that. I have a lot of experience with bundling, so.
**Daniel Dyla (Dynatrace)** 09:01 I appreciate that.
Thank you.
**Jared Freeze (embrace)** 09:03 Yep.
**Daniel Dyla (Dynatrace)** 09:11 Alright! That's it for me.
**Ted Young** 09:13 Yeah, nice.
Okay. So next up, think I can share my screen here.
Sec.
so Martin did a great job creating just sort of a rough draft of our data model. It seems like part of you know what we're trying to do at this, you know. Very early phase of the Sig is, you know, go get a little more fine grained from our initial proposal of what the areas of work are that we want to focus on 1st to like actually breaking that down. Enough that we have a model of like what complete this would look like. And once we're agreed on that, we can start kind of like forking things off into like tasks or some kind of like, you know, roadmap for how we're gonna tackle everything.
And Martin did a great job of creating just a 1st pass at like what that data model like look like look like for the browser. Everything we need to cover.
I definitely think this should be a feedback loop with us, picking a set of existing implementations to use as our kind of references.
So that, I think, is probably kind of a next step task, I would say, for this talk. The 1st is, you know, people please review this and just look for things, you know, that might be missing. Or if you have questions about anything in here, add them as comments.
And we'll try to build this up. But the next step after that, I think, would be to then go look at some, agree on some set of existing implementations that we're gonna look at and kind of like, essentially fill these kind of documents out for them as well.
because that's going to kind of ground us a bit in reality like, we think this is the right set of things, or we think these are, for example.
page loading that should be modeled using these events. But I think we want to check all of our assumptions in all of these areas by reviewing what what other implementations do.
And that'll give us kind of a good sense of what the landscape is, and I would like us to kind of build out a bit of that test harness like a bit of that like target setting early. So that as we're working on our prototypes, we can kind of track their progress into, you know what percentage of completeness we think we're at. How well do we think we're doing against other implementations out there?
And that'll give us a sense when we've moved from like total new prototype that barely works to like something that feels like it's it's at least in the ballpark of what our target implementations are doing in terms of like the features that they cover but also in terms of like benchmarks that we want to hit like, you know.
the artifact size, you know, page load.
So that's kind of like the next step. But this, this 1st part, just understanding in terms of data, modeling what it is we actually need to hit.
I thought this was a nice, nice overview. But it's pretty clear we need to flush this out in more detail.
So I'm curious if people have any like comments or questions just like top of mind having a look at this this data model, Doc.
**Jared Freeze (embrace)** 13:18 I mean, I'll I'll echo Joaquin here some something we've we've spoken about. A lot is session End.
because, you know, you're closing a browser. It's much different than a mobile experience where it's just different, right? Or or the server, whatever it might be. So that once you start to unravel it. It goes in a lot of directions. So that definition is gonna matter. A lot.
**Ted Young** 13:46 Yeah.
That dovetails with in terms of organizing our test harness. I would like to propose that we kind of break it into like a couple of pieces. One is like benchmarks, things I'm calling benchmarks, which are like like quantitative ways of being able to measure progress because there's certain things that from like a quantitative standpoint you could measure. But then some of these things around like, what is a session like? What does it feel like to to go through like a set of pages. I feel like also capturing a set of like example scenarios that we're trying to model.
Would be very helpful.
So that like, when we're trying to evaluate the experience of using this roam client that we're making, it's like we're all kind of in agreement of like what these scenarios should look like. And then you could also run through those scenarios with alternative tools.
so you could easily see one of those scenarios being like a sequence of rapid page loads right like this. This session that we're trying to model is a person walks through adding a couple things to their cart and then checking out or something. And that's done by a series of rapid page loads versus what would that experience be like in like a react. Single page, app right where there were no page loads. But the URL was changing. For example, and just thinking about like, what are these like kind of scenarios, where we want to evaluate the experience of using this thing to observe which also kind of dovetails with like what what is kind of the initial set of features that we expect this client to offer.
and by features here I mean kind of more just like back end features like, are we expecting people to just set up like dashboards and alerts? What are what's the kind of like default set of dashboards and alerts we would expect someone to stand up using using our instrumentation.
It. It feels like if we kind of front load doing some work on like defining those experiences. And then even building out using, like the Hotel Demo app, or something like that.
A version of that that uses alternative existing implementations that'll actually give us some really nice kind of a B testing.
So that's something I'd like to kind of propose to this group that we kind of focus our early efforts, not just rushing into building the prototype, but also like doing the work early on to kind of stand up a lot of this stuff that will allow users to evaluate what we're doing.
**Dan Gomez Blanco** 16:49 Yeah.
on that on that note. I was gonna add a comment. But I'll probably ask now, just in case I saw that there was a like someone working on the corporate vitals instrumentation in the past, and we've got here, and you know we've got page view and navigation timing as part of the events do we have already, or like envision having the performance paint timing, I guess. Event for the Lcp. And you know. Fcp.
1st paint type of thing.
I can add a comment, because I think you know, I'm not. Yeah.
**Ted Young** 17:25 Yeah, no. I mean, I think this gets into like data modeling slash scenarios, right? Like, there's this question of like the browser can give you all of this information has, like all these different kinds of events and all of these different, you know, Apis, you can use to pull stuff out of it. But like what information we're pulling out, I think you 1st have to answer the question like, why are we pulling any information out? And I. My feeling is having that written out as kind of these example scenarios that we're trying to like. Example sessions. Maybe that's the right word here is like, let's actually like, get a set of canonical sessions that we're trying to model and then be like.
well, you could actually walk through this session as like a human. We could even set up some automation to walk through that session for us and record it.
Yeah, something like that would be very helpful.
**Joaquín Díaz** 18:27 I've been working on that recently for our own room. So so I can start with that at least document something of what we did, and how we did it.
So we have something to start the conversation.
**Ted Young** 18:39 That would be great. Yeah, if you want to get that together and like, kind of present it back to the group that would be super helpful.
**Joaquín Díaz** 18:47 I can do that for for next week.
**Ted Young** 18:49 Nice cool.
Okay.
we've got 10 min left, and you know we're trying to be more asynchronous with this group, so I won't like dig through the details here. But I would say, Yeah, everyone just have a look at this. And if you can think of more sessions, you want to see us model. more events or Apis that you know other platforms are leveraging. Just just add them as comments and suggestions into this Doc, and we'll start organizing our data model here.
Going back to next item. So we have this project. I've been setting up for the group. Just spend the last 10 min kind of walking through my 1st stab at how it might be useful to be organized.
So you've got a project.
A project can have a couple of different views. One view I've made is a project roadmap.
So having a set of issues that define high level projects for the group to work on. So our primary project is like the browser phase, one like this is like the top of the hierarchy. This is everything we're trying to do.
But then I tried to break that down into like a set of sub projects.
There's a semantic conventions is like one track of work that we're we're doing that somewhat independent from everything else. There's all the work we need to do around sessions and session management as like a data model.
That includes like entity provider prototypes, and like all kinds of stuff like that.
And then there's the Api work we need to do. There's already a prototype in progress. Dan, I think you convinced us pretty hard that the work you were doing is like the best starting point for this group.
and to pursue trying to just create a new Javascript Api for open telemetry, not fork off and create like a browser. Specific Api And then the other thing that I just kind of mentioned is this test harness. So I started kind of trying to figure out how to break this out into like a set of deliverables.
That we would want to figure out. So I would love feedback on this.
Maybe we can do our ideating in slack. And in this this data model, Doc, for now. But I would love that to turn into like a list of the benchmarks, like what are practically the things we want to stand up in, like a dashboard or something, where we can look at new builds of our prototype and compare it against baselines that we extract from some target implementations figuring out.
you know what kind of scenarios we want to support. These are the more qualitative things like like, what dashboards do we want to have set up?
Do you think users would want to have set up, you know.
like slow user interactions is like a common thing.
You would want to model. So like some example scenario where we model that a session that represents a set of rapid page loads, we know, we.
we want to know what that experience is like.
And then, last, but not least, we have to figure out which our target implementations. We want to use is our like consistent references.
So 2, 1 is obviously the prototype we're going to build we need to know about that one. I think another one that's worth looking at is our baseline is like our existing Javascript Api and implementation, you know. Where does that live compared to everything else.
And then the 3 that I've heard that we have available, you know, access to faro from Grafana labs, Microsoft application insights. We know we want to compare against that. And then, Dan, you recommended boomerang.
which is an open source implementation that Akamai is currently referencing, like, I don't know if this is the right one, or if there are other ones that are right. But these are the 3 I saw recommended.
So figuring out that list, I think, is another good 1st task to help farm these tasks out, I added another view.
Which is, I'm calling the task picker.
So here we have work streams. Right? We just, we kind of defined. There's like kind of a set of sub projects for this sig to work on. Which are these kind of independent work, streams.
semantic conventions, working on the test, hardness, working on the prototype directly and figuring out our session data model for session management.
and for each one of these work streams just being able to divide things up into like tasks that are the right size for someone to like pick up and implement.
And I kind of broke the test harness thing out as like an example. So you know, setting up a benchmark, comparing, like artifact size for a prototype versus what other things deliver to the browser a compatibility matrix, right? Like the things we're comparing against. What do they support versus? What do we want to support.
The just. What are the resource overheads and latencies for loading this thing versus existing solutions?
What kind of like libraries are supported out there like when it comes to deciding which.
you know, react versus view versus other things like what what's already well supported?
And then building out these example scenarios right? Like, what are, what does the default dashboard look like slow interactions, handling rapid page loads.
And then we can figure out some way of like being able to triage this, and, you know, add things to it.
So I'm curious what people think about this as like kind of like a 1st stab.
Does this feel like a good baseline for getting getting the group organized?
Yeah.
**Daniel Dyla (Dynatrace)** 26:01 Looks good to me.
**Ted Young** 26:03 Should also add, there's a table view when it comes to just like hacking on these things.
Github projects man. It is like the lumpiest of experiences.
and one thing I find is, for whatever reason, in some of these views, you can modify things in other views, you can't access them. It seems a little arbitrary. So I just have kind of like a database table view in here. And I found, like, if you're just trying to like.
develop one of these items, or, like, get it into shape. This is like the easiest way to actually modify it or see what's in there.
**Dan Gomez Blanco** 26:44 Just what one question about the number 4 in there, like the browser phase, one issue is that supposed to be like the the the issue. For this, I mean, it should cover the the whole duration of the what this board is represented.
**Ted Young** 26:58 Yeah, totally. Yeah. So I have a couple of issues that I'm defining as like project issues which are like our tracking issues. And so you've got one that's just tracking the overall thing.
I also had this information up here in this like project details phase. But this thing is like hidden by default.
and it doesn't. I thought it might be more helpful to move that information into something that's just like the rest. So then, when you look at your roadmap.
You can see the overall roadmap, and then you can start to see the subtasks.
This is where the data model starts to get wonky. So there's a concept of issues with parent issues and sub issues. So there should be a way to organize all of this into a tree and get like an actual gantt chart, or trace view of, like the Sig, which would be really cool.
But those features are only available on issues. It seems the other thing you can put in here are like draft issues or just drafts.
And they're like a partial data model. So like the things in here, I made as drafts. You can't put them into parent-child relations because.
**Dan Gomez Blanco** 28:20 They don't.
**Ted Young** 28:20 Under the hood. Those are for issues. And these things are not really issues like, there's just some weird half assery with the data model
**Daniel Dyla (Dynatrace)** 28:29 They also don't show up in like the issue view, or search.
**Ted Young** 28:33 Which is my final question for the group, which is, I made these all as drafts because I didn't. We discussed working out of the Javascript backlog for the time being, rather than creating a new browser github repo before we figured out what, if anything, we'd want to put there.
So one thing I could do is I could turn these into real issues in the Js backlog which would help drive attention to them. But I also don't want to like spam that group by having just like a whole bunch of shit appear there. So I wanted to kind of check in with you first.st
**Daniel Dyla (Dynatrace)** 29:14 At the risk of sounding overly self deprecating. I would not overestimate how much attention you'll get by adding it to the Js issue list.
**Ted Young** 29:24 Right. I guess I'm more worried about the opposite, like, like, it seems like these these stupid things just work better if they're real issues, but that would don't think.
**Daniel Dyla (Dynatrace)** 29:37 Gonna bother us.
**Ted Young** 29:38 Yeah.
**Daniel Dyla (Dynatrace)** 29:39 Maybe, Trent, you will. You're also here. If you have an opinion. I don't think it's gonna bother me if they're in the list.
**Trent Mick** 29:46 It's all good. Yeah, yeah.
**Ted Young** 29:49 No problem.
**Daniel Dyla (Dynatrace)** 29:50 Find some like milestone project, label some way to delineate these as, like browser phase, one project.
**Ted Young** 29:59 Yeah.
**Dan Gomez Blanco** 30:01 Except.
**Ted Young** 30:02 I did not create again. Likewise, like milestones, all of this stuff, you have to make them real issues, to gain access to all those things.
**Daniel Dyla (Dynatrace)** 30:11 I mean you. You should have, like probably admin permission to do whatever you want in the Js repo. I think because of your role as a Gc. Member.
**Ted Young** 30:20 No, we actually, we have all that shit locked down pretty tight. Gc, members don't actually have any admin rights. There's just a select few Gctc people.
**Dan Gomez Blanco** 30:32 I think we might have triage. I think we've got at least permissions to move issues about. So.
**Ted Young** 30:40 I'll see. I'll see what I can do.
**Daniel Dyla (Dynatrace)** 30:42 Yeah.
I mean, I was, gonna say, maybe we should create a browser Sig team that has some permissions on the Js repo, specifically around issue management, I think, is going to be a big problem.
**Ted Young** 30:55 Yeah.
**Dan Gomez Blanco** 30:56 Because.
**Ted Young** 30:57 I think.
**Daniel Dyla (Dynatrace)** 30:57 Like a normal user can't even add labels.
**Dan Gomez Blanco** 31:00 Yeah.
**Ted Young** 31:02 Yeah, I'll poke at it and and get back to you. I think this is also like a trial balloon. I would like us to like kind of expand out project management a bit more across open telemetry, and so kind of like. The next phase of that would be like. Once we learn what we like doing here in the browser Sig. It would probably be cool if, like the rest of the Jsig adopted something similar. I'm not saying for everything but the degree to which there are like initiatives happening there, like, you know, an SDK overhaul or like implementing this new chunk of the spec or whatnot.
I'm curious to see if we could develop this idea more.
With the hope of eventually being able to produce these views, to like our end users around being able to have high, level roadmaps of the project at different granularities.
**Daniel Dyla (Dynatrace)** 32:06 And.
**Dan Gomez Blanco** 32:07 I thought you were. Gonna say, with the hope that Github can improve some of the reporting on projects.
**Ted Young** 32:12 They. They seem to be actively working on this stuff. And one of the next things we're interested in is like org wide projects, like projects are. They're sort of half acidly or org wide right now. But you definitely can't have like projects within projects. But whatever I think we could potentially drive some of that stuff like we have some common contacts at Github. We're like a really big open source project. And if we're coming to them, or like we are heavily leveraging the heck out of projects. You know, this is like, we're a good case study to drive this out like I do think it's possible for us to get a feature to added, if we're desperate for it.
But we need to get into a place where we're kind of modeling it for Github and showing them how a big organization could use this effectively.
**Jared Freeze (embrace)** 33:12 So I just changed one thing I kind of like to view. So if you take out your search term and then under Project roadmap, dropdown, do group by project.
**Ted Young** 33:21 So if I take out this search term right here.
**Jared Freeze (embrace)** 33:23 I don't.
**Ted Young** 33:24 Okay.
**Jared Freeze (embrace)** 33:25 And then in the dropdown for the tab.
**Ted Young** 33:31 For the.
**Jared Freeze (embrace)** 33:32 Yeah, no. Just above, yeah. Where the blue.is.
**Ted Young** 33:34 Oh, yeah.
**Jared Freeze (embrace)** 33:35 You do? Group by project.
**Ted Young** 33:38 Group, by project.
**Jared Freeze (embrace)** 33:39 I like this view.
**Ted Young** 33:41 Cool.
**Jared Freeze (embrace)** 33:42 Little better.
**Ted Young** 33:43 Yeah. Oh, look at that.
**Dan Gomez Blanco** 33:46 That's good.
**Ted Young** 33:48 Yeah, now we can kind of see everything, and we have an attached, you know.
deadlines to these things yet. But I think that would be helpful to start doing it like I just started attaching kind of like arbitrary deadlines is like.
you know, end of the year end of the quarter, but for certainly, for whenever something started or in flight.
getting into the habit of having kind of like an estimated deadline, even if it's way off.
just like, probably like a good practice for us to start. And this roadmap view, I think, incentivizes us to do that.
**Jared Freeze (embrace)** 34:31 It's kinda nice, too. There's another option slice by. If you do assignees like we could bookmark our own work, which is nice. So.
**Ted Young** 34:38 Oh, cool. Yeah, yeah. I'm excited for us to. I think they have actually put enough in here. At this point. It is possible to find good ways for everyone to start working out of github projects in a way that like actually feels productive.
like the traditional like, you know, to do active done kanban thing. I haven't found super helpful, but being able to see all the different lines of work with the available things up to the top as like an easy way to be like, I want to just start something new.
What's Yummy? And you know, would be helpful to this project? I think that's like a very useful open source tool to have.
I've definitely seen a lot of examples of organizing things with good 1st issue and stuff like that kind of does help people feel like they can jump in.
So I'm curious to see if this accelerates the amount of like parallelization we have, as far as like actually getting work done.
But knowing what what all, even like, there's no details on any of these things right now, we need to like flush a lot of this out.
That's actually another question I have who has access to edit this thing?
If people try to edit these draft things, are you able to do it.
**Dan Gomez Blanco** 35:58 Do you.
**Daniel Dyla (Dynatrace)** 35:59 So this is all project level. It's gonna be you and Dan.
**Ted Young** 36:03 And I probably almost no one else.
**Dan Gomez Blanco** 36:05 Well, actually, if you, if you go to settings. Well, if you were to create that group that Github, you can.
**Daniel Dyla (Dynatrace)** 36:11 Team. Yeah.
**Dan Gomez Blanco** 36:12 Yeah, you can just assign make make them admin as well. So yeah.
you can make a github.
**Ted Young** 36:20 Okay, so we can make a team and assign it to this project and give them project board access essentially.
**Dan Gomez Blanco** 36:26 Yeah.
**Ted Young** 36:28 Okay.
**Dan Gomez Blanco** 36:29 That's another thing that's in by default. Maybe that change now, by default, they're created private. I think you need to make it public, so that people that are not part of open telemetry of your.
**Ted Young** 36:38 I did make this public. It is a public thing, so I think anyone should have permission.
**Daniel Dyla (Dynatrace)** 36:43 Permission to edit this. I have permission to edit stuff.
**Trent Mick** 36:47 I think I do as well.
**Dan Gomez Blanco** 36:48 It might be that everyone that's in the org can edit it. I don't know.
**Daniel Dyla (Dynatrace)** 36:54 That's probably yeah, probably fine, but.
**Dan Gomez Blanco** 37:00 It's up to the it's up to the I guess, to the project author, or the Creator or the Admins. You can lock it down I'm assuming, but I think I think that is fine grained access there.
Yep.
**Ted Young** 37:11 Yeah.
Let's see.
**Daniel Dyla (Dynatrace)** 37:13 I can even change settings on this project.
**Trent Mick** 37:16 Can delete.
**Ted Young** 37:17 Yeah, manage.
**Trent Mick** 37:18 So I think.
**Ted Young** 37:19 Manage access. Yeah, I mean, it says, base role. Everyone in the organization has right access.
**Dan Gomez Blanco** 37:30 Alright. Okay.
**Ted Young** 37:31 Can see and make changes to the project, but they can't add new collaborators.
**Daniel Dyla (Dynatrace)** 37:37 That's probably fine for now. But we should create a team for this project, anyways, and then we'll lock it down at that point like.
**Ted Young** 37:44 I think the chances.
**Daniel Dyla (Dynatrace)** 37:45 Somebody's gonna come delete all our issues is like super low.
But now he's here, be coming.
**Ted Young** 37:53 Org member, but.
**Daniel Dyla (Dynatrace)** 37:55 Yeah.
**Ted Young** 37:55 They could still accidentally do something dumb.
**Daniel Dyla (Dynatrace)** 38:00 We should lock it down just as a matter of course eventually, and you know fairly soon. But I don't think it's something that like.
**Ted Young** 38:07 Not a rush. If someone destroyed it in its current state, we just recreate it.
**Daniel Dyla (Dynatrace)** 38:13 Yeah.
I know, we're over time. I just wanted to real quick ask, if anybody had time to look at the Api poc. I know I promised to put together a little presentation. I didn't have time to complete that. I started working on it.
But I'm also generally looking for feedback on that.
**Ted Young** 38:35 Nope.
**Daniel Dyla (Dynatrace)** 38:40 Sounds. Like, no. Okay.
**Ted Young** 38:42 I I mean, I will definitely take a look at it, you know. But I'm I'm a little rusty. So other people should look at it.
**Jared Freeze (embrace)** 38:52 Yeah, I I looked it over. I'll need to refresh, though.
**Daniel Dyla (Dynatrace)** 38:56 Okay.
**Ted Young** 38:59 Cool all right. See you all on slack.
**Trent Mick** 39:04 Excellent.
