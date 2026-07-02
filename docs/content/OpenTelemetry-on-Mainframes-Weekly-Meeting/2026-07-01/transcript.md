SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-07-01
Duration: 37 minutes
============================================================

## Zoom Recording Transcript

**Ruediger Schulze (IBM)** 01:38 Hi, Antoine.
**atoulme** 01:39 David, how are you?
**Ruediger Schulze (IBM)** 01:41 Good.
**atoulme** 01:43 Okay, so… let's get that…
**Ruediger Schulze (IBM)** 01:47 Might be a smaller group today.
**atoulme** 01:51 Yeah, you need something to approve? I should have temporary rights to approve things.
**Ruediger Schulze (IBM)** 01:57 Yes, and that's actually what I wanted to discuss, and also a few other questions, obviously.
**atoulme** 02:04 Okay.
**Ruediger Schulze (IBM)** 02:06 So, that'd be, yes.
**atoulme** 02:14 Oh, wow, that's a lot of CI.
**Ruediger Schulze (IBM)** 02:17 Deadly, yeah, it is.
**atoulme** 02:19 Nice.
**Ruediger Schulze (IBM)** 02:20 Essentially, the copy of… I think I have it already off in front of you, but… Yeah, so it's essentially what the GenAI repo has for CI.
And also for generally working with semantic conventions, being brought over here to… The mainframe repo.
**atoulme** 02:43 Nice.
Beautiful.
**Ruediger Schulze (IBM)** 02:46 Actually, I should be here.
I started to adjust a couple of things, but, you know, this definitely needs more work.
But what I wanted to, yeah, essentially get done is that we have a starting point.
**atoulme** 03:01 Exactly.
**Ruediger Schulze (IBM)** 03:01 And, yeah. If you… if you… It's a lot of fires, obviously, but if you maybe can go through, and if you feel it's okay, and, you know, give your thumbs up, that would be great.
**atoulme** 03:15 Yeah, so my approach to this type of things is that there is nothing right now, so whatever you have is better than nothing.
So, I'm more than happy to approve it.
**Ruediger Schulze (IBM)** 03:26 Okay, that's great.
**atoulme** 03:29 Dude, always work. Okay.
**Ruediger Schulze (IBM)** 03:30 Perfect. Then, actually, supposedly should go through.
**atoulme** 03:34 You wanna scratch your American?
**Ruediger Schulze (IBM)** 03:36 Yeah, let's do that. Let me have it.
**atoulme** 03:39 It's easy.
**Ruediger Schulze (IBM)** 03:40 Okay.
I have, at least one more topic that I wanted to discuss. Okay.
I wanted to understand, you know, a little bit the position around reference implementation.
And when I think about reference implementation, specifically what they… hey, Greg.
**Greg Shriver** 03:59 Hey, Ola, sorry I'm late.
**Ruediger Schulze (IBM)** 04:01 No worries. What the GenAI semantic conventions did, obviously, they have these different Gen AI libraries, frameworks, and… You know, with a proper model or some, you know, testbed behind that, they can generate true data.
**atoulme** 04:18 Yep.
**Ruediger Schulze (IBM)** 04:19 Obviously, from our perspective, it's a little bit more tricky. Access to a mainframe environment is not as straightforward.
And also, for some of these things, we don't have implementations yet.
So what I was actually rather thinking, if we could go with synthetic data and a simple Python implementation, for instance.
And, generate this type of data, that we would expect.
from a… It's not so much from the value domain, it's more from, okay, this is the names, this is the metrics, this is the structure of the data that someone would expect, and then over time can evolve that.
**atoulme** 05:04 Did you know that Weaver does that? I think Weaver has the ability to do that already.
**Ruediger Schulze (IBM)** 05:10 Okay, I'm aware, but we were allowing you to validate, for instance, data, and… Obviously also helps you to set up the documentation, but you say it also gives us a way to produce synthetic data?
**atoulme** 05:24 Yes.
**Ruediger Schulze (IBM)** 05:25 Okay, I need to look at that.
Yeah, that sounds good.
**atoulme** 05:29 registry emit.
Try that.
We could try that in the repo.
**Ruediger Schulze (IBM)** 05:37 Okay.
**atoulme** 05:38 So you can emit that, and then you can… oh, you have to send it to another.
**Pellared** 05:41 You know?
**atoulme** 05:42 Okay.
a little trick.
**Ruediger Schulze (IBM)** 05:45 Okay. Hi there.
**atoulme** 05:48 Yeah, I think if we can use Weaver for most of this, that will help a lot, in terms of maintenance.
And I like the other thing from Weaver, which is the life check feature, so what you could also do is say, we don't have the ability to just summon a mainframe, but we can make this, we can set this at the output of a mainframe, and just run the life check, and see if it passes, right? Right, exactly.
**Ruediger Schulze (IBM)** 06:18 Right.
**atoulme** 06:18 So, this allows you to have some sort of a discussion with the implementers afterwards. It's like, I was expecting those three attributes, I don't see them the right way, or they don't pass validation, let's discuss exactly what's going on here.
So… Yeah, that probably is gonna help a lot.
**Ruediger Schulze (IBM)** 06:37 Sounds good. Let me have a look at what Vivo would give us.
For the moment, I just kept the, you know, structure within the repo for references, but, you know, this is something to explore, obviously.
**atoulme** 06:49 I mean, it didn't look bad to me. As long as you have a registry that Weaver can make sense of, we're good.
**Ruediger Schulze (IBM)** 06:55 Yep, yep.
And then the other topic, just to mention it, I was on this semantic convention SIG meeting on Monday.
And, obviously also for GenAI, they didn't go yet through the release process, and Lydmilla offered that once we are there, we actually can go through, together, through this initially for, for confederated, repose, which would be, I think, good. So, let's say the big ambition is here that we, you know, in the next four weeks, maybe produce something, what we would call an initial release of… Semantic conventions for the mainframe.
Then goes through the release cycle, and obviously also establishes, you know, among This, this proof here.
But then we then have also all processes in place, and then can actually get things rolling more.
Quickly.
**atoulme** 07:54 Okay. That's… That's good news over all of our… Okay, so with that merged… We have something to look at.
We can iterate on this, we can emit some of the telemetry.
We can generate some, some front-end or whatnot, like, to try this out and see how it looks like, and then we can work from there.
**Ruediger Schulze (IBM)** 08:18 And just, yeah, I mean, obviously, right now the model is very minimal, it only has what we had before there in the base repo.
But, I have a, you know, some time over the next days and wanted to get started to put things in there.
And, then you have something more specific also to discuss from a… Naming point of view, and so on.
**atoulme** 08:43 Yeah, it should be fine.
Yeah, we can, we can open that up and discuss more.
What do you want to do next in…
**Ruediger Schulze (IBM)** 08:55 So, I mean, the way we always started to discuss this, even from the beginning, was to, you know, have a… One approach is to go from the HMC point of view.
**atoulme** 09:06 Yes.
**Ruediger Schulze (IBM)** 09:07 And, I think we discussed this even here once. There is a HMC Prometoise exporter, which writes Prometoise telemetry, and obviously this has Prometoise.
metric names, so getting them over into something that is open telemetry-like, and also reflects the model that we want to have in mind later on, right? So, Yes. Supporting this whole idea of what we discussed also here in this group.
Virtualization versus mainframe-specific representation, so, you know, we have with the mainframe, we have the LPAR, or the… More at the hardware layer.
Type of virtualization, and then we have, obviously, other ways of virtualization as well.
And I think one of the activities in this space is really to Look at how we want to do this from a mainframe point of view, but also there's this introduction to what we discussed to… generally how to represent virtualization within, open telemetry.
So, what we can do here is to give it a start, but probably, in some way, we also want to reconcile with, you know, general discussion around virtualization.
**atoulme** 10:27 these tools. This means that vibrational concepts and prior experience are not just night… Sorry, guys. Sorry. I'm not easy.
**Ruediger Schulze (IBM)** 10:35 So, this is… this is one site, and then obviously spans, right? So we discussed lots of, you know, times already about spans.
There's this long-lasting TPS PR, I think taking this or bringing this over is one of the next activities as well.
**atoulme** 10:54 Okay, so let's… can we open issues on that, so that we can start…
**Ruediger Schulze (IBM)** 10:58 I think we started, actually, to do that on the last…
**atoulme** 11:01 Okay, we used to be able to work.
Sorry, I was away for 2 weeks, and now, looks like you're way ahead.
**Ruediger Schulze (IBM)** 11:08 Not sure if I put the HMC one here already, but… HMC…
**atoulme** 11:14 I'll do it.
For HMC, we could just work, like you said, reverse engineer from the output.
**Ruediger Schulze (IBM)** 11:22 Yeah.
**atoulme** 11:23 Okay.
We can do that. I think we can close issue number 5, is that right?
**Ruediger Schulze (IBM)** 11:30 That looks actually good, yeah, that looks good, yeah.
**atoulme** 11:34 Do you wanna, I think you should do the honors, but…
**Ruediger Schulze (IBM)** 11:37 Yeah, I would do that.
**atoulme** 11:39 So, the other one, issue 6, you have already done some of that. You need to deprecate in the main repo.
**Ruediger Schulze (IBM)** 11:47 Right, right.
**atoulme** 11:48 Yay.
And then, for the next ones… So…
**Pellared** 11:55 That's fine.
Are you sharing your screen, or not really?
**atoulme** 11:58 No, I'm not sharing my screen.
I'm being lazy.
Bingo.
No… Okay, so, that should be fairly clear.
That… do you see it?
**Pellared** 12:10 I'm sorry.
**atoulme** 12:13 reload. So, this one is the thing we just merged, right?
**Ruediger Schulze (IBM)** 12:16 Yeah.
**atoulme** 12:16 Actions, we're good. This one is now done. Actually, wait, let's just stop about this.
**Ruediger Schulze (IBM)** 12:21 I will update that one.
**atoulme** 12:23 Down with the merge of… PR… where was it?
Yeah… What were your… You said clue.
Just to be… Just to be respectful that it's your issue.
**Ruediger Schulze (IBM)** 12:47 Yeah, thanks.
**atoulme** 12:48 Next one, so… with… 11… We now have the definitions in this repo.
In theory, we need to do the second part.
And, deprecate.
instant calm. Do you want to do that, Whitiger?
**Ruediger Schulze (IBM)** 13:14 Yeah, I will do that. I… actually, Lyudmila also advised me there's this, this way where you can use an annotation that you don't pull in from the base repository, we started this already, and I will do the deprecation there as well, so.
**atoulme** 13:29 Okay, I just… sure, So, next one is not signed, or it's just, like, at this point, it's an idea, right? Keeks and IMS.
Is there anybody here who's…
**Ruediger Schulze (IBM)** 13:42 Yeah, so this is what we… there's a PR, actually, it's in our document.
It's the, it's the PR, the long-lasting PR, which I think in the end, in the base repo, we will… We will close, but then move over the content.
This is… this is PR.
**atoulme** 14:05 Used for this.
**Ruediger Schulze (IBM)** 14:10 1896…
**atoulme** 14:12 1896, okay, so… 18… 96… Let me get you…
**Greg Shriver** 14:27 Isn't that 1898?
Where'd go.
**Ruediger Schulze (IBM)** 14:30 Did I ever say it wrong?
Oh, you're alright, I should probably clean my glasses.
**atoulme** 14:38 No worries.
Okay, so we can use that… So this is actually… the work is done, it's just take, take the, take the, the, the, let's say, the, The smart work is done.
Now we just take this, and we… push it into this new repo, is that right?
**Ruediger Schulze (IBM)** 15:03 Partially, right? I mean, the definition as it appears on the issue is a little bit broader, as it's completely for, like, kicks and IMS. As it currently stands, there's also extensions to this, which are more product-specific, so… Essentially, what we want to do is… and then we can look at this then also to… fully validate the format. So, there's multiple implementations of spans for… on the mainframe side from lots of different vendors, I think.
what, in the end, we want to do is, get started with this TPS definition here, but then, I think we want to validate that we have, you know, good representation of spends for Kix IMS across the ecosystem, and, that might include, Also, vendor-specific extensions, if this is, you know, needed.
But let's… let's get started with TPS, so with the PR, and then, you know, let's take it to… You know, anything that needs to go in addition.
**atoulme** 16:17 Okay, so we can start with that, because at least we'll have something to debate,
**Ruediger Schulze (IBM)** 16:21 Right.
**atoulme** 16:23 And, yeah, okay. I mean, I'm happy to put my hand up and do the manual work of taking… extracting from this and pushing it in here, if that helps.
**Ruediger Schulze (IBM)** 16:34 Yeah, if you want to do this, Antoine, I appreciate that. Yeah. Otherwise, I have a couple of days now where I want to do this type of work, so… Whoever goes first.
**atoulme** 16:45 Okay, just, let me just ping here if you… what I'm going to do is not very intelligent, right? I'm gonna pick whatever I can from here, try to learn a little bit, and push it in the repository using your latest and greatest.
And then we'll see if the CI works well, we'll see if the… if we're able to generate those things, and then we can move from there very quickly, and we can have more people, kind of chime in.
**Ruediger Schulze (IBM)** 17:08 Yeah. We feel that.
**atoulme** 17:09 Okay, that's that. Now, this ZOSMQ, is there? There's no work for that in here, is it?
**Ruediger Schulze (IBM)** 17:17 There is no work, there's documentation based on what is actually with the product.
And I suppose… Because this was when the product came out, certain things also changed.
I suppose the… the naming not completely aligns anymore, how the SPAC would… Require it, so this is something to figure out.
And then again, the same applies, right? I think there are multiple implementations from different vendors. Let's also look at this.
**atoulme** 17:50 Okay, and these are spans of ZHMQ, okay.
Okay, is there anybody here who would want to kind of take a crack at this one?
If not, that's okay, we can always do it later, or whoever has time.
**Greg Shriver** 18:08 I'm gonna be out next week, so I don't want to take anything that, We're counting on doing, or getting done by… by that time.
**atoulme** 18:17 That's good to know. I mean, if… then, you know, if you… when you get back, we can get back to that.
That's cool.
And then the last one that is open right now is for databases.
And for databases, we said, there's no work either. It's probably going to be kind of the same idea, Ridiger, right? That's what you mentioned.
**Ruediger Schulze (IBM)** 18:36 Yeah, and it's the same… okay, it's the same thing, you know, the product has certain support, and the speciality is this is a database server span, where even the database spec doesn't have anything today.
Because today, it's just client spends.
So…
**atoulme** 18:57 Which is different from the work.
On semantic conventions… Four databases today.
Which is… Cook his dog.
Collins fans.
Okay, so we can start to go into all those directions, and there's one more thing you said we wanted to document, we did not. What was it? You said…
**Ruediger Schulze (IBM)** 19:23 SMC.
**atoulme** 19:24 Is that true?
**Ruediger Schulze (IBM)** 19:24 Yeah, HMC, we want to add an issue.
**atoulme** 19:27 you.
HMC metrics… And produce a set of metric definitions.
For review by the group.
**Ruediger Schulze (IBM)** 19:39 And I would… take that one. That's the next one on my list to go through, because I want to… actually, Craig, you have been part of this. We have been looking at this for a while, so I wanna get this somehow in a form that we can… In a more formalized approach, work on that.
**atoulme** 20:00 Rigger is offering to… Take this up.
And present to the group.
Okay, that's… that works for me. Let me assign… Somehow.
Okay.
Alright, so… We're unblocked, and we can start to palletize some of the work. That's cool.
And we have a working thing, and do you want an issue for the first release? Just retrack it somewhere?
**Ruediger Schulze (IBM)** 20:32 Yeah, you can create it, and like I said, let's target something in 4 weeks from now, ideally, if you have something.
And also, let's use this as, you know, Establishing this process.
Both, oof.
You know, getting two releases from… from…
**atoulme** 20:55 To get a release, going regularly in combination with, closer, semantic convention.
Oops.
**Ruediger Schulze (IBM)** 21:07 And this is more for FYI, so what Miller said is there's still this question of how the federated semantic conventions would publish their content, then, into the documentation.
So, that's one of the questions that, obviously, on the way, would have to be solved.
**atoulme** 21:28 Okay.
This is great.
Okay.
**Ruediger Schulze (IBM)** 21:37 Thanks for taking notes, and Filling out the issues.
**atoulme** 21:41 Yeah, that makes us real, right? Yeah, no worries. I mean, you… you… this way we can… Ideally, I want to make it easier for others from my team to jump in as well, so they don't get as much context otherwise. It's difficult.
Okay.
Okay, that's it for me, is there anything we should discuss here?
**Pellared** 22:03 The other…
**Ruediger Schulze (IBM)** 22:04 Yeah, go ahead.
**Pellared** 22:05 I added a few bullets to the agenda.
Oh, yes, surely.
**atoulme** 22:10 Sorry.
**Pellared** 22:11 You can still share, I think it will be good if you will be sharing.
**atoulme** 22:14 Yes, sir.
**Pellared** 22:16 Thank you.
**atoulme** 22:17 Of course. So.
**Pellared** 22:20 please take a look. So, recently, we have been discussing, because the new, you know, the move from the Gen AI, like, also, like.
we saw it when we were… when there was a new semantic convention release, and it also affected our code generation in Go.
And then Tyler Rian also stepped up and started reviewing these ops.
And, so I put two issues, and one period, one issue, when we tried to basically, you know, find some possible problems, etc.
So, there are questions like how, like, right now, if I remember correctly, the Domua had this, or maybe, I think, also charged that there will be only one parent, and you can depend only on the core semantic conventions, but what will happen if you want to, you know, there will be, for example, certain virtualization semantic conventions, which is, you know, very important for mainframes, etc.
Or if you would like to use database, semantic conventions, and stuff like that.
So, we find this is very important. Also, how the releasing, etc.
would affect, you know, code generation, assembling everything together, you know, so we have questions like that, and maybe you can just even take a look at existing comments, just read through, if anything is a blocker and critical for you guys, just to make sure that, you know.
So, maybe… Just check it, maybe you can even say that something is not important, and maybe, all the things which were called out here, but anything for you will be helpful.
**Ruediger Schulze (IBM)** 24:00 Yeah.
**atoulme** 24:00 It's good.
**Ruediger Schulze (IBM)** 24:01 Yeah, thanks. Let me go through this.
**atoulme** 24:05 Yep.
**Ruediger Schulze (IBM)** 24:08 I have to say, so far, taking this over from GenAI was pretty much straightforward, but obviously we… We also didn't put in any model content yet, and, you know, the true questions will just come, right?
**atoulme** 24:23 Yes.
It's really a good prompt to have. I really like that we're having this problem.
So… I, but I think we're not as mature as GDI, right?
**Ruediger Schulze (IBM)** 24:38 Nowhere near.
**atoulme** 24:40 So, Jenai might have bigger opinions about what they want to do, and, we're very happy to kind of be, kind of using whatever they learned,
**Pellared** 24:51 Yes, yes. Of course.
**atoulme** 24:54 But, of course, we're happy to review and help, shape these up.
We… Yeah, thanks.
**Pellared** 25:01 I'm not sure if… So the only thing which I am not sure is that my… probably… I'm not sure Gen AI will need that much, you know, semantic conventions from other semantic conventions. I think that… the… I think that this one may be more dependent on others, but it's just, you know, a feeling. Nothing that I can, you know, be for sure.
**atoulme** 25:25 Yes, sir.
**Ruediger Schulze (IBM)** 25:25 Yeah, I think you touched on an interesting point. This is, you know, when we think about messaging and databases, obviously.
We… we would want to base on what is there, and we don't want to actually create a… you know, completely isolated definition. And… That actually… and thinking about virtualization, so it's… virtualization doesn't even exist today.
But, you know, let's… let's assume we start, but virtualization is such a broad topic in the industry, so others also want to use this, so… so how would we do that? Or, you know, potentially, you know.
We may actually treat virtualization as a separate federated repository at some point.
**Pellared** 26:21 That's all from my side.
**atoulme** 26:24 The thing that's gonna happen is when we start to emit some of that telemetry with Weaver, for example, we will run into this type of situations, and… we will see what blocks us. So, maybe what we could do is open an issue. Just, when we started with regards this meeting, we talked about Weaver… emmett?
Dude.
**Ruediger Schulze (IBM)** 26:46 We could… let's open an issue for reference, implementation, or for… I think that that's the ultimate goal, right?
Yes.
**atoulme** 26:58 Great there.
reference mutation, or mock.
Or where to generate more data.
I don't know. Okay, we… Want to generate mock data.
Permitted to vendors. Representative.
Of a, mainframe.
That… can help, validate… It can help, on one end, generate enough data that… It can be used for… Vendors to build.
Dashboards and partitions.
And on the other hand, validate that we, emit the right data.
from… Mainframes down the road.
So… For that, we can use Weaver… Note, to remit.
Life check.
Data, we will need to offer documentation.
And steps to do so.
We will also need to, make sure this works.
With the new federated model.
And here, I've got… I'm gonna point… To the work that you're all doing.
here.
Let's see… For context to motivation.
**Richard Nikula** 28:46 Isn't that… sorry, I joined late, but isn't that very vendor-specific? Although in this case, Fred, I mean.
**atoulme** 28:51 No.
**Richard Nikula** 28:52 very quickly kind of push it back to IBM to say, hey, create good data for your data you're permitting, right?
**atoulme** 28:57 So, yeah, what happens is that we have now, in this repo, a bunch of YAML files.
that we can use to generate fake data using this Weaver Registry Emit functionality.
So, what we would want to do is this, it has two functions you can use with Weaver. One of them is you can send data to a Weaver client. It's going to just tell you whether it's matching this YAML or not.
So, do we see the right attributes? Are we seeing the spans we thought we would see? Do we see the metrics we thought we would see? That's one. The other is, you can use this to generate fake data along this YAML.
**Richard Nikula** 29:35 Yep.
**atoulme** 29:36 We're going to generate, like, a number of those metrics and spans and whatnot, and we can send that to any observatory vendor. It could be Datadog, it could be Dynatrace, it could be Splunk, it could be Grafana, and what have you.
The idea, then, is that you can tell people, this is the choke point. This is… you're going to build an observability solution based off this, it's going to look like it needs to be able to handle this data, and then you, from the point of view of emitting data, you need to emit data that is valid according to that spec.
And that's how we do it.
**Richard Nikula** 30:09 Okay.
**atoulme** 30:12 So it's not vendor-specific too much, right? Hopefully, what could happen is that the vendor could come back and say, hey, we don't support histograms that way.
We don't like this data. We would like you to change the data at the end of the discussion. Okay.
**Richard Nikula** 30:25 F.
**atoulme** 30:26 this talk, right? That's gonna happen. That's gonna happen.
**Richard Nikula** 30:30 Yep, I got it.
**Greg Shriver** 30:32 But that sounds like an opportunity for communication, which is what we want in the end anyway, right?
**atoulme** 30:37 Yeah, it's gonna be, like, a very iterative process, and every… so what's going to happen is that every time you change those YAML files, you're changing the shape of the data, which makes it so that we… every time we make a release, then we go and each of us have to validate, are we still emitting the right data, are we still observing the right data?
Right, my challenge personally is that I need to have some sort of a standard set of data types that I can use to feed into dashboards, and sometimes, just to bear on some personal anecdote, right? For example, recently I was working on IBM MQ in the Java Contrib.
And some of my dashboards were not lined up. One of my customers, like, I'm opening this dashboard, and I'm not seeing this particular view being filled.
what is going on with this? Is the filter wrong, or is the metric name wrong? I had to go change my metric names, and my dimensions were whacked out because I didn't follow the latest, and we had made changes in the code in Java.
But we did not follow up in the dashboard.
So we also need that as a… for maturation of the industries, like, everybody needs to be able to say, we are going to work with version 1.10 of mainframes, and it's got this data, and then therefore I know my dashboards work the right way.
So this way I can sleep at night.
It's kinda neat.
**Greg Shriver** 31:59 use Weaver as a, like, a tool on the… On the client side to, like.
in your CI-CD pipelines and stuff, to…
**atoulme** 32:11 Well, not yet. Weaver's kind of new. It's been introduced, what, like a year ago? A year and a half ago? But yeah, we should. We… the thing that's really blocking Weaver the most for me is that we've had so much, like, dead wood from the past that we we have not built enough Weaver models. Well, Weaver has a immense value for us, in the sense that you could get so much mileage without doing so much work yourself. I would imagine that we would do more of that later. For example, not to disclose too much about what we do, but we… so we have a whole infrastructure monitoring solution for our vendor, for Splunk, for our customers.
How do we know that a Mexican database is sending the right data?
Well, you can have some sort of a test, integration test, that checks that all the data that you expect is coming out. We have that in the collector control repository, you can see it, it's a YAML file, and we check, by actually running MySQL in the Docker Compose environment, and we're getting what we think we should get.
But, if you're going to build dashboards, how do you make sure that you're getting the right interactions on all those things? Well, the team ends up having to run MySQL for real.
That's expensive, and that makes it so that the dashboard team now is, you know, responsible for the maintenance of, like, a MySQL database, Postgres, Oracle, SQL Server, and now it multiplies that by how many technologies you want to support out there.
So, Weez Weaver… We could possibly have some sort of an automated harness that just runs with whatever we think is best, and then, you know, also life checks that the data that we want to emit is there.
And I would reduce a little bit some of that cost.
**Greg Shriver** 33:52 That's wrong.
**atoulme** 33:53 I think it addresses really nicely the… I think the cardinal issue of mainframe, the SIG, in a sense, is like, you can't just run a mainframe in a Docker container somewhere.
Right.
**Ruediger Schulze (IBM)** 34:06 It's not made for that. It's intentionally not made for that.
**atoulme** 34:12 I spent about 2 years of my life just running payloads in Docker containers to make sure we got the right matrix out. Like, this was just my life as a QA engineering manager, to make sure we were able to certify that the things we thought we would get was the thing we would get.
So… Yeah, this is nicer.
**Ruediger Schulze (IBM)** 34:32 And now let's look at this.
adding to everything that was said, I just… one thing that is, I think, important as we get started is also to get these entities right. I think with the entity model that is now available.
I think we really want to be clear on what are identifying attributes.
And iterate on that as well, so… How about…
**atoulme** 34:56 Open a niche for that, then, okay? So, build the first entity model.
**Ruediger Schulze (IBM)** 35:03 Yeah.
And that's partially overlapping with what I have in mind for the… from an HMC point of view, but .
**atoulme** 35:10 Okay.
**Ruediger Schulze (IBM)** 35:11 Yeah, you're right. I mean, this goes and also further, obviously.
**atoulme** 35:17 Okay. I'll just open a very innocent issue right now. It's like, build a first entity model.
Yeah, we'll go from there.
Okay.
**Ruediger Schulze (IBM)** 35:33 Okay, good. It's good now. I think we are in good position now with these federated, repos or conventions to make progress.
**atoulme** 35:47 Alright, I… don't have anything else. Anybody else?
**Ruediger Schulze (IBM)** 35:54 I just want to mention this, but I still need to go back, we just kind of discussed this next week. There was, this one company who was offering, Java library building on, I think, the DDS server, REST API, so emitting certain data also in OpenTelemetry format.
They had to… some legal questions, I think they figured this out. I will update you on the next meeting on that. It's just FYI. Still to go through this.
**atoulme** 36:29 Okay.
**Ruediger Schulze (IBM)** 36:31 So there might be an asset that may either lend with somehow the OTEL community or the Open Mainframe project, But, yeah, that's, you know, one step at a time.
**atoulme** 36:44 Okay, great, yeah, cool, let's… let's do it.
Alright, I gotta go.
**Ruediger Schulze (IBM)** 36:57 Okay, thanks. Talk to you next week. Bye.
**Greg Shriver** 37:00 Thanks, everybody.
**Pellared** 37:02 Bye.
