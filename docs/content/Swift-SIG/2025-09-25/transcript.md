SIG: Swift SIG
Date: 2025-09-25
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Bryce Buchanan** 00:56 Hi, Martin.
**Martin Holman** 01:00 Blue.
**Bryce Buchanan** 01:01 It's gone.
**Martin Holman** 01:05 Is it a Sriracha t-shirt?
**Bryce Buchanan** 01:08 Oh, yeah I thought this was, it's pretty funny.
**Martin Holman** 01:15 Nice.
Get that docket up.
**Bryce Buchanan** 01:26 And the best part is, like, the letters, like, don't fit properly on the shirt. They get, like, bunched up on one end.
**Martin Holman** 01:34 It definitely looks kind of homemade.
**Bryce Buchanan** 01:36 Yeah, cracked. I was like, I have to get that, that's hilarious.
**Martin Holman** 01:46 Mayor.
Delia.
**Bryce Buchanan** 02:36 arms.
Gonna say, you were the… you were the topic from last week. I am the topic.
**Martin Holman** 04:01 It's like a small meeting today.
**Bryce Buchanan** 04:04 Yeah. I think, Nacho was saying he wasn't gonna make it.
**Martin Holman** 04:08 F.
**Bryce Buchanan** 04:24 Alright, let's get started then. So, topics from last week. So, Vinod, any progress on this issue?
Are you there, Vinod?
We can come back to them.
Let's see here, so this behavior is still not documented. I… I think we need to do a release, but I also had a, discussion about the package resolve I wanted to talk about, too, so perhaps I can, take this on and do a release, Once we sort out the package resolve stuff and get this other thing merged from Billy.
Okay, so, and we also got this remove NEO from the tests.
In the core, or in the main repo.
Looks like we have a couple of… It looks like that. You can resolve those, Martin, if those… if you finish them.
**Martin Holman** 05:47 I think, like.
there are some other changes we can make, but I think this, like, moves us forward a little bit.
**Bryce Buchanan** 05:54 Yeah, yeah, okay.
Cool, I'll, I'll take a look at that too, and then I think it looks like we can probably merge that either way.
**Martin Holman** 06:02 Sweep.
**Bryce Buchanan** 06:10 Okay, so… Billy's PRs, Oh, it looks like both, Mitch.
Damn.
So… Cool.
I guess this was the other one that I wanted some other people to look at, very good. Yep, yep, yep, yep, yep, yep, yep, cool.
So, we can get that, support log events.
Is that another… that might be another PR, actually. Let me take… Let's go back over here… Here we go. Okay, so this is the other one that I wanted to get some eyes on.
Before merging.
But, this just updates our, the way that the logs create, or can create, events.
Because… let's see, so, like, for example, like, the event domain has been deprecated, and they added a… an actual, like, event… name, like, first class field in the Protobuffs.
So it no longer needs to be passed through, the attributes.
So this kind of just brings the log stuff in line with that, and You know, takes out the, The, the event, domain stuff.
So I'll just add this in here.
But, yeah, pretty straightforward.
So, the… the, Oh, Billy had a question, sorry. The package resolve that I wanted to discuss, just go here.
These are all core.
**Martin Holman** 08:26 So…
**Bryce Buchanan** 08:30 now that we have, like, the two repos, I was thinking that maybe… Hey, Billy.
We might consider removing the package resolve, Because that pins, like, the Swift Core version there, and I want it to be able to be a little bit more flexible.
So that, the, the main repo can be updated with the latest version of SwiftCore up to a point.
So that we don't have to do, like, a manual release every time we do a SwiftCore release.
**Martin Holman** 09:09 Do we have sufficient testing for that? Like, that we can be sure…
**Bryce Buchanan** 09:12 That's the thing. I don't really know, because I've never really, like, designed anything to do this before, I'm not really sure what the SPM behavior behind this would be. I don't know, like, can we… can we just, like, remove Swift Core from the package resolve?
That's… or should we not even commit the package resolve? I need to do a little bit more research on this, I think.
Boom.
**Martin Holman** 09:40 I think, yeah, I have a lot of experience with Ruby in this, and you would just not chicken the package resolved, but…
**Bryce Buchanan** 09:46 Yeah.
**Martin Holman** 09:47 Swift, I'm not sure.
**Bryce Buchanan** 09:49 Okay.
**Ari Demarco** 09:55 I'm… I'm just opening the… the package.swift.
wouldn't that solve the problem, per se? Because the package resolve is just for the ones that… Actually go and try to build the code by themselves.
**Bryce Buchanan** 10:18 I'm not sure what you mean. Can you elaborate?
**Ari Demarco** 10:22 So, let's say, like, somebody is using OpenTelemetry Core to… Dot 3.
An OpenTelemetry Swift.
**Bryce Buchanan** 10:32 It's using as a dependency.
**Ari Demarco** 10:35 Opens elementary core from 2.1 and upwards.
That should just work. You don't depend on the package result whenever you consume that dependency.
**Bryce Buchanan** 10:46 Oh, okay.
**Ari Demarco** 10:47 I am the one… if I am the one trying to force that, I will have to force it personally.
in my development, but that… at some point… at that point, I think we should do a specific request, a specific update.
So we say we support from this version and onwards, and that's it.
**Bryce Buchanan** 11:08 Okay, so the package resolve isn't even affected by that, or it doesn't even affect that?
**Ari Demarco** 11:14 I think that the package result it's just for when you develop on that specific library, in this case, OpenTelemetry Swift. But, for example, in the case of Embrace, Embrace We'll use my dependency, so…
**Bryce Buchanan** 11:29 If… if…
**Ari Demarco** 11:30 if I'm open to use OpenTelemetry 2.1 and upwards, and OpenTelemetry Core 2.2 and upwards, it will try to do whatever it wants based on those package definitions, not Based on the package results that are committed.
**Bryce Buchanan** 11:46 Okay, okay.
Interesting. So, the package resolve doesn't really affect much anyway, Unless you're just developing in that repo specifically. Do we… do we even want it committed? Like… Does it provide any value doing that?
**Ari Demarco** 12:06 It's a good question. All the others are fixed, isn't it? All our other dependencies?
**Bryce Buchanan** 12:16 I think a couple of them aren't, but… They can be if they are a problem.
**Ari Demarco** 12:24 So, it's… the only… the only usage for package result is for reproducible builds. So, if all our dependencies are fixed.
And the one that won't be fixed is… .
**Bryce Buchanan** 12:38 War.
**Ari Demarco** 12:39 Sorry. And the one that we want to don't have fixed is score, we can just remove the package result. I don't think it's needed.
I've never done it in Swift, but it's… it's feasible in that way.
**Bryce Buchanan** 12:55 Okay. Yeah, I'll try to do a little bit more research, just to understand a little better how it's supposed to, or, like, how it behaves, and, if that is in line with what my expectations are. We do have these, three packages as well from Apple, which are using from, I guess, and NEO as well, but, since those are all kind of, like, first-party packages from Apple, I'm not concerned about them so much.
I would rather them be pulled in the… in the latest minor version.
Okay.
**Ari Demarco** 13:32 Yeah, yeah, I don't think they are going to be problematic.
**Bryce Buchanan** 13:35 Yum.
**Ari Demarco** 13:36 what I would… what I would do is… Like, open patches, or if we really, really trust them, open the minor versions.
And that's it.
**Bryce Buchanan** 13:47 Cool.
**Ari Demarco** 13:48 Obviously, you could have specific problems if you don't have the exact number, like somebody saying, hey, this is not working, and that under the hood uses, I don't know, Swift, Atomics, or SwiftLog, or whatever. You have to find out which specific version they are using, because maybe there's a specific mismatch on one of those versions.
But I don't think that will be always the case. I think that for minor patches, that shouldn't really happen that much.
**Bryce Buchanan** 14:25 Cool, okay.
Yeah, and leaving it a little open might help resolve some of those situations as well, wouldn't it? Like, if a dependency somewhere else required a version in that range, maybe it was pinned to something But it's in our from range, then that should resolve without issue, right?
**Ari Demarco** 14:47 Can you repeat it? I didn't understand the case.
**Bryce Buchanan** 14:50 So, yeah, so let's say, a package, depending on our SDK, also has another dependency in our dependency tree, but they have it pinned to a specific version, but that pin is within our range of acceptable versions.
Then they will, they'll, they'll, it'll resolve, without any issue, right?
**Ari Demarco** 15:14 Yeah, SPM will do the magic. It'll try to find First, the one that has the most strict versioning mechanism, so if somebody's using Exact, it'll try to find that the others Correspond to that.
version…
**Bryce Buchanan** 15:32 Right.
**Ari Demarco** 15:32 If not the imprint.
**Bryce Buchanan** 15:33 But if we were to… if we were to pin it on a specific… specific version, and they were to pin it on another version, that's… then it would… then it would resolve.
**Ari Demarco** 15:43 Yeah, exactly, that will fail on trying to download everything on SPM.
**Bryce Buchanan** 15:47 Okay, yeah, okay. So, yeah, it seems like being a little bit more open will produce a little bit better… you know, it's like a trade-off, right? It might be a little less stable, depending on how stable these dependencies are.
But it'll allow for a little bit more flexibility in which version is actually pulled.
**Ari Demarco** 16:07 Yeah, in the end, if we want, whenever that happens and we have doubts, we can just ask, whenever somebody submits an issue, the package result.
And that's it.
**Bryce Buchanan** 16:19 Cool. Okay.
Alright.
So I'll do a little bit more.
Research on that.
Okay, so Billy had a question in Slack.
Oh boy, that's not gonna work.
Okay. Nice.
**Billy Zhou** 16:44 It's okay, it was just about the log events stuff.
**Bryce Buchanan** 16:48 Oh, okay, yeah, it looks like that got merged, so I think… what I'll do is, I think we'll do another release, it's been 2 weeks since the last one.
And, and yeah, we'll just do a whole… a whole stack release, and I'll document… The release behavior as well.
Well…
**Billy Zhou** 17:08 I think, the event name thing instead of core hasn't been merged yet. I think we wanted a second review on this, or at least to discuss it with everyone else.
**Bryce Buchanan** 17:19 Oh, you're right, it's not merged. Yeah, so let's, let's just, since we're all here, let's just take a quick look at it.
I'm not sure, were you here, Ari, when I was mentioning it earlier a little bit?
**Ari Demarco** 17:38 Do you mean about this, PR? No.
**Bryce Buchanan** 17:44 I'm not sure if I was discussing it with Martin before or after you arrived.
**Ari Demarco** 17:52 No, no, no, I wasn't here. I arrived a bit late.
Some connectivity issues.
**Bryce Buchanan** 17:57 No problem. I can… I'll just, give you the rundown. So basically, this PR is just bringing the, log stuff in line with the more recent updates to the, spec, where the, domain is removed.
Because that's no longer used, and the use of the actual, First class, like, protobuf field for event name is also being used now.
Rather than injecting it into the, the attributes Like it was originally designed.
So, pretty straightforward, the old ways of doing it are still here under a deprecated method, which I think is fine.
But it also provides this new, API on the blog record builder that lets you set the, the first class event name.
**Ari Demarco** 19:00 Great, and that's… that's behind the protocol, that new method?
Add new method, it's behind the protocol.
**Bryce Buchanan** 19:11 Yes, yeah. Yeah, it's on.
Yeah, the logs, record, builder, medical.
**Ari Demarco** 19:22 Okay.
**Bryce Buchanan** 19:23 Yep.
**Ari Demarco** 19:24 And it has the noop on the extension, mostly… mostly to not break, generate that breaking change on anybody that is implementing the log record builder.
interface?
**Bryce Buchanan** 19:36 Yep.
**Ari Demarco** 19:38 Okay. I think it's go.
And it's up to date also with the entity.
Definition.
**Bryce Buchanan** 19:48 The entity definition.
**Ari Demarco** 19:55 Sorry, Evan's definition.
I… changed the… I changed the concept.
**Bryce Buchanan** 20:07 I'm not… I'm not, I didn't quite hear you, the what… which definition?
**Ari Demarco** 20:12 Oh, no, no, I, yeah, yeah.
I was wrong, I meant, like, the event definition, not the entity's definition.
I was just reading your PR the other day, so I got confused, but yeah, yeah.
**Bryce Buchanan** 20:24 Oh, I see, okay. It doesn't actually look like there's a… well, in the default one, there is a no-op, but, let me… Let's see, builder… So it does depend on the event builder.
Yeah, so I think that might need to be verified if… if… whether or not it will, propagate that to a custom implementation or not.
But, yeah. Ari, maybe you can take a look at this and give your approval if you… if you think it's… Alright or not.
**Billy Zhou** 21:21 Oops.
**Ari Demarco** 21:22 Yeah, understood.
So does the new method have to be, like, optional or something to avoid breaking, customers?
**Billy Zhou** 21:35 Set event name thing.
**Bryce Buchanan** 21:38 That might be one way to resolve it.
I'm just, trying to… Verify the… the inheritance chain here.
**Ari Demarco** 22:03 We can test the branch in our SDK, as I think we have a… an implementation of the interface, so if it breaks, I'll know it by just compiling. I can test it out after the meeting.
**Bryce Buchanan** 22:18 Yeah, go ahead.
That would be helpful, because,
**Ari Demarco** 22:21 Mmm.
**Bryce Buchanan** 22:22 Exam… or a test like that.
**Ari Demarco** 22:24 Okay, and I can either comment or approve the PR.
Based on… on that test.
**Bryce Buchanan** 22:30 Alright, sounds good. Alright, and once this gets merged, then I'll do a release.
**Billy Zhou** 22:38 Thank you.
**Bryce Buchanan** 22:41 Cool. Alright, any, any other topics?
Alright, proving.
We can, have a short one today, then.
**Martin Holman** 22:58 Sounds good.
**Ari Demarco** 22:59 I'll check that out for you, Willie, and then… assuming the… Really? So I can approve or comment on the bureau.
I'm so glad I can't unblock Bryce to do the release.
**Billy Zhou** 23:12 Thanks. I think I also have to do, like, a follow-up PR in the main repo, put out a draft PR. I think I have to, Let me just share my screen real quick.
**Bryce Buchanan** 23:25 Sure.
**Billy Zhou** 23:27 I think I made a mistake in this too, actually. I think it has to be a top-level field, so… Like, we need this to, like, actually put the… Event name in here.
But… and it tested at end-to-end, but, I think it's supposed to be a top-level field instead of an attribute, so I think I need to do this again, actually. Just realized.
Anyways…
**Bryce Buchanan** 23:58 It seems like it's still going into the attributes for some reason, or maybe that's just the default behavior still coming through?
**Billy Zhou** 24:05 Yeah, so I'll have to fix this, but yeah, like, the goal is to get one of this… something here, out as well.
**Bryce Buchanan** 24:12 Yeah, it should definitely be in the top level.
Okay.
**Billy Zhou** 24:17 Okay.
**Bryce Buchanan** 24:18 I'll look for that.
**Billy Zhou** 24:19 Thank you.
**Bryce Buchanan** 24:21 Cool.
Okay. Oh, and I just wanted to… make a note that, I am investigating how to… Replace, or how to… how to do, like, the, raw metrics using the 2.0 metric APIs, so… Hopefully that'll… that'll… that issue will be resolved.
Okay, if there's nothing else, then I guess let's call it here.
**Martin Holman** 25:00 Cool. See you all next time.
**Bryce Buchanan** 25:02 Bye, everybody.
**Billy Zhou** 25:03 Bye, guys.
**Ari Demarco** 25:04 Okay.
Yup.
