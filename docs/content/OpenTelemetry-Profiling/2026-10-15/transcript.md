SIG: OpenTelemetry Profiling
Date: 2026-10-15
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Paris (21RC)-7.01 Champagne** 04:49 some… Hello, everybody!
Since we're 5 min in, I suggest we get started, and as usual.
work our way through the previous action items in the meeting notes document. If you haven't already, you also put yourself as an attendee.
The first review action item, I think it's a little celebration. Maybe, Henriette, if you want to talk about it. Yeah, so the spec PR for… virtually the OTIP profiles is merged.
Yeah, let me share my screen.
And the collector implementation that adds the… Version 1 metadata was also merged as well, and was released in the productive release that was done on Thursday.
So, we should be done.
Very nice. And yeah, I'll share my screen now so everybody can see the meeting notes. One second… How can I actually do it? Just to consume and share screen.
There we go. Okay, let me just catch up on notes, update PRs have been merged.
Was there any detail we need to include you on that? No, it's also on the collector as well. So the collector.
Sweet. Yeah, my, my updates will be, pretty short. And also like, we don't have any agenda items today beyond the action item review. So if anybody here can think of a agenda item for afterwards. Please feel free to edit while we're speaking.
Check that the notes here.
So I have two action items here. And the short update there is I have not made progress because I was on PTO and we're doing team meetups this week, including our new colleague Florian.
And so I will get to this, however, next week. So I expect to have pull requests raised, and I will share it in the Slack channels, asynchronously, so hopefully we can get this, in a good place until the next meeting.
Then do we have Alexey here today? Is he here already?
**Alexey Alexandrov** 09:32 Yes.
**Paris (21RC)-7.01 Champagne** 09:34 Sweet.
Cool. Do you want to talk about this quickly?
**Alexey Alexandrov** 09:39 This is merged.
**Paris (21RC)-7.01 Champagne** 09:43 Okay.
Awesome.
**Alexey Alexandrov** 09:44 Yeah, so, done, basically.
**Paris (21RC)-7.01 Champagne** 09:47 I did see like an action item from, or not an action item, but like an item from last week's notes. Ivo said you wanted to refuse on… On this PR, so Ivo, do you know if this needs more refuse, the Node.js thread context?
I think we're good. I think we not need to merge it. Do we have? Do we have enough to merge now.
I guess we need 2 people right? I think there was feedback from Timo but it was addressed.
when one's feeling. Is that spell checking? Or yeah, I think we can ignore this.
Partners.
I need to switch accounts.
And I think this one in particular, since this is more of documenting how the thing is going to work.
it's like there's a non-zero chance. We've been trying this and implementing this and whatever, but there's a non-zero chance that, like, we might change, like, a comma here, a comma there. But I think it's more, like, the intention of the document is more to go, like, are we all in alignment, and does this seem sane, and we want to move forward? And so, I think, like, if people have feedback, and please continue sharing any feedback, and we will integrate it in the document.
and obviously make it better. Yeah, I actually put it to do for myself that when I get to some hotel stuff next week to also take a look. But unless there's concerns, we can squash and merge this.
Let's go, and let's… let's get it done.
Let's put it into the notes here as well.
Docs.
Okay, that… means we have made our way through all of the action item review and we are Currently looking at no further agenda items, so we will rely on the Spontaneity of this group to either come up with some or have a very short meeting today until we have some more things to discuss next time.
Maybe a question is we on the Sig Profiling Repository. We have the roadmap to Profiling Beta. Yes. Do we want to add it here? So it gets more attention. And we Focus more on getting… getting it down the road.
Yes, I think we do need to start asking ourselves what needs to be done there. Let's I think it was linked somewhere. I added it. Yeah, it's up here.
So we can kind of look through that. So yeah, we've got, Jonathan's, PR that I think we, basically, once we feel we're getting close to beta, we can merge. Actually, I think now that we have the versioning, with the versioning, this is unblocked now. So, I'll leave a comment on this PR to make it clear and put it on the agenda item.
Meeting notes as well.
Yeah, yeah, we need to bump the browsing. Yes.
Yeah. But if you resolve the conflicts and bump the version, this change is good to go.
Okay.
Just second the doc.
Left certification now.
Oh, somebody already put it here.
Oh, no, that's a different one. Yeah, and that's the root method. I guess.
It's getting serious now. Yep.
Yeah, since we… I think we have Thomas in here, is that something you can, push forward?
**Jonathan Halliday (IBM)** 14:39 Yep, sure.
**Paris (21RC)-7.01 Champagne** 14:41 Awesome. Cool. Thank you so much.
Then let's see what else someone else wrote back.
pure type. Yeah, this is already in the action items. It's on me right now. Standardizing document.
Yeah, maybe I should take ownership on this, since… or maybe market is done to. Well, I'll just put my name instead.
Let's see some more comments.
Umm.
This is a work in progress. There was a Pr. I opened A few weeks ago, but there was… I took some time off and it was deferred, I would say. So I will come back to this.
Okay, I will just make an action. Listen, no docs.
Okay.
Nope.
Okay.
Yeah. And I think this one doesn't have an owner yet. Analyzing the UN 3264. I think the issue describes what what we need to analyze here.
I think it is… Otl Tl. Ottl has only IN64 and FLOAT64 as data types, and we are using other data types in our signal, and the question is, is it fine for an UIN64 to be converted into an IN64 when it flows through OTTL? I guess one theoretical problem there is, like, a very large duration nano could become negative, and if there's an OTTL check to check that duration is positive or something, it could fail. Yeah, we… I think somebody just needs to think about this a little bit more, look at code, maybe talk to people.
And I guess primarily we need an order. Is anybody here interested in picking this up? Or should we come back to it later?
Oh.
As far as I remember, the memory mapping message is not even implemented on the Ottl side yet.
Heading of the location message.
So… It really is just an… theoretical issue at the moment.
except for the The first things, but, yeah, it's a general question.
Around… Different kinds of types.
So in Otgl, all the sub messages need to be implemented.
Before you can actually interact with the sub message like mapping location.
and as far as I remember, mapping and location are not implemented yet. So I can quickly… Okay, so in other words, nobody can use OTTL for profiling right now? You can, you can, but only for the very top message. So for resource attributes, but in resource attributes, we're not affected.
and message profile.
is also implemented. So the duration, nano, and dropped attributes count does affect us. So Win64 and Win32 Are the two of them.
Okay, so we do have. It's not theoretical for now. I'm seeing that there is a unit support on the metrics portal.
So I wonder how other people are doing this. Yeah, somebody needs to look into it. Maybe. Yes.
Yeah, I think primarily we need somebody to raise their hand to either, like, hey, I want to look into this and do this, or if not, we can just keep it on the list and come back to it later. We could also decide that this is not critical for going to beta, I don't see it as critical to be fair.
Okay, but this one, just my personal… I'm feeling, so I don't have any data to back it.
I guess my thinking would be, like.
Otpl is like a capability that sort of builds on top of the signals. And it's Otpl's job to support the signals, not the other way around. Maybe. Is that potentially reasonable. Then maybe we will just update the roadmap to this not being a must have and that also means there's less pressure on finding an owner. For now.
Yeah. So we we can basically look at this list below here for before we go to better, we can take another pass and see if, like we want to do anything now, but I will demote it for now to to that section.
July.
**Boris Marinov** 20:16 Sorry sorry for crashing in, but I was just looking through the units, and I don't think we can get to the values which would cause an overflow here.
But yeah, just just my 5.
**Paris (21RC)-7.01 Champagne** 20:28 You're thinking duration couldn't get so large that it would be an actual issue.
**Boris Marinov** 20:32 I mean, it's like what? It's like hundreds of years, something like that. Or I need to do some more napkin map, but.
memory, address, and so on. I don't see anything which could get that large.
**Paris (21RC)-7.01 Champagne** 20:47 Yeah, I mean, that would be one answer to why we might be okay with it.
Is memory like addresses typically just don't get very large?
because virtual memory space. How how large does Linux support virtual memory?
address space. Does it use all 64 bits?
**Boris Marinov** 21:10 Good question.
**Paris (21RC)-7.01 Champagne** 21:13 I mean, I agree that, like, this is probably not, like, a very common problem we're gonna have, but yeah.
I agree on the duration. That seems I would like to The drop attitude might overflow, however, but if you have And who in 32 dropped attribute?
Thank you.
That's true. And also if you just thinking about if you have a reporting interval of, I don't know.
1 min, 5 min, and you exceed U and 32. Then Yeah, but for you to go in.
Yeah.
And I looked at the memory addresses, so what would overflow is something bigger than 2 to the power of 63, right? Yeah, and that's 9 exabytes.
Yeah, I don't think anybody is running with that. Well, because it's virtual memory. Anybody could just make an allocation. Yeah, it's really large. And like, maybe somebody has fun doing that.
But… Yeah. If there's a machine with that amount of memory, I wouldn't talk today. Today's memory prices? I don't think so.
Okay, then let's basically conclude we're we're demoting this now to non-proper consensus. We're not seeing this.
Walker, look that up.
it's very unlikely we will hit the edge cases here. More importantly, OTTL Folks need to probably worry about how to support.
All the signals were directly dependent.
The signal it's deciding.
many themselves around OTTL constraints.
Okay.
Cool.
But yeah, basically, I mean, we're getting very close here to knocking out the remaining action items that would allow us to go to beta. Yeah, and then… I think we are going to… has the opportunity at Datadog to do a lot of testing and to actually ship it to people using it, so we'll get plenty of feedback and experience with the beta version, and I think pretty much we only will have to address real-world things, I guess.
we we can push on hotel Sdks to start implementing the the signal like the go. Sdk, would be a good target. Get feedback from those people. So that would be the post that I work.
But yeah, I think we're in a decent shot now to get it done before the end of the year for sure. You can assign the release OpenTelemetryProto for beta for me.
29.
You have to… Okay.
I'm…
**Matt Tichenor** 24:27 Hey, on that… hey guys, sorry, I've joined these a couple times, but, Matt from AWS. On that SDK path, like, what… What would be the path to… contribute on that. Is that, like, a separate steering meeting? So I'm still learning, like, how Ulta works and all that, but basically, something I'm trying to do from AWS is see if we can't, like.
Get some development resources to help contribute on the.
SDK repos to help contribute on the, like, ad profiling to the.
**Paris (21RC)-7.01 Champagne** 25:00 Got it.
**Matt Tichenor** 25:00 But I, like, on my side, I'm just trying to get, like, advocate to my leadership to get the… get the headcount to kind of be dedicated to this, but, like, I don't know what the path would be, you know, like… Paris (21RC)-7.01 Champagne 25:12 Yeah, I would say, first of all, thank you for potentially being able to contribute in this area. Amazing.
And so we have an issue here. It's on the beta roadmap Profiling support on the SDK. So it's not blocking the beta, but obviously it would be great to push this forward as we approach the beta. Frederick, who often attends these meetings from Polar Signals.
has made a meta issue and created sub issues in all the SDK repositories.
And so, I think clicking through these links and seeing what the status of these discussions are, like, for example, here's the Go one, which I guess was raised, and… somebody had already volunteered to maybe take this. But there's no action taken yet. And last update was in June. So basically, the the next step would be to to ping some of these issues. But I think in a lot of cases you could just be like, Okay, we we have bandwidth to do this. And then I think just each of the Sdks follow some contribution process that Yeah, they have their own meetings as well, I think all the language SDKs have meetings. It might be good to show up there for a meeting with, like…
**Matt Tichenor** 26:20 Alright, alright.
**Paris (21RC)-7.01 Champagne** 26:21 We have interest. But yeah, pushing on these issues, you could also ping Frederick to just check if there's any context that's maybe not captured in the piece on the CNCF Slack to see if there's any context on these issues. But yeah, I think that would be the path forward.
**Matt Tichenor** 26:35 Okay, thank you so much for walking me through that. Super helpful. Sorry for a newbie question, but I feel caught up now. Thank you.
**Paris (21RC)-7.01 Champagne** 26:41 Wonderful question, and much appreciated.
So, let me just… I'll just capture some notes here.
I think. For Java. However, I think Jonathan has already done work. Is that correct?
**Jonathan Halliday (IBM)** 27:36 Yes, I'm currently looking at implementing the context OTAPs, for example.
**Paris (21RC)-7.01 Champagne** 27:46 So, for Java, we might be good, but, like, all the other languages, I'm not aware. I think the .NET folks did some stuff very early on, I don't know what shape that is in, but I think most of the SDKs, no work has been done yet.
And if Go is something you'd be interested in, I'd also be happy to chat about this.
**Matt Tichenor** 28:03 Okay. Yeah, I was actually going to start with Java. It sounds like that's already working in place there. So let me.
**Jonathan Halliday (IBM)** 28:10 John.
**Matt Tichenor** 28:11 Jonathan, I might ping you.
**Jonathan Halliday (IBM)** 28:12 I have some mobile.
**Paris (21RC)-7.01 Champagne** 28:13 I need some help.
**Matt Tichenor** 28:14 Haha.
**Jonathan Halliday (IBM)** 28:15 So, I'll drop a link in chat for you that's notes on where things are at with Java, that's the place for you to start.
The Profiling Signal is a weird one in terms of the OpenTelemetry SDKs, because for the other signals, it's the SDK that generates the signal.
So, they have to have an API defined, and they have to exist in the SDK, or they can't be used.
Profiling doesn't work that way. It's the profiler that generates the the signal, so if you're doing something like eBPF profiling, the SDK isn't necessarily involved.
So the Java one, for example.
It's… it's not the thing that's going to be generating and sending the The wire message.
**Matt Tichenor** 29:05 understand.
**Jonathan Halliday (IBM)** 29:05 I mean, I mean, you potentially can. You'll see in some of the scenarios in that Google Doc, it does. Like, you can, you can have it read Async Profiler or JFR files and convert them and send them.
That's one possible use case.
And it's gonna need to implement the OTEPs for the thread context, so it can expose them to external profilers.
So there's… there's definitely things to do, but they're not necessarily the same things as other signals have to do.
**Matt Tichenor** 29:39 Okay, great. Thank you for sharing the doc, Jonathan. I'll take a look.
**Jonathan Halliday (IBM)** 29:43 if.
**Matt Tichenor** 29:44 If you don't mind me, I might stalk you down on Slack if you don't mind. All right, excellent. Thank you.
**Paris (21RC)-7.01 Champagne** 29:50 I think it's also worth noting that Async Profile itself, I think, has already added support for OpenTelemetry. Yeah.
**Jonathan Halliday (IBM)** 29:57 That's mentioned in the doc.
**Matt Tichenor** 29:59 Yeah. Yeah, that's what… because that… yeah, no.
**Jonathan Halliday (IBM)** 30:02 Matt, Matt, what's.
**Paris (21RC)-7.01 Champagne** 30:03 Like, also testing and, like, picking up.
**Jonathan Halliday (IBM)** 30:05 That's an interesting one, because on one hand, I love that they're getting involved and, you know.
**Matt Tichenor** 30:10 So yeah, I'll follow you up on Slack, Jonathan. I'll read through those docs, see where you're at so far, and then, like.
**Jonathan Halliday (IBM)** 30:16 Yeah.
**Matt Tichenor** 30:17 The main maintainer for Async Profiler is a guy at AWS that I know, so we can pull him into the conversation too, if there's benefit to that.
Oh.
**Jonathan Halliday (IBM)** 30:27 Right.
**Matt Tichenor** 30:28 Cool.
Awesome.
**Paris (21RC)-7.01 Champagne** 30:33 Good. Okay, then… Yeah, I think we managed to get through all the stuff that was on the critical path for the roadmap.
And… Not sure if we need to discuss more there. Any other things we're getting on the roadmap?
Well, I mean… nothing serious. We will probably like, we probably want to do blog posts and things like that once we get to this point.
No.
**Jonathan Halliday (IBM)** 31:11 Do we have plans beyond Peter? You know, there's certain decisions we took.
Along the way, like we said, we weren't going to.
trying to do.
the sort of self-describing user defined events that Jfr. Does. For example, we said, Yeah, that's that's out of scope for the 1.0 format. We might do it in a A post 1.0.
And the other one that springs to mind is symbolization and whether we want to do anything around standardizing for that.
Are we saying once… Beta ships and, you know, transitions into stable eventually and once the OTEPs are merged.
Are we done, basically? Are we just in maintenance, then?
**Paris (21RC)-7.01 Champagne** 31:58 you I have the feeling that, We can go fast to beta, but I I have also the feeling that we will not get fast from beta to stable, so it will take some time.
**Jonathan Halliday (IBM)** 32:14 Yeah, absolutely. I think that's the right thing to do. It needs to bake in the community for a long while before it's declared stable.
**Paris (21RC)-7.01 Champagne** 32:21 Yeah, and as a Profiling SIG, I think we can take this time then between beta and stable.
to gather more feedback, but also to focus more on the symbols symbolication protocol.
I would not… I think we can build a symbolization protocol independent of the profiles protocol.
So I would not mix them.
But I think so, too. I don't think it's on the critical path for getting the core signal stable, but it is on the critical path for saying, hey, the Profiling SIG is now maintaining the signal, rather than we're done with our work. I think we do need to shift the simplification protocol to really declare Profiling to be comprehensively covered by OpenTelemetry.
Yep.
Yeah, there's also the work.
Now, colleagues from Datadog do on the process context side.
Yeah. But I think we, as a profiling sick.
I think most of us approved the process process context protocol stuff.
But we're not that much involved, so… There's also a lot of learning from this side.
And I think there's no SDK that implemented Prosex context yet.
Yeah, we've been trying to to get it into rust. And well, you started some work on go. But yes, we still work in progress. Unfortunately, for different reasons. In diff in in each case, there's there's been like questions or things that we've yeah, or it kind of got stalled. And we've not gotten enough reviews or or feedback on it.
Yeah. On the question on self describing events. I don't know if there is enough appetite to to go try to support all of what Jf. All can do. At least not for like stable post stable. I mean, I guess all options are on the table. So if there's enough interest to to make a more complex version 2 at some point, or figure out ways to extend what we have through semantic conventions or other means. I I suppose it's on the table, but somebody would probably have to come up with something a strong yeah, use case for for doing that. I I think we shied away.
consciously from making the hotel Profiling signal a super set of Jfr in the past, because it's just yeah, very complex data format. But that could be revisited if we, if we find a good reason to do I don't know if you feel strongly about it, Jonathan. I'd be curious.
**Jonathan Halliday (IBM)** 35:29 Yeah, I'm inclined to take a wait-and-see approach. I don't think proactively working on it is the way to go. We need a use case, a driver from the community.
**Paris (21RC)-7.01 Champagne** 35:42 Yep.
Okay, cool.
Any any other things we should discuss. We have more time, but we can also give time back.
on… Just letting the question linger a little bit to give people a second to think about it.
But… If I see no hands here going once, going twice or three times, then perhaps this was a very nice and efficient meeting where we covered a lot of ground. It's clear what we need to do next. And yeah, thank you everybody for the participations, all the work done. And yeah, have a nice local time.
See you all. Yeah. Thank you. See you. Thanks, everyone.
