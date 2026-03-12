SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2025-07-09
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Richard Nikula** 00:55 At least the smart ones figured out where to be. Oh, wait! We got one more.
**Greg Shriver** 01:02 Hey! Richard.
**Ruediger Schulze (IBM)** 01:06 Hey! Greg, hey! Richard!
**Greg Shriver** 01:09 Hey! Rudiga.
**Ruediger Schulze (IBM)** 01:25 Let me share my screen.
The agenda roommates may still wait another minute.
Yeah.
**Greg Shriver** 01:41 With the time change and the date change or day change, anyway.
**Ruediger Schulze (IBM)** 01:46 Yeah, Morgan said. He can't do it today. But let's see who else is joining.
**Greg Shriver** 01:55 Yeah, I saw his update.
**Ruediger Schulze (IBM)** 02:29 Do we want to start.
**Greg Shriver** 02:34 Yeah, we may as well, I mean.
**Ruediger Schulze (IBM)** 02:36 Yeah, okay, yeah. Like, always, you know, add your topics to the agenda. And I've seen, I think, Craig, you made a couple of updates at the bottom.
we still have this Tps Pr open, as we know. And one of the reason was that there was this request about this workflow definitions. And I need to go here just to illustrate this to.
you know, have a perspective of workflows, would, you know, make a fit for this transaction processing system as we have to find it.
I had a couple of internal discussions, and I also wanted to get your opinion on on that.
But I think the bottom line is that the view is these type of transactions that we are looking at here.
This is a different concept than workflows. And hence we would not like to.
You know, having these transactions or transaction processing systems being represented through this workflow mechanisms, essentially, transactions would be more of you as an automatic. Sorry, not automatic. Obviously they are automatic as an autonomic operation.
Why, workflows, in fact, can be very complex, can be also long running can be consisting of multiple transactions. So from this perspective, I think at least our point of view would be to to go ahead with Tps. As we had originally defined it.
**Richard Nikula** 04:32 I sort of see it as one is more plumbing. Right? It's like.
it's really more technically, just describing what's happening. Right? It came in here. It went here. It went down here, went here, went here versus the workflows, which are okay. It had order id 15, and then that split into.
you know, 2 sub processes, and whatever right? So that's that to me is a workflow where the transaction processing is just a whatever you want to call it.
**Ruediger Schulze (IBM)** 05:06 Hmm, hmm.
**Anand Somasundaram** 05:08 What can we look at it as like a a distributed application flowing into a Http server, followed by an app server, and probably a database.
Would that be considered a workflow on.
**Ruediger Schulze (IBM)** 05:28 It's not.
**Richard Nikula** 05:28 To me. It depends on how you orchestrate it right. If if you simply following the piece parts, I don't think it's a workflow in my view, I think that's the distinction.
Right? I mean it. It could be, but it by itself doesn't necessarily define a flow. It's just defining some it doesn't define a workflow. It defines a flow right? But.
**Greg Shriver** 05:58 I mean I I could. I could totally see where you know one or more transactions that that we're defining under Tps right? One or more transactions, maybe with different trace. Parents could all be part of a workflow.
**Richard Nikula** 06:16 Sure you could. You could. If if you could.
harvest things out of it, you could make a workflow right.
**Greg Shriver** 06:24 But I tend to agree.
I mean, I I haven't spent enough time really understanding the workflow. What? What work, what? What's really re?
what's really proposed by the workflow proposal. But but I tend to agree with Rudiga that at least from yeah, that they feel like they should be different.
**Ruediger Schulze (IBM)** 06:59 Yeah, I will formulate an answer here in this kind of like context tomorrow. Then let's see what we get back. But ideally, I would like to make progress with Tps.
Workflow is also still in draft.
Don't know yet of what the perspective from the community on this is to be honest.
or from the semantic convention sick.
But yeah, I would like to respond tomorrow and then see what we get back to this.
Okay, good. Yeah, thanks for for the input.
I want to switch gears a little bit and go back to something that we started very early when we established the Sig.
You may remember our document, which we had originally drafted about semantic conventions, and we essentially we started to look at what the semantic conventions define. But then we also pulled out metrics examples.
We also had this discussion around events.
And then we yeah, we had, you know, a couple of further definitions where I essentially want to go is looking at metrics now and we at that time we started from what is available as Hmc metric groups and and aiming to kind of like map this into how to represent this from a semantic convention perspective. I think at that time we never really finished this work.
And what I would like to discuss is I mean, keeping in mind what we also learned about entities recently.
do we wanna progress from here from this document? You know, with one year in between. Does it feel like we need to start somewhere else and to take a different approach to this just, you know, would like to have a discussion of how you feel in in terms of getting started with semantic conventions for metrics, and if the approach that we choose at that time is still the good one.
or if maybe we, we want to pursue a different different route to, to progress on that.
**Greg Shriver** 09:46 So. Yes, we've discussed this a couple of times, and I mean this document was good for us to get. I think it was very useful for us to get, you know, our thoughts put into I into a into a sort of a framework, and to discuss it.
But at this point this document feels a little bit dated, and you know now that we have now, now now that we.
now now that we're we already have, you know, Prs against.
you know the actual repo. It seems like changes to that existing repo. Would, you know, proposed changes to that existing repo would would best be done with Prs and Github.
and they get, you know, they get the appropriate scrutiny across not only our group, but all the other groups within hotel, as well.
**Ruediger Schulze (IBM)** 10:45 Right, right.
**Greg Shriver** 10:48 So I guess the question would be, is there anything that's still in this document that we want to like? Keep, or make sure doesn't get dropped when we translate over into. You know the the Pr. Or Prs. Obviously it's going to be more than one Pr. But in the Prs that go against the the Github Repos.
**Ruediger Schulze (IBM)** 11:10 Yeah, I think we had a couple of maybe mappings already identified is probably something which is useful. Input when we start with Prs and I will talk about how to approach Pr's in a second, but I think we had a couple of definitions being captured, and also some proposes already like here for Cpc, I think we made some definitions.
Also, I think, as I was mentioning this in context of entity, we really need to as we move forward, then really look at what are identifying attributes for these entities.
and then in correlation to to the respective metrics that we are setting up the thinking, for instance, about partitions.
what are identifying attributes of a partition as we progress. And and then what audiences hit it?
Metrics. We want to see there.
Yeah.
**Greg Shriver** 12:28 Yeah, especially where this stuff like, yeah, especially where this stuff intersects with like the resource semantic conventions. That's super. I mean.
that's super important. And and I myself have been kind of.
you know, vacillating between, you know, trying to trying to reconcile. You know, the the straight hotel.
The straight hotel spec.
And and trying to make that fit with mainframes.
And I think that I've really come to a like a 1. 80, not a 1 80. But but just, you know, trying to keep them separate, because it seems.
And I guess where I'm coming from. This is just a simple example, like we had a discussion last week about process id.
And process. Id, you know, seemed to, you know, I think we kind of rationalized our way to thinking that you know process Id might be an asid in Zos.
but I think that's I think that that just or that I think that was probably a mistake to to say that that could be a valid process. Id. I think that we should really think about like keeping process, because that process, the process models between unix and traditional zos workloads, non unix system services workloads. They're different.
And and for us to try and smash them together, you know, I'm not really sure what the benefit there is, and I think it probably makes things more complicated, I think would be better off to leave in this, in that example, to leave process alone and have that by, you know, if you're describing a unix system services workload or a posix workload, or you know windows or Linux, that's fine, or Linux on Z. That's fine. But if you're talking about a traditional zos workload with no unix system, services that should probably be appropriately namespaced under zos, and we probably should leave process alone.
Now I that I kind of went down that rabbit hole there. But I'm using that as sort of a straw man to say that.
I I and I'd like to hear what you guys think like rather than try and smash these things together at the you know, at the expense of of making each individual attribute more complicated. Maybe we should just, you know, the things that fit naturally make them fit the things that don't fit naturally segregate them off into appropriately namespaced stuff.
**Ruediger Schulze (IBM)** 15:23 This is a good one, Craig. And the reason why why this is a good one is because we also have internal discussions around this whole topic of how to name. You know concepts that are there on the mainframe for a long time, and how to map them to you know, co-common terminology that you find in in the in the it today. And process obviously, is a is a good idea there, or a good good example, and that there's 1 consideration is on on our end is to go actually with what are the common names within in the in the broader community? So not in the Mainframe community, but outside of the mainframe community, to help to to bridge this you know this.
that there are 2 different concepts or 2 different names for things which are sometimes they are logically, you know, maybe similar. Sometimes they are completely different, obviously.
and one way of of doing this would be, you know, trying to use these established names, but then always give a give an explanation for the mainframe. You know. Process Id might imply that this is an as id right. But this is then also requires that you know there's for each of these common names a specific instantiation of what is this for the mainframe to be given so?
**Anand Somasundaram** 17:21 That is from the zeros perspective, right?
**Ruediger Schulze (IBM)** 17:24 Right, right.
**Anand Somasundaram** 17:25 There's also Zvm, I don't know how far Ztps and how far we want to carry those other operating systems.
**Richard Nikula** 17:33 Right. But the other side of the coin is the people that are trying to make sense out of all of this right? So.
To them, you know, if you go with the model that says, well, the mainframe is just another piece of the puzzle.
then it's really confusing. If that piece of the puzzle has its own names for the same things that other places have right.
**Ruediger Schulze (IBM)** 17:52 Yeah.
**Greg Shriver** 17:53 Yeah, I agree.
**Richard Nikula** 17:54 Yeah, that's it's a. It's a tough one. I agree.
**Greg Shriver** 17:57 It is, it is but a and and almost like I totally get it. If if there's if there's like a if we have a a zos specific name for something, but it really is exactly the same, as you know, and the models don't differ between. You know the rest of the world and the mainframe, then maybe it does make sense to stick them together. But in the case of like process Id. I mean, where that mapping is not natural.
and you know it's it feels it's tempting. It's tempting to make it natural, you know, with like hey process, id could be an asid. Well, that breaks the moment that you have an asid. That also has unix system services workload in it.
So I mean, in that case, maybe there's a case where we just separate it, you know. And if you've got unix system services, workloads that you know where where we can process id makes sense great.
Put the process id in there, but it's not. But don't you know, have like a a big, complicated flow chart to say, Well, if you're on zos, you know, process Id is really the asid you know, and I I don't know how to succinctly say that.
But I'm I'm just. I'm kind of thinking out loud with this group, thinking that, you know. Maybe it makes some sense to.
**Anand Somasundaram** 19:22 That always.
**Greg Shriver** 19:22 You know, to to try and separate, to try and separate them, where the where, where the mapping is just not natural.
**Anand Somasundaram** 19:30 Yeah, I agree with you, Greg. You can have a mbs started task at a bad job, creating attaching tasks and then dubbing it as a unix.
so under the same view.
**Greg Shriver** 19:49 I mean, and that additional complication doesn't really in in it doesn't really enhance or help observability in general, it actually probably makes it worse, and it probably makes it, you know, difficult for the people that you know, that already understand the rest of the world. You know the the traditional, not the traditional, but the you know, the distributed or non mainframe it world. They're like, what in the world is this.
**Ruediger Schulze (IBM)** 20:17 Right.
So I I think I I can actually follow both lines of argumentation.
**Greg Shriver** 20:26 Sure.
**Ruediger Schulze (IBM)** 20:27 When when I originally was talking about putting the mainframe into semantic conventions, the way I always envisioned this is that we represent the the obviously telemetry or the definitions that are necessary for an sre type of person to get an understanding what this telemetry is.
and eventually we would put their things like asid and task ids and others like like we do already with Tps, because this is then you know, it's accessible for this sae type of person which is maybe not so familiar for the mainframe. But it's easy to understand. Okay, there are semantic conventions. I can go there. I can read up on this what this, and I have the information that I can give to my mainframe colleague, and and then this person can go off with, you know this telemetry having already the right naming language that this person then understands, and to to move ahead.
What I think is we? This is actually a topic where we need to somehow come up with a with a with a rule of how we wanna do this.
**Greg Shriver** 21:45 Yeah.
**Ruediger Schulze (IBM)** 21:46 And and this needs to be generically applicable, then, for for anything that we want to do, moving forward. What I will do is, as I said, we have discussions on this.
I want to run this with with this team again, who? Who is looking at this? And I want to get their perspective and also want to bring this, then back to our group here.
If you maybe have internally similar type of discussions.
you know, would be great also to hear about the perspective on them. And then, I think we need to.
you know, make a definition of of how we want to pro proceed and and and potentially even put this to the.
to the naming conventions that the semantic conventions define somehow need to to document this in in context of the semantic conventions.
so that this this is also visible for for others that you know. Look at this at some point.
I mean the the semantic conventions. They try to generalize, but you know also they give space to have your own namespace, as we know, and make your own definitions.
**Greg Shriver** 23:07 Sure.
**Ruediger Schulze (IBM)** 23:09 Yeah.
**Greg Shriver** 23:11 Yeah. And I agree, I agree with your proposed path forward.
and I can certainly we can certainly have some discussions within our organization as well.
You know. Ha, ha! Yeah, I mean I I think it's I think it's a good path forward.
**Ruediger Schulze (IBM)** 23:31 Yeah, let's let's do that. And I think this is key to anything that we want to do.
I mean, there are a couple more things right is, how do you call these different processor types? And all these type of things can think of probably of a lot of lots of famous topics. This particular? Right? Yeah. Okay. Now, this is, yeah. Go ahead.
**Greg Shriver** 23:57 And at the same time, you know Richard's point about well, gee! If we put a whole bunch of zose stuff in there, and it doesn't enhance. You know, it doesn't help a an a distributed sre. Better understand the mainframe. Then we're doing our and we're doing everyone a disservice. So somehow, we need to balance all of that. And this is not, I mean, and and how we do that is gonna probably have a a big impact on how successful this. You know how successful we are, and making the mainframe understandable to the rest of the world.
**Ruediger Schulze (IBM)** 24:32 Right?
Yeah, this is good point, too.
Okay?
Yeah. So coming back to to the document, and you mentioned Ps, Craig, I think there's probably maybe the pass forward is, if we look at, I think we have, you know, kind of like roughly listed this out here on the table of contents.
If you look at these metric groups that the Hmc defines, you know that there's multiple of them. But maybe we should be just trying to start with a Pr which lays out. You know this, for instance, the Cpc concept as A as a Pr. And map the the metrics that are there on to to the semantic conventions, and then we can, you know.
go to logical partitions, and, and, you know, continue to go through this, probably 1 1 Pr per metric group. Even if it's not, maybe it's even more granular.
So what I would suggest is maybe for the coming meetings that you know, we take one area of of the the metric groups, or one particular metric groups discuss what that is and how we would try to map this to to a Pr. And then, you know, you know.
somebody of us can go ahead and maybe draft the Pr. And and you know, by doing so we can also get feedback and and get the practices feet. And and also you know how the community is perceiving this as we then progress with this maybe that's that's a way of of how we can move forward with getting those semantic conventions in place from bottom up for the platform. And we have an understanding, for instance, of how to represent the different processor types, the utilization on them, and so on.
And then, once we covered the Hmc part, we can go to the next level.
**Greg Shriver** 27:03 That seems reasonable. I mean, are you suggesting that that we we have? That that we take them as a team, one group at a time.
or that we split it up and have maybe 3 going at 2 or 3, going at the same time, and just work our way down.
**Ruediger Schulze (IBM)** 27:20 I would suggest, we as a team, start with one just to kind of like, learn the mechanics around it, and and also maybe understand where the challenges are.
and then maybe we can split it across.
You know the group here to to scale essentially the effort.
**Greg Shriver** 27:43 That makes sense so start together.
**Ruediger Schulze (IBM)** 27:46 Start together, get an understanding. And I think we need to. Just I mean, it's a while ago, as we said, right? And we probably need to start again when we look at, for instance, the Cpc metric group. Okay, what's the telemetry in there? How would we represent this?
What predefined metrics or attributes would be reuse.
Or what do we need to find to define you right.
**Greg Shriver** 28:18 Sure.
**Ruediger Schulze (IBM)** 28:19 Yeah, okay, sounds good.
So there was this reminder on the publishing. The survey results.
I would just take an action to to have a draft ready by next week.
I think this is long overdue, and then I think you also discussed this last week. So I think we have a, you know, a good lineup of of session proposals at these various conferences that are coming up in the autumn timeframe. So tech exchange. We submitted 3 sessions under the open mainframe project.
One is about instrumenting the the mainframe. This is kind of like, you know. One thing that the survey also revealed was.
there is still a need for educating the mainframe community about open telemetry. So the aim of this session is to address this and then bringing this together also with distributed tracing functionality.
The second session is really an update for our work as a sick, and, in fact, I put a couple of topics in there which we, you know, which we have on the agenda. But you know, until the the October November timeframe. Hopefully, we can make some progress on this. So probably in the next or the week after meeting. Let's take a look at this of how we can maybe also drive some of these activities, Richard, we spoke earlier about the C plus plus SDK to bring it to Cos. So it's probably one of these activities to look at, of how to to make progress on that.
and then the last one. This is actually not so much related to observability or open telemetry, but in context of the Omp, also giving a chance to talk about the mainframe architecture. And there's also an open mainframe education project under the Omp.
So the idea here is to talk about transaction processing on on the mainframe, on the architecture behind it, but then also maybe get into a discussion with the the open mainframe education project and maybe contribute some of this. What actually is a result also, to some extent of observability being able to see what's in the system. What kind of subsystems are contributing to the transaction processing. Get this documented under the open mainframe education project.
**Richard Nikula** 31:17 And then on the last week, when we were discussing, there was one question about who was going to be at the Tech Exchange.
**Ruediger Schulze (IBM)** 31:27 Right. So tech exchange. The the way was that you can only specify one speaker. But I assume that multiple in the end can get on stage.
And so, from an Ibm point of view, I hope to be there, and you know I would be happy to bring somebody else on the stage to talk through these topics.
**Richard Nikula** 31:52 Okay, yeah. So at this point I'm still planning to be there. So it would be something I'd look to.
**Ruediger Schulze (IBM)** 32:00 Yeah.
**Richard Nikula** 32:00 With your answer.
**Ruediger Schulze (IBM)** 32:01 Right and and Richard, this would be great to get together on stage and talk about these topics. And, by the way, this the same is true for Gse Uk, obviously.
And then for Gz Uk, we have a similar topic about this. You know educational concepts or educating about the the observability concept. And then again, this proposal about the mainframe architecture.
transaction processing, and then also looking at of how to contribute this to the open mainframe education project.
and then at last break. I think this this is stern from you. The proposals made for for Kubecon, which I think is a great idea.
**Greg Shriver** 32:55 You know. We'll see if they get confirmed. Who knows.
**Ruediger Schulze (IBM)** 32:59 Yeah. As I was saying, we had something submitted for for Cubeco in Europe, and it was was not accepted. But you know mainframe becomes or will play into this. So maybe what we we one day we get a.
**Greg Shriver** 33:16 Right.
**Ruediger Schulze (IBM)** 33:17 If you get a chance.
**Greg Shriver** 33:19 Well, I mean, I attended observability day. Actually, I attended Cubecon November 2023, and it was it. I can see why they have such a problem, because, like, especially for observability day, they have like one room, and it's, you know, and they don't have a whole lot of slots. And there's a zillion topics that are all important, so I can see their difficulty in scheduling so.
**Ruediger Schulze (IBM)** 33:45 Right? Right?
And the topic is still evolving. There's still a lot of also innovation happening in this space.
Obviously, right?
Good.
Other topics for today.
Okay, then we talk. Next week I will bring the the draft for the for the survey results.
and if you know, have a you know, have some discussions, some considerations about this terminology topic.
we will take it also back to our team that looks at this.
And then we can, you know.
Maybe take next steps for for metrics.
Thank you.
**Greg Shriver** 34:44 Sounds good.
**Anand Somasundaram** 34:46 Okay, so what I think this.
**Greg Shriver** 34:48 Thanks, everybody.
