SIG: Sampling SIG
Date: 2025-11-20
Duration: 40 minutes
============================================================

## Zoom Recording Transcript

**Joshua MacDonald** 00:43 Hi, Peter.
**Peter Findeisen** 00:47 Hi, good morning.
**Joshua MacDonald** 00:49 learning.
I was all prepared to have nothing to talk about, and then this, found this, this, new thing.
So here we are.
Oops.
Alright, Yonghan joined us. Peter…
**Yuanyuan Zhao** 01:07 Yeah, I was absent for a while due to some personal reasons. Now I'm back!
**Joshua MacDonald** 01:12 Great, welcome back.
**Yuanyuan Zhao** 01:14 Thank you.
I have actually a bit of, good news to share. The, new, trace ID ratio-based sampling, right, and, the OT keys.
I'm gaining a bit of traction on Datadoc to support that.
**Joshua MacDonald** 01:35 Dang.
**Yuanyuan Zhao** 01:35 Excellent.
**Joshua MacDonald** 01:37 That's the sort of news we want to hear. I would say, update from other things. There's been, a talk of…
When and how to… stabilize…
and ensure complete SK support for sampling. Basically, there's a question of, like, a more existential question that OpenTelemetry is facing right now of, like.
Can we… it was a graduation request first. Could we graduate CNCF? No, it's not ready, it's not done.
Which I sort of agree with,
And so there's been lots of talk of, like, when do we have all the SDKs doing a thing? When can we move it forward like that? And the answer is, I don't know. There's not… there's, like, a lot of… attention is spread in different ways, and not everyone's doing this sampling work.
Yet. So, there's questions, no answers, as to, like, when will all the SDKs get on board with it?
Just… that's just a, like, a note from the field.
**Yuanyuan Zhao** 02:41 You're referring to the latest, trace ID based on the composite, composable,
**Joshua MacDonald** 02:49 That's right.
**Yuanyuan Zhao** 02:49 And… Intentions.
**Joshua MacDonald** 02:51 merged. I'm not aware of any outstanding defects or adjustments that we're making. It's just kind of like, we finished, and then we come to this meeting, and then what's next, guys? And I don't know that…
I don't know when.
or what exactly is next, other than we kind of want the SDKs to move forward, and then when someone asks me, okay, what's really next? And the answer is always declared a config, and then I said, well, maybe that's… that'll happen, and then this just got opened, I just learned about this.
PR here. So, I thought that's probably what we could talk about.
Has anyone else seen this yet?
**Peter Findeisen** 03:28 Yes.
**Joshua MacDonald** 03:29 Yes. I, I saw it.
I know it is written in JSON schema, so I can't read JSON schema very well, but we can read this example.
Interesting. Okay, composite development.
I don't…
**Peter Findeisen** 03:51 Oh, sure.
**Joshua MacDonald** 03:53 Interesting.
**Peter Findeisen** 03:54 Well, so…
**Joshua MacDonald** 03:54 It'd already been some work.
**Peter Findeisen** 03:56 Right, so one, comment before we look at this code,
This is targeting a specific rule-based sampler, not the rule-based sampler that we developed.
There was another one which is… which is not consistent probability-based.
And it does not accept any predicates that would
determine which sampler is to be used. Instead, it has…
Covers the most common case, which is it… it either matches
So, it looks at the attributes, at span attributes, Only.
**Joshua MacDonald** 04:45 And…
**Peter Findeisen** 04:46 They either match a regular expression which is provided, or have to be equal to a certain value, and this specification covers this case only.
So, there was, there was a message from Jack Burke in, in our.
**Joshua MacDonald** 05:08 In the Slack channel, yeah.
**Peter Findeisen** 05:09 channel.
The question is, how do we go from this very specific case to… to…
Expressing arbitrary predicates, and whether we need that, I'm not sure whether…
The… the challenges predicates is, of course, that they… they… They cover a much more…
ground than this specific case, and they can be very verbose if we want to write JSON
specification for these things. We would have to… I believe,
Use… provide logical operations, provide,
way of extracting data from… from the spans. For example, span name.
it is possible to write a predicate that decides whether to sample or not based on the span name. I don't think it's very useful, but there is a possibility.
And to express this in JSON would be really… quite…
Well, not difficult, but not readable.
**Joshua MacDonald** 06:38 I wouldn't say.
I'm… I'm… I'm trying to guess what the next words you were gonna say might be.
At least I… I'm, like, I'm doing autocomplete in my head.
What do you… what do you think, Peter?
**Peter Findeisen** 06:59 So, I did not comment on this pull request. I believe that most of customers would like to have a more readable specification in JSON.
At the cost of being less expressive.
But I could be wrong here.
**Joshua MacDonald** 07:25 Yeah, I… I have… I have thoughts and feelings on this topic. Well, first of all, I'd like to welcome Evan. Hasn't been in a while, but I've seen… we've… we've seen you before. Hi, hi, welcome back. And Carlos joined us as well. Hi, everybody. So this is a rather large meeting for us.
I…
I… the… the autocomplete that was happening in my mind as you were speaking was sort of like, it sounds like you don't like this… like, the idea of a query language is difficult to express in nested structure with YAML.
of course, we've seen it before in OpenTelemetry. The OTTL is sort of an obvious candidate for, like, near similarity, and I'm… I'm… one of my feelings is, like, has any… has any comparisons been done with that, maybe?
The other larger topic that I have that comes to me, you know, most of my efforts these days are in the Otil Aero project, and, there has been, sort of.
Prototype or a proof of concept begun in trying to make a…
More of an expressive query language that would be more human-readable.
being as I come from Microsoft these days,
it is modeled on KQL. It's not… it's a joint project with us and F5.
So that's been, like, teased out a little bit. We started looking at how to convert
like, pipeline-oriented query language into query plans and so on, but it's all very, very, like, wishful thinking at this point, so…
I can see there's a will for more expressive query languages. That's my one point.
And then…
And then, the other thing is that, and I mentioned this a couple, maybe, months ago, actually, more like 4 or 5 months ago, I was… we were talking about
The tail sampler, tail… Tail-based sampler… tail sampling processor for the collector.
And it has a structure which looks a lot like this…
you know, ANDs and ORs being combined. This… this example that I saw… where'd I see it? Oh, God, I didn't see it.
this and… the ANDs and ORs of this type of composition, that's also happening in the tail-based sampler.
And I really don't want to see us build two tree-based… tree-oriented YAML-structured tail-based sampler configurations. That sounds terrible. So, like, one obvious candidate is
That this is very close to…
the AL sampling processor's configuration.
The other thing that I… that I mentioned from 4 or 5 months ago is that I was,
Exploring rate limiters for the collector.
As a sort of, like, the idea that th-th-that…
Mature collectors of this nature often have a way to…
configure memory limits or rate limits. And so then you start looking, what's the state of the art? Well.
you can always point back at that tail sampling processor. It has rate limit configurations, tree-oriented structures, predicates, all of the above, and it can configure rate limits, although I'm not convinced it's expressive enough, or powerful enough, or easy to understand for users, but it does meet that kind of…
Set of requirements.
The thing I was saying, I'll get to it now, is that Envoy is my other example. I studied it pretty carefully. How does Envoy let you configure rate limits? Because they have predicates, they have… they have all this ANDs and OR structure there as well, and it's,
It's a different…
it's a different structural model than the tail sampling processor. It's less hierarchical, and it's much more like lists of, vectors of predicates that can be enabled and disabled. There's more of a, like.
N squared appearance. It looks like you've got n configurations and n predicates, and you're just gonna, like, run through all of them. Instead of having a tree, though, it seems to be a different model.
I also sort of hinted that I would make a report on this topic, and I never got around to it, so that's all I have.
What do you think… how do you feel about the direction of the PRR, Peter?
**Peter Findeisen** 12:22 This particular PR, I can add some comments, but I think it's good to go.
We will have to do much more work in order to support To support,
Composable, samplers with predicates, and…
And as Jack mentioned, this is marked as experimental, so we can really change that.
It's not something that… Will stick with us forever.
**Joshua MacDonald** 12:59 And Jack was the one that was actually proposing, kind of, more advanced stuff.
With ANDs and ORs, whereas Honorog started with only rule-based.
**Peter Findeisen** 13:10 Oh, okay, I admit I didn't see this comment. When was it added?
**Joshua MacDonald** 13:14 This is, well, last.
**Peter Findeisen** 13:16 Okay.
**Joshua MacDonald** 13:17 No, I just looked at the code, not at the comments, I didn't see them.
**Peter Findeisen** 13:22 Yeah, wait, wait a minute, wait a minute.
Are we looking at the same…
**Joshua MacDonald** 13:28 This is the.
**Peter Findeisen** 13:29 Oh, this is the issue, not the PR. Okay, okay, okay, yeah, I didn't, I didn't see that, sorry.
**Joshua MacDonald** 13:37 I'm in the wrong GitHub.
alias right now, so I can't even comment. I…
I'm… does anybody else have, like, something to say on this topic?
**Evan Torrie** 13:55 I am… I haven't been here for a long time, but
Yes, I do think that trying to have
One method of doing this across different things that have the same Nope.
Root.
Well, ultimate goal of structure is the best thing to do, rather than having different things at a very high level.
You could always say, it looks like the way people are going is eventually you'll have tools on top of this that generate these, and somebody may just have a…
tell AI, generate the configuration for this, right? And then the actual underlying thing, so long as it can express everything that you want, maybe that doesn't matter in terms so much of usability, as much as people have tools to create that from some other more usable thing, but…
you know, that's… that's a long way off in the future. I know we need to build the…
build the underlying core, I guess is what I would say.
**Joshua MacDonald** 14:51 Yeah, I've seen that sentiment a few times recently. You know, like, we have these YAML structs, and, like, no human wants to write that. It's quite verbose, it's quite… it's quite awful, but we don't intend to write them by… as humans. We convert other representations into them, I think.
Yeah, that's a theme I'm definitely picking up on.
**Evan Torrie** 15:12 Yeah, I mean, I've also seen things where you have even graphical UIs, right, for building these composable pipelines and workflows, and then it generates a structured text reference.
**Joshua MacDonald** 15:24 Yeah.
**Evan Torrie** 15:25 You know, that it was about, so…
**Joshua MacDonald** 15:26 Yeah.
I… I… I'm in a… I'm gonna…
just add a link to my Envoy thing, because it also… it's hard to read this, this syntax, but again, I don't know that users
necessarily write them, especially. How… let's see…
As for… so then, Peter, back to the code that you have seen.
it sounds like you're more or less thumbs up on it, and given that there's… it's still experimental, we understand that, and there's more to do, but this is step one, and it's glad to… I'm good… I'm glad to see people taking steps.
**Peter Findeisen** 16:11 Yes, so before I comment on this, in the PR, I will look at the description in the issue. I think it's very valuable from Jack there, so yeah.
**Joshua MacDonald** 16:27 Cool. I also… I think we shouldn't try to read this right now, here and now, because it's quite long, but.
**Peter Findeisen** 16:33 Oh, yeah.
**Joshua MacDonald** 16:34 I, I'm glad that we all have had a chance to circle around it, and
I already responded in the channel that we would talk about it today, so, I, this fellow, Anurag, is in, a time zone that's hard to meet with for us. I know, I know that. He's in Japan, and, so I'm not sure if we can get him to this meeting at this time slot, but,
he's someone that's been involved in OpenTelemetry for a very long time, so I would… I would, I also have trust in him as a kind of, kind of, like, person that can execute OpenTelemetry. So, I also would support this, especially with your stamp on approval, Peter.
I'm just gonna add to the list. I feel like… I feel like…
I have nothing else on this topic other than I'm excited, like, I felt like I was gonna come to this meeting and say, the next thing, like, all I can think of is declarative config, and then it landed right now. So here we are. Things are on track.
I have to admit, I don't have any more agenda than to have the discussion we just had.
Never afraid to end this meeting early, is what I like to say.
So… Unless we have more, I vote to, call it, and then… There's a holiday now.
**Carlos Alberto Cortez** 18:08 Good to see ya.
**Joshua MacDonald** 18:09 Two weeks from now, we'll be back.
**Carlos Alberto Cortez** 18:12 Sorry, I wanted to talk about something, briefly, because I saw that, yes, I saw that, the first item, I joined late to…
what's the status on that front? Mostly as a summary, I guess, is that the last specification call, we were talking about
having all the six implement, W3C Level 2, which includes the randomness lock.
And start to actually, you know, have some of the things that this group has created as GoStable. And one small piece that seems simple enough, and it's related, is ID generator telling the SDKs whether the generated ID is random or not. I think we can start with that.
Unless people are not here confident about that, or you would rather have
The entire thing goes stable at once.
**Joshua MacDonald** 19:04 Oh, I would, I would support… I think the high level… the PRs were… the spec changes were broken into basically three parts, and I would support following… stabilizing them independently. So, the first one was…
the randomness stuff, the second one was trace ID ratio, and the third one was composable samplers, basically speaking.
So, I would agree, Carlos, the… and there was a discussion about it. I gave a link in the notes to how the specs do cover ID generator case, and I did implement it in Go as a… I think this is going to be a language-specific thing. How do you mark the generator
Or have the generator report.
There's a couple ways you could do it. If the generator returns a trace context instead of a trace ID, then it would be natural. You could have the trace ID generator
Set that bit.
itself, and then it could even vary it. Like, half the time I'm gonna make a compos… a consistent, or a…
a trace ID that supports level 2, and half the time I'm not. That's possible, but I don't think that's desirable. So, in the Go case, I just had a static
check. You know, in Go, you can try to convert a type. So I'm looking at my sampler, I get its ID generator, and I say, are you an instance of consistent random ID generator? If it's yes, then I will set the bit, and if it's no, I will not set the bit. So that was a solution that worked for Go.
And it… there's a…
one sentence in the spec saying, make it so, make it so that the ID generator is able to control that bit.
Of course, my guess is that the ID generator, if it's being used, is
Well, I shouldn't guess that. Amazon X-Ray bits, you know, are the reason why I think people have the ID generator.
for the Amazon X-Ray, trace ID, so that… and that is compatible with Level 2, so it means to be able to say, I'm compatible with Level 2.
**Carlos Alberto Cortez** 21:10 Nice. Yeah, so, that was one part I wanted to talk, mostly. The other thing we don't have to talk about is about the new probability sampler, the one that will replace the
Deprecated, now deprecated, or soon to be deprecated, Trace Radio. Trace,
I forgot the exact name now, sorry.
**Joshua MacDonald** 21:31 Translate.
**Carlos Alberto Cortez** 21:32 Where are you based?
Yes, correct. That one will be deprecating soon, and we have this one
Which is doing the same, but, you know, properly documented. I think that those two items, for me, ID generator changes that you explained, and this one.
could go stable before anything else. I agree.
**Joshua MacDonald** 21:51 Composable samplers wait, and that's fine with me. I don't think anyone's pressuring us, and we just talked about this next topic for a while, as you were here, to hear… to listen on, like…
until… I think until there's a declarative configuration, we wouldn't want to talk about stabilizing the composable samplers.
**Carlos Alberto Cortez** 22:09 Yep, that makes sense. Yeah, that can come later, definitely.
**Joshua MacDonald** 22:19 Okay, and then I say easy. Relatively easy.
And then…
**Carlos Alberto Cortez** 22:24 Yeah.
**Joshua MacDonald** 22:32 The clarity config below is settled.
Cool.
Thanks for the addition, Carlos.
So I totally agree. There's three steps, 2 of them should be not so controversial. The third one, it's just a… it's a big piece of spec. We should let it take some time.
**Carlos Alberto Cortez** 22:53 Yep. Okay, so it's, like, go ahead.
**Yuanyuan Zhao** 22:56 This is probably obvious to ask. The OT keys.
the TH, those keys, they are stable, right?
**Joshua MacDonald** 23:05 Oh, That's a fair point.
I…
I think we're very close to calling that stable, I do, because we waited so long and were so careful and so deliberate about the process of making them.
You know, like.
We had a draft of that a year and a half ago that was totally different, and we changed it, and we reimplemented it.
**Yuanyuan Zhao** 23:34 Yeah, bye.
**Joshua MacDonald** 23:35 we've been through a few cycles on that stuff, so, I… I don't see it changing, and I don't see it…
So I don't see it changing.
**Yuanyuan Zhao** 23:50 What does it take to.
**Joshua MacDonald** 23:52 Yeah, that'.
**Yuanyuan Zhao** 23:53 So that we can base, like, vendors can, right, base their support on that.
**Joshua MacDonald** 24:02 Okay, this… there's… there's… this is… this… I'm gonna make this a new topic, because this is… this is worth calling out.
So this is about the OpenTelemetry trace.
**Yuanyuan Zhao** 24:21 Crispay, yeah.
**Joshua MacDonald** 24:22 OT keys. Yep. Yep.
So, I guess my position is that these are very unlikely to change in any way.
I…
I also… you know, we had prototypes out more than a year ago that do the… support those values in the collector.
So, probabilistic sampler processor, for example, I feel like that was proven.
Over a year ago.
And given those… that evidence, as a vendor, I would feel comfortable supporting these.
So, I think, Yuan, Yuan, that's a good question for vendors. My old company had an implementation of this.
You know, brand new as it was a year ago, but we did.
**Yuanyuan Zhao** 25:10 Yeah, so, it might sound just like a formality, but,
When it comes down to, like, the support, compatibility, those things.
**Joshua MacDonald** 25:23 Yeah.
**Yuanyuan Zhao** 25:24 It is, it is an important humanity.
**Joshua MacDonald** 25:33 I… so I think that's an important point. Vendors are not going to commit, and I… I will…
speaking frankly, I, had to implement two standards of this, and I implemented the early one, the one before we did rejection threshold. Right. And I was using it for my legacy samplers, like, inside of my old company.
we used that technique of giving explicit randomness to, like, encode another hash decision… a hash-based decision, but I did it using the not-rejection threshold technique. So I had two copies of this code, and the old one, sure, I had to maintain it, but the new one was supposed to be the finished copy, and so… Right. So the new one should go…
**Yuanyuan Zhao** 26:13 hand-in-hand with trace ID racial base, right?
**Joshua MacDonald** 26:16 Yeah, I think that's right.
**Yuanyuan Zhao** 26:19 If we clear the bar for that, then we should be able to clear the bar for…
**Joshua MacDonald** 26:31 Right, so after we've implemented randomness.
**Yuanyuan Zhao** 26:33 Yeah, and we grant you
these two things can be separated, but, right, like, the THPs, those things can be made differently by some other samplers.
But… trace ID ratio based, if that's formal and approved. That implies
The keys, because they rely on this.
**Joshua MacDonald** 27:00 Okay, so what about parent-based?
I feel like I have a question that I don't have an answer to. I've always… I've made the mistake of leaving parent-based out of my thinking in the past.
So, it's covered in the composable sampler stuff for sure, but if a user… if we're gonna say, composable sampler's not here yet, or that's experimental, and you just want to keep the basic samplers that we have.
Does a parent-based need to change
For our spec, I have to go review my own documents at this point. I can't think of,
There are some rules about…
Peter, you have a better answer than this. I think there will be a question, I think this is what we should think about, talk about in two weeks, is…
Is there a subset of the stuff that we need to do for parent-based sampler that we would require to be done to call OpenTelemetry trace state keys stable?
**Peter Findeisen** 28:06 I think so, yes, but I would have to have a closer look, yeah. So, the risk which I see, potentially, is that we will leave those keys in the trace state, even though we decide not to sample.
Which will violate our, invariance.
**Joshua MacDonald** 28:26 You know.
**Peter Findeisen** 28:27 That's probably the most likely outcome.
**Joshua MacDonald** 28:31 Okay.
**Yuanyuan Zhao** 28:38 The property, like, there's some inheritance relationship.
I, you're… Like, no matter what sampler produced that result. If those keys represent
like, the rejection threshold proportionally, right? Then… those, like, Those keys,
Convey the same information that can be used.
to, calculate the spam metrics. So that's the property we want. All samplers, whether they inherit.
the something decisions, and as long as they maintain that invariant, then the TH keys will be
usable. We also have, what is that, a reliable adjuster count kind of thingy, but that was in the process that clears out the TH, right? That's kind of like a guarantee for maintaining the invariance,
But… but the point, I think here we are trying… what's striking is that some review probably is needed, and this… this needs to…
goal at the Easter.
hand-in-hand with trace ID ratio-based when they were made.
Small law.
**Joshua MacDonald** 30:14 Yeah. Okay. I've noted that we can't leave behind the parent-based question, or the little corner cases stuff, like about the parent threshold invalid, as I recall we called it.
It sounded like you were also sort of like, maybe we should go back to that document that specifies those keys and say, ultimately, our biggest… the biggest requirement here is that you maintain
unbiased, estimates.
Otherwise, do something else. Don't use these keys if they're not… if they're not… if they're not, accurate. So, we could think about adding… adding that as a blanket statement.
But I think we should be specific about the parent-based case, since it's where those corner cases lie.
**Peter Findeisen** 31:01 Yes.
**Joshua MacDonald** 31:01 Alright.
Cool.
Thank you. I'm glad that we kept talking. Thanks, Carlos, for bringing that up. I think I have an answer now. If someone were to ask me the same question from last week in the SAG, or this week in the SAG, I would have a better answer, and maybe that'll happen two weeks from now as well.
So that we can…
fit this into the schedule. I know that there's going to be a lot of demands on the SDKs to catch up in other areas, so, I can't promise. We'll see.
And I'll know more in two weeks.
Thank you all.
For joining. Thank you. Discussion as usual, as always. I'll see you next time.
**Evan Torrie** 31:44 And Josh, Josh, could I… Have you hang on for a couple minutes.
**Joshua MacDonald** 31:48 Absolutely.
**Evan Torrie** 31:49 ask you something.
Sure.
**Joshua MacDonald** 31:52 I mean, anybody can stay if it's sampling-related or whatever.
**Evan Torrie** 31:56 Well, actually, yeah, this is non-something related. I was going to ask you a little bit about the Arrow, project, because I do have interest in that. Do you recommend I just turn up to the Arrow Special Interest Group and introduce myself, or is there some sort of, preparation I should do before I.
**Joshua MacDonald** 32:13 No, I, it's an open meeting, I mean,
it's an open meeting, it is… tends to be full of people from Microsoft and F5, because we're… we're collaborating really closely, but it's not always just those groups. There's… there's definitely outside interest. There's an academic fellow that keeps joining us to, like, working on a master's thesis, and there's,
interest from a couple of smaller companies, like Polar Signals and, Datadog has showed up, so Datadog's signaling interest to me was a big deal. I know we're being recorded, but this is all public information.
So yeah, I would… I would advise to show up. There seems to be momentum growing.
**Evan Torrie** 32:57 Yeah. The one thing I was interested in that is that when I read the original announcement of this special interest group, it was talking about
exploring the integration of Rust-generated components into a Go ecosystem, is that correct? Am I imagining that?
**Joshua MacDonald** 33:14 That's, like, the million dollar question for me. I did, I can dig it up for you, slack you later. I did, multi-month-long investigation, where it was kind of my primary kind of focus for a while.
And I… given where we were at the time, it was sort of a negative result. This is really hard. Like, Go and Rust, like, really don't want to fit together. And… and yet, it's more of an existential problem for the… for the Rust effort to say we can't. So,
we… we talked about it, I researched it, I made a proposal that was
quite a lot, but I think it was the most feasible one I could find.
to bring the two together, in a way that I thought people would like.
I'll show it to you. I closed it after a while, because it was just sort of like… the collector group is saddled with a lot, and I'm sometimes critical of the progress and the rate and the choices they make, but it was not the right… it's not the right time last summer to do that, so I stopped.
**Evan Torrie** 34:26 Okay.
**Joshua MacDonald** 34:27 However, the… the way we framed the project, it was,
Like, 6 months of charter for us to do this exploration, and we're basically at the end of the 6 months right now.
Results are very positive. We're getting good performance improvement, like, multiple… like, factor of 5 better.
**Evan Torrie** 34:49 I'm like…
**Joshua MacDonald** 34:50 way better, because no garbage collection, because Arrow, because SIMD, all this stuff. But… but those are very limited, isolated tests, so it's like, that's… we're choosing the best case for ourselves.
**Evan Torrie** 35:02 Right, yeah, right. Promise not to exceed this benchmark result, right? That's a…
**Joshua MacDonald** 35:06 Yeah, so take it with a grain of salt.
**Evan Torrie** 35:10 Yeah.
**Joshua MacDonald** 35:10 But so… but the point is that, like, every… every… everything we thought we would get done has succeeded, and… and it's like, there's nothing negative right now, so super positive about it. Therefore.
Except for that extensibility, the interoperability question that I kind of failed at, or, you know, decided to not pursue last August.
**Evan Torrie** 35:29 Or July.
**Joshua MacDonald** 35:31 So, but that is almost the only question I know I have to answer in the next period. And, what was said,
So, two weeks from now will be another sampling SIG, 1 week from now is the U.S. holiday.
**Evan Torrie** 35:48 Three weeks from now.
**Joshua MacDonald** 35:50 In this room, in this time slot.
Because Arrow and SamplingSig share a Thursday morning, and I alternate.
So, a week from now, it'll be a holiday, three weeks from now, this room will have the people, and we're going to talk about this very topic. I will definitely raise interoperability, because to me, that's the… the question is, what's Phase 3? Do we have permission to do phase three? And if we have permission to phase… do phase three.
The obvious question is, when do we integrate with the collector? We still aren't calling ourselves a Rust collector. It's still just a Rust data flow engine that does OpenTelemetry pipelines.
And,
you know, we've intentionally stayed away from being compatible for a lot of reasons, but it's time to start having that conversation. So I need to answer this.
We need a new charter for Phase 3,
It needs to address interoperability. That's what I know.
**Evan Torrie** 36:44 Okay.
It's interesting stuff. So, I… I have traditionally been a C++ guy, and
And now trying to learn Rust, so I…
I can help you necessarily with the rest of it, but I'm interested, maybe this can be a task that helps me learn it better.
I would say.
**Joshua MacDonald** 37:02 Thank you. I mean, I'm excited to hear all that, and I will say that many of us are pretty new at Rust. I still feel new at Rust. I've been programming at Rust for about 18 months.
So, it's got a learning curve to it.
**Evan Torrie** 37:17 And I feel.
**Joshua MacDonald** 37:18 I'm very confident in Rust now, but I know the dark areas where I'm not fully getting it. Like, async is hard, and I'm not… there are devils in there.
**Evan Torrie** 37:29 So.
**Joshua MacDonald** 37:30 Are there more devils than there were in C++ first, though? There are not more devils, and I, I always liked, functional programming. Like, scheme was my jam back in the college days, and I do enjoy the ability to chain together iterators and do functional stuff.
It feels more… I'm like I'm home.
**Evan Torrie** 37:52 More home in there, yeah.
**Joshua MacDonald** 37:53 Yeah.
**Evan Torrie** 37:54 Compared with Go, where Go is, like, has a little bit of functional programming style, but it doesn't compose very well, and it reads kind of awkward, and…
**Joshua MacDonald** 38:01 Rust is just, like, super concise, like, there's always a way to turn an if statement into a map, and it's like… and it takes a while, like…
these standard types like option, result, iterator, you gotta know them, like, inside of you. You have to know.
**Evan Torrie** 38:18 Yeah.
**Joshua MacDonald** 38:18 I still have to go to the reference page to, like, remember, how do I turn an option into a result with this type of function when I want the sum case to be, like, all that stuff?
**Evan Torrie** 38:28 Yeah.
**Joshua MacDonald** 38:28 But I'm feeling more and more confident every day, so…
**Evan Torrie** 38:31 Yeah. I guess…
**Joshua MacDonald** 38:33 people.
**Evan Torrie** 38:33 Yeah, I think the only way for me to get confident… well, to even start, right? Well, you can't get confident until you start, so you need to start.
**Joshua MacDonald** 38:42 So, cool, yeah, there will be some low-hanging, like, if people want to get started, I'm sure there's lots of tasks. The issues board will be full and stuff, so we'll be welcoming when we see you.
**Evan Torrie** 38:53 And, I haven't talked to you since you moved to Microsoft, so, I guess congratulations on that. I know you like to stay.
**Joshua MacDonald** 38:59 Yeah.
**Evan Torrie** 39:00 ServiceNow thing is, unfortunately, unfortunately gone down, but, I still see occasionally a lightstep.zoom.us URL, which I think was originally, originally LightSteps. Maybe I'm just in some old, old invites.
**Joshua MacDonald** 39:17 It'll be them. I know that they kept the domain name, they kept the GitHub.
**Evan Torrie** 39:21 Yeah, they're a good head.
**Joshua MacDonald** 39:22 Some of the tech is still alive, but, yeah, it's basically dead. Yeah, I joined Microsoft almost exactly a year ago.
It's… Really great for me. Really great.
**Evan Torrie** 39:39 That's good. Okay, well, I'll… I'll try and show up then to the… I guess, the next sampling meeting, and then to the next one, which will be the arrow one. Sounds good. All right. Thanks, Josh. See you later. Bye-bye. Good to see you. Cheers. Bye.
