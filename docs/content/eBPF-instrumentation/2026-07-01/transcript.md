SIG: eBPF instrumentation
Date: 2026-07-01
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Giuseppe Ognibene | Coralogix** 00:38 How are you?
**Florian Lehner** 00:51 Tyler, I think your microphone is not working.
**Tyler** 00:56 How about now?
**Mattia Meleleo** 00:57 Hello.
**Tyler** 01:00 Yeah, gotta turn it on. Step one.
How's the, the European weather over there? Is it hot for y'all?
**Mattia Meleleo** 01:12 Way too hot.
**Tyler** 01:16 Yeah, one of my colleagues, a lot of my colleagues are in Poland, and they're, like, dealing with, I don't know, it's like 38, 40 degrees Celsius, and, like, I mean, they, yeah, they just don't have AC, like, they've never seen that kind of stuff. Yeah, there's one of them.
**Pellared** 01:31 What are you talking… what are we talking about?
**Tyler** 01:33 Your heat wave that you're dealing with up in Poland, and how you don't have any AC, yeah.
**Pellared** 01:38 What's AC? I don't understand.
You mean the current? You know, you mean the AC current?
Yeah, right.
**Tyler** 01:48 Yeah.
**Pellared** 01:49 Yeah.
**Tyler** 01:50 Mattia, how about you? You're down in southern Italy, right?
**Mattia Meleleo** 01:54 Yeah, I'm in South Italy, but nowadays, like, I think North Italy and Northern Europe is hotter than here. Also.
**Tyler** 02:05 We're always…
**Mattia Meleleo** 02:05 had AC, because historically it was hotter here, so we don't have any issue with that.
**Tyler** 02:12 Yeah, you were already prepared, yeah.
**Mattia Meleleo** 02:14 Yeah.
**Tyler** 02:16 I gotcha.
Yeah, I think Robert was saying that it was hotter, in Poland than it was in Africa, just the other day.
**Pellared** 02:26 not hotter, almost that hot. Like, I heard that it's only 5 degrees Celsius temperature lower than on Sahara, or something like that.
**Mattia Meleleo** 02:39 That's crazy.
**Tyler** 02:41 Yeah, that's pretty nuts.
Well, cool. We can probably get started here in just a second. If you haven't yet, please go ahead and add your name to the attendees list. If you have agenda items you wanted to talk about, go ahead and, add them there as well, and yeah, we'll get started here in just a second.
Cool. Alright.
Let's jump in. So, I've got a lot, on the agenda. I went through… I think, just to maybe back it up, we made the V010 release, yesterday, which was pretty exciting. It had quite a lot in it, so pretty, pretty happy about that. A lot of fixes, and definitely some features in there as well. So, yeah, congratulations to all people on the call that made it happen. It's great work. I'm really happy that we got it out.
It's definitely a lot of work, so… yeah. That being said, I wanted to take this… Time in this meeting to kind of get our next planning goals, in place.
So, we are definitely more than halfway through the year at this point, and so I wanted to check in on our goals, given that, like, these are the things that we've said that we were trying to do.
And we've told the public, And, Yeah, I've definitely gotten a lot of questions from other community members about this project board, from other… colleagues and, other… even customers, so people definitely are looking at this, so I wanted to double check that we're… On target here, in that, like, we're making progress.
I don't… If I'm being honest, I think we're, at risk at this point. There's very low chance, based on our current progress, that I think we're gonna actually achieve all of these goals.
So I think it may be worth… They're planning to get these things done at this point.
Or starting to communicate that these things are gonna slip into, Not getting done, or getting moved into next year, or whatever.
Whatever it is, but I think we should probably start to try to communicate these things, outward. So, yeah, maybe we could just go through top 5 epics right now, and then maybe chop down into the bottom list.
So the Epic, stable OBV1 release, I think this is… something I can report that I'm very actively working on. A lot of the rest of the items I have on the agenda are related to this, in trying to get this done, and I think that this is, Yeah, I saw this the other day. We did have target dates, believe it or not. I think this is achievable. I had a target date originally of, like, June, which was too ambitious. I've reset that to be KubeCon at this point.
I think that that's achievable.
Based on what I've, got planning going, but… Yeah, so, this is gonna be, I think.
doable. I think, like, there's risk if we don't get the config v2 out in the next release, or then we're probably at risk of this not actually getting completed, Before KubeCon, maybe before the end of the year, even. So, yeah, just kind of a status update on that one. Yeah, actually, maybe I could… Capture some of this stuff.
Yeah, okay.
So next up, is the, Additional protocol support one. This is something that Nimrod and Mark have been working on. I mean, I think there's a lot of people working on this one.
I don't know if this is up to date.
I don't know if Nimrod's on the call, actually. Let me see if I can… oh, okay, cool.
**nimrodavni** 07:02 I added… added another thing here that is not on the… It wasn't on the… on the initial list, which is error spike, and I opened an FTR card.
Let's go to the top, I think the Mongo stuff… we had plans of… of, working on, but it just kind of got postponed. I'm hoping we can get it done by… KubeCon. The rest of the stuff… Yeah, I'm… to be honest, like, all the cloud stuff, I'm not exactly sure what do we need to do there regarding instrumentation. Is it cloud services? Like, because we have stuff like S3 and SQS, so I'm not sure exactly what does that mean. Is it, like, resource enrichment?
And Redis PubSub, we haven't gotten to it. I don't think there was a lot of, Requirement, but we can also work on it as well.
**Tyler** 08:07 Yeah, I mean…
**nimrodavni** 08:08 SanRPC, I think, is done by Mike?
**Tyler** 08:11 Yeah, that shipped, this past release, yeah.
Kinda weird where you have, like, these… Acceptance criterias and sub-issues. I don't know which one to look at.
**nimrodavni** 08:23 I think this is the user's more, probably, up-to-date.
**Tyler** 08:27 Yeah, I think you're probably right on that one.
Okay, yeah, I mean, I think the original ask for the services, the cloud services, Yeah, it was, like, API access and integration with those, so I think that, like, things that you're talking about, like, with AWS is pretty shored up. I think Azure and, like, Google Cloud stuff is definitely… On the, yeah, probably… Probably not happening.
So, I mean, I guess that's kind of the question, is like… If things are gonna slip, and we don't think that this could be achieved in this year.
how do we want to communicate that, I think, to the people that are actually watching?
So, if that's the case, like, does it make sense to… add, like, a post-V1, protocol support issue, and then move… move things that we don't plan on getting done here, there, and, like, just communicate that in a comment.
**nimrodavni** 09:30 Yeah, I think, like, maybe… Yeah, and then having maybe, like, another label, or, like, Goal 2027… Or adding… Yeah, kind of saying that, like, we don't commit to these things to release.
**Tyler** 09:49 Yeah, I mean, so… so the thing is, is, like, we've already committed to trying to get these out, and, like, we've told people, and there's, like, a blog post on it, right? So that means we're just not gonna change that. So what I would say is probably don't add a goal 2027 to… the issues, just because that would just mean that we're committing again to trying to do this, and I think that we probably want to do some planning, come December, or maybe January, like, on, like, what our next goals are.
But I do think, like, if we wanted to say, like, we're re-scoping this at this point, and, like, dropping, I think that's important, because, like, it's easy for us to say, like, hey, like, let's do that, but if we have, like, a really strong community that's just sitting there waiting, and they've been waiting on the manga stuff, I don't think that's the case, I'm just saying, like, then we probably want to make sure that that's communicated so they know, like, heads up, like, this isn't… this is not happening this year, actually.
So, yeah, I think that makes sense to me.
Is that something that you can do in updating the issue? Creating the other issues and stuff, and just communicating that?
**nimrodavni** 10:50 how do you want me to go… like, you want me to create, like, another epic and, like, move these sub-issues, or, like, recreate those issues? Like, what's the…
**Tyler** 11:00 Yeah, definitely, definitely move, is probably what I would do.
I… to be honest, I think, like, putting him in another parent issue seems fine.
The thing that needs to happen, though, like, ultimately is, like, if these are not gonna get done, and we're gonna drop them from trying to complete this, and we're gonna try to complete this issue, then they need to get removed from this issue in some way, and that removal needs… that removal or that move needs to get communicated, right? That's the thing that I think we need to do.
**nimrodavni** 11:30 So, like, comment on this issue, or, like, every parent, or every, like, child issue, saying, like, we're not gonna complete.
**Tyler** 11:38 Yeah, I mean, I don't know if these are tagged. Yeah, so they also have the tag and the label, so yeah, so maybe since it's, like, tagged like this, I would remove the tag and maybe comment that this is not a goal anymore, something simple as that, right?
But yeah, it's more just, like… it's more about planning and, like, communication than anything. I can be very prescriptive about what I would do, but I don't want to, like… like, just as long as, like, the end of the day, like, what we're not actually gonna get done and what we don't plan to get done anymore.
is… not actually reflected here, and then excommunicated. Those are the only two things that I think we really need to do.
**nimrodavni** 12:12 Okay.
**Tyler** 12:12 However, yeah.
**nimrodavni** 12:13 I'll plan to do one, I'll, like, discuss with you, if that's, like, a correct wording or something, and then I'll do the rest.
**Tyler** 12:21 Okay, yeah, yeah, I'm happy to help, yeah, sounds good.
Okay, Cool. And then, next up, the support for the .NET.
I don't know if, Raphael's on.
**Mario Macias** 12:44 No, most of the Grafana team, the people in Canada is holiday today, and some others, I'm only from Grafana. Yeah, to be honest, I don't know what's the status of this task.
**Tyler** 12:58 Okay.
I can, hmm… So, Raphael's off today, or is he off for the rest of the week?
**Mario Macias** 13:09 I think he's already off today.
**Tyler** 13:11 Oh, okay, alright.
I can… I can maybe just ping him… after the meeting then, or tomorrow, or something like that, and find out. Okay. Because I don't think that we've had any movement on this, and I do want to get his estimate if this is actually going to get done, before the end of the year, so we can… update that. But okay, I will… I'll take the action item on, following up on that one.
Okay.
Next up, OTL API, SDK, and integration. This is kind of a… big one. I think this is something that Nicola, yeah, had been assigned. He's also not here. This has definitely got a lot of moving, pieces in it.
I do know that we are working on… like a pseudo… not a pseudo, a recreation of the hotel auto, integration, so that's, like, with spans.
There's, like, a lot of things here, though.
There's that partial, hotel SDK traces stuff, and partial OTL SDK, like, wrapping stuff. This has a lot to do with Nimrod, the thing that you had last, meeting, talking about work in the specification, if I'm not mistaken.
**nimrodavni** 14:33 Yeah.
**Tyler** 14:34 I mean…
**nimrodavni** 14:35 I think there's some comments there that I didn't refer to, so I'll need to do that.
**Tyler** 14:42 just comment here, you mean? That we need to have…
**nimrodavni** 14:46 Check on the, on the, proposal for this.
**Tyler** 14:48 Oh, oh. Oh, okay, I see what you're saying. Yeah, okay.
Yeah, I think that we probably need to get the acceptance criteria really defined on this one.
**nimrodavni** 15:00 Yeah, I think this is, like, it's, like, a lot of different axis that we're moving in, and, like.
Either we're improving our integration with the SDK, or with, Yeah, like, I don't know, support manual spans in other languages, and a lot of stuff. I guess we need to define… I think we already improved it a bit, but I just don't know what's… what do we mean when we, like, how do we know when we're done?
**Tyler** 15:29 Yeah, that's a… that's kind of an important part. Yeah, okay. So… I think… because I think there's been a lot of great work here, I think… yeah, things like DNS support when… Or, like, wrapping things, and not just dropping and completely stepping out of things would be great, so… I think there's already, like, work here, but it just needs to kind of get shored up.
This, I think, was kind of a catch-all, so, I can also work with Nicola on getting this well-defined.
I don't know… if this is in the cards of getting done this year, so I'll also check in and see if, like, this is something that may slip. So yeah.
Okay, and then last up, improve the integration test quality. Again, Steven's not here.
Let's see, I know Robert's here.
I don't know… this does have some pretty good acceptance criteria.
So, yeah, maybe, Robert, I don't know, like, how active you've been in this, but, like, what are your thoughts on getting this done before the end of the year?
**Pellared** 16:35 So, Stefan, is also, I think, is more, active recently.
Yeah, also, you know, the excipients criteria here are pretty, you know.
Not concrete, like, they are, like, you know.
make something better, faster, etc, without good numbers. I'll need to probably… I will probably need to, you know, double-check what is the status right now, because, to be honest, I'm not even familiar what is the current status of integration tests, what are the problems, etc. If any of these things have been solved.
I'm not sure, any thoughts from your guys that you've been, you know, you're maintaining it, basically?
**Mario Macias** 17:18 I… I think many of the current, points are already covered.
For example, this identify existing code duplication. I think we have done many work on this, for example, regarding… the integration tests in having to deploy always similar Docker Compose files.
Also, determine reasonable approaches… For improvement and plan for implementation? No, I don't know this.
this agri process to address flaggy tests, I think it is… it is done.
**Pellared** 18:06 Yeah, this is improvable, yeah.
**Mario Macias** 18:08 Yeah…
**Pellared** 18:11 What about the error messages and things like that? When these integration tests are failing, are they telling you anything?
**Tyler** 18:19 I mean, still… Captured… captured in, like, an…
**Mario Macias** 18:23 external.
**Tyler** 18:23 Log, so it's not in the… There's a lot of opaque error messages still. I'm like…
**Pellared** 18:29 I see.
**Tyler** 18:30 It's not really I think the main pain point… the main pain point is that they still are flaky. Like, things still… fail indeterminately.
Steven's done a lot of great work, because, like, he's done, like, a lot of auto-restarts, so things will just, like, automatically get run.
Two times, because, yeah, but then even, like, by the third time, like, I've had to run tests, like, four… like, yesterday during the release, like, it took… two different tests, like, one four times and one five times to run to get done. You know.
Each one taking 20 to 30 minutes.
But that's also, like, looking at the commit history, not… it definitely isn't a nearest neighbor problem, because, like, that was not happening through the night, when… when the US was not up, right? So… Yeah, it, like, I don't think it has anything to do with, like, our… concrete testing correctness, it's more about, like, its, susceptibility to lag and timing, is likely where I would guess. But, like.
Anyways, I think that, like… To not derail the agenda item too, too much, like.
this, I think, needs, I think, more explicit and, objective acceptance criteria, because right now, like, these aren't, like, I think, concrete enough goals, because you could say things are accomplished, or you could say things are not accomplished.
**Pellared** 19:54 Yep.
**Tyler** 19:54 So… Robert, is this something that maybe you could just take a look at, later today, and then if you have… Questions of whether or not this could get done, within the end of the year.
**Pellared** 20:05 Personally, Personally, I think I'll… idea, I'll just sync with Stephen.
What are his thoughts on this, and try to restructure.
And my opinion, but I can also, you know, my proposal is just, you know, to have this epic, maybe restructure it, and how much we do, it will be great, and we'll just create a new epic and, you know, iterate again, for example, next year.
So that…
**Tyler** 20:36 Yeah, I'd like to have, like, goals that are achievable, so we can measure success, and we can say this is done.
Rather than just, like, a generic, like, we're actively working on it, and this is just representative of work. So, like, if we can… if we can restructure this into saying that we're going to achieve X, Y, and Z, and then… next year, if we're gonna achieve something else, I think that that's great, like, literally, if we.
**Pellared** 21:01 So, like, there's.
**Tyler** 21:01 Concrete tests, yeah.
I mean, I definitely know that you had really great concrete tests of, like, you were gonna refactor how things actually We're structured here, and that doesn't… it's not included here anymore, which is fine, like, yeah, that's fine, but it's just, like, I'd rather it get replaced with something that is, like, actually going to tell us what we want, right?
**Pellared** 21:23 Okay.
**Tyler** 21:24 I'm happy to work with you as well, if you wanted me to help on this one, so yeah, let me, let me know.
Okay.
**Pellared** 21:31 I was thinking, like, and then Lynx team as well.
**Tyler** 21:34 Yeah.
Cool. No.
Cool. Alright, then, next up, proposal adopts OpenTelemetry semantic conventions for network flow attributes. This, I think, is actually quite a big… task, I think.
**Mario Macias** 22:21 Yes.
**Tyler** 22:22 Yeah.
**Mario Macias** 22:24 I… I can provide some updates.
Last week, I resubmit the proposal. It got automatically rejected because some of the fields didn't have assigned, an existing Sikh group.
So I… I asked in the semantic convention channels, and they told me that once the new network group.
is created, they can assign those items to that group, so we can keep working on the… on the semantic conventions without getting automatically closed.
**Tyler** 23:05 Okay.
Yeah, alright. What is your thought on this getting, resolved by the end of the year?
**Mario Macias** 23:15 I think it's possible. I think it's possible, but it's… it's still blocked by the availability of the… of the semantic convention group.
And also the network seat, and also the rest of the semantic convention people.
giving feedback, or collaborating, approving. So, I think there is a high chance we don't… we don't get it by the… by this year, but it's… it's not impossible. I… I… I see a lot of external uncertainty.
**Tyler** 23:55 Yeah, okay, I think you're right, yeah.
**Mario Macias** 24:09 The… the actual semantic convention proposal is already written, and I mean, it's… it's there. We just need to start discussing, modifying to… To accommodate all the… all the feedback and… and get it approved.
**Tyler** 24:28 Yeah, right. I mean, I… yeah, I think… Share your pain on that one. I think the collector stuff suffers from that as well, so… Yeah, okay, cool.
All right, good. So from our end, though, I think we're doing… we're doing pretty good on that. I think that align the OB networking attributes as well is kind of in the same boat, probably should have wrapped these in. Yeah. Yeah.
The rest Tokyo context propagation, this is… Nimrod, you've got a sign here, I don't know if this is…
**nimrodavni** 24:55 Yeah, actually, I think Pino's in the works on this. I don't know the… I think it's kind of close, but Pino might know better.
**Giuseppe Ognibene | Coralogix** 25:04 I'm working on that.
**Tyler** 25:06 Oh, okay, cool.
Yeah, that's great.
**nimrodavni** 25:10 Probably be done in the… in the next, for sure, in the next month.
**Giuseppe Ognibene | Coralogix** 25:14 Yeah, yeah.
**Tyler** 25:14 Okay.
Cool. Before I lose that, let's, I'm just gonna put it here.
How'd I close that? Okay, anyways, Switch to using tracing, programs instead of K-probes, This is an optimization work here.
**Mario Macias** 25:38 Yes, from my side, we have worked in few experiments.
But, we haven't yet replaced any… any tracing program, any K-Pro by tracing programs. If the objective of this task is having a… I guess it's not replacing, because tracing programs are available… in… in later, if I'm not wrong, in later kernel version, but if… if the issue is to provide an alternative tracing implementation for all the… For all the K probes we already have.
probably I would say that it's unrealistic to have a duplicate version of all the programs by traces.
by the end of the year. Maybe we can have a few… Maybe the most critical ones.
**Tyler** 26:37 Okay.
**Mattia Meleleo** 26:41 I haven't had much time to look into this, but I can, give it a shot, not, Maybe not this month.
**Tyler** 26:56 Well, sure.
I think saying that we're not gonna actually get this done is also viable, like, I do want to point out that, like, I did want, like, the next milestone, like, we do have a very limited amount of developer capacity, so, like, Mattia, I think that's my admiral, but just, like.
If you're also working on, like, 20 other things, like… Let's… let's… I think that we want to just make sure that we are… Yeah. I don't know if this is gonna get, like Mario says, like, to switch all of the programs?
sounds, like, extremely ambitious, in our timeline, but I think maybe, to your point, maybe just working on it in piecemeal might be helpful.
**Florian Lehner** 27:39 maybe just a trick, in the profiler side, we have the same… I wouldn't… would not say an issue, but, we… have all profile or a trace programs also as K-Probe and mu probes, and the trick is just to compile it differently. So, depending on the helpers you are using, you can just take the very same program and compile it in three different ways.
**Mario Macias** 28:02 Oh.
Okay.
**Florian Lehner** 28:08 That's why… that's the trick, how we keep the eBPF prop quite small.
**Tyler** 28:13 Hmm.
**Florian Lehner** 28:14 The trick is really just to have the… Tail maps… for the specific target. So, in every program, you have these tail program, tail maps, and these nits need to be specific for the… For the, for the program type. And that's… that's… solving this is only the hard part. The rest is just compile it in a different way.
**Tyler** 28:39 Could you, maybe add a comment here, Florian, as to, like, the details, so that maybe we can take a.
**Florian Lehner** 28:46 I can… I can follow up.
**Tyler** 28:49 Awesome. Yeah, that can maybe help speed this along, that'd be great.
Look at that cross-collaboration.
It's working. Some managers somewhere are super happy. Okay, next.
Improved service metadata, when not running in Kubernetes. This is, I think, something that actually has had a fair amount of work on it.
**Mario Macias** 29:09 Yeah, I, I think feature-wise.
at least what I have in mind is already provided, which is metadata for hosts, VM, Docker container metadata, and also cloud metadata for the three major providers, EKS, GKE and Azure, so this is already available. What's missing?
Is this, inner task.
Of, refactoring the metadata sources and decoration, which doesn't add any feature, but We'll help maintaining and extending the… the… the metadata, if we want to add more metadata sources in the future. But I don't know, or I would suggest to move this sub-issue outside of this Of this issue, as it doesn't… it's an optimization, it will help the code maintainability, but it's not really adding any extra feature that the user will appreciate.
So I will move this to another epic, or another… or as an issue itself, and close this, improvement service metadata.
**Tyler** 30:28 Yeah, I think… I agree with that, that sounds, sounds great.
Any opposition?
Cool.
Okay.
Awesome.
Similar here, provide runtime metrics with Obi. I think that we have started on this.
**Mario Macias** 30:48 Yes, Mark has been pushing hard for this.
**Tyler** 30:54 Yeah, we definitely need, I think, to get a little bit more clarity around the scope. I know Java is active. Go, I think, was also talked about, but…
**Mario Macias** 31:01 Yes.
**Tyler** 31:02 Yeah, if it's just those two, maybe this is achievable, but if it's more than that, yeah.
**Mario Macias** 31:09 You're right.
**Tyler** 31:16 Okay.
Improved trace log correlation.
I don't… For some correlation rehearsals.
**nimrodavni** 31:28 Yeah, I think… I think most of… I think the first two ones are… done.
I think… it's not, like, sub-issues, but they're done. The last one, we still didn't… don't have a clear direction.
for it… As a result…
**Mattia Meleleo** 31:48 We are also missing the plain text logs here.
**nimrodavni** 31:53 Yeah, and we… I think there's some plans of… having, like, supporting plain text. I don't know… I don't know if we agreed on, like, just doing, like, if we still need, like, structured text logs, or do we just append trace ID span ID at the end?
Or having different… it's… yeah, so I think…
**Mattia Meleleo** 32:14 If I'm not wrong, we agreed on something, maybe it was in the… written in the issue?
I'm not sure.
**nimrodavni** 32:22 I think there's another issue on, TraceLog on, like, text.
Trace correlation, trace law correlations, we can add it.
I'm just wondering if we will get, like, if we will get to it this, yeah.
I think it's…
**Tyler** 32:40 it's something… I mean, I… I think that that's…
**nimrodavni** 32:43 Yeah.
**Tyler** 32:43 So I can search for plain text logs, yeah, okay.
**nimrodavni** 32:48 I think the virtual thread-aware is probably also done, I think, Mattia, right? Because we already have Java correlation?
**Mattia Meleleo** 32:55 No, because Java was for, I don't exactly remember, but virtual threads are something different. I think there was a… Some, community… community member, which, was maybe… Volunteering for… for adding support for that.
**nimrodavni** 33:15 Cool.
**Mattia Meleleo** 33:17 Let me search one second.
**nimrodavni** 33:19 So I think we should probably say exactly one… what we want to do with Like, how do we say when we're done, supporting text-based logs? And, like, what's our plan? And then we can decide if we… Like, if we need, like, a structure to the, Text logs, or do we just do, like, append it.
**Tyler** 33:42 Yeah, yeah, yeah, agreed.
I think… I think exactly that, Nimrod. If… if Mattia or… or you could, take a look at this and scope this, saying, like.
we really want to do this, this is what it is. Also, this isn't originally included in the 2026 goal, so do we want to include it here? Like, are we actually going to try to get this done? Is another question. Like, this could also just be postponed, there's a lot of other work we're doing, so… Yeah, I added it as a sub-issue, but maybe it's just more pruning this, and then we can clean it up, or leaving it in. I guess that's just more for you guys, to decide on that one.
**nimrodavni** 34:19 I guess me and Mateo will sing, and See the scope of it, and if we can get it done.
**Tyler** 34:25 Okay.
**Mattia Meleleo** 34:27 Yep.
**Tyler** 34:27 Yeah, that… Sounds good, Okay.
build hotel collector distribution Yeah, this could be the rest of the meeting.
Yeah, it's a work in progress. Again, this is another one that is… is kind of conditional on other… Teams… it's not kind of, it's entirely conditional on other teams, so…
**nimrodavni** 34:59 I just saw the thread today, so many responses, it's insane.
**Tyler** 35:02 Yeah, So I do have to say that, like, I do think that this is, like, it is moving. The OCB builder stuff is moving. This is conditional on the Convigv2 stuff getting done, because that was a big ask from them that, like, we support, partitioning.
I think… Getting it by the end of the year, I think, is achievable. Getting it by KubeCon is… is… is… not achievable. I do think that that's gonna be, probably out of scope of that, especially if I'm focusing on all this other V1 stuff. So, yeah, I think this is still achievable, but it's probably, I'd say, maybe slightly at risk, yeah.
Okay.
Last step is the Python async context propagation. I think this is done.
**Mario Macias** 36:17 Yes, I'm not 100% sure, but I'd say that that was finished some months ago.
**nimrodavni** 36:24 I think, like, last meeting, I remember Nicholas saying something about some… Easily.
**Tyler** 36:30 No, I did.
**nimrodavni** 36:31 It's still not supported, but maybe.
**Mario Macias** 36:33 It could be.
**nimrodavni** 36:33 split off.
**Mario Macias** 36:34 Okay.
**nimrodavni** 36:35 up-issue. I guess we need to… like, sync with Mark.
But, I mean, the… we can… I think we can say that we support it with caveats, and maybe they call it a deal, I don't know.
**Tyler** 36:50 Yeah, I think that's probably worth doing.
I think I'll, I'll take a look at this, afterwards as well.
But yeah, I think that's probably the way to do it, Imran. Good point.
Okay.
It took, about as much time as I would expect, unfortunately, probably not.
Where's the set?
I'm gonna put it at risk on this one for some of our goals. Okay.
Next up, after all that planning, what are we doing next?
So, I've got a, kind of an overview of the V11, the V011, milestone. I've set a release date for August 18th, so far, I've only put in… well, not only, I've primarily, put in goals to make the Configv2 feature complete and publicly accessible. So this is one where we have, like, a release block on trying to get, like, all of the utilities out. I think that's… that's totally achievable. Like, if it does slip, we can go into that, but Yeah, so I think that, Configv2, stuff, just… yeah, I think that is, you know, kind of laid out here, we need configuration validation, V1, V2, the standalone OB runtime loading, so essentially build that into our binaries. The existing OB collector-receiver needs to update its configuration to actually support, like, the parts that we said that we wanted to support. The schema examples, the migration document, all that kind of stuff.
The only thing, then, is then, like, I guess we don't need a final, final decision, but, like, there's a lot of decisions on, like, existing, like, configuration stuff I've got listed above that we need to talk about.
Ideally, we have a path forward, or we're, like, out of… we're moving them out of scope by the end of the, the end of the milestone.
I came up with this date primarily based on these numbers, so, August 18th, is the V11, 011 config v2 feature complete. The V… the next milestone, the V012, I'm trying to shoot for, September 22nd, I guess is what I heard here, kind of an arbitrary… but it definitely ends sometime in September.
Meaning that we have, like, stabilization done at that point, and we're doing our release candidate early October, ideally, like, the start of October, meaning that we have, you know, 2-3 weeks to let it sit and soak before, KubeCon.
KubeCon's November 9th?
surprising how that's, like, right around the corner. So, essentially, like, we need to get the config v2 done, like.
this release. August 18th is kind of an important thing. I did want to point out some of these dates, though, because, like, if we're looking for stabilization, you know, to be finalized by the 22nd of September.
like, anything else that people are trying to work on, or related to it, like, just keep that in mind. That these are, like, kind of like a timeline for what I'm seeing on this thing. Also.
you know, track this work in line with other goals we just went over, right? I do want to point out that, like.
Nobody does anything at the beginning of November. Everyone's at KubeCon. No one does anything the third week of November in the U.S.
everyone's, off on holidays, for Thanksgiving, and then no one does anything the second half of, December, because they're all off on Christmas. So… really, the end of the year is kind of, like, the end of August. Like, you have… you kind of have one more month after, or I'm sorry, at the end of October. You have one more month at the end of October. Like, you're not really gonna get much done, there, so… when thinking about all of those things we just talked about, like, understand that, like, getting it all done by the end of October is kinda… Ideal, you're really pushing if you're… if you're going past that.
what I've done is I've actually added stuff for the config v2, we can take a look at the, milestone, it's, again, all the stuff, but I want to know, like.
Questions for you all is, are there anything that are must-haves that need to get done in the V0111? There likely are, that I haven't included, and I'm asking for them.
I do want to know, like, if it's, ownable, like, make sure that, like, it has an owner and not just sitting there, and it's not gonna just languish. If we don't have additional capacity for the V011, like, what are we kicking out, at the same time?
Also, does this timeline make sense to you? August 18th, is… over a month away at this point, so I think it seems reasonable. Ideally, maybe we can even push this up a little bit, but yeah, so, like, does that seem reasonable to you all based on our current schedules?
**Mario Macias** 41:29 Yeah, I, I will raise the concern that, this holiday's time, at least usually in the… here in the Mediterranean zone, Spain, Italy. Many people… it's on holiday, so maybe not many people is available. I don't know the rest of the team. For example, I'm taking holidays the first… the three first weeks of August.
I don't know the rest of the people is going on holidays or not.
**Tyler** 42:05 Yeah, that's a great point. Any other big vacations coming up for folks?
**nimrodavni** 42:14 Don't think, like.
**Tyler** 42:15 Yeah.
**nimrodavni** 42:16 A couple of Israeli holidays, but they're not… And, like, enduring usually, like, September, October, there's a long stretch.
But they should still be with Lake Parking in between them.
**Mario Macias** 42:31 Okay.
**Tyler** 42:32 Okay.
Yeah, I've definitely already noticed European colon… our colleagues taking time off, at this point. I'm pretty sure in France you're not allowed to work at all during the summer, is what I've got out of this, but yeah.
Okay.
Yeah, yeah, good, good point. So, just to kind of, like, gauge our developer capacity, keep that in mind, that, like, we're not going to have a full team, probably for… maybe most of the rest of the year at this point. So, yeah, it does behoove us to kind of think in terms of, of terms of what is actually achievable based on our capacity. So that being said, maybe we can just go over what is in the milestone right now, and if you have other things you wanted to talk.
About, this track, the Gen AI stuff, I think there's an opt-in question, this is a follow-up to an existing PR. I've got a thing later in the agenda on this one we don't have to talk about now.
This is configv2 stuff, Configv2… I did want to talk a little bit more about, this is classifying, this is a big V1 stability surface area, issue. I'm trying to get that done within this next milestone as well. There's definitely just open tasks of, like, we need to understand, like, what's going to be in scope, what's not going to be in scope.
This is the configv2. This is a part of the config v2. I've got open questions on this. We probably need to get either this scoped to get resolved, or closed within this issue.
More questions in the agenda on that one. I think all of these other things are config v2 stuff. This is a telemetry contract, so this, again, is just a V1 stabilization one.
The rest Tokyo contacts propagation, Giuseppe, this seems… I added this, is this something you plan to get done sometime before August, 22nd?
**Giuseppe Ognibene | Coralogix** 44:24 That's Tokyo, yes.
**Tyler** 44:27 Okay.
**Giuseppe Ognibene | Coralogix** 44:27 Otherwise, I will be completely dead, because I'm… I'm working on that.
**Tyler** 44:34 Okay.
**Giuseppe Ognibene | Coralogix** 44:35 I'm trying to…
**nimrodavni** 44:36 blowing up.
**Tyler** 44:40 Okay.
What else, from all that stuff we just talked about, like, what's really hot on your mind right now that we need to add to this that you're gonna get done within the next month, month and a half?
**nimrodavni** 44:53 I'm hoping we had the Aerospike instrumentation in, not sure… How… how much we, wanna commit that, but… I think that's a linked issue here. I think we… I'm hoping to get it in.
**Tyler** 45:12 Is there a tracking issue? Is this the… is this the…
**nimrodavni** 45:15 Yeah.
**Tyler** 45:16 Okay.
Okay.
Cool.
This… probably not gonna go in.
This could probably get closed, you're talking about… This improved trace log correlation stuff, is this something that, we plan to look at?
**nimrodavni** 45:47 I don't know if for V11, I think we still need to decide the scope of it.
Okay.
And, and regarding the telemetry schema, there's a, like, telemetry schema and… I think there's two issues there that I think kind of… intertwined. The… the LMG contract and, And… oh, maybe just the telemetry contract.
So I'm trying to do more stuff around, like, Weaver, and maybe we can… I think most of the stuff there, like, we defined, like, of what, like, we're leaning onto OTOL plus a couple of the stuff that we have custom.
And I want to add, I want to add more things that, like, Weaver doesn't fail if you just, like, add, additional attributes, or, like, give attributes of existing namespaces, or add, like, new, let's say, like, a new DB system name, like Couchbase, that is not official.
So if you want to be, like, fully complicit and, like, document everything that is changed, that is not as, the, the hotel semantic ventures described, like, you want to, like, harden the validation and then add, like, kind of describe it more thoroughly.
But I think most of the stuff, like, we… we are, like, already documenting. But I think most of the stuff we produce is hotel.
hotel, schema, and then there's some additional stuff, but I want to keep expanding on that.
**Tyler** 47:27 Okay.
Yeah, I think there's an issue before this. I think you're probably thinking of the same thing. I don't know where it is, but maybe if you can find it, go ahead and add it.
God, I thought it was, like, a schema… maybe I could just do a quick search here.
**nimrodavni** 47:50 It's, like, I think under the same, sub… adopt tele… yeah, maybe it's adopt telemetry schema and define OB telemetry contract, so I think they're kind of… Maybe we can say we already adopted telemetry schemas, and just defined the contract a bit more?
**Tyler** 48:05 Yeah, I think you're right.
Okay.
Well, I'm gonna… I'll put this in the milestone so we don't lose it, but maybe you're right… maybe this can get closed, and we'll just… we'll add another tracking issue around, like, what you just talked about. Yeah, I think maybe that's the way to do that.
I don't wanna lose this.
Okay.
Cool.
Yeah, that's already in there.
This might actually be doable as well, if it's as easy as Florian says, but okay.
Okay, cool. Well, if that's the case, there's only 13 issues open right now, only being that these may take quite a lot to get done, but if there are things that you also are planning on doing, over the next month, please, please add them here. We'd like to track that, and so we can get it all, sorted out.
Okay, I think if that sounds good, I think we can commit to that August, 18th date. I would like to maybe even get it done sooner, so if we get all the issues done, I think we can… we can keep going, but yeah, otherwise.
So, jumping into some of those, open issues there, maybe, we can just start talking about… I don't know if we're gonna get through all of these. So the declarative config placement.
So one of the things that we did in this is that we actually, started to integrate into declarative Config. There's an open question here around whether our integration was, like.
I think as extensive as we want it to be. Mostly right now, like, all of our… not mostly, all of our extension right now is in this… encapsulated in this extension, OB.
There's an ask, because this is kind of, like, a long-standing issue in the declarative config, like, there's not stable instrumentation, sections, should Obi live there?
This already, like, it's… we have another issue tracking this in semantic conventions, it conflicts or overlaps. The problem is that instrumentation was completely defined, like, for Java HTTP instrumentation.
And it's not really well structured for OB. Similarly here, I think there's a question around extensions, and distributions to Obi.
There's also a recommendation to put it into distribution, it's not really a distribution.
I don't know if anybody has any strong opinions on this.
I don't think I want to move forward, with a lot of these things, but I maybe just want to think through, like, if this makes sense. I did want to know if this is a blocker, I guess is more of my ask for this question, on, like, whether we want to, like, get this resolved and say yes or no prior to stabilizing the V2 config, I guess is the main ask.
**nimrodavni** 51:02 I… I think, to be honest, I'm not super sure what the, like, the points of these, Intending to, but if there's some valid points there, maybe we can consider them.
But I don't, like, I don't know if it should be… A blocker if we considered all of those points and we think they're not, relevant?
**Tyler** 51:29 So, I…
**Mario Macias** 51:29 Yeah, I agree.
**Tyler** 51:31 I've got mixed feelings on them. I do think that it's, like, valid in the sense that, like, OpenTelemetry declarative Config, like, kind of has, a place that you would put this, like, an instrumentation, but if you go look at it, it's like… it's not structured in a way that, like, you would expect Auto Instrumentation to put things there. In fact, other auto interpretations have already complained that that's how it is.
So, I think it's valid in the sense that, like.
Our thing is very separate right now, and it seems like there are places that they kind of overlap with existing definitions for OpenTelemetry, semantic conventions.
The problem that I have, though, is that, like.
trying to integrate this means that we will need to upgrade the semantic conventions. I'm sorry, not, the, declarative config.
Which puts a dependency on an external group to get this resolved.
Which… definitely says to me that, like, we're not gonna get this config V2 done, in this milestone.
**Mario Macias** 52:28 Yeah.
**Tyler** 52:31 So, I don't know, I don't know an answer, I guess.
**Mario Macias** 52:35 I… I wouldn't… I mean, maybe as… as Nimrod said, maybe we can see if there is somebody point that we can integrate, but as you say before, Tyler.
I have the feeling that the declarative config is… the format is more suitable for an instrumenter inside an application, so you add the agent to the application and configure it for that concrete application.
But for something that is external to that application.
we can struggle. Maybe if we try to adopt some… some extra points.
Then what we get finally is not so valuable or so convenient for our users.
**Tyler** 53:20 Hmm, yeah, yeah, yeah.
Okay.
Okay, I, I… that's good feedback.
I will… I'll take a look at this, and I'll try to respond, and I'll try to get a plan together. I would like to get this resolved in this milestone, so, yeah, let's keep it in, and then… Even if that's closing, saying we're not gonna do it, or if it is, like, what we're gonna do, but… okay.
**Mario Macias** 53:40 Okay.
**Tyler** 53:44 Yeah, this is another one, it was opened by, Nikola, I think, prior… way prior to the V2, Maybe not, I don't know.
I did an audit of this, essentially, it's just saying that, like, the declarative config fields, describe a lot of overlap, which was true, and we definitely, like, addressed some of that.
I did a little bit of an audit to see if, like, we could just close this, and I did want to kind of, like, maybe bring up some things, unlike, if we wanted to take a look. So right now, like, our resource parsing, we really only get, like, a hostname and host ID from that section.
Yeah, it's not really, like, a full support of, like, our resource definition.
I think that that's something that, like, we could actually move forward on in a post-V1.
For a lot of this stuff.
So, like, adding more support for this configuration, since we would accept it in the V2, seems possible. Like, maybe right now we only support partial… Things coming out of it, but, like, it doesn't stop us from, like, accepting this and keeping going forward, so just maybe just keeping that in mind.
Similar for, like, the sampler, we support a subset, processors, we really only support one batch processor with an OTLP. Actually, I think it's an OTLP or HTTP exporter now.
same for the meter providers, like, we only support one, but there is, like, I think an opportunity to extend these things, now that we are currently already supporting it, like… If somebody wanted to come in and say, like, hey, don't just have, like, one batch of the processor, let's have, like, you know, one here and one there, we could always do that.
I think more the, thing that I'm interested in is, like, propagators?
Yeah, that's, I think, interesting. Because that… means that, like, do we want to support, like, the B3 propagator, or, the environment variable propagator, things like that, I think are, open questions.
But yeah, I mean, I don't know. Like, these are just things that, like, we support, we don't support.
I guess my question to the group is, is like, is this, like, is what we have right now good enough?
And just saying that if we wanted to add support for more of these things going forward, like.
that's not gonna block the V2 configuration, or do we want to, like, try to incorporate some of these other things into the V2 configuration at this point?
Yeah, maybe logging level's kind of an interesting one.
That might… that might be worth changing.
Okay, we are running up on the end here, so there's a lot more details on, like, what that support looks like in this issue. If you have thoughts, please take a look.
And, yeah, looking for some feedback on that.
Looking for a lot of feedback on a lot of these issues, but… That's not how we completely capitalize.
Mattia and Nimrod, I saw that you had two issues, on here as well.
Unfortunately, I've run the clock out. Is this something that… Mattia, are you looking for feedback on this one?
**Mattia Meleleo** 56:49 Yeah, it's not super important, I just wanted to bring some attention here, and if someone wants, they can, can, review this, not this PR, but there is one documentation file in this PR which, Which can be looked at, and see the features, see if you like it, and, Yeah, I will, probably… Split this into… into some more smaller reviewable PRs, once we agree on some configuration and the basic, The minimal feature set.
Yeah. So…
**Mario Macias** 57:31 That looks… so it's… you are manually inserting spans by passing the goals… the symbols of the… of each function?
**Mattia Meleleo** 57:44 bypassing. So, the… these are just, user-declared, spans.
**Mario Macias** 57:50 Okay, okay.
**nimrodavni** 57:52 And it's not only in Go.
It's a lot.
**Mario Macias** 57:55 Not only go, okay, that's super cool.
Nice. Yeah, but…
**Mattia Meleleo** 57:59 For non-compiled languages, like Python, Java, there are some cabbits. Like, most production builds don't ship with Dtrace support, so there is no.
**Mario Macias** 58:09 Huh.
**Mattia Meleleo** 58:10 no possibility to, to have USDT markers, so…
**Mario Macias** 58:16 Okay.
Cool.
Cool, I will take a look, thank you.
**Mattia Meleleo** 58:21 Yep.
**Tyler** 58:25 Cool. Yeah, and then… Nimrod, you were asking about nightly builds. We were running up on the end of the hour. Is this something that maybe… could you put together, like, a proposal for this? Like, I'm interested in seeing a proposal, and maybe we can talk about it next week?
**nimrodavni** 58:39 Yeah, I can open an issue, and… Right, Tom.
**Tyler** 58:42 Yeah.
Awesome.
Awesome. Okay, cool. Definitely more to talk about, as we can see here. But that's all gonna be next week. Okay.
Thank you all for joining, right up on the end of the hour here. So, yeah, I guess we'll end the meeting here, and yeah, awesome. Thanks for all the engagement. Thanks for all the hard work. Obviously, we've done a lot of stuff, and let's try to get some stuff done by the end of the year. Alright, buddies.
**Mattia Meleleo** 59:08 Bye-bye.
**Mario Macias** 59:09 Bye-bye!
**Pellared** 59:11 Phew.
