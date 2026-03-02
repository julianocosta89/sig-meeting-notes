SIG: JavaScript SIG
Date: 2025-07-16
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Daniel Dyla (Dynatrace)** 01:42 Hey, there, everybody!
Mark's not here today, and I've been admittedly distracted on other things recently. So this might be a short meeting.
I guess with that we'll we'll get started here, share my screen.
see if it can. Everybody see it.
**Raphaël Thériault** 02:14 You know.
**Daniel Dyla (Dynatrace)** 02:16 Okay. Mary Leah, I think you have the 1st topic here, the only topic right now. So anybody wants something talked about today.
Now's the time.
**MG Marylia Gutierrez** 02:29 So yeah, this is a context that
Ted was sharing with me and another group that the Gc now is looking to
ways of like helping people find issues. And that is something like the consumer. Experience also is trying to help. So one of the ideas is for all the projects start using the github projects feature as example, the one of the browser. I think, Daniel, you are joining that one.
but for now it's just more than a sense of feedback. If people think this would be useful or not. If makes sense for the Javascript repo to have something like this, it would help if we would just create a lot of work. So yeah, just trying to get some feedback at the moment.
**Daniel Dyla (Dynatrace)** 03:17 Yeah. So I I was in the meeting in the browser when he said that. I
I'm willing to give it a try
I think in the past we've used projects, and then they always end up like
it always ends up a little bit unused.
I guess we could get around that, maybe by having a dedicated project triage session in each meeting.
But I think the people that come to the meetings generally know what we're working on. We do have the focus areas, issues that are pinned, that mark created that are quite detailed.
and the people who don't come to the meetings, I think, are unlikely to look at those projects.
so I'm I'm willing to give it a try if if that's what the what the project as a whole is doing.
But I don't.
I don't see an immediate benefit of it over what we're currently doing.
**MG Marylia Gutierrez** 04:27 Yeah, because, yeah, one feedback that I gave was also cause. Sometimes I get like random message of people like, I wanna help contributing which issue should I take, but not specific for Javascript, just like anything in hotel. So it's hard to find, like one good issue like in hotel in general. So one idea was
having, like a view something like this, but actually open issues for all hotel repost. Then we can separate. I don't know languages, or whatever type of thing that would be something for people that wants to join open telemetry in general, easier to find, and I will be doing that as part of the consumer experience. Sake, I don't know if that is also something that
you think that makes more sense than having the project specific for Javascript.
**Daniel Dyla (Dynatrace)** 05:17 I think that makes sense like a good 1st issue. Tag. We've never been very good about using that. But
If we could get used to using it. I think that that makes sense because you're I have similar questions. People ask.
what can I work on? You know I I know, python, what can I work on? And I'm always like, well, go to the python issues and see if there's 1 tag. Good 1st issue. If there isn't. I never know what to tell them. So if the project as a whole got better at that in particular, I think it would be a good idea as well as some things like
there are some cross language projects like updating Http instrumentation for stability. Ha! Is across all the languages, and like, I'm sure the same thing database messaging whatever. Like all these cross language things would probably be helpful to be tracked in some way.
But yeah, I I think that's much lighter weight. That's like adding a a label to issue.
and then having, like a project, wide label, filter.
**MG Marylia Gutierrez** 06:22 Yeah, just if you're curious. I created one time like a bot to find good. 1st Asian, all hotel, and he's very like
can diverge a lot for the repo for the Javascript we use up for grabs lots. So I think that is also a good point to align. We have, like good 1st issue. But we use a lot of the up for grabs, and then all the ones that are for the
the hack fest, and things like that eventually become good 1st issue. So I I also tag those ones that the things to look for.
**Daniel Dyla (Dynatrace)** 06:58 I think the up for grabs is a little different. They're not always a good 1st issue.
Some of them are quite complex, and it's more like
this is something that needs to be done. But nobody's actively working on it right now.
But some of them are quite complex.
**MG Marylia Gutierrez** 07:14 Here! Hold.
**Daniel Dyla (Dynatrace)** 07:17 I feel like the only one that has given any. Does anyone have thoughts? I don't want to dominate this conversation especially because I gave up, I think, somewhat negative feedback. So if somebody has positive feedback, I'd like to hear it.
**Trent Mick** 07:36 So similar. I'm willing to try it. My experience with Github projects is unless
yeah. Maybe this answered by what you said, Dan. If there's regular bullet item on this weekly review to be looking at it. That's otherwise. It goes. They can tend to go stale.
while so github projects, allows you to kind of have a single view for what you would.
We used to use milestones for, but crossing a number if it's crossing multiple repos. So that's that can be really handy.
If there's a well organized kind of
project that has a measurable end goal kind of thing. That could be useful, because otherwise, like milestones, we, the milestone that we used for the SDK. 2 point oh, was quite useful, I think, in us being able to see. You know how far away we are, and
I guess another place where
a well run project would be useful for people coming to the project is if they don't just want to grab whatever issue they want to have some sense of being impactful, then it's not necessarily about good 1st issue, but it's about something that
is important to the project to work on right now, as opposed to like the big, long tail of issues that might be nice to get done. But it's not the thing we're focusing on right now. I agree. Mark's focus topics really help there for js,
I guess the part where I'm maybe a little bit hesitant is if there are
like a Github project that's trying to capture
the current set of focus things for the whole open telemetry project like, who's managing that? And I I don't know how well curated those projects will be, so I guess.
Don't maybe you know better, Marilia.
**MG Marylia Gutierrez** 09:24 No, it'd be like. For example, each repo has their own like project thing. So it would be just for the Javascript. The Maintainers will be the one like looking into. And then
that's kinda it. So each one is responsible. But it's more for like people that wants to join any of the 6. They will look to that 1 first.st cause the if I can actually share the
where are you?
If you look at the link that I share the the second tab is a task speaker. So anything that is now mark as available is an easier way for people to grab something to work on.
so that is something that they were like looking for, but that
creates like the onus on the Repos itself, to have all of those always up to date.
So is the question, is it worth it? Do we see that as a problem for this repo.
**Trent Mick** 10:26 So how do I know from this anything that says available here.
**MG Marylia Gutierrez** 10:30 Yeah, anything is available should be something that anyone can pick up.
**Daniel Dyla (Dynatrace)** 10:46 Yeah, not a lot of detail on these.
I think something's just available if it's not
assigned, though, right? There's no actual. Oh, it's it's in. I got it status available. Somebody wouldn't mark them.
It looks like everything is basically available.
**Trent Mick** 11:12 And there's some that are in progress. But yeah.
**Daniel Dyla (Dynatrace)** 11:15 The Prs are in progress.
**Trent Mick** 11:19 Right.
**Daniel Dyla (Dynatrace)** 11:23 Yeah, I mean, it seems like a lot with, you know.
I'm I'm sure that it's well intended.
But to be honest, this seems like the type of thing that would need a dedicated project manager
and Ted is a project project manager. So he comes naturally to this kind of thing.
As far as I know, there's nobody working on the Js Sig, that is a project manager
or comes from that background.
it looks like a lot of overhead to me. I understand that it's good info that, like the Gc. And the Tc. Want to have visibility on what's going on in the in the sub projects, and that makes a lot of sense.
I think if we go to js, not Js contrib.
Like, if we go to the the focus issues the focus topics. This is very similar. It's just less overhead like this is not expected to be updated all the time. It's like we. We update this what once a quarter or something like that
and do a very detailed job when we update it. But
it doesn't require maintenance every single day which I feel like this. Would
**MG Marylia Gutierrez** 12:50 Yeah, because I feel like this, maybe are for project. There can be very complex and like big or something. I don't feel like, this is a problem for our sake, but I just wanted to bring the topic anyway, because at some point they might reach out, and we can have, like already, an answer ready.
**Daniel Dyla (Dynatrace)** 13:10 Yeah.
I don't know. I I don't mean to give such negative feedback about it. I don't mean it in a negative way. I think it's well intentioned and could be a good idea. I just don't.
I'm hesitant
to commit to it, because I don't know that we'll be able to actually follow through on it.
and I don't want it to become a situation where bad information is worse than no information like, I don't want a project that's just out of date that people are looking at and getting even more frustrated because, like this says available. But somebody's working on it. Or this says somebody's working on it, and I haven't seen a Pr. And
I am not confident in my own ability to
keep something like this up to date all the time.
**MG Marylia Gutierrez** 14:05 Yeah. And even if people are gonna check because who guarantees that people will look at those projects at all.
there is also.
**Daniel Dyla (Dynatrace)** 14:14 I would like to hear from. There's a handful of people in this meeting that contribute somewhat regularly. But aren't maintainers.
Does this solve a problem that all of you have like I I don't want it to be like, Oh, well, I'm the person that has to maintain this, and I don't want to. Maybe it's some massive problem that I just don't feel, because I have a better idea of
the roadmap, because I'm the one that came up with it.
**Jonathan Munz** 14:45 I don't have a strong opinion. I was just gonna mention a couple of folks from embrace are
starting to be active in the browser Sig. So I was gonna keep track of their feedback. Of how well
that style worked in the browser, Sig, because, yeah, I'd be curious to see how it compares, but at the moment I don't have a strong opinion.
**Raphaël Thériault** 15:07 Yeah, I think it's
okay. So like, it would probably be fairly useful if it was kept up to date at all times. But otherwise I don't really see myself using something like that. If it's just like who, if the information is even
meaningful in there, then I don't think it really solves that big of a problem, at least, for, like
people with tender sick, you kind of get a general idea of what the what the roadmap is
without having to just have it laid down somewhere that clearly.
**Daniel Dyla (Dynatrace)** 15:46 Yeah, I I feel like the people who join this meeting.
I I hope, generally know what's going on.
And then the people who don't join this meeting are unlikely to find the project. They're not particularly well surfaced in the Github Ui.
**Raphaël Thériault** 16:03 Yeah, I feel like it's mostly drive by contributions. And then people run the
I tend to say again, there's not really.
And in between that would benefit that much from having the project around.
**MG Marylia Gutierrez** 16:18 We can keep an eye on the browser one, and if we get feedback like oh, my God! That was the best thing ever in my life, then we can consider but.
**Daniel Dyla (Dynatrace)** 16:27 It goes really. Well, I think there's 2 things, one, it could go like a really well. And it's like, we gotta take advantage of this because they're getting a lot of value from it.
Or it could be that the Gc. Says you have to do this now, because this is how the Gc. Wants to have visibility on the Sigs, because from their perspective, I can tell you, from being on the Gc. Every every sig doing their own different style of project, management, and roadmapping makes it difficult to know what's going on in any of the Sigs.
which is a trouble from a governance perspective. So even if we as a sig don't get value from it, the project as a whole might
it becomes a little bit like Tps reports at that point. But.
you know, there's a reason that those types of things exist, and it's entirely possible the Gc. Will just come and tell us you have to do this now, this is what the project does, in which case we probably will.
But
th, those are the 2 ways that I think we could really like that. I could see us using it. I'm not gonna jump in this as an early
adopter, if it's optional. And
the people in the Sig aren't asking for it. If I if I start getting people in the Js. Sig saying, like, Hey, other sigs are doing this, and I think it'd be a good idea then I'm totally willing to do it. But if nobody asks for it, I don't want to maintain it just as like a
a time sink that no one gets value from.
**Trent Mick** 18:11 So I'm curious to back up where?
I guess. What? What is the
I was? Gonna say use case. But like, how? How does a person that comes to hotel.
I was just clicking around a little bit and wanting to contribute to the Js. Part of it, how they would
get to where our current state is
and if you go from open telemetryio and search for community, and if you manage to get this far you can get to this special interest groups link which gets you to the huge table. And if you can find Js on there, the the only real link you get is to the doc
that we're that we have open right now. And I wonder if having a section at the top that says, like, here's our roadmap. It's basically that link to that focus topics thing that is effectively the best collection of our roadmap. Right now, that might be the best we can do to advertise what our current roadmap is. And maybe
if what you're bringing up really, if the Gc. Is looking at creating some page in open that does a more direct link to what kind of major roadmap items are. I know there's a there's an open telemetry
roadmap
thing which doesn't get into what the Sigs are doing at all. Where did I find that that was?
Century I/O community roadmap!
I don't know if something, if they're.
**Daniel Dyla (Dynatrace)** 19:43 Make this whole section a little smaller. It's enormous at the moment.
**Trent Mick** 19:49 Yeah, it's picking up more space than it needs to to say what it's saying.
**Daniel Dyla (Dynatrace)** 19:53 The cursor parking lots unused. It was a fun idea, but I'm gonna get rid of it. Somebody.
**Trent Mick** 19:57 And I used it.
**MG Marylia Gutierrez** 20:05 And share a link. I don't know if that is the 1. 0, you also share one, Trent.
**Trent Mick** 20:10 I did this on the
if someone's clicking around trying to say, Hey, like what's going on in hotel, and I want to help. I think they might land there. But that's not gonna that doesn't cover any Sig stuff like I'm curious of the DC. Or the Docs group would consider adding.
**Daniel Dyla (Dynatrace)** 20:28 Alright links to.
**MG Marylia Gutierrez** 20:31 Yeah. The only one that I know is the one that I sent. That is a general project of hotel, but it's very
like.
**Trent Mick** 20:39 The one you just put
**MG Marylia Gutierrez** 20:40 Yeah, that one is like very high level.
**Trent Mick** 20:43 That's a closed project, though.
**MG Marylia Gutierrez** 20:44 Yeah.
**Trent Mick** 20:45 Says, closed.
**MG Marylia Gutierrez** 20:46 Yeah, that was the only one that we're using before. I don't know if they like.
**Trent Mick** 20:51 Okay.
So as you're saying like, I'm totally cool. If if we monitor and a number of us are gonna be
watching or be involved in the browser
phase one sig thing. So if, like, the experience is super positive there, then maybe we consider doing the same.
independently. I wonder if we can do a better job advertising the
the focus topics issue that that we have
cause. That's basically the best thing to say, hey, if you want to make an impactful change in Js and get involved, I mean, obviously come to the Sig and you can push your own
agenda. But otherwise, if you want to contribute to what the group is kind of agreed to focus on, then that's the place to go right now
and then. Unrelated to this. A personal comment on it like it used to be, use Github issues. And you'd have a Meta issue to track
multiple issues going on it. And then 1st version of Github projects came along, and you could kind of do it there, but they were tied pro to repo and then
get org projects is a new one. And now you can have sub issues on issues instead of just a big list of links. And I'm kind of lost personally on what the best way to use all this stuff is and how they interact.
Like our sub issues related to Github projects are not really. They're independent.
**Daniel Dyla (Dynatrace)** 22:12 They're independent.
I think projects take advantage of some sub issue features now. And probably will more in the future. But they're independent. I think it's
they're they're adding features, because every team works slightly differently, and they're trying to make it so that there's something for everybody. My coworker called it the gerification of Github the other day, and I thought that that was very apt description.
Jira Jira can work any way you want it to, and that's part of the reason that everybody hates it.
**MG Marylia Gutierrez** 22:48 Oh, yeah, I hate Jira.
**Daniel Dyla (Dynatrace)** 22:50 I think Github is gonna have to be careful to not become that as well. Fortunately, that's not my problem. That's somebody else's problem.
**Trent Mick** 22:59 I see it like C, plus plus. If you can organize A, an agreed upon subset to use in your group, then it can be fine. But.
**Daniel Dyla (Dynatrace)** 23:07 It's fine. Yeah.
**Trent Mick** 23:08 It's a big, wide open minefield, if you'll have better. But yeah.
**Daniel Dyla (Dynatrace)** 23:11 I don't think it's I. I think Jira is totally there. I don't think Github's quite there yet, and I hope they don't. But who knows.
**MG Marylia Gutierrez** 23:19 Yeah, I was a manager for a few years, but I had a Pm. That he really loved Jira so every time that I had to touch like here for you, and I would give to him, and he was happy, and I was happy that I didn't have to touch. So yeah, we went.
**Daniel Dyla (Dynatrace)** 23:35 So we've dedicated about 20 min to this already. I think I'm gonna move on. Marily, are you
like? Is there somebody tracking this among all the Sigs? Was this something that somebody asked you to bring to the Sig? Or is this just something you heard in the Browser group? And you thought you'd bring up here.
**MG Marylia Gutierrez** 23:55 So I have. We have a meeting, and internally at Grafana for hotel stuff, and Ted brought this up, and he wants to know how each of us that joins it would feel about it. So this is why I say, okay, let me actually get more feedback from the Sig itself. Not just my own.
**Daniel Dyla (Dynatrace)** 24:11 I forgot you were Ted's coworker.
**MG Marylia Gutierrez** 24:13 Yeah.
**Daniel Dyla (Dynatrace)** 24:15 Yeah, I I think it's well meaning I am not
overly enthused about it. I'll do it if I'm told to.
Yeah, I guess I'll leave it there.
**MG Marylia Gutierrez** 24:27 Yeah, sounds good.
**Daniel Dyla (Dynatrace)** 24:31 Alright!
Rough need someone to look at. I assume this is an exporter related issue.
**Raphaël Thériault** 24:40 Yeah. So like, I don't mind waiting for Mark if we just wanna wait for him. But that does unblock, roll up, bundling at the same time so.
**Daniel Dyla (Dynatrace)** 24:52 Yeah.
**Raphaël Thériault** 24:53 That's the whole one, though, with the the tests migration thing.
Yeah. And actually, while we're on the I just want to like quick aside. Marilia, did you plan on doing the other database drivers some kind of migration? Or is that kind of up for grabs.
**MG Marylia Gutierrez** 25:11 Yeah, I'm I have started now the my sequel, but we have a lot of others. So if any you know want to help with any of the others.
though I would be very happy, and I can help out as well. If you
need to understand anything. I'm happy to go over.
**Trent Mick** 25:36 Comment on your thing. Really good thing. How is adding
customization? For of the HP. Agent for exporters related to roll up.
**Raphaël Thériault** 25:47 Because I this ended up like I needed to touch some code that did like. I think that's the only remaining
dynamic require that was.
**Trent Mick** 25:59 Okay.
**Raphaël Thériault** 25:59 So it it kind of just happens.
**Trent Mick** 26:04 Okay.
So I'm interested in learning the exporters better. But
there's no way I'm getting anywhere near there before Mark comes back in a week. So
yeah, that won't be any help.
**Daniel Dyla (Dynatrace)** 26:20 Yeah. I remember looking at and talking about this issue or this. Pr, I haven't.
I haven't really thoroughly reviewed it myself. I
I have to admit I typically
defer to mark on anything exporter related, because they
are a minefield which he is slowly improving. But I think he's still the only one that has a really good idea of what's going on with them.
Alright!
I guess that's it. Then, if anybody else has topics feel free to interrupt because I'm not gonna be probably looking at the meeting notes while we're doing the triage.
But I'll start with bugs.
Eager error tag support.
set up an Otlp exporter, start a span, set error status, and end it. Go to Jaeger, open the trace expected error equals true
does not have error equals true.
Yeah. So I think.
Oh, the deprecated exporter, Jaeger did that. So if you're exporting Otlp to Jaeger.
I think this is not on us like we're not adding.
because that would error equals true tag would go to all Otlp endpoints.
I don't think we can send anything that specifically goes to only Jaeger and not other Otlp receivers in the Otlp exporter.
So I'm inclined to say we won't do this.
**Trent Mick** 28:19 He wants span dot set status to
also set an attribute called error.
**Daniel Dyla (Dynatrace)** 28:28 Yeah, because in the old Jaeger exporter I believe Jaeger doesn't have like and status.
So if it was an error, they just tagged on error. True, so that you can filter by by errors, by spam status
**Trent Mick** 28:48 Yeah, I would think you just okay. I I agree with what you're saying. I think the workaround would be to add a span processor that does that. If you care about that.
**Daniel Dyla (Dynatrace)** 28:56 Yeah, the workaround is either a Jaeger span processor, which I even think that that's not the the true solution to this is for Jaeger to implement this in their otlp ingest
like if they if Jaeger supports Otlp as a as supports receiving Otlp data, I would
I would build this functionality in there.
In any case, it's definitely not a bug.
**Trent Mick** 29:27 I would say feature, request.
**Daniel Dyla (Dynatrace)** 29:29 I'm gonna say,
probably not going to be able to easily find
probably cult. Oh, it's probably in jester, isn't it?
Yeah, I'm actually just gonna send them this.
And then I'm gonna say, not planned
with comment. We're good with that.
**Trent Mick** 31:24 Yeah, that sounds appropriate.
**Daniel Dyla (Dynatrace)** 31:27 Thanks.
Okay.
no contribut bugs did we get through all of the old Pr.
Sure.
**Trent Mick** 31:45 Remember.
**Daniel Dyla (Dynatrace)** 31:45 We did we? We moved on to the main repo. Didn't.
**Raphaël Thériault** 31:49 Yeah.
**MG Marylia Gutierrez** 31:49 When we start to look at the.
**Daniel Dyla (Dynatrace)** 31:51 Should we go through all of these again? Real quick? It looks like a lot of them have updates. We'll just go through the ones that have
component owners both updated here.
So I think this one, it's not reviewed. But now both component owners have given their thumbs up. So
I think we're good to go when this gets reviewed. Did the both the component owners review this?
No.
**t2t2** 32:33 Which gave thumbs up, but also the spiel needs to be redone for the new folder structure. Anyway.
**Daniel Dyla (Dynatrace)** 32:39 Yeah, a lot of the Prs need to be updated for the new folder structure.
**t2t2** 32:50 The same is already aware of it. He's just a few days.
**Daniel Dyla (Dynatrace)** 33:02 Alright.
Gcp, oh, this is the one where we
let's see. So on the meeting notes, Pr is actually discussed.
I'll try to start joining the meetings. Person's not here, are they?
Looks like, now.
yeah.
**Trent Mick** 34:26 You could also mention, at least it was true last time that the
their resource detector is not updated for SDK 2.0.
**Daniel Dyla (Dynatrace)** 34:34 Yeah, we.
**Trent Mick** 34:34 Source stuff quite changed.
I don't know if that'd be a kicker for them, because I mean updating their minimum node.
**Daniel Dyla (Dynatrace)** 35:14 I'll just leave it at that.
Alright
Ecs Bargate, where did we leave this one? Looks like it needs reviews.
Jonathan. Please take a look new branch.
Push the new branch.
I don't think Jonathan is in this meeting right now.
Workflows still need to run.
**MG Marylia Gutierrez** 35:56 If he's saying he's a new branch is like an a new like Pr, and this one can.
**Trent Mick** 36:01 He just he just means he update. He updated the Pr for the new.
**Daniel Dyla (Dynatrace)** 36:04 The update.
Oh, okay.
**MG Marylia Gutierrez** 36:06 It is. Yeah, yeah.
**Daniel Dyla (Dynatrace)** 36:07 Pushed. My guess is, he just figured it was easier to. I don't know
whatever it is. This Pr is updated now. Jonathan gave it a thumbs up to please review. So
I think it's fine new pr workflow. This is a draft.
I'm clicking on it just to get rid of the activity indicator there.
Oh, renovate!
I don't want to
label No. 8.
**Trent Mick** 36:51 Dependencies. You want.
**Daniel Dyla (Dynatrace)** 36:57 Yeah.
**Trent Mick** 37:04 Alright, that's me still to do.
Oh, no. Sorry. This is the newer one. Yeah, merely. I
answered a couple of your questions. You could.
So you have a chance to re-review. That'd be great.
So I guess I have one review. I could just merge it, but.
**Daniel Dyla (Dynatrace)** 37:19 It's got an approval. If you're happy with it, you're fine to merge it. But unless
I don't know what Mary Leah's comments were, but I trust that you're on it
minimum. Oh, this is the open telemetry bought one, mark approved this.
I think it was conflicted, and that's why
I'm gonna I think I'm gonna merge this.
it just adds like the minimum permission for each of the jobs.
**Trent Mick** 37:54 Yeah, go for it.
**Daniel Dyla (Dynatrace)** 38:02 Okay. Union type support
enable support for installing field instrumentation on union types.
Yeah, I can't review this on the call. Obviously, see what was the last?
Cla issues resolved. Oh, yeah, Bart.
Mark said. He reached out to him, and he said, he still wants to maintain his packages, but I am.
have to admit losing confidence.
**MG Marylia Gutierrez** 38:56 Alright and Trent. I just approved that Pr and I click on the update branch because it was out of date.
**Trent Mick** 39:02 I hear it. Thanks.
Did that work.
**MG Marylia Gutierrez** 39:07 It is doing.
**Trent Mick** 39:08 That was through the whole package renaming. But anyway, okay, cool.
**Daniel Dyla (Dynatrace)** 39:12 So this is an X-ray rate, limiter.
approved by an Aws contributor. Looks like there's a lot of open comments on it, though.
**Trent Mick** 40:02 This pair is also to a package that's an incubator directory. So I don't even think we're
publishing this thing so kind of a lower bar.
**Daniel Dyla (Dynatrace)** 40:10 Yeah.
**Trent Mick** 40:15 Anyway.
**Daniel Dyla (Dynatrace)** 40:30 I don't remember what the deal was with this way. I think we were just skipping it right, because there was.
**Trent Mick** 40:38 Oh, yeah, David's away this week. So it's.
**Daniel Dyla (Dynatrace)** 40:42 He can.
**Trent Mick** 40:42 Get back on it next week.
**Daniel Dyla (Dynatrace)** 40:47 Release main.
That's can't merge it right now, because we're waiting on the actions, anyway. But my SQL update
metric inch. Oh.
**Trent Mick** 41:02 This is me. And this is 17 h ago. So the fact that we're discussing this in a weekly.
**Daniel Dyla (Dynatrace)** 41:08 Yeah, we're in close. This is good. This is the process working as intended.
**MG Marylia Gutierrez** 41:14 See you were so concerned when when we started this with
5 years ago. Look where we are now.
**Trent Mick** 41:22 Cool. Yeah.
**Daniel Dyla (Dynatrace)** 41:25 Alright
**Trent Mick** 41:28 Anyway, people can review when they have a chance. We don't need to spend that time here.
But this was so. We added the update metric instruments as a mechanism for instrumentations that have metrics to update because
it's basically a got it a hack, because our meter provider doesn't
do the proxying thing that the other providers do. So that's necessary. This hack update metric instruments was added at about the same time that this instrumentation, Mysql. Pr. Was being updated to add metrics to that instrumentation. So that's why they they kind of crossed.
**Daniel Dyla (Dynatrace)** 42:07 Got it.
**Trent Mick** 42:08 On the road.
**Daniel Dyla (Dynatrace)** 42:14 Okay, so needs reviews.
If that was 17 h ago, we're definitely oh, there's only one more here. Look at that.
3 h ago.
Kafka does not instrument send batch, or send methods if they're called during a transaction. So this obviously just also needs reviews.
It looks like a lot lot of tests, though. Like to see that. Okay, is this waiting on
workflows? Yes.
only 28 here also, and actually a lot less of them Async hooks es lint warnings.
Oh, stale man, I want this guy back.
I am going to assign myself to this so that I can get this reviewed this one and the other one are both probably the same.
Sign myself.
**Trent Mick** 43:33 I wanted to review these, but oh, do they get into deep typescript stuff sometimes.
**Daniel Dyla (Dynatrace)** 43:38 Yeah, they do. I mean, he's mostly fixing warnings by, like, there's a lot of
**Trent Mick** 43:44 That's a good thing to do.
**Daniel Dyla (Dynatrace)** 43:46 Yeah, I am a hundred percent in on these. It just
they can be tough to review and understand why things are happening
wired open 3 different exporter. Prs.
Trent, you requested changes on this. It looks like he updated the change log.
But it looks like a lot of these are still open. So that's probably
this has been approved by Trent and Svetlana updates code user to help your libraries to retrieve environment variable names. Only 2 files changed? Can we just merge.
**Trent Mick** 44:35 Means this trying to keep up with you.
**Daniel Dyla (Dynatrace)** 44:39 Yeah, sorry
this is adding the get string from env
helper. Instead of doing the trim, it's using the helper method.
**Trent Mick** 44:58 Yeah, I had a couple of nits on this like way back when I was gonna when was this April?
And then he hasn't gotten back to.
He doesn't. I mean they're just nits. So that's why it was approved with.
It's he didn't get back to it. And now it has a Saint George conflict, so
I'll take it on me. I'll put on the list. I can finish up the nets and just merge it.
**Daniel Dyla (Dynatrace)** 45:29 Date.
and oh, same thing, just in a different
looks, like you also had comments here, but I think.
**Trent Mick** 45:42 Different package. Same thing, I think probably right.
**Daniel Dyla (Dynatrace)** 45:44 Yeah.
**Trent Mick** 45:46 Okay. Hold on.
**Daniel Dyla (Dynatrace)** 45:50 Type metrics attribute looks like Hector approved. This reports the error type attribute on Http. Metrics whenever it is already reported on spans.
Is this required by specification.
**Raphaël Thériault** 46:10 Yeah, it is it might be recommended. I'm not sure I remember exactly. It's either like recommended or required.
**Daniel Dyla (Dynatrace)** 46:19 Okay.
In that case Hector's already approved this.
It's, I assume, not a very big change.
Can you link the
**Raphaël Thériault** 46:33 I think it should be linked in the issue. Let me check real quick.
**Daniel Dyla (Dynatrace)** 46:37 Yeah, I didn't find it on the issue.
It just says, using stable semantic conventions I'd appreciate. Oh.
**Raphaël Thériault** 46:44 Of that.
**Daniel Dyla (Dynatrace)** 46:45 Yeah, mark, did.
**Raphaël Thériault** 46:47 Oh!
**Daniel Dyla (Dynatrace)** 46:50 The request fails. Okay? I think this can probably be merged.
I'll give it a quick once over after the meeting. And merge it.
I'll keep that one open for now
support Http. Headers as an array. Http. Package node supports, receiving the headers as an array of strings.
**MG Marylia Gutierrez** 47:31 There's a draft.
**Daniel Dyla (Dynatrace)** 47:33 It's a draft. Okay, it's a pretty.
I mean, it's a month old as a draft.
make sure he doesn't feel ignored, add schema, URL,
Mark requested changes on this.
This is a pretty big Pr, what was Mark's issue with this?
Just a small blocker left.
Yeah, okay, so this is now marked as resolved.
for now.
**Trent Mick** 48:57 Oops!
**Daniel Dyla (Dynatrace)** 49:03 Yeah, I don't have a strong preference. If that's what Mark wanted, then it's fine.
This looks resolved. Negative test case.
Looks like Jackson was happy with that.
No response. Here I will dismiss Mark's
request changes because it looks like it's been
alright.
Any value attributes for logs. This is definitely required by spec,
looks like there's some reviews here.
We did additional test coverage negative tests. That's probably what that is.
hey?
He's got conflicts there, anyway, in the change. Log
node. SDK, multiple metric readers
export to multiple destinations.
Oh, I gotcha!
I'm not sure.
Do we have a multi metric reader, I think we do.
It looks like mark
readers. A list.
Hmm!
Where does it actually.
**Trent Mick** 52:23 Oh! We should totally support this.
**Daniel Dyla (Dynatrace)** 52:24 Yeah, we should.
**Trent Mick** 52:25 Just looking. Yeah.
**Daniel Dyla (Dynatrace)** 52:26 What I'm wondering is he adds, the configuration for multiple meters
pushes, readers, dot push. Oh, it was already an array.
**Trent Mick** 52:38 Yeah, it was already an array. The environment variable accepts multiple values already.
**Daniel Dyla (Dynatrace)** 52:44 I was. Gonna say, I don't see anywhere where it's using like a multi metric reader, or anything like that. But it's all. If it's already an array that that explains it. I wonder how
that happened. In the 1st place.
Finally.
**Trent Mick** 53:00 What happened. In the 1st place.
**Daniel Dyla (Dynatrace)** 53:02 Well, how did we end up with it? The
array, like configuration, with only a single reader possible in like?
Why is it using an array property when it only accepts a single reader. It looks like somebody
maybe thought about multiple readers, but then
didn't follow through on it, or something.
**Trent Mick** 53:28 Yeah. Don't know the history.
**Daniel Dyla (Dynatrace)** 53:30 In any case, I'm totally fine with this.
**Trent Mick** 53:33 But, like the note SDK configuration used to just accept one span processor. Then we made a plural and deprecated same with log record processor.
**Daniel Dyla (Dynatrace)** 53:40 Yeah, I remember doing that.
**Trent Mick** 53:43 Going through it for every signal.
**Daniel Dyla (Dynatrace)** 53:45 It looks like, Mark requested. Changes.
I'm gonna go ahead and mark this, as I think we haven't accepted. Yeah.
cool.
**MG Marylia Gutierrez** 54:27 Yeah, now we're entering the one week Pr territory. So you might wanna keep more time to people to review.
**Daniel Dyla (Dynatrace)** 54:36 Yeah. Sorry you mean more time. It's like, take more time in this meeting on the issue. Or do you mean.
**MG Marylia Gutierrez** 54:42 Oh, no, no! I've seen like people probably didn't see the ones that you were about to open now, because now we are on the it got opened in the last week.
**Daniel Dyla (Dynatrace)** 55:01 Oh, this is just updating the example.
**Trent Mick** 55:07 Which is totally cool. So yeah, there's this long, slow process to go through all the examples.
And this is probably fine.
**Daniel Dyla (Dynatrace)** 55:19 Yeah, I think it's probably fine.
he said. He ran Npm start and got an error. Then he fixed the examples. My assumption would be that he
fix the examples to get it working for himself.
So it's also not published or anything. I'm not worried about it at all, signed the Cla.
I think I'm just gonna add it to the merge queue.
**Trent Mick** 55:47 Really, fast.
**Daniel Dyla (Dynatrace)** 55:49 Well, I I guess I mean
it's it's just the example. They're already way out of date, anyway.
I guess.
Yeah, I think I'm happy with just merging this.
**MG Marylia Gutierrez** 56:07 I'm just curious like, why not to update to the latest of the things? So, for example, Semantic mentions going to 1, 22 instead of the I don't know. We're at 34, 35 now.
**Daniel Dyla (Dynatrace)** 56:23 Hmm! That is a good question.
**MG Marylia Gutierrez** 56:26 I don't know how much is the level of the others, but.
**Daniel Dyla (Dynatrace)** 56:28 Already there. 1, 22.
**MG Marylia Gutierrez** 56:30 Okay.
**Daniel Dyla (Dynatrace)** 56:31 It's it looks like a changed line, because.
**MG Marylia Gutierrez** 56:34 Yeah.
**Daniel Dyla (Dynatrace)** 56:35 They reordered Trent's right. We could be a little bit more careful here. I think
I'll run it when I I'll run it after the meeting. I don't think it needs change log, though.
I got too excited about the idea of merging. Prs.
Wait, what happened? Oh, that's the wrong view.
We only have 3 min left, and I think we're this is
getting into very recent stuff, anyway. So probably.
**Trent Mick** 57:13 Just.
**Daniel Dyla (Dynatrace)** 57:14 Yeah, we could just stop add advisory attributes parameter to metric instruments. This is a big.
this is a big topic.
400 lines of code. Yeah, this is not something we're going through right now. And it looks like Mark already reviewed it once. So
I think we're we're good to call the meeting, for now, alright, I think we're
up to date on all Prs. Here for the 1st time in a long time, so.
**Trent Mick** 57:46 Nice.
**Daniel Dyla (Dynatrace)** 57:47 Feel pretty good about that.
I guess that's it. Thanks everybody for your time. We'll see you next week.
**Raphaël Thériault** 57:55 See you.
**Hector Hernandez** 57:56 Thank you.
**Trent Mick** 57:56 Thank you.
Let's do it.
