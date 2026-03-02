SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-01-07
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/6WP_u2nlYhX4ULI8djwVOXVnRoIqqcN2k8_XjGicRx0WxNhAb_1c2vLjEw_E-vGX.DdMUTfDV8czM68PJ
============================================================

## Zoom Recording Transcript

**Jim Porell** 00:20 Hey there, just wondering if anybody else is joining today.
**Kai Kirsch** 00:25 Hello? Yeah, pretty sure. Let's give them a few minutes. I hope so.
**Jim Porell** 00:31 Oh, yeah, that's quick.
**Greg Shriver** 00:41 Guys?
**Jim Porell** 00:42 Hey, Happy New Year, Greg.
**Greg Shriver** 00:44 Happy New Year!
**Kai Kirsch** 00:45 Good, Rick.
**Greg Shriver** 00:46 Hey, Kai. Hey, Jim.
Cool.
So, I didn't see anything in the chat to see.
**Jim Porell** 00:57 No, I didn't either.
**Greg Shriver** 01:00 Yeah, I mean, I was hoping we would,
I was hoping Morgan would be on, and Rudica might… may have been on.
Because I know we still have this… the one thing that we have still outstanding is moving the meeting to make it…
to make it more convenient for, actually, everyone in EMEA.
**Jim Porell** 01:21 Oh, there we go.
**Greg Shriver** 01:22 Cool. I think he's the decision maker, so that's good. I think so, yeah.
**Ruediger Schulze (IBM)** 01:26 Hey there, Happy New Year, everybody.
**Jim Porell** 01:29 Favior to you.
**Ruediger Schulze (IBM)** 01:32 Whoa.
**Jim Porell** 01:33 The hot question that we started with was… there was a poll last quarter to move this meeting one hour earlier, but does that screw up your dinner time? So everybody wanted to find out.
**Ruediger Schulze (IBM)** 01:45 You know.
**Jim Porell** 01:46 your response.
**Ruediger Schulze (IBM)** 01:47 Actually, I was today already wondering if we meet at 6 or at 7, my local time, and I concluded, oh, maybe it's 7, like it was before, but I think, actually, we want to go 1 hour earlier?
**Jim Porell** 02:02 Correct.
**Greg Shriver** 02:03 Yeah.
**Ruediger Schulze (IBM)** 02:04 What do you…
**Jim Porell** 02:04 But everybody's been waiting for you, because you're the kind of key person, and if this was your dinner time, we weren't gonna move the meeting. Right.
**Ruediger Schulze (IBM)** 02:12 No, actually, it's fine, and, in fact,
I took the liberty, so we had to write for the mainframe project, we had, like, to write a report about the SIC,
And there, I already wrote that we are meeting at 6, my time, Okay.
Like, pre-announced it. It's now… it will be in the papers, we need to move. Okay. Okay. So, into the new year. First of all, Greg, thanks for… I assume this was mostly from you, the PR for the, mainframe section and the documentation.
**Greg Shriver** 02:51 That, that PR, yes.
**Ruediger Schulze (IBM)** 02:53 Yeah, I looked at it. There's only one minor change that I will make, but I think it's quite comprehensive.
And it's a good starting point for somebody who is new to the topic, so I will approve it after this meeting here.
**Greg Shriver** 03:11 Sounds good, sounds good, yeah. Yeah, I wanted you to take a look at it, because I do mention some IBM stuff in there, and I sure would like for you to take a look at that.
**Ruediger Schulze (IBM)** 03:20 Yeah, but it's minor things, it's just, you know, I've been making an update there.
**Greg Shriver** 03:27 Great, thank you very much. Cool.
**Ruediger Schulze (IBM)** 03:30 Okay, so, Antoine is also there, so maybe let's recap a couple of things.
Also, let's update here.
So… Maybe on… on… Juan, as you are there, we discussed about the…
the JITAB Action Runner, self-hosted Chitub Action Runner, also under the CNCF. I think there was also a follow-up on Slack.
I think the idea was to have a meeting with the CNCF team on that one, right?
Right, I'm okay.
**atoulme** 04:08 Bye.
**Ruediger Schulze (IBM)** 04:09 That's what I understood, you were having a discussion with someone at the CNCF that was much higher placed.
**atoulme** 04:15 than, our project, right? So it's no longer just an open telemetry thing, it's… has to be, reviewed by someone, either at CNCF or even, NF.
And Morgan is having a discussion with you and that person, is that right?
**Ruediger Schulze (IBM)** 04:32 Yeah, there was something on Slack, now I can't see it anymore, it's probably in his story somewhere here, let me check it.
**atoulme** 04:38 Right.
Yeah, the person mentioned that they were not going to be available right away because they were in Japan for some conference.
**Ruediger Schulze (IBM)** 04:48 Right, Jeffrey Sika, right, exactly.
So, yeah, so… we… I think we wanna…
Put up on this discussion here, and then also include,
Than our person from the open source office.
Okay.
**atoulme** 05:10 How do you want to… how do you want to proceed with Jeffrey? Do you want to reply on that and say, hey, it's time to engage?
**Ruediger Schulze (IBM)** 05:17 Yeah, yeah, let me do this. I was…
**atoulme** 05:21 to kind of quote what he's saying in that discussion, he said, we're in talks with IBM now. I'm not sure what that means.
**Ruediger Schulze (IBM)** 05:27 They, yeah, this means they are talking to, she's called Liz. They are calling to Liz from our IBM open source office, for IBM, for the mainframe.
True. We need to bring her in, obviously, as well, but I think it's…
It's good if we… if we, you know, pull this together.
Okay.
Yeah, let me, let me post here later on some, some, some update.
And also, let me pull in this, on this one.
**atoulme** 06:00 Okay.
I don't have much to provide, because we're… I'm just sitting here, not knowing, because TNCF needs to talk to ABM, ABM has to…
**Ruediger Schulze (IBM)** 06:10 Yeah, yeah.
**atoulme** 06:11 what's gonna happen there. So, if I can facilitate anything, but for the most part,
It's up to Jeffrey and to kind of get on this, and I guess Jeffrey and Lee is right at this point, right, from what you're talking about
Okay.
**Ruediger Schulze (IBM)** 06:25 But we could be, like, early adopters if this works out.
**atoulme** 06:29 Yeah, we should be the… should be first in line.
**Ruediger Schulze (IBM)** 06:35 Good.
That's this one.
I'm just reading up the notes. I think there was discussion on the previous meeting around the messaging, semantic conventions. I think,
Angelica, you had, I believe, some updates there.
And also, from a distributed tracing point of view, We want to submit the… The attributes of dispense.
So I… so I assume we just go through regular semantic conventions, And, put this forward.
Right.
**Angelika Heinrich** 07:18 Yeah, I think, Kaya, he met with the…
committee, and I think Kai's on the call, so he can probably give the update, but I believe we do have to wait.
On Antoine, is that right, Kai?
**Kai Kirsch** 07:37 No, actually, yeah, I met with the general sick, was just proposing, right, to add IBM MQ to the list of new MQ managers, but the outcome was basically that there should be, right,
a messaging SIC, which is now on pause, and, the general SIC is basically full of… with work, and, so the idea is
Either we can revive, basically, the messaging SIC, or wait until the general SIC has capacity, which should be
once, I think they're finished with RPC, then Trust me meant that he would probably engage or start looking at the messaging next.
**Angelika Heinrich** 08:22 Right, that was Trusk, sorry, I got the wrong name. Okay.
**atoulme** 08:43 Yeah, I had a… actually, I had a talk for KubeCon EU to go and talk about IBM MQ, and it was just rejected yesterday.
**Angelika Heinrich** 08:51 Okay.
**Ruediger Schulze (IBM)** 08:52 Sorry to hear.
**atoulme** 08:54 Yeah, all my talks have been rejected, there's one in waitlist. I'm not holding on much hope.
**Ruediger Schulze (IBM)** 09:03 Yes, what did you say? They… Trusk is working on… this was…
OPC, right? Yeah, I think you said OPC.
Yep.
**atoulme** 09:17 For what it's worth, we might have,
I don't know if this is going to resonate with people on this call, but since there's been this weird tangent where we talk about mainframes and we end up talking about MQ, which is a much more broader topic,
we have some interest in implementing some IBM ACE, or IIB-type support, that would be mostly through the REST API, from what I understand, of the product, that would allow us to scrape metrics from the state of this type of
of products so that we can
we can monitor them, and I wonder if this is relevant to mainframes, or at least work…
**Ruediger Schulze (IBM)** 09:53 the…
**atoulme** 09:54 Good crowd here.
**Ruediger Schulze (IBM)** 09:54 Yeah, so…
**Jim Porell** 09:55 is.
**Ruediger Schulze (IBM)** 09:56 Yeah, exactly. And Ace… Ace has already some open telemetry support. Now, if you say metrics, I can't answer, you know, what particular you're looking at.
But there is some support, IIB is other, rather… Unlikely to get OpenTelemetry support.
Maybe if this helps.
**atoulme** 10:19 Yeah, just some really good things in the REST API that we could use to just derive some really good metrics.
**Ruediger Schulze (IBM)** 10:25 Yeah.
**atoulme** 10:26 We… we would want to maybe…
Build a receiver in the collector for?
we have opened an issue for that that is under Java Contrib, and I think the feedback from the Java folks was like, there's nothing here that is Java-specific. Would you want to rethink this to be a collector-receiver? And if we were to do that, then I think it might be very quickly streamlined. It's not as much of a lift.
I just don't know…
If this is something that would be interesting to more than just us, frankly, that would be great. I don't want this to be just us, because having a broader support from the committee standpoint always helps, kind of.
Q, if I…
**Ruediger Schulze (IBM)** 11:07 Actually, DOS, from a, even from a mainframe point of view, because customers, run IIB
Or are directed, actually. IIB is, like, the previous product, and customers are actually directed more to move to ACE.
**atoulme** 11:29 Yep.
**Ruediger Schulze (IBM)** 11:29 So, it's… It definitely has a footprint on the mainframe, and it has a use case.
**Jim Porell** 11:40 Yeah, I can tell you that we're actually going into…
you know, using ZOS to go monitor that, so…
We can go into their containers and grab the data and grab the metrics today, so… makes sense.
**atoulme** 11:56 Yeah, I think at this point, we're seeing a lot of people who are just… have ACE deployed in a variety of formats, and some of them are going to be on ZOS, but a lot of them also on just Linux, from what I get.
in containerized forms that also are interesting on their own, so having a REST API interface kind of, removes some of the difficulties of having any OS-specific bindings or anything like that. So…
Again, like, just looking at what you can get from the REST API, it's just enough that it would help us. What we're seeing also is that people are doing a lot of migration work towards ACE13, and so that would actually reduce some of the migration kinks that they are thinking about at this point. They just need to know that things work well.
When they migrate?
And they don't want to do this blankly, if that makes sense.
Okay.
I linked in, Zoom chat, the issue that we've opened on JA Contrib, but we could move it elsewhere, if we want to have, maybe.
Could be moved on the mainframe SIG or something, to get more people to look at it.
**Ruediger Schulze (IBM)** 13:11 I mean, I'm not so much formula with Ace, but…
was just reading. So we have ACE tracing support, this I know for sure, but I'm not sure what metric support is there out of the box.
**atoulme** 13:23 Yeah, I think of this as, like, super basic metrics, like, I want to know how many integration servers are up.
**Ruediger Schulze (IBM)** 13:28 Yeah.
**atoulme** 13:29 Monitoring by using just,
there's… there's actually too much going on here. Display monitoring status, right? So, just looking at some of the feedback that you get when you run, the flow monitoring or things like that, that would be good enough.
There is some things about resource statistics that are also useful, like how many messages have you sent? How many messages have you seen? These type of things. That's good enough.
for basic monitoring that can be done at the REST API level, which is great, because you don't need to deploy, then, the collector conveniently to the ACE deployment. You could
We could do that, we could have, like, one collector, 10 ACE deployments. These type of things are what customers want from us at this point.
**Ruediger Schulze (IBM)** 14:20 Good.
**atoulme** 14:22 Thanks.
**Ruediger Schulze (IBM)** 14:28 How many days that signals have been created.
Offered follow-ups…
I think, maybe, Craig, I need to refer a little bit to here… I think I wasn't on this meeting right. Looking at the previous meeting.
I think you had a discussion around signals.
And how they are being derived as test… or as golden signals, I have to say.
**Greg Shriver** 14:54 Oh, yeah, that was… I believe that was a, Question from Andresh.
And the things that were listed there, I think, were things that Antoine, you know, listed as… or offered as, you know, things to look at.
**Ruediger Schulze (IBM)** 15:20 Okay.
**atoulme** 15:22 Oh yeah, so that was a… actually, unrelated to the mainframe world, is, in general, if I was to do integration testing, how do I make sure that I can have some certainty that I'm emitting the metrics, traces, logs that I want from a particular integration?
It's just tooling that we use in our own, in our own collector setup, because we have the same problem, right? So, for Postgres, MySQL, for example, we actually have a, what we call a golden file in YAML format that allows us to do some level of fuzzy matching against what is being emitted. So, we can explicitly ignore timestamps, or some values of some attributes.
Which are not reliable between runs.
But for the most part, you can actually make sure that you get a good sense of what is going to be common. And,
Those golden files are very useful, even just for developers to look at what the metrics look like, because sometimes you want to jump to the source of truth.
If the test passed, then you can actually be somewhat certain that the attributes that you think are going to be on the metrics are there. So, we have been using those golden files elsewhere as well, where we ingest those metrics, those golden files, and then we build pivot tables where I can tell you
For those metrics, here are the dimensions that you could expect in that situation.
**Ruediger Schulze (IBM)** 16:47 Interesting.
**atoulme** 16:49 It can even be a source of docs, right? So… but it's nothing to do with the bank frame, it's more like.
**Ruediger Schulze (IBM)** 16:54 Yeah.
**atoulme** 16:55 Like, how do you test this stuff, right? And then,
Unbeknownst to us, there has been a lot of effort in the last two years to build a set of tooling around certainty conventions and specification work called Weaver. And Weaver also can do this type of work. So that, I think, is the second link. The second link points to a feature in Weaver
Where, Weaver can do many things. It can, you know, emit YAML, it can do all sorts of stuff, but one thing it can do also is run as a server, and you can send it data, and it will check against the schema that is loaded from its own YAML, its 70 conventions and whatnot, and it will tell you.
if you're doing okay or not. And it's kind of nice, right? So…
It's an understated feature a little bit, but it's coming up. I was in the maintainer sync meeting yesterday with all the maintainers. Weaver is actually doing,
It's moving to 2.0. One thing that the folks behind Cement Conventions wanted to make sure they communicated to all maintainers is that the 17 conventions have been stocked… they've been all stored in one repository so far, under,
under-sematic conventions, but it's… they can't take it anymore. It's too much work, and it's a small team,
they've been centralizing a lot of things. What they've started to do is they've started to build a roadmap where they're going to say that they're going to own the core concept, but, and frankly, at this point, they have that, right? They've done it for a while. But for any SIGs that want to have semantic conventions, then it should be possible for those SIGs to deploy their own semantic conventions
part of their own Git repositories. So, what that means is that you would be able to import the common core concepts from them.
using these new Weaver capabilities that allow you to do cross-Git repository imports.
But, for example, for mainframes, we would be able to have our own semantic conventions, which would be much faster in terms of, like, you know, expertise and locality of data, and even the release cycles of those things. You would then be able to completely control that, because we don't right now, right? Which…
Not ideal.
It's in plans, and I think there is this…
there is a PR open for that, I can find it for you, just for your own education, if you're interested, but it's very early, they're not ready for us to kind of come over, but I just wanted to mention it, because it should inform a bit how we want to work moving forward.
**Ruediger Schulze (IBM)** 19:24 Yeah, so this is, this is, this is good information. How is this about…
does it change the approval flow? Right now, you know, it's the…
The domain SIC is approving, and then the semantic convention SIC is approving.
**atoulme** 19:40 Yeah, it would remove it from the semantic convention scene altogether.
**Ruediger Schulze (IBM)** 19:44 Okay, so it would be… the mean…
SIG would be the authority, then, for the specific domain to approve the conventions.
**atoulme** 19:53 That is correct. That's my understanding. I will… Find that,
I need to find that… is it an issue? It's the pull request, sorry.
So…
I'll find it for you, and post it in the chat and in the doc. But this is ongoing. And I think it's still time to comment if you have any comments back, but what that also means is,
Which is kind of,
a bit of a letdown is, it used to be that we had one semantic conventions repository for everything, so now people will need to do some discovery to find out about the mainframe semantic conventions, which might be in a separate place. And I don't know that we have an idea how to do a catalog.
of the CMT conventions. For you, it's actually pretty, like, domain-specific, mainframe, probably okay. I'm thinking about, like, more poignant use case, like, I have a, you know, fast statistics. It's going to be something that is going to be under-contrib for collectors, kind of specific to collectors in that particular receiver.
no way people are going to find that stuff by themselves. So how do we… how do we then kind of create a catalog of all those things, and kind of also harmonize the release cycle in some sense, so that people know, like, in March 2026, this is what this landscape looks like, and what people have, and what the latest version of everything looks like, right?
But that's not addressed yet. And frankly, it's too much to ask for them. They have too much work.
**Jim Porell** 21:22 I was wondering if it's going to delay adoption of mainframe stuff, because it's irrelevant, because it's not being viewed by the broader community.
Because the whole goal here is to make this stuff work as a hybrid environment. Certain vendors are going to do the right thing, but some might not.
**atoulme** 21:43 So, I think this is where we… we may have a bit of a stick, where we can also say that, you know, there's a level of…
We're having discussions with different SIGs. One of the things that we expressed earlier in the week is, I think it might make sense for us to also have a bit of a vendor
handbook that we would want to kind of start to place on vendors and say, here is how you interface with the OpenTeametry,
ecosystem so that you can be successful. And we can offer, right, at first, just
We're just here to help, right? So we could… we could make a Acme-type vendor who's just new to the ecosystem, decided to go into OpenTemmetry as a base, and we give them, like, an adoption scenario, right? It's like, okay, start with this, adopt semantic conventions, look for mainframe semantic conventions to support mainframes, and it kind of gives them a way to go about this, because
I think vendors are just really confused, and I'm not talking about the rank and file, like, people who are maintainers and participate in the project, but even at the VP level or things like that, they would need to have some sort of a guidance, but it's not such a hairy project. You can come and play.
And if we were to do that, then over time harden those as compliance or
you know, a badge of sorts, right? It's like, are you actually following this? Is there a certification suite that we can apply to this, and do you follow that? And then we can play that hardball, but that's years away, right? From now. But…
that would probably be it. First, you start with a nice approach. You make it so that people want to come in because they feel like, okay, this is not as scary as before, I don't have to do as much discovery, and then we… we then start to kind of, you know, get the water levels up and up as… as things get more and more, like.
declarative. And one of the big things that we want to do is to make sure that people don't fork the code.
Right? Because when a vendor forks, then, well, we're creating a tension in community. So how do we avoid that, and how do we give them an ability to wrap around some of the code that we offer? And frankly, I'm talking about ourselves, too. We're in the same boat, right? So how do we… how do we do that?
by the same effect, then how do we pass that back as a requirement for all OpenTeometry developers? They need to think about this when they develop code. They need to make it so that it's easy for people to offer additional configuration or extensions that allow some vendor-specific logic, because vendors have good reasons to offer additional things for themselves.
So, yeah, that's… You know.
taking the long view, that's where you would probably want to be. And you're not alone here. The mainframe is not specific, like, it's just one of many SIGs that are… is in the same situation, right? So, database semantics, right, are in the same place. Kubernetes semantics, same place. So, I really think we all need to
Approach this as a whole.
**Ruediger Schulze (IBM)** 24:48 Right, and I think… yeah, thanks for the update, Antoine, and I think it's a good segue into… I think one of these priorities for this year is really that we make progress with the semantic conventions, you know, various things ongoing as vendors, as, you know.
providers also of the system software, but I think the focus for this year really has to be on semantic conventions to make this tangible from a mainframe point of view, and also from a perspective of the SIC.
And I think we talked about approaches already before, right? Small PRs, I think this is what we need to get going in order to do this.
I think we heard also, for instance, about MQ, a couple of things, but as we progress into the year, I think it's really…
you know, let's use this meeting here to work through small PRs.
Let's start with HMC-based data, lowest level.
and move it up the stack, I think that's…
And then let's also work with the community on solving this.
You know, we talked about entities last year a couple of times, quite intensive discussions that we had.
**atoulme** 25:59 I think.
**Ruediger Schulze (IBM)** 26:01 I wanna follow up on this, and…
And also understand what are the entities that, you know, would have to be represented in the…
semantic conventions from a mainframe point of view, and also from a virtualization point of view, so…
It's actually not about mainframe in this case, it's also about virtualization in general.
**atoulme** 26:20 Interesting.
**Ruediger Schulze (IBM)** 26:21 Yeah. Okay.
Okay.
Yeah, I think this defines the roadmap, 2026 perspective.
There's more, as we discussed also,
I think I can say this much, we have an internal discussion around getting the OpenTelemetry SDK for C++ onto…
The community support, but again, this is dependent on the…
the ability to build in the community on Linux on S390X.
Yep. And, as soon as we make progress with the GTOP Action Runner.
But actually, this can become a topic as well with the C++ team.
Right.
**atoulme** 27:12 Understood. Morgan joined us, so,
we discussed this first when we started the call around this GitHub Action Runners next steps. Ridiger, you were going to comment on that discussion with Jeffrey, right?
**Ruediger Schulze (IBM)** 27:27 Yeah, yeah, I'm doing this just after the meeting, just.
**atoulme** 27:30 Oh, okay.
**Ruediger Schulze (IBM)** 27:31 getting my thoughts together, then, before I reply there. Morgan, one thing we discussed also at the very beginning, so, as is sick, I think we are at the point to move this meeting one hour earlier.
And, I think…
**Morgan McLean** 27:48 That's right! I had taken the action to do that, and I didn't get to it. I will do that today.
**Ruediger Schulze (IBM)** 27:52 Yeah, I think you have.
**Morgan McLean** 27:53 Apologies, I thought I had done that.
**Ruediger Schulze (IBM)** 27:55 Yeah, no worries. Okay. Okay, good. What else?
Let me see if I look here at the previous meetings…
Okay, MQ, we discussed. Craig, just out of interest, your EZCLA challenge is resolved, right?
**Greg Shriver** 28:17 Yes.
Yeah, that's… that's taken care of.
**Ruediger Schulze (IBM)** 28:22 Okay, good.
**Greg Shriver** 28:24 Thanks.
**Ruediger Schulze (IBM)** 28:27 Any other topics that you would like to discuss?
**Angelika Heinrich** 28:36 No, although anything I talked about in the last meeting was, drafting a PR for database,
resource attributes, so I've been comparing the…
attributes that we had defined initially in our OpenTelemetry, conventions for Mainframe draft document.
**Ruediger Schulze (IBM)** 28:59 to what is, in the semantic conventions, and I'm just looking for anything that we.
**Angelika Heinrich** 29:06 Called out as… needed, and then once I have a draft, I'll share it with the SIG here.
And then we can go through those together. I don't think we have very many mainframe-specific resource attributes at this point.
But there are just a couple, I think, that are worth calling out.
**Ruediger Schulze (IBM)** 29:30 That sounds good.
Nope.
Sounds good.
And just…
There's also one topic that we need to come back as we look at entities and, you know.
That may actually also help or guide our discussion about what you just said, Angelica.
As we move into entities, we really need to look at what are the identifying
Attributes of these entities that we are…
Defining, and if you define databases, we also…
Maybe this is then already given from… You know, the generic definition.
**Angelika Heinrich** 30:13 Maybe.
**Ruediger Schulze (IBM)** 30:13 Something that we need to consider, and similar for any other entity on the…
And I say this because our current definition, we need to fix this, for CUS softwares, actually.
It's incorrect, currently, at least as it's on the documentation.
**Angelika Heinrich** 30:32 Okay.
**Ruediger Schulze (IBM)** 30:34 I'll keep that in mind as well. Okay. Yeah, from an entity position point of view.
**Angelika Heinrich** 30:40 Okay.
**Ruediger Schulze (IBM)** 30:41 Oh.
Okay, then, yeah, happy to, you know, continue the mainframe sect this year.
Thanks everybody for joining, and then… Let's continue next week.
**atoulme** 30:59 Alright.
**Morgan McLean** 30:59 do it. Alright, sounds good.
**Richard Nikula** 31:01 I agree.
**Greg Shriver** 31:02 Everybody.
**Jim Porell** 31:02 Bye.
**Angelika Heinrich** 31:03 Right?
