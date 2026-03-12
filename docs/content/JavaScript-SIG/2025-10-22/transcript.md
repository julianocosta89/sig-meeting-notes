SIG: JavaScript SIG
Date: 2025-10-22
Duration: 62 minutes
Zoom Recording URL: https://zoom.us/rec/share/A7B_xfkc4aWg7xAKZ4zLFxEUXN2Lz10Ejn16AaqLf9MD9hNR3HLP9pWTiJ54Xp8.RCXjsFWKT6Vlpyiq
============================================================

## Zoom Recording Transcript

David Luna Bistuer 00:02:22 Morning.
Hector Hernandez 00:02:26 Hello.
Marc Pichler (Dynatrace) 00:03:14 Hello.
Hector Hernandez 00:03:20 Hello.
Marc Pichler (Dynatrace) 00:03:42 Everybody… Let's get started. The first topic here is from Aurelia, feedback from, the survey.
MG Marylia Gutierrez 00:03:56 Yeah.
like, it's one of those days of, like, just… I feel like I'm giving a TED talk, just three topics, all me. But yeah, the first one is, getting a few more, answers from the survey. The majority is still giving, like, for the main repo, it's a lot of 5, with no comments, but a few recurring comments on contrib is a little confusion about the… because people are seeing, like.
I got an approval, but it's not getting merged. So why is it not getting merged if I got the approval? So I think it's not clear that… like, code owners can give the approval, but cannot merge. So I was thinking, like, maybe we can add something specific, like, on contrib, on how the process works, just to make it a little more clear to people.
Marc Pichler (Dynatrace) 00:04:45 Yeah, I think that would make, make sense. I think now, with the workflow, to add the labor when, when it has been approved might also be helpful. Yeah. But maybe having some sort of a… comment or something like that, to let people know that, it's gonna be merged in soon. Might be helpful.
I wonder if it will get better now that the label is on there, because then it should be easier for us as well to filter these things. We actually have one.
MG Marylia Gutierrez 00:05:22 Hi.
Marc Pichler (Dynatrace) 00:05:24 so… yeah.
I think that's… that's good feedback. One thing that I also… seem to require is that people who are not part of the organization can't see who's, In the requested reviews, section here. I think they can see SNEs, but they can't see, and see assigned reviewers. So that's also a source of confusion sometimes, because for them, it seems to be that, like, this reviewer section is completely empty.
Doesn't say, like, approvers are assigned as reviews… reviews.
MG Marylia Gutierrez 00:06:08 Oh, really? I have no idea that happened.
Marc Pichler (Dynatrace) 00:06:11 Yeah, I… I seem to remember that, being an issue in the community repo at some point, that… We never see it that way, because we are always logged in, and we have access to that, but apparently that section is not shown, but only this one here.
So… Yeah, I think there's a few tweaks that we can do, for sure, to make it a bit more apparent that But these things can be… can be merged in.
So I think that's a… it's a good point.
Also, having some sort of a, comment tool that outlines, like, hey, these are the component owners, and these should be pinged for review, could also be helpful already.
And then… We could, Yeah, wasn't sure where I was going with this, but there's some tweaks that we can do for sure, yeah.
And as always, if anybody is interested in… interested in making such tweaks, it's highly appreciated. So, if… You ever run through a process, and there's something that's not clear, it's always appreciated to update docs and stuff like that, to make things a bit clearer there.
MG Marylia Gutierrez 00:07:48 Yeah, next topic is… so, I noticed that it was happening the past two weeks, not just on this repo, but a lot of repos. I noticed a lot of people doing, like, very… tiny PRs, and then I realize, oh, it's Hacktoberfest, and maybe they don't realize that we are not part of it.
Because I'm seeing a lot of just fixing typos all over, and… because a couple of them, I was like, actually say, like, well, if you want to come, might as well get one of our good first issues, and then I went to check.
And we have one. So even if I try to, like, push people in to do it, we don't actually have things to push to people. So, yeah, I was just gonna say, like, if… when people have time, if you open, like, an issue, and you think the one that you created should be a good first issue, let's tag a couple there, just try to take advantage of that.
Marc Pichler (Dynatrace) 00:08:43 Yeah, that's, definitely a good idea. I, myself, I find myself not adding it too often for the reason of, I'm not sure if I'm gonna… going to have time to walk people through, the contributing process and stuff like that.
One thing that can be helpful is that if any of you know, like, you're gonna have some time to, help new contributors along in the next few weeks or something like that, is to go through and apply labors to issues that already exist as well.
And then helped us out. I think that's, That's always appreciated. It just is some time effort that, make sure to block some time to, make sure you can get to, get to help people.
That are, looking to do things.
MG Marylia Gutierrez 00:09:38 And even if you don't have the time, point people, we do have a new channel that is Hotel New Contributors, that a few maintainers are there to help this out. That was precisely because a couple people don't know where to start, so we have a few… just, like, give some guidance on general stuff on how to contribute it, and we have people from different repos, just to make sure that, like, okay, this is for this repo, this is how you do it, to at least give some pointers to people, but we… do… it is a very recent, Slack channel, but that is a good one if you want to point people to it as well.
Marc Pichler (Dynatrace) 00:10:18 That's a, it's a great idea. I think it would… probably even be very helpful to, note that in Contributing MD, to… Let people know that this is where one can go if they're a new contributor.
Because I think often it's not completely apparent to folks that we even have, like, a CNCF Slack and stuff like that.
So, yeah.
MG Marylia Gutierrez 00:10:52 Yeah, and even not all six has the, like, dev channel. That is something also we were trying to align, make sure it's a lot of SIGs have that, so we can focus just, like, on development for contributors. But still, we are still, like, trying to find ways to let people know that those channels exist, which so far has been, like.
whoever, like, we… I created the channel and, like, posting on, like, LinkedIn or Blue Sky and stuff like that, but the majority of people that I know there are already, like, contributors, so it's… it's a little hard, but I… Yeah, if we can, like, help putting, like, the word out, but yeah.
Marc Pichler (Dynatrace) 00:11:35 Boom.
Yes, I will definitely look for some places to add this, if you have some, a little bit of time to add it to contributing MD, I think that would already…
MG Marylia Gutierrez 00:11:49 I can do that.
Marc Pichler (Dynatrace) 00:11:50 Get the word out a little bit. Yeah. And, yeah.
We can see if there's other places where we can add it to, I was starting to work on, like, this pinned issue for, like, things to do around the repo that need to be done all the time, like core chores and stuff like that. It might also be a good place to put this.
And then pin it, so that… People who are new to the repo can see it immediately.
Yes, but I fully agree we need more good first issue things as well.
MG Marylia Gutierrez 00:12:34 Any other questions on this one? Or I have the other one?
So the other one is a little more of a FYI, in case people are not following and starting to think the things that we can do is related to OpenTelemetry graduation, so there was some feedback Basically, on areas that they want to see improvements before they actually mark as graduated, but it's not like all… they kind of, like, divide it in four areas, and it's not like we have to do those four areas in the next six months, but it's… Pretty much, like, good to have.
And a few of them.
we need still guidance on, like, GCTC level. Like, for example, one of the things that I see happening a lot, I'm assuming you will see with your customers as well, is people don't really understand what stable means, and it's a lot of, like, okay, this instrumentation is stable or not is just because it's not following the semantic convention, but it… some of them, like, don't follow, but that does not mean they're not production-ready, or they're just, like, full of bugs. It just means that it might change the metric name, or something like that. So there is one, idea of just decoupling semantic convention stable, and instrumentation being stable, so you have, like, two labels. But for that one, there's nothing we can do at this moment. They are gonna open, like, issues to get feedback from people. The ones that we… can start thinking about or doing stuff about. One of them is related to performance, so maybe we can have, like, some tests just to see how our SDK is doing, any areas that we could improve.
There is one… So the one about quality is that they are considering if they should have, like, one big version of OTEL that, like, tests with the latest version of everything, just connecting to each other. For example, the SDK connecting to the collector, and say, like, those two versions work together. But for that one, they're thinking, actually, maybe creating a SIG specific for that.
So, for now, it's just, like.
Keep in mind, whatever we can add for tests.
And the other thing that we can do now is related to documentation, because there is the feedback that people do not like to go or cannot find documentation on GitHub, and they, like, end users prefer, like, the official hotel docs.
But a lot of our stuff is not there, so there is something we can start bringing the existing documentation to the official, basically, documentation page. And when we are doing this, there's also a chance, because we… we got, like, some good feedback that we are one of the few that have on our packages saying, like, is it stable or not? Is, like, in a good, like, label for ours? But that is a good chance to see if any of our stuff that is market experimental should be actually updated to stable, because it has been for a while.
But I think now, maybe that is even, like, one thing that we can mark as good first issue, just copying documentation to the official, but we just need to think about a good structure to add our stuff there.
And… yeah, I think that is the gist of my TED talk.
Marc Pichler (Dynatrace) 00:16:08 Yeah, thanks for bringing all that up. There's… Quite a few things, especially in this, Recommendations document, that we would probably need to need to address here, I think I saw… like… This one here seems to be a tricky one.
But, yeah, there's, lots of things, I'm wondering if we should… Like, start creating issues for these sorts of things, especially the moving the documentation and stuff like that is, I think the first part would be identifying which ones we actually want to move.
MG Marylia Gutierrez 00:16:57 And there's quite a few ones that are…
Marc Pichler (Dynatrace) 00:17:00 actually outdated, which we would probably want to get rid of. So identifying that as a first step would be… Probably a good issue to define, and then we can break that down into smaller chunks, and mark these things as good first issue, once we've done the research of what should go where.
But I think that's a really good point. I, myself, find myself using, OTLIO more than the GitHub docs, so I can see end users doing that as well. That makes sense.
Jamie Danielson 00:17:34 Like, anytime you're maintaining docs in two different places, you're gonna have drift, and so, like, the most ideal scenario is probably if we could have, I feel like, the docs in the repo that get, you know, either automatically or somewhat manually brought over to the public site, but… in practice, that's really hard to do, especially since all the different languages are there, and everyone has different setup and everything, so it probably makes sense to just have very bare minimum in GitHub.
as a… just a rule, and maybe a link to the main OTOL site.
almost in every pack… I don't know if we already do. I don't like the idea of us necessarily doing direct links to pages, because if those move, then we have 404s and shit to deal with, but… That might even be a thing, like, for more documentation, go to Opentelemetry.io, and it's kind of a reminder to not put stuff in there.
MG Marylia Gutierrez 00:18:27 Yeah, and it even adds localization on top of it, which is… As soon as, like, I finish, like, translating something, and we do have a script that let us know if the original English, like, changed.
Jamie Danielson 00:18:41 Whoa.
MG Marylia Gutierrez 00:18:42 So yeah, we have one that… this is why we were asking, like, that PR, is that every time you create a localization one, you have to add an extra value on the title, which is, like, which commit you base your localization on top of it. And we do have a script that basically checks all this time, and whenever it changes, it adds an extra one, say, like, Drift, pretty much. So from time to time, we have to go back to all the ones that are marked drift, and update, whatever it is, so it is a never-ending thing.
Jamie Danielson 00:19:17 Yeah, that makes sense. I was wondering how those stayed up to date. Like, once I saw when the localization efforts first started, I was like, I hope there's something that lets people know when something changes.
MG Marylia Gutierrez 00:19:29 Yeah, and the Portuguese one, for a while, it was just me, so now I have another person help me out, and he's helping with the Spanish as well, so that's been helpful.
Jamie Danielson 00:19:45 We have, like, a docs directory, too, right, of some of those things should maybe be moved over. Like, that's where we put the… ESM support, and…
Marc Pichler (Dynatrace) 00:19:55 A couple other things.
MG Marylia Gutierrez 00:19:57 Yes.
Marc Pichler (Dynatrace) 00:19:58 ESM support is a big one, that… like, anything that's geared towards end users, I think, makes sense to have on… on OpenTelemetry I.O, and anything that's for people developing, I think it makes sense to be here.
Jamie Danielson 00:20:14 Yeah.
MG Marylia Gutierrez 00:20:15 Agree.
Marc Pichler (Dynatrace) 00:20:16 So…
MG Marylia Gutierrez 00:20:17 Yeah, I can create the issue, I can create, like, the General one, and then we can start creating, like.
Issues that we just, like, use that one to kind of, like, track the others.
Marc Pichler (Dynatrace) 00:20:30 Yeah, and I think one that already exists on the OpenTelemetry I.O. repo is this here, the upgrade to 2. OpenTelemetry I.O. I'm not sure if that was done yet or not.
Jamie Danielson 00:20:49 didn't seem like it. I came across that issue yesterday. I'm finally catching up on all of the old notifications, and I think that's still, like, an open request to move this over there.
Marc Pichler (Dynatrace) 00:21:04 Yes.
Yeah, but I think having the issue there, and then having sub-issues is a good first step, and then we can… Continue on, to other things once that is done.
There's also probably a question of… Where do examples go? And how many do we want to have?
Especially because a lot of our examples right now are outdated.
MG Marylia Gutierrez 00:21:32 I'm more concerned with the contrib one. Are we creating one README for each of the packages? Because I feel like that is the one that I'm thinking the most, like, there is a lot there, and we need to move all of them.
Marc Pichler (Dynatrace) 00:21:48 I'm not sure I fully understood now the examples you mean, or the.
MG Marylia Gutierrez 00:21:52 No, like, for all the packages we have there, they have their own, like, README on how-tos, so I'm assuming all of those we want to change. So I'm just saying, like, we have a lot, yeah, like, all of those.
So…
Marc Pichler (Dynatrace) 00:22:06 Yeah, having had that in there, the usage.
MG Marylia Gutierrez 00:22:09 Yeah.
Marc Pichler (Dynatrace) 00:22:10 Vegas?
To some extent, it, makes sense to have that in greet me here as well, because when you go to, NPM, JS, and you're looking for a package, then…
MG Marylia Gutierrez 00:22:28 Newport here.
Marc Pichler (Dynatrace) 00:22:28 We will also be shown here. So moving all of them might be a bit tricky.
It would be interesting to know how the collector folks are doing it, because the contrip, Collector has asked quite a few.
Components that have their…
Jamie Danielson 00:22:48 The same issue. Yeah, I think they have the same issue that they're trying to sort out, exactly the same, because they have a ton of docs in GitHub itself. Like, the, like, OTTL stuff, there's a ton of examples in the GitHub repo, and so they're trying to figure out How much to move over, where to put it, things like that.
Java? Does Java have it done right, probably?
I know they had, like, at least some examples.
MG Marylia Gutierrez 00:23:17 Yeah, we… I know that we did, like, a restructure on the Java, docs, like, on hotel.io, so maybe we can also take a look.
And see if we can, like, use the same format for a couple of things.
Jamie Danielson 00:23:33 Oh, and they have their repositories listed.
And, like, what each of the things are. Yeah. It's kind of cool.
MG Marylia Gutierrez 00:23:40 Yeah. Yeah, that was the one that we just did, like, a whole big restart. Like, forget everything that we had for Java, and then create it from scratch. Like, what will it look like now?
Marc Pichler (Dynatrace) 00:24:06 Lots of work. Yeah.
Lots of work ahead.
Jamie Danielson 00:24:13 But at least now that there's, like, that one's done, that's like a guide, which is helpful. I feel like doing the first one is the hardest, and so this also makes it easier to… Maybe have some of them be good first issues, too, of just, like.
do this part of this page matching how Java does it?
Maybe.
Marc Pichler (Dynatrace) 00:24:33 Fact.
a Java agent, being… more feature-rich than what we have might complicate things, because they have a lot of fancy, Fancy stuff built around.
The basics to make things easier for users.
MG Marylia Gutierrez 00:24:57 Yeah, there is one project that, actually, is a colleague from my team that is working on Java, and he's looking for, like, okay, what is the next repo that he's gonna start working on it? And I kind of, like, okay, we can do it in JavaScript. It's gonna give, like, be a lot of work.
But it's gonna be really helpful. That is… it's pretty much, like, he's calling, like, the metadata project that basically say, like, for each instrumentation, what exactly is sending? So it actually runs every night, whenever there is, like, a new change. So you can actually compare with, like, semantic conventions, and say, like, see, this is completely compatible, this is not compatible, and is this emitting, like, this data and that data?
So you can see very clearly, for all the packages, what to expect.
Jamie Danielson 00:25:43 Is that something that'll be public? Because that seems like it would be super useful.
MG Marylia Gutierrez 00:25:47 Yeah, so he's already adding that for Java.
And then I think he… then he's… now he is working with the docs team on how we can add this to the official documentation. So, it's kind of working for Java, so… but the hard part is doing the manual part of, like.
actually storing, like, all the information that it needs. So that is the part that takes a long time, and hopefully we can add this for all other repos.
Jamie Danielson 00:26:17 Yeah, cause, like, there's some of the stuff that we've… I feel like, like, the semantic conventions, for example, right? Like, we manually crafted the table based on whatever was there, and people occasionally do ask, like, what should I expect coming out of this instrumentation? So it'd be nice to have that just automated instead of… Either non-existent or handwritten.
MG Marylia Gutierrez 00:26:40 Anthony.
Marc Pichler (Dynatrace) 00:26:40 So, sounds like, it could be something that's interesting for reviewing changes, if there's a way to… like, figure out what changed in the PR, that… yeah, we immediately see that there's something different now, or something doesn't match, whatever SAM conversion we say we support.
Jamie Danielson 00:27:08 A lot of potential.
MG Marylia Gutierrez 00:27:10 Yeah, if you wanna just take a look, like, this is the UI for it. Share here.
Marc Pichler (Dynatrace) 00:27:17 I will stop sharing one second, if I can find the button.
MG Marylia Gutierrez 00:27:21 Oh, I just, I just shared the link on the, the chat, yeah.
Marc Pichler (Dynatrace) 00:27:25 Weird that over.
share again.
Jamie Danielson 00:27:33 Well, I guess it's sort of similar, like, the collector has that, right?
Where it automatically… it, like, generates… Basically, the metadata In there somewhere.
MG Marylia Gutierrez 00:27:49 Yeah, so see, like, the first one is showing, like, the semantic conventions that are related to this one, and you can kind of, like, compare between versions, or stuff like that.
So those are the ones for Java, pretty much.
Like, if you click on, like, the actual… yeah, then… Does it say, like, what is compatible to Mentic convention, what is not?
Marc Pichler (Dynatrace) 00:28:26 That's really cool.
like this.
Alright.
I guess there's time to talk more about docs or other things if anybody wants.
MG Marylia Gutierrez 00:28:52 Okay, as a reminder for everybody, don't forget, next week, elections for GC.
Marc Pichler (Dynatrace) 00:29:01 How long will they, when will it start again? It's Monday, Tuesday, and Wednesday is where you can vote.
MG Marylia Gutierrez 00:29:09 And if you see the names, it's gonna be a familiar name there. Hi.
Marc Pichler (Dynatrace) 00:29:22 Right, I will keep that in mind. I will be out of office next week, but I will take some time to go and vote everybody.
MG Marylia Gutierrez 00:29:29 No, it's not important. Voting for Maria That is the important part here. Put in an alarm, doesn't matter what you are, everybody here. I have some friends that were saying that they were just gonna have a t-shirt saying, like, both Amarilla and Join call.
Marc Pichler (Dynatrace) 00:29:50 Alright, That's, it's a good reminder that the election is coming up. I would have, probably missed it. So, thank you for bringing it up.
Alright.
Any other topics that we want to discuss?
If there aren't any, then I guess we can move on to our favorite part of the SIG meeting, which is issue triage and PR triage.
As always, if you have something that comes up while I'm talking here, or while we're going through the issues, please feel free to just interrupt me, and then we can go back to the agenda and talk about your topics.
Alright.
The first issue here is unable to use OTRP metric exporter.
with common JS.
That doesn't sound too great.
callback was invoked without… I'm not yours.
That was, I think, from the change… But… introduced, what's it called now? The…
David Luna Bistuer 00:31:33 the usual agent factory.
Marc Pichler (Dynatrace) 00:31:35 Yeah, the… not the usage of victory, I think.
David Luna Bistuer 00:31:38 The HCP agent, sorry, sorry.
Marc Pichler (Dynatrace) 00:31:40 Yeah, the HTTP agent, yeah.
I was under the impression that that one would actually be rewritten to require for Or the common JS.
thing on… When it gets transpiled.
I'm pretty sure we had been using that in the… And resource detectors for longer now.
So it's a bit surprising to me that this is happening.
That's not GS20.
So that's definitely something that we should support.
Though I'm pretty sure I have used, I've used that exporter before with, like, an… Or the Node.js version, even today already, so it's a bit… A bit confusing to me that this is happening.
Jamie Danielson 00:32:56 I guess we should probably ask for their tsconfig, right?
Raphaël Thériault 00:32:59 I think that's specific to Jest.
Because that config flag, you need to pass it to Jest to be able to support dynamic import, and the example code that we're showing looks like Jest to me.
Jamie Danielson 00:33:10 Yeah.
Yeah, and that's their dependencies, it's all just, yeah.
Marc Pichler (Dynatrace) 00:33:21 That's interesting.
So… I guess it's a s… It's safe to say that this is not happening in production, because we would have probably noticed a long time ago already.
So… Are put, out here.
OTRP, export a base on here.
Jamie Danielson 00:33:54 Yeah, like, maybe we should ask, like.
have you tried it in production? It's implied, I think, that it doesn't work in production, and they use the test to prove it, but… It seems like it would be good to confirm, like, if they have a… a repro.
Marc Pichler (Dynatrace) 00:34:11 it… it would also make sense that they just tried to update it. They figured out that it's not working, and they never… it never went to production for that reason. Right.
So, the tests are blocking.
Them from actually going through with it.
I might assign this one to myself, and look into it a bit more. I haven't used chests in some time now, so… I tried to come up with a way to reproduce this, and then, I'll put a comment here.
with updates on what I've found.
I think it's a good pointer that, this is likely chess-related.
own… It would still be interesting, though, to see if, the… Actual code that we publish has the import in there.
And it must be in there, because otherwise, They wouldn't be running into it, so… It's just… oh… What is it? HTTP exporter transport?
That actually does have the import thing in there.
That's really interesting.
I was convinced that it would rewrite it to… Required at some point.
Raphaël Thériault 00:36:00 Yeah, I think it could be that, like, I remember the TSconfig being migrated to use, like, module resolution node 16, which I think no longer translates that.
Because it assumes, like, node 16 and up do support dynamic import.
Marc Pichler (Dynatrace) 00:36:27 Oh.
Lost pain.
Either one of these two, I suppose.
Raphaël Thériault 00:36:35 Yeah.
Because I know if you set it to, like, CommonJS, it does translate them, but the newer, like, Node 16 and Node 21s don't.
So that's probably been, like… there's been some dynamic imports in some code for a little bit. We probably just didn't run into it in tests.
Marc Pichler (Dynatrace) 00:36:58 Yeah.
Right.
Thanks for all the context. I will, have a look at this offline, and then… I will properly assign a, priority to this.
Ideally, it would be… us maybe changing some of the tsconfig, and having it compiled down to the require again, and then… It might start working for them.
Yeah. That's… Yeah.
Could be probably helpful, too.
Also have it working in chess.
Because a lot of people are using that for testing.
Right.
Yes, that's this one here, that's sent to me, so we can move on to contribute now.
Let's see, this one here is Instrumentation Express.
I'm gonna make cream.
B.
That's just a Kent, right?
I don't know.
Jamie Danielson 00:38:41 booze.
Marc Pichler (Dynatrace) 00:38:59 I guess we don't know exactly which versions they're using there.
Floni example for OpenTelemetry Instrumentation Express.
Maybe the example is outdated.
Physicists, you're right.
doesn't report all the spans with Express 5, and Express 5 was added some time ago.
But not too long ago, so…
Jamie Danielson 00:39:40 Yeah, the example app is still using Express 4.
Marc Pichler (Dynatrace) 00:39:47 Alright, yeah, then I think that's a documentation issue.
Jamie Danielson 00:39:53 You can assign me to it, if you want.
Marc Pichler (Dynatrace) 00:39:57 Thanks, Cheryl.
I'm… what… E4 on this, because it's… Really just documentation and updating to the latest version should… Solve the issues.
Jamie Danielson 00:40:20 Oh, it might be a good first issue.
Marc Pichler (Dynatrace) 00:40:24 Might be.
MG Marylia Gutierrez 00:40:24 No, everything now, no, it's good for this year.
Jamie Danielson 00:40:27 Everything is a good first issue.
MG Marylia Gutierrez 00:40:30 If you try hard enough, you can do it as the first one.
Marc Pichler (Dynatrace) 00:40:36 I guess the resolution for this could also be to just spin off a new issue, let them know that this is the problem, spin off a new issue to update the documentation, or update the packages in the example.
then, mark that as a good first issue.
Follow.
Since I probably, they will be… I'm happy to hear already that, like, just updating it will solve the problem.
And then, there's… Not too much time pressure to actually get the… Example update done.
Alright, thank you for picking that up.
And the next one is… Spans are not visible in Jacob when running all the management. I looked at this one earlier, This is running a supported version still, and… They seem to have trouble.
get their spans into Jager. I actually tried to reproduce this both.
with this… Reproducer here, because it's fairly… It doesn't have too many dependencies, and it's fairly minimal. I tried to reproduce this myself.
That's weird.
But the spans are actually showing up, so… I guess I'll keep that at needs reproducer for now. Unless… anybody knows Immediately what the problem could be.
they're running into.
there's nothing really obvious sticking out, so I wouldn't expect anybody to, To know it immediately, but yeah.
or actually also assigned this one to myself, to make sure it doesn't get lost in my inbox.
Doesn't help always, but helps sometimes.
Right.
And I guess we can move on to Old Country PR triage.
Alright.
So, the first one has actually activity on it, which is nice.
Marten Hennoch 00:43:11 Yeah, CM fixed everything, I think.
Marc Pichler (Dynatrace) 00:43:17 Hopefully.
Marten Hennoch 00:43:18 So we can get rid of it.
Marc Pichler (Dynatrace) 00:43:21 Yes.
There's a few more things, Yes, I'll give this another review, I'll just assign myself.
And… Let's see that we can, get this merged so that it doesn't show up next week again. Alright.
East here didn't have any activity.
So we'll skip them for now.
We have… This one right here, with the environment variables.
Oh, no.
Jamie Danielson 00:44:25 Oh, that's the one I was starting to look at. Yeah, we were looking at weather environment variables or code.
Should win, and we're not consistent.
Actually.
Marc Pichler (Dynatrace) 00:44:38 Yeah, that was… I was actually wondering if the way we could do it, Because there's, like, one or two places where we are inconsistent in, like, who wins. I think it's the resource detectors.
in… SDK node.
End.
That's, I think, one of the… Only two outliers that we have.
The rest does something along the lines of Having the code provided, config win.
Whenever it exists.
Unless it can be merged, then it merges it together.
Except in a few places where it actually, like, it could be merged, but we don't do that. I wonder if it would make sense to just align these cases, where it could be merged, we merge it, and where it's not possible to merge it, we just override.
And have that be on you, Way of going about things that's consistent, and… And we could also let them know here that, We would still have the programmatic config be… the… be the thing that wins, unless, like.
There's one instrumentation config that, like, is not set in the programmatic config, and you set it in the environment variable, and then you just filter it out.
Could be one of the ways to go about it.
Not sure yet.
In any case, I don't think it's something that we can source on the card today.
Oh, So Let's skip this one for now.
And we have… Instrumentation AMQP.
I actually looked into this one with, wow, from the SEMConf.
seek, and I opened this issue here, because while I was talking to him, I… Founded, the… Where was it?
GenAI semantic conventions actually have this neat little… an AI latest experimental thing, which I kind of love, because it says experimental, and it lets people know that things might change, and it also would allow us to update to the latest SEM cons.
Without breaking everybody immediately.
So… That one is… marked as accepted, so I will actually issue a PR, towards the semantic conventions repo, and… we'll try to get that in, and then we can continue with this PR.
bye.
recommending the OTERSM constability opt-in Messaging Latest Experimental.
And the work isn't lost that the person did here, and people can start using it if they want to.
So that's the update on this one. I will… I think I'm already assigned on this one.
Yes, good. So, the next one is… SQS contact propagation… I think we talked about this last week.
I think Brad agreed to look into this one.
Just… Mostly.
Things to be… Lambda spec still does… Mention something here… Later was, romantic conventions… Bing?
That's… Right, change something like this.
Pretty old already, so I must be misremembering.
Birds.
Get this link and put it on the list of things to do, whenever… oops.
Uber, reach out to… Print… If there's an update on this… Alright, this is the langchain instrumentation. There's been no activity, and I haven't looked into it, further yet.
Understood.
Redis Cluster Instrumentation support.
Which also didn't have any activity.
I guess most of these are just sitting, waiting for, technical reviews, but it's something that we… are somewhat in agreement that we want to add, so… If anybody has time to… Review that feature, it would be, would be very much appreciated.
So, the next one is… hoisting RF dependencies to root.
volume.
What a disruptors in NPMCI.
It actually seems to have started working now again.
So… Yes, we should be okay. I'm gonna wait for, Trent to be back, as he seems to.
have the most context on this PR here.
But yeah, I think overall we're in agreement that we want to do this, because I think it's not possible at the moment to npm install in one of our sub-packages. We always need to install the whole monorepo.
Nowadays, so, having them hoisted, makes sense in that regard, and also avoids having, drift in the… Different package versions, which can be annoying.
Alright, this one here… Things already assembled, so… let's skip that one.
This one has… Owner approval, I will merge this in later.
Then… There's this… Fixed.
Or instrumentation runtime node.
Use absolute results in event loop utilization.
Jamie Danielson 00:54:36 So it looks like they're working.
Together, towards fixing it.
Marc Pichler (Dynatrace) 00:54:41 Yes.
It was 18 hours ago, so… I don't think there should be… Well, on its way to getting merged.
And this is, initial package skeleton for instrumentation length chain.
If anybody has time, please feel free to also have a look at this one. As I said earlier, I will be out next week, so, It might be that, you have to wait a bit longer for me to, Respond to things.
So, anything that can be taken care of.
In the meantime, let's, very much, appreciated.
Right, that is just renovate bot doing… renovate things.
I'll just leave this as well.
Or maybe we'll just merge this in because, hey, then we can at least cross one PR off the list.
Alright.
Alright, Damn.
Never.
Which I also wanted to get to, This actually seemed reasonable to me, if I recall correctly, but… With these things, I like to, try it out.
before, to make sure I get everything right, because I'm not too much up to speed on every instrumentation, so… Keep forgetting the details, because there's just too many of them.
Alright, this one has a sponsor, which is Trent. There have been… Some comments, so… It's also on its way.
Then we have… BlockFair maintenance.
That one will get updated.
I renovate Bot… And then there's… Just a new cross identification instrumentation.
David Luna Bistuer 00:57:53 I'm debating this one.
So…
Marc Pichler (Dynatrace) 00:57:55 Sorry?
David Luna Bistuer 00:57:56 I'm reviewing this one, so hopefully I'll have some feedback today, or maybe tomorrow.
Marc Pichler (Dynatrace) 00:58:03 Awesome, thank you.
That sounds good.
This is just, hmm.
No more bootstripping.
One thing that's important now, with the new publishing process is if any of you ever run into a new package and you merge the PR, please also open an issue and assign it to me, that I actually publish the package to NPM first.
Because with trusted publishing, I have to do that manually the first time that the package is created. After that.
it works, but you can't publish new packages using the trusted publishing process. You need to… Do it, do it yourself first, and then, it starts working, so… Just a heads up. Is that just for contract?
MG Marylia Gutierrez 00:59:08 Or for…
Marc Pichler (Dynatrace) 00:59:09 That's for country band core as well.
MG Marylia Gutierrez 00:59:11 I'm thinking, like, the configuration one that I created, so I need you to do something?
Marc Pichler (Dynatrace) 00:59:16 Yeah, for the instrumentation one, what am I saying? The configuration one.
MG Marylia Gutierrez 00:59:22 sufficient, yeah.
Marc Pichler (Dynatrace) 00:59:22 Yeah, it would also make sense to have, an issue. So once we remove the publish, what is, like, publish config private or something, that's set, once we remove that, I should also go in and, publish that.
once we.
MG Marylia Gutierrez 00:59:43 Yeah, because my goal is, I have only one PR open. After that ones get merged is when I want to start using now in another repo. So I guess as soon as that gets merged, I… Open the issue and let you know?
Marc Pichler (Dynatrace) 00:59:57 Yeah, so… it only needs to be done, really, on the day that I, or we publish the next release. So there, usually the pipeline will run, and then it will fail on that package, and then I have to go in and do it. But knowing it ahead of time is usually helpful, especially if It's being used in… let's say the country repo or in the core repo is a dependency of some package, because if the… Configuration package wouldn't be published in that case, then publish for the package that depends on it would also fail.
So we need to make sure that, like, everything's kind of sorted out there.
MG Marylia Gutierrez 01:00:46 No, just think about the order, because… how I'm gonna put as a dependency on another if it hasn't been published yet.
Marc Pichler (Dynatrace) 01:00:57 So in… so if you're doing it in the core repo, let's say one of the core repo packages, depends on the configuration packages, then it will just link it up, locally first.
So that won't be an issue. But as soon as we publish it, we need to also publish it to MPN. Yeah, that's… it's one of the, changes that we did with the workflow in the trusted publishing thing. It's not supported to… create new ones, unfortunately, I noticed immediately on the first two releases.
All right, looks like we're out of time for today. Thank you, everybody, for joining.
I won't see you next week, but I will see you the week after that.
have a nice… Have a good time until that, and see you. See ya.
Jamie Danielson 01:01:55 Thanks, everyone.
Raphaël Thériault 01:01:56 Thank you.
Marc Pichler (Dynatrace) 01:01:57 Thanks, Laura. Bye.
