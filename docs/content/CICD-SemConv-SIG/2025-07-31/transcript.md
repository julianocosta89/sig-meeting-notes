SIG: CI/CD SemConv SIG
Date: 2025-07-31
Duration: 40 minutes
============================================================

## Zoom Recording Transcript

**Adriel Perkins** 01:38 Good morning or afternoon.
**Martin Costello** 01:41 8 or day.
**Adriel Perkins** 01:44 How are you?
**Martin Costello** 01:45 Good. Thank you. How are you?
**Adriel Perkins** 01:47 Doing all right. Thanks.
Oh, you've already approved.
**Martin Costello** 02:40 Yeah. I took a look at that last week after the meeting.
**Adriel Perkins** 02:51 Appreciate it.
Oh, screw that sorry! I couldn't hit the mute button fast enough.
**Martin Costello** 03:00 Yeah, I've had that happen to me before.
**Adriel Perkins** 03:19 To top it off. My mouse has been giving me problems where it will like disconnect, and then, after wiggling it around for 30 seconds it'll come back.
and I went to go. Move it to get the mouse button, and it decided to disconnect right then and there.
**Martin Costello** 03:33 So that's the thing I like about my microphone is a hardware mute.
So I just touch it.
**Adriel Perkins** 03:39 You know what I should have done that cause. This light is the hardware mute, and I always forget about it.
**Martin Costello** 03:51 The disadvantage of the hardware mute is sometimes I get hardware and software muted. So I mean, I think I'm unmuting myself, and no still no one can hear me.
**Adriel Perkins** 04:02 Yeah, double muting.
It's a thing.
Alright, let's see.
Feel free to fill out the sheet.
And I think we did a little bit of triage last week.
We can do a little bit more this week, but I don't want to take up too much time doing triage.
There we go.
We're still where we're at with those. I don't know anything about them.
I think we still have a few things to figure out if we want them to be in phase 2.
See? Where did I? Let's see, yeah. Cicd, phase 2.
Who's that merged?
It's closed. Okay.
so this one probably needs to come into phase 2 as well.
just as like a minor piece of work if we can't get it done. Now.
I'm sorry. Face, too.
Also. Phase 2, all right. So let's look at the alright. This one needs to be reviewed. I think this one has a lot of different metrics, and it's just kind of like all encompassing, but I think we can break this down and close like the majority of it. So we'll reach out to Christoph and see how we can break this down into either a new task or close it because it's been completed.
I feel like a review.
I'm gonna say, needs triage on that one because we need to review it.
Yeah. So needs triage and phase 2. And the reason why?
Okay.
oh, wow, we're almost done with all of them.
Hmm.
yes, it's part of test attributes.
Okay, so this actually needs triage.
And because that's a long one.
I think this one could be custom.
Yeah, that one needs triage. Still.
this is that long running pipeline one where it's like, is it a problem?
Is it not? A problem?
Don't know.
**Martin Costello** 12:56 Hey?
It might be because I and I'm related to Cicd. I noticed the thing with Grafana the other week that I wasn't aware of that.
It requires that to be by default, like a minimum amount of time between when the trace was produced, when it was ingested.
So if you've got like a Cicd system that takes half an hour to go from A to B by the time it emits the trace at the end. You'll be like, well, this is really long. I'll just junk it.
**Adriel Perkins** 13:30 Oh, wow! Okay.
**Martin Costello** 13:31 Because the drift is too much cause. It's typically more geared to like real time ingestion.
**Adriel Perkins** 13:39 Right.
That's a back end thing, though.
Yeah, the the we've had. There was a really good, and I hope there is a, let's see.
is there?
Yeah? So this is not. This is a spec issue predominantly.
Nope, where is which could potentially be solved? Which could this actually could help the back end problem.
which is write partially completed spans.
Have you heard of dagger at all?
**Martin Costello** 14:25 I've heard the name, but that's about it.
**Adriel Perkins** 14:27 Okay, they did. They did some wild thing where in their utility they emit hotel.
but they emit their hotel spans early, so they actually omit the start of the span so that you can watch the trace essentially grow as time proceeds. It's kind of nifty like. It's a really cool visual effect. But how much use does it have? I don't know. But if if we send spans early right, the start of the spans, then at the back end just waiting for the close. And you can probably do the root parent linking a lot faster. Because you have that start span without having to wait for everything to complete So that's a spec issue that they've been talking about for a long time.
and I'm not sure if we will be able to address it as a group.
**Martin Costello** 15:32 Yeah, okay.
**Adriel Perkins** 15:33 So let's write that down work. I think Kubernetes workflows and Argo CD, workflows have have a similar problem.
There's also, I guess a workaround that is span linking.
but I don't think it's elegant.
**Martin Costello** 16:30 No, I think when I've used that in the past it might be dependent on the back end. But, it's like you can usually go one way, but not the other.
**Adriel Perkins** 16:39 Hmm, yeah. Yeah. Yeah.
Yeah. There was. What was I trying to do with spam leaky the other day?
I don't remember.
Don't remember.
See, add, or do we already have this? This might be done.
Well, if it's not done.
we should get this done, because that's an easy piece of work. It's like, literally.
it's like a 2 line change.
Oh, great! There's another layer.
Oh, that's right.
We have pearl build.
Oh.
this one actually does need triage.
Alright. So we'll mark this one as triage and all it already is, and maybe we'll put that there. Okay.
that's good on, I think what we got there?
So any subject that you want to talk about.
**Martin Costello** 19:36 Not today. No, as I I've made a point of bookmarking the backlog. So at some point next week I can have a look through it. Catch us on some of the issues that I haven't done that yet.
**Adriel Perkins** 19:48 Cool.
**Victor Lu** 19:49 Some more questions actually on another topic. So the Cicd it's how about data? I know they are. Some way, some data and like data is not always about changing the schema, right? So about also about actual moving data up what we that belong to this convention, I mean what is called Cicd convention symmetric, because that would belong somewhere else.
**Adriel Perkins** 20:24 Which which one do you think long somewhere else? Sorry I missed the 1st part of that.
**Victor Lu** 20:30 Yeah, probably can use the word data Ops as a description.
**Adriel Perkins** 20:35 Ops. Yeah, can you elaborate a little bit on what you mean by data? Ops.
**Victor Lu** 20:42 Just any task related to data. It could be like generating metadata like instead of have, like static schema, you could be using AI to like, scan it like unstructured data, and create like schema on the fly. So metadata on the fly. So those kind of like metadata operations is an example. You can also be like moving data like you can copy data from one place to another, moving it between storage and memory. Just just, I'm just even just random examples. Do those belongs to the. Those are also pipelines. Basically.
**Adriel Perkins** 21:27 Yeah, like, like a Etl pipeline kind of thing.
**Victor Lu** 21:30 Yeah, yeah, exactly. Yeah. That's a good example. Yeah. So that this belongs to this.
**Adriel Perkins** 21:36 No, no, that's I would probably bring that up in the general simcom meeting on Mondays, and possibly the spec meeting on Tuesdays.
basically like what this group is focused on is pipelines is is part of it. But they're specifically Ci CD pipelines. And it's it's all about the the semantic conventions and portions in the spec that enable those kind of things to be traced properly. There is, like general log of it semantic conventions. But we're all talking about the attributes that come with telemetry for for open telemetry. Those standards across the the industry.
I think the Etl stuff just in my mind, like those types of operations. You know, the open telemetry collector, for example, has Ottl which allows you to pretty much do any type of data changing in that pipeline. But I don't think that itself is observed in any way with any type of semantic conventions for saying like these attributes were changed into these attributes, or anything like that. So I would say, probably take it to the General Semantic Convention meeting on Monday, and, like, bring up that topic, put it on the agenda, and like, see what what their thoughts are around that.
**Victor Lu** 23:07 Okay? So at this point, there's no specific spec, that's for that.
Get off and pl at the.
**Adriel Perkins** 23:15 Yeah. Semantic invention. I don't think so.
**Victor Lu** 23:22 Also, the tricky part is when you're talking about data Ops training a schema which is part of Cicd is also considered part of data. Ops.
**Adriel Perkins** 23:38 Yeah.
I'm I'm not sure if there is or not. I don't see anything that says data ops clearly, but the purpose of like a Etl pipeline in my mind, or any of these telemetry pipelines would be to change them.
change whatever data there is into the semantic convention. So what we've done in the past is for, like what one of the things we have to add here is like Github events which is just arbitrary information that comes from Github as a log event, we do transform that into the semantic invention. So we take whatever they have and map it into the semantic inventions. But we don't have that mapping defined in the semantic conventions yet. That's 1 of the pieces of work that's on our board, so that people can clearly see that like, hey? Okay, Github spits out this right today. But this is how it maps to the semantic inventions and the standards.
But that's the thing that we have to do. We haven't haven't done it yet, but it is like on our task, and they do some similar things with. I think some of the dB. Conventions, but I don't think it's a general set of provided guidance for data in general.
**Victor Lu** 24:51 Oh, yeah, actually, there is a database convention. Yeah, maybe something there. Yeah.
Awesome. For Ci. CD, is there a list of like a task, especially like just trying to find the small smallest granular task list. Is there such a list.
**Adriel Perkins** 25:10 Yeah, for Cicd.
If we go to the registry on hotel this is what the attributes are for the telemetry, and of course you can put these attributes on a log event on a span.
on a metric.
though cardinality comes into play on metrics, but these are the the list of them, and for tasks we have the task, name the task run id the result, the URL, that and the type. Those are the the key ones and tasks can be like. In Github, for example, a step is a task a job is a pipeline, a workflow is also a pipeline, so those 2 are both pipelines. And then tasks can be steps. But then inside of those steps can be other tasks. Right?
it's not necessarily meant to have like a new name for each hierarchical step. But in traces you just do span linking. So it's just a child span of a of a parent span, and both can be tasks. But that's how we've addressed this one is is this is the list of the the task ones. But then go ahead. Sorry.
**Victor Lu** 26:25 The actual granularity of a task really depends on the actual implementation.
**Adriel Perkins** 26:31 Yes.
**Victor Lu** 26:32 Okay, got it. Thank you.
**Adriel Perkins** 26:35 You're welcome.
**Dotan Horovits** 26:36 And then.
**Adriel Perkins** 26:37 Questions.
**Dotan Horovits** 26:37 Dependent on the on the platform, because, as mentioned, the examples from from a Gita. But then, again, if you switch over to other platforms, the the cement, the meaning. Sorry of what? What is the entity depends on there. So it also depends on what your what framework is that you
**Victor Lu** 26:57 Yeah, I said, I'm more interested in their side. Etr, definitely is a good- good example.
yeah, I guess that's just a I probably need to look at the database dimensions using anything there. Yeah, thanks.
**Dotan Horovits** 27:12 Yeah, although database conventions is less, it's not squarely, Etl, it's like understanding your your query performance. And the you know the the queue and and things like that, but definitely not less relevant than Cicd. So they may have other perspectives, and what we present here, and the general, same as, as Adriel already mentioned definitely, they will be able to provide some more more insights from their side.
**Victor Lu** 27:44 So. So if you if you change a schema as part of a Cic CD pipeline.
that's a Cicd task, right? Not a database task, is it?
If you, if you add a column to a table, for example.
does that belong to Cicd or to belong to a database?
Okay.
**Adriel Perkins** 28:05 A column to a table.
Not talking about telemetry. Going through a pipeline would probably be database. Talking about telemetry going through a pipeline might be a Etl like operation. That's not Cicd.
but is a data, a general data, not a database, but a just general data operation. I'm not sure we have any semantic conventions for data operations in a purist form.
**Victor Lu** 28:36 Okay. So just to confirm, at least you're not aware of any data specific, Etl type of a convention, but for changes to table. If it's not part of a pipeline, then it's probably a database task. If it is a part of the pipeline, then it probably is Cic.
**Adriel Perkins** 28:58 It's part of a Cicd pipeline. It's Cicd.
**Victor Lu** 29:01 Yeah, that's cool. Yeah.
**Adriel Perkins** 29:03 I think there's there's nuance there.
This would definitely be a really good conversation, though, for the general semantic conventions, because I think they could provide guidance on whether or not maybe there's interest in forming, like an Etl or data Ops specific Sig around that that addresses those types of things, because the thing that comes to mind for me is like what it? What in the world does the hotel collector do when you stick it through a processor and change all the telemetry to match semantic conventions. I don't know that those operations have a semantic convention in of themself.
I know they take the data and turn it into something that has semantic conventions. I don't know if the operation itself has a semantic convention, or is observed in a way that is semantically compliant. And so I think that's what you're kind of talking about and push back if I'm wrong here. But it's the actual operation of changing the data that you're looking for the conventions on. Is that correct?
**Victor Lu** 30:05 Yeah. 1st of all, that that term data Ops is not a, it's very vague term. So that probably needs to be defined first, st and then probably can decide whether a separate convention is needed, or it may be just part of a just combination of a Ci CD database, or some general task, because is just copying right moving data. And and maybe it's part of a general convention already.
**Adriel Perkins** 30:35 Okay.
**Dotan Horovits** 30:36 I would also try and understand which is what we did is what what's done today. We've done the similar things with other Sam corners, and then just try to generalize and create this vendor agnostic tool agnostic way. So what is the way that today you'd use to monitor and and query such operations just to get a sense of how it works today for you.
**Victor Lu** 31:01 Yeah, there are a lot of different. Usually, it's up to the like, for example, in from medica, right? So that's a like traditional etl tool. So each each step whether it's moving the data or transforming data, have their own statistics. How long does it take? And what is related. Matrix.
yeah. So it's it's all. There's also Ert, that's actually transforming your data after loading the data.
Yeah, so and I'm not expert in some discussion about data Ops, and just curious on open telemetry has those kind of thing or not. And, for example, they're also when it comes to performance. There's also similar.
Gap is just. There's so many things to capture, and nobody takes time. But, for example, when when you run a job right? I see the the hardware spec, for example, having information about like, how how long does a task run right? So that task is like in in the whether it's a traditional job, a Ml. Job or Etl job, it's all on the on the you can see the business level like, how how long does that process business process run? It doesn't go into like, how long did they spend on like CPU or Gpu, for example? And and what what is the cause of that? So that those seems to be not there? Yet.
**Dotan Horovits** 32:38 Yeah.
it makes sense. I just I would say that this is like squarely looking at it. For example, the example that you gave with understanding each step of the the Etl process. This is definitely something that falls beyond the scope of a of a Cicd. It's something that merits its own. It's a different type of pipeline for the sake that needs its own types of monitoring and observability. So and semantic convention. So yeah.
**Victor Lu** 33:09 And also, as as far as you know, there's not no such a convention yet.
**Dotan Horovits** 33:14 Yeah, no. But what I'm saying is again, for example, here you can see the common denominator across different tools in this space. They say Jenkins and and Github and Gitlab, and and I don't mean city and whatnot. And then you start seeing the the common denominator, and and our work is primarily essentially just generalizing. This.
**Victor Lu** 33:32 Yeah.
**Dotan Horovits** 33:32 There is something that we start from, which is what's. And this is why I asked, what's the current way of of doing it today. So a similar process, thinking process will probably be done in this domain with the relevant etl suites that you mentioned and others, and then try to understand and generalize this these steps of of the the Etl pipeline, and so on. But.
**Victor Lu** 33:56 Yeah, yeah, this is look like it's the 1st step is actually get the the players who are doing something, maybe differently, to get a like a broad terms and categories categories of task and then be able to generalize from that. Yeah, it's a as I said, the data Ops term itself is up to interpretation at this point that I need to be determined first, st I guess.
**Dotan Horovits** 34:23 Yeah.
**Victor Lu** 34:25 Okay. Thank you.
**Dotan Horovits** 34:26 But thanks for bringing it up. I think it's an interesting discussion. And definitely, I think the global Semcon will find it interesting. Maybe it has come up, and that's their advantage as well that they get signals from many other directions, much more so than us. And maybe they've already heard some discussions taking place along these lines in other forums, and they can connect the dots and maybe even team you up with others that have similar interests so definitely worthwhile bringing it up.
**Victor Lu** 34:54 Yeah. Which which meeting you said, is it a general meeting.
**Dotan Horovits** 34:58 It's a Monday one, right? Adrian. I get confused between the same corner of the spec, but I think Monday is the same corner.
**Adriel Perkins** 35:04 Yeah. Monday is the Monday at 11 Am. Eastern.
Okay? It's just called semantic convention working group, or, Oh, yeah.
**Dotan Horovits** 35:18 Yeah, bye-bye.
You'll find all of them on the Cncf. Calendar. Sorry the auto calendar. So just have a look there and and join the one, that is, if it's you, but Levitly recommended.
**Victor Lu** 35:31 Yeah, sounds good. Thank you.
**Dotan Horovits** 35:34 Sure.
**Adriel Perkins** 35:37 Total side note my talks did not get accepted, for Kubecon.
**Dotan Horovits** 35:44 It's fine.
**Adriel Perkins** 35:46 But I just wanted to let you all know.
And mine either.
Okay, yeah.
**Dotan Horovits** 35:51 We're in the same boat there.
**Adriel Perkins** 35:53 Yeah, this is wondering.
on on a more positive note, though. There is an Mcp. If you're into AI at all, there is an Mcp now for hotel instrumentation.
there. It was originally created by there was a prototype originally created by someone at at Honeycomb.
and then I rewrote it and added functionality for the instrumentation score and and the ability to like run it in production over Http streaming and Ssc support and I used it to instrument itself. So the Mcp is also instrumented. It was a fun cycle but feel free to use it and give feedback. It's open source.
that posted about it on Linkedin. It's open source, with the correct attribution to the original Creator, and it works not horrible, so like i, 1 of my coworkers is like. Hmm! I asked questions about open telemetry before it had access to the Mcp, and it was pretty bad.
I had access afterwards, and it was like I had given it a book. And it actually read the book. So it's like, cool. But yeah, it's it's feel free to check it out.
Post about on Linkedin and try it out and give feedback. And if you have bug fixes or improvement things feel free to to reach out.
**Dotan Horovits** 37:22 Nice way to go Hydro. Is that the the scoring by Oligarden.
**Adriel Perkins** 37:27 Yes.
**Dotan Horovits** 37:28 Okay. Nice.
Nice.
Are they? Involved also in the Mcp itself.
**Adriel Perkins** 37:36 Loosely in in that one like me and Dressy have been talking about it. But there's something else coming to a theater near you soon that is more involved. So we're just.
**Dotan Horovits** 37:54 No worries, slack.
**Adriel Perkins** 37:57 Yeah, yeah.
**Dotan Horovits** 37:58 No worries, but really happy to see that. And yeah, great work, and glad to see.
**Adriel Perkins** 38:03 Yeah, thank you. Thank you. I'm just really looking for feedback and people to use it and try it and let me know. So.
**Dotan Horovits** 38:12 Yeah. Great 1. 1 administrative part just for the as we go into August. Are we keeping the weekly as a scheduled. I know that I will.
I won't be available. I'm going on vacation, not sure about your plans, just checking if you want to keep it, or just see per week by week by week, or any any thoughts about August.
**Adriel Perkins** 38:36 Oh!
**Dotan Horovits** 38:37 Of course it shows us, Adriel, if anyone else like Martin, you've been joining us for some time. You're you're regular, so feel free to chime in, as well.
**Martin Costello** 38:47 I'm I'm happy to just like. Come along and see if anyone turns up. If there's anything to talk about.
**Dotan Horovits** 38:53 Okay. Sounds good.
**Adriel Perkins** 38:56 Ditto.
**Dotan Horovits** 38:58 Okay, great. So we can keep it up. So again, apologies in advance that I I'll be absent in the coming one weeks. But thanks for keeping it up. And any another question any of you, is planning on by any chance being at Open Source Summit, Europe in Amsterdam end of August.
Adrian, I think I asked you said no, but Martin, you you also know right on this one.
**Martin Costello** 39:23 No, I'm not there. No.
**Dotan Horovits** 39:25 Okay, okay.
So anyway, I'll be there. If you know of anyone that is on the on the friends of Cicd that is going to be around happy to catch up with them and team up similar to what we've done at Kubecorn, and others like the more the merrier and the more voices and champions we'll have on the ground, so just feel free to help me connect the dots and see we have on the ground boots on the ground, and what what kinds of join for join joining forces we can do around the Cicd and others.
**Adriel Perkins** 40:08 Sounds good if there's nothing else. Y'all enjoy the rest of your day and enjoy your vacation.
**Dotan Horovits** 40:17 Thanks. Bye, everyone have a good day.
