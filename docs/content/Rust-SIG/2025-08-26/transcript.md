SIG: Rust SIG
Date: 2025-08-26
Duration: 14 minutes
============================================================

## Zoom Recording Transcript

**Cijo Thomas (Microsoft)** 01:37 Oh.
**BA Björn Antonsson** 01:46 Hi there.
**Cijo Thomas (Microsoft)** 01:54 Hey, Bjorn, are you able to hear me?
Glow.
**BA Björn Antonsson** 01:58 Yep, I can hear you. Oh, okay.
**Cijo Thomas (Microsoft)** 02:00 Okay, yeah, I had some trouble with Zoom app, so I'm joining from browser today.
**BA Björn Antonsson** 02:07 Oh, okay.
**Cijo Thomas (Microsoft)** 02:08 Yeah, but anyway, you can be able to hear… able to hear each other, so that's good.
Yeah, let's see if anyone else joins.
I think we can start, … Yeah, usually only, like, 2 or 3 people join these days, so we don't need to wait a lot.
I don't see anything in the agenda.
I missed the meeting last week, so there was, like, a couple of topics which was… pundit from last week. Maybe it's something we can take today.
But unfortunately, Scott is not here. Yeah, the… the OTLP, back of retry, something which Scott, sent to Pierre, but he's not here today.
The other topic was about… different time zones. I think there is a poll which Scott shared in the maintainer channel earlier today.
I… generally okay with that. I mean, we don't have much people here to come in. I think, like, beyond, it should be okay for you, right? Like, because you are also in the similar time zone.
**BA Björn Antonsson** 04:27 Yeah, I replied to the poll, which stays well for me, so it would be great if we could switch.
**Cijo Thomas (Microsoft)** 04:35 Yeah.
**BA Björn Antonsson** 04:35 So, I just realized that I only pushed, commits to the tracing open telemetry.
PR. I have not commented, so maybe that's why I haven't gotten a response. I'll comment in there as well.
**Cijo Thomas (Microsoft)** 04:50 I fixed all the….
**BA Björn Antonsson** 04:51 All the things that, … We're requested, so we'll see if it's okay now.
**Cijo Thomas (Microsoft)** 04:58 Okay, yeah, yeah, yeah, I'm, like, eagerly waiting for, like, that… that PR to go through, then we can start making few breaking changes.
In our SDK and APA as well.
Yeah, nothing else to be discussed.
**BA Björn Antonsson** 05:14 I actually added a small PR that I have, which allows for… transformation of the resource when you, build a tracer provider?
**Cijo Thomas (Microsoft)** 05:29 Okay, do you want to discuss it right now? Why is it specifically on Tracer? Like, why not on… meter and logs as well.
**BA Björn Antonsson** 05:41 I have no idea, because I don't work with metering logs, so maybe it should be there as well. That's a valid comment. The reason for it is that we want to add more settings that are, like, vendor-specific, but we don't want to, like, trample over the… Default ones that are picked up.
We can't really do that right now in a good way.
**Cijo Thomas (Microsoft)** 06:09 Yeah, I think I need to take a look at, like, what we have currently. I think we allow people to add any number of resource detectors.
And they have a well-defined behavior where you can use it to overwrite.
The existing ones.
Is that what you were, like, looking for, like, when you said, like.
**BA Björn Antonsson** 06:29 The resource, the textures are, like… Well, yeah, maybe working, but… As far as I remember, you only have a builder, and you can't really read from it, so you don't know if you're overwriting someone?
**Cijo Thomas (Microsoft)** 06:47 Yeah, you wouldn't know if you're overwriting. Yeah, it'll… I think there is.
**BA Björn Antonsson** 06:50 Which is, which is… Which is really bad. I mean, if… do you want to have, sort of, like, a hierarchy of things where you do things based on what others have done, then… then it… I mean, it just….
**Cijo Thomas (Microsoft)** 07:12 And there is also, like, yeah, yeah. Yeah, I'll take a deeper look. There is another aspect which I want to bring up. There is a huge refactoring or redesigning of resource in the spec. They're calling it entities, which is supposed to solve a lot of shortcomings with resource. I haven't, like, had a chance to, like, review the entity spec in detail, but if you have a moment, like, just see if that would indeed, solve this problem which you are describing.
We haven't implemented it in trust. I think, like, Josh, who is one of the… persons driving the entity, spec work, he said he'll be like, okay.
**BA Björn Antonsson** 07:52 This is Surat.
**Cijo Thomas (Microsoft)** 07:53 Yep, yep, just read. Okay.
Yeah, he said, like, he will add, like, entity support to Rust, like, soon, but, I mean, he's working on so many other things, so I don't know whether this is, I mean, his top priority, or, like, somewhere in the bottom. Yeah. Anyway, I'll check the PR, like, my only quick observation is, is it something which we can solve other ways, but if no other way to solve it, then we can add it, but we'll need to add it.
**BA Björn Antonsson** 08:19 I would love to find some way or understand how the resource, The, the, … No, not the builder, the things that are supposed to discover things, how they should work, because I can't really figure out how.
To hook that in in a nice way for a user with… Yeah, no worries.
**Cijo Thomas (Microsoft)** 08:47 So, like, can you give one great example of your use case, so I can use that as an example to think.
**BA Björn Antonsson** 08:53 I mean, it's just… it's just sort of, like, overloading things. If you have not set this, like, … service tag with the OpenTelemetry, ones, then we will read up environment variables and use them, like Datadog-specific ones. I mean, we don't want to trample all over things, because we want to have, like, an order of who Who has precedence.
And also, we compute other tags based on what has been set, so… Okay. We need to be able to read stuff, and add information, but yeah.
**Cijo Thomas (Microsoft)** 09:36 I see. So the main limitation right now is there is no way to read what was already set. That's one key limit.
**BA Björn Antonsson** 09:42 Yeah, I mean, as far as I remember, but… I'm not sure if there was a nice way to hook in the discovery things….
**Cijo Thomas (Microsoft)** 09:56 When you say discovery, yeah.
**BA Björn Antonsson** 09:59 I mean, you said you call them a resource, whatever, the things that populate the resource. What did you call them? I can't remember. Yeah, resource detectors, yeah, resource detectors. Detectors, yes, yeah.
I think that, that's sort of, like, is, is, … It's just using the default one.
**Cijo Thomas (Microsoft)** 10:18 Yeah, maybe, like, this is probably a limitation in the tracing. We probably never, like.
took care of resource in the Spacer Provider Builder, but maybe it's already.
**BA Björn Antonsson** 10:28 Okay, so maybe it's fixed in the other ones. I should.
**Cijo Thomas (Microsoft)** 10:31 Yeah, I'm not saying we have fixed it, but at least, like, logs and metrics have been reviewed quite heavily. I hear what you're saying. Yeah, I should probably take a look at how they work.
**BA Björn Antonsson** 10:42 As well then. Yep.
**Cijo Thomas (Microsoft)** 10:43 Yeah, but if it's not there, then yeah, we can definitely add things.
**BA Björn Antonsson** 10:48 Yeah?
**Cijo Thomas (Microsoft)** 10:49 … Okay, yeah, and we'll use the poll to find a new meeting slot. I think, like, Utkarsh… oh, Lilith, you're also here. Hey, just, like, while both of you are here, Lilith and Utkarsh, any, thoughts on the 8 AM Pacific time meeting, which, Scott has posted in the Slack, a while ago?
You know, it's quite early, but yeah.
**Utkarsh Umesan Pillai** 11:14 Also, what day would it be? Just, like….
**Cijo Thomas (Microsoft)** 11:17 Yeah.
**Utkarsh Umesan Pillai** 11:17 Tuesdays.
**Cijo Thomas (Microsoft)** 11:18 It's, yeah, it's like, we can pick, like, any day, but Tuesday cannot be put, like, today, because Tuesday, 8 o'clock, is the spec meeting. We don't want to be, like, interfering with that one, I think. I'm generally okay with that time slot, except,
**BA Björn Antonsson** 11:34 So the, the, the Europe folks have said, … All three Europe people have said Monday or Wednesday.
**Cijo Thomas (Microsoft)** 11:44 Okay.
Oh, yeah.
Okay.
works for me. I think, like, Wednesday may be more, easier for most people, because waking up early in Monday is generally harder.
**BA Björn Antonsson** 11:55 Gosh, it's Monday, yeah.
**Cijo Thomas (Microsoft)** 11:59 I have to check whether we are going to conflict with any other, like, SIG meetings, because most of the people, like, they attend, like, multiple SIGs, like Arrow, Collector, C++, I mean, we don't attend .NET these days, but at least, yeah, I'll see, like, if Wednesday 8 a.m. Pacific time can be, the future, Kate. Hey, Lilith and Utkarsh, any, comments on that one?
**Utkarsh Umesan Pillai** 12:23 So, yeah, I just wanted to know, like, would this be, like, an alternating thing, or…?
Are we saying, like, every week we only have it at 8am?
**Cijo Thomas (Microsoft)** 12:33 That's a good question, yeah, we didn't… that is definitely an option, like, we'll keep the same time, one week and the other time, but again, it has to be changed from Tuesday if you want to, like, alternate.
**Utkarsh Umesan Pillai** 12:45 Yeah, I think… Yeah, I think, like, with Arrow Repo, for example, we do it 4PM Tuesdays, 4pm Pacific time, and then next week it'll be Thursday, 8 AM, so….
**Cijo Thomas (Microsoft)** 12:58 Okay, yeah, so then maybe we can experiment with that one, like, we'll keep this one, like, Tuesday at 9am Pacific, and then the next other week, it'll be Wednesday, 8am.
**Utkarsh Umesan Pillai** 13:09 Yeah.
**Cijo Thomas (Microsoft)** 13:10 Yeah, at least that will give, like, more opportunity for people, to join, yeah. I think most sticks have such rotation thing, it's just that, like, Russ didn't have, like, strong push to make that happen, yeah.
But now that we have a lot of people from different time zones, yeah, we should make it happen, yeah. So I'll post, to… as a reply, what we discussed, so maybe I can write it into the meeting notes itself, like, so it'll be… Tuesdays, 9am PT, and… And this is… 8 AM.
18, yeah.
And I'll post it in the Slack chat in reply to Scott, so make sure, like, if anyone has other thoughts, we'll be able to consider that as well.
All right, we don't have anything else in the agenda. It's generally, like, quite light on agendas these days, so I'm not surprised.
Anything else we want to discuss? Otherwise, we can give back time to everyone.
Okay, alright. Thanks, everyone. See you next week.
Bye-bye.
