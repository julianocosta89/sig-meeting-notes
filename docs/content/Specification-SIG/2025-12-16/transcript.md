SIG: Specification SIG
Date: 2025-12-16
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:19 Hi, everyone.
**Daniel Dyla (Dynatrace)** 00:32 Hello Not very much everyone here today.
**Liudmila Molkova** 00:39 Yeah, this is the last call of the year, right?
The SPAC call of the year.
But I have some backed agenda.
I think Robert is offline.
Oh no, you're online.
**Pellared** 01:13 Change of plans, I was able to join.
**Liudmila Molkova** 01:20 Nice, so let's give people a few minutes to join.
While we are waiting, Carlos, I saw, I wanted to merge this one.
And I saw you wanted to discuss it in the spec call. Do you know what do we want to discuss here?
**Carlos Alberto Cortez** 03:03 It's not, like, actually discussing, just letting everybody know.
**Liudmila Molkova** 03:07 From now, we will be forcing more,
**Carlos Alberto Cortez** 03:11 change logs, if you don't… if you think that this is an editorial change, just… you have to include a label. You know, the one you see in the, the label section here in this PR, like, skip changelog.
So, yeah, just for, you know, hopefully this will make things easier for everybody.
And that's all, yeah, I think we can merge that.
**Liudmila Molkova** 03:32 Yay! So let's… let's consider it to be the announcement.
Let me do the honors.
Craig, so, sorry for jumping in front.
Let's get started! Do we have quorum? We have… Quite a few folks here now.
Robert, let's talk about stabilizing complex attributes.
Do you want to present? Do you want me to present?
**Pellared** 04:13 I can try, and you can just… you can just add any additional comments, which I… if I miss anything. So, this is just the PR, which… about stabilizing the attribute… any complex attributes, and also the any… the empty, attribute as well.
And this isn't just about making this stuff stable, also cleaning up a few things which are redundant, as this is going stable.
And we have 3 prototypes. These are only prototypes because this is, like, all of these types are in common packages, and I think doing it in some experimental stuff is very problematic.
At least we have a kind of a branching go. In Python, there will also protected. In Java, I see it's already merged into incubated, because Java has an incubating.
So, I was considering adding it to spec-compliant metrics, but I saw that I haven't found any good place to do it, so if the TC or anyone want to add it, I just… I'm just fine doing it as a separate PR, I just had no idea where to put it in the spec-compliant metrics, or if we have even needed there.
And yeah, we wanted to have the merged in, kind of, beginning or at least mid-January, because we said in the… in the blog post that we want to basically have supported in 3… in about 3 months.
So, that's it from my side. Ludemua, do you want to add anything from your side? We also get no feedback against going further.
any issue, we haven't got any issue, any comment. We haven't received any comment that this is a bad decision.
or… Apart from the comments that were before, of course.
**Trask Stalnaker** 06:03 Just a clarification, it was 6 months from the… when the OTEP was merged.
**Pellared** 06:10 I thought it was free, but time is going fast.
**Trask Stalnaker** 06:13 And, we are… we've… we have, we are chomping at the bit in Java for it for two reasons. One is, to stabilize To stabilize the complex attributes in logs, which we could have done already, but… or actually, I guess we did… did we do… Jack… No, we never stabilized complex attributes in logs, because we were waiting…
**Jack Berg** 06:45 It's for the log body, not the actual.
**Trask Stalnaker** 06:46 Yeah.
Yeah, so that's one reason, and the other reason is, the GenAI instrumentation folks want to… are asking to start using this on spans. So we do have a span use case that people are… are waiting on.
**Pellared** 07:16 Yeah, it's also a blocker for stabilizing the… In autogo, the logs.
**Jack Berg** 07:26 I'll review this. I don't see why any reason why we shouldn't proceed with this.
We've talked about this in circles forever.
on the spec compliance matrix, I do think that this should be called out specifically, because it's such a significant departure from expectations. There's two places I can think of.
there's, specifically in the span… the traces section, we call out, like, hey, do you support adding a Boolean attribute? Do you support adding a string attribute? Do you support adding a double attribute?
And then we don't have symmetry there with the log API and with the metrics API. So, like, basically, the trace API calls out specific attribute types, metrics and logs don't. Maybe it makes sense to extract a section specifically to attributes.
And then there's another section that comes to mind about the exporters.
you know, basically, like, OTLP exporter capability. Does it support the serialization of complex attributes?
So those are the two things that come to mind.
I'm not particular about whether it gets merged as part of this PR or in a follow-up, but.
**Pellared** 08:40 I prefer having a separate PR, it can be even much sooner.
**Jack Berg** 08:45 Oh, that's true, actually, right? Yeah, because it's not dependent on stabilization.
**Pellared** 08:48 Yep.
I will create an issue afterwards.
**Trask Stalnaker** 08:56 As.
**Pellared** 08:57 You can block it or not, it doesn't matter for me, but let's just have it merged mid-gen, if possible, stabilization.
**Jack Berg** 09:07 The Jan 1st merge data is tough. Oh, it's January 12th. January 12th, okay. 15, yeah.
**Trask Stalnaker** 09:13 15.
**Jack Berg** 09:14 But then what does the 112 mean in the notes?
**Pellared** 09:20 Probably my mistake.
**Jack Berg** 09:22 Okay.
Okay, so we should target the 15th, because that's the 6-month mark.
**Liudmila Molkova** 09:29 I think it makes a difference for anybody 12s or 15.
**Jack Berg** 09:33 Yeah, I just didn't… I just wanted to make sure we weren't merging this on, like, when we said OTEL was off for the last two weeks of the year.
**Liudmila Molkova** 09:40 Yeah.
**Jack Berg** 09:46 So let's get, some reviews before this last week of OTEL.
being on, so we can be in a good position to merge it. Maybe it's not urgent, because we have till the 15th, but, reviews and approvals, so we can just merge on command.
**Trask Stalnaker** 10:06 Yeah, I mean.
**Liudmila Molkova** 10:06 That's.
**Trask Stalnaker** 10:07 We can make, if the spec maintainers could plan on a release shortly after that.
That would be awesome.
**Ted Young** 10:19 be a great.
**Trask Stalnaker** 10:19 That will, I think… I always forget what we say, if it's official, once it's merged, or once it's released, but just to give us the go-ahead in the languages to, to stabilize.
**Jack Berg** 10:36 probably, official once it's released, but I know at least some of the time in Java, we've… We've kind of merged things, dependent on The stable spec before the spec was released, so… it's good to have both.
**Liudmila Molkova** 10:55 Usually, it's Carlos who releases, I don't know why, but if he's not available, I can release.
**Trask Stalnaker** 11:07 Whoa.
**Liudmila Molkova** 11:10 Cool.
Then let's move on. Robert, you're still on stage, optional ergonomic API, and I think we have some approvals here, quite a few. Is there anything to call out?
**Pellared** 11:25 just an important fact that this is not stable, so it's not that dangerous, and I think I even… I'm not sure if I did to the spec compliance matrix or not.
I am not sure, but also, I think I did add it.
Still, it's a May, so yeah, I added it as well.
So, yeah, a lot of approvals, so just asking for reviews if someone is interested, if someone to check the language, etc, if everything here is clear.
That's all from my side.
**Jack Berg** 11:59 Before we move on to the next topic, I'm just… I'm just checking that… we have a change log entry and a spec compliance matrix entry, and we do, because this has plenty of approvals and has been open for a long time without dissent, so I don't see any reason why we shouldn't just merge this.
**Carlos Alberto Cortez** 12:19 Yeah, especially…
**Jack Berg** 12:21 The build is failing because of a link check, but, like, you know, there's been plenty of time to, you know, disagree with this.
**Carlos Alberto Cortez** 12:30 Yeah, also, it's in development, so I think it's totally fine for now. Once we want to go stable, we will have to make some hard calls, probably, but in the meantime, I think it's fine.
**Jack Berg** 12:41 Alright, I'll merge this as soon as the build is passing.
**Liudmila Molkova** 12:47 Wonderful.
Okay, Tad, do you want to talk about Autel Unplugged?
**Ted Young** 12:56 Yeah!
So, just one final shout-out for the year, and I'll try to go around to the different, like, SIG channels and things, but, we're doing OTEL Unplugged at Fostum. If you haven't heard, OTEL Unplugged is an unconference.
So this means we'll be spending the day, basically doing Birds of a Feather breakout sessions with each other, so rather than having, like.
A conference track where we all have to sit there and not talk to each other while somebody gives a lecture on something we may or may not be interested in. We're just picking the topics and, having communication between us and our end users.
We're also going to run, like, a project planning session to try to get, like, roadmap ideas from our community, try to get a sense of, like, what people, think is important.
We threw one of these a couple of years ago, before the pandemic in Detroit, or maybe that was after the pandemic, I can't remember anymore, but it was in Detroit, and it was a really good time.
And these things work best if we have maintainers, you know, TC people, GC people, attending. So… If you can come, it would be awesome, and if you're thinking about coming, my request is that you buy a ticket. It's 20 bucks, and buying a ticket will let us know, who's coming, and whether or not we need to, like, freak out about attendance. So… If you're thinking about coming, please buy a ticket. I'm actually curious who here on the call Is thinking they'll be able to… to go.
I know, I'll be there.
Maybe nobody?
Well… Anyways, for people who, have, European wings of their operation and their SIGs, please, please put a shout out.
That's all I got.
**Liudmila Molkova** 15:05 Yay, thank you! It's exciting. I wish I could come.
**Ted Young** 15:09 Yeah, I hope it'll be exciting, but also, like, yeah, a little bit worried that, yeah, I've never been to Foston, but February in Brussels, you know, so… I do feel like we need to make some noise to get people to come. Especially because, weirdly, this is the one year there's always, like, an observability dev room at Fostum.
And due to just, like, mistakes-were-made kind of tragedy, there's no observability dev room at Fostom this year. So I am a little worried that people are gonna, like, hear that, and not hear about OTEL Unplugged, and then think, like, there isn't a lot of observability stuff happening at Fostom.
So, double reason to, like, spread the word about this, because it'll be, like, our dev room alternative.
Cool. That's all I got, for real.
**Liudmila Molkova** 16:01 Yeah, nice. Thank you. David, let's talk about metric start time.
**David Ashpole (dashpole)** 16:07 Woohoo. Yeah, so I'm trying to help unblock the remove API effort that, Antoine is working on, and so one of the things that I think needs to happen before we can really talk about a remove API is, Improving the spec around, start time.
And in particular, for cumulative metrics, a lot of SDKs today will use the process start times, the start time for all metrics, and if you can remove series and restart them, then that becomes problematic. So, this is an effort to, first, for this page that we're looking at, I think.
I'm just unifying the language, so we had a few different ways that we described the start timestamp in this document. I've just changed them all to use the same language, which is, that one that's used there for synchronous gauge. Start time is the timestamp that best represents the first possible moment.
a measurement for this time series could have been recorded. So I'm sticking to that language throughout.
And then in the SDK section, I've added a new development start time section, and… It all builds off of that language from the existing data model, which is that it's the first possible moment something could have been observed, and then adds some additional requirements.
My question for this group, well, of course, I appreciate reviews, but the main question I have today is.
I assume that we… that all this new language has to be a should, because we're not going to be requiring SDKs to implement a remove API, right?
I see maybe some nodding.
Like, there's no precedence for us adding new, like, must requirements for SDKs after 1.0.
**Jack Berg** 18:01 That's… that's tricky, because it could be a completely new area.
And so if you have, like, a new… if you have a new area that's optional, then that new area can have musts within it, right? Like, you know, for example, cardinality controls, the cardinality limits, if you… if those didn't exist before, you should add cardinality limits, and the cardinality limits must behave this way, right? That should be allowed.
**David Ashpole (dashpole)** 18:28 Okay, but this is definitely, trying to change existing behavior, so I'll leave it as should for now.
**Liudmila Molkova** 18:36 Like we use, we say, if this is implemented, then it must be implemented this way.
**David Ashpole (dashpole)** 18:42 I see, I see, okay.
We can add that language once the remove API exists, I think.
**Jack Berg** 18:50 Do you think this is, like, I haven't been following the remove stuff very closely. I'm supportive of it, I just haven't had a chance to engage in it.
**David Ashpole (dashpole)** 18:57 Do you think this is strictly a blocker? Because, like.
**Jack Berg** 19:00 Is there anything in the SDK spec that would suggest that, you know, an SDK can't, you know, produce start timestamps like this? It seems to conform to the data model.
**David Ashpole (dashpole)** 19:12 There's… there's nothing there. I think it's… I just think it's helpful to talk about and write down… How you should handle start time.
before we talk about the remove API. Otherwise, it's, like, a lot in… 1PR, conceptually. So, that's my intent here.
**Jack Berg** 19:29 Yeah, yeah, that's… that's fine.
it's like, yes, sometimes there's a lot of implicit context in, you know, inspect PRs, and I guess what you're doing here is making it more obvious how to implement this thing when the remove API comes around.
**David Ashpole (dashpole)** 19:46 Yes, so then it'll be obvious, like.
oh, we see a new series. Well, actually, if you implement it this way, then remove becomes Like, not… Really easy, right? So that's the goal, is make the hard thing a little easier, yeah.
Josh?
**Liudmila Molkova** 20:06 Oh, you're muted, Josh.
**David Ashpole (dashpole)** 20:09 Or we're listening to… His ceiling. No, we're…
**Liudmila Molkova** 20:13 Still no.
**Joshua MacDonald** 20:22 Alright, okay, so you can hear me.
Yeah, I think there's something, that was left out, like, that was completely underspecified in the original work, so… so in the sense that Jack asked, like, this isn't really break… this isn't optional, like, finally we're specifying what you should do, and I think it would be okay to put a must in at some level.
This is great.
we've needed this for a long time. I also sort of think that the words best represent are loose enough to give SDK authors actually a lot of decision-making power to keep compatibility that they had. Like, there's nothing saying they had to use process start time either, so that's the sense in which I don't think this is breaking. It was just left out.
**Jack Berg** 21:06 That was just the simplest thing to do, because there weren't requirements that suggested any other implementation.
**Joshua MacDonald** 21:12 Right.
**Jack Berg** 21:21 I'll take a look at this, David, and you know, likely just approve this.
**David Ashpole (dashpole)** 21:25 Okay, I will be working on a prototype in Go, but of course I would welcome any Help from people who work in other languages to make sure that this makes sense there, too.
Cool, that's all from me.
**Liudmila Molkova** 21:42 Wonderful.
So, if there is nothing else, Done?
Happy holidays! It's the last meeting of the year, we will have a break till January 2nd, or… I think even later than that, no?
January 2nd, okay.
**Trask Stalnaker** 22:03 It's at the top of the screen now. I just post… I just put up the, What do you call them? Notification.
**Daniel Dyla (Dynatrace)** 22:13 This meeting will be on January 6th.
**Liudmila Molkova** 22:16 Yes.
And yay, it was a great year!
we almost graduated. We did a lot of stuff in the spec, and every… everywhere else in… up in telemetry, it was great.
Working with you all, and looking forward to 2026.
**Jack Berg** 22:41 I wonder what everybody's timeline was of 2020.
**Ted Young** 22:43 2025. We don't need to do this on this call, but I… what's the… what's the best improvement OpenTelemetry made in 2025?
**Jack Berg** 22:50 You should collect that, and someone should do a blog post.
**Trask Stalnaker** 22:54 declarative configuration.
**Ted Young** 22:57 Yeah.
**Jack Berg** 22:57 Oh, I'm honored.
**Ted Young** 23:00 I feel like it doesn't, our effort doesn't quite line up with the calendar year, but yeah, just stabilizing everything and putting a bow on it with, like, configuration and everything getting marked stable, having more, like, auto-instrumentation stuff, like the injector to… and, like.
to be able to, like, actually, like, package all of this up for people, I feel like we're… we're, like, 3 months away from OpenTelemetry being in kind of, like, a really, like, a new phase of its existence, and I'm really excited about that.
So, happy holidays.
**Liudmila Molkova** 23:40 Holidays!
**Jack Berg** 23:43 Bye.
**Trask Stalnaker** 23:43 Thanks, bye.
**Carlos Alberto Cortez** 23:45 Dude.
