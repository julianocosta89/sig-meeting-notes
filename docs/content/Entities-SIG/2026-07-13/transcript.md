SIG: Entities SIG
Date: 2026-07-13
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Dmitrii Anoshin** 04:04 Everyone. George said he'll be late. 5, 10 min.
So wait.
Can just wait for him.
**Josh Suereth** 07:31 Hey folks, how are we all doing?
**Dmitrii Anoshin** 07:36 Hello?
We do.
I'm well, how are you?
**Josh Suereth** 07:42 Not bad, not bad. I'm, like, triple booked today, so I have to leave a little bit early, and I, I'm cooking lunch while we're here. So apologies that a little late.
But… I wanted to cover a few things, but Dimitri, do you mind running the meeting?
**Dmitrii Anoshin** 08:01 I can. Yes. So let me maybe share my screen. Then.
**Josh Suereth** 08:15 We're just adding a few notes to it.
**Dmitrii Anoshin** 08:34 Okay, so we don't have much agenda. And yeah.
SDK proposal.
**Josh Suereth** 08:48 Yes, you can look at this. This just needs some reviews from folks in the SIG and things. This is the bare minimum SDK changes that we need to get our initial prototypes out the door for like Java and JavaScript.
Basically, it proposes two things, right?
it proposes a set of retrieval methods, because already today in the SDK, on a resource, you can say, give me the attributes associated with the resource, right? This gives you the ability to get the entities off, and the unassociated attributes And then the other thing is it just updates the merge specification to say that you need to, merge things if entities exist. Oh, I guess there's a third, which is the create method now has, entities in it.
And I need to fix that bracket to actually not be a link. That's… But anyway, so it's really, really, really minimal.
Effectively.
**Dmitrii Anoshin** 09:51 That was good.
**Josh Suereth** 09:52 Yeah, just looking for reviews. Once we get enough, I can take it to the spec meeting and get folks to, to prove, but it… it… the… the biggest concern I have is the term unassociated attributes.
In other places, I call them raw.
And people didn't like raw, they thought it was confusing. So, started… there was, the Java SIG was like, I think it was Jack specifically, was like, why don't we use unassociated?
I think that's a good term. So after this one would be submitted, I might go update all of the, like, non-spec-related docs to call it unassociated attributes instead of… something else. And yeah, if you want to see the Java prototype, you can see.
**Dmitrii Anoshin** 10:36 We discussed it last time, I guess.
**Josh Suereth** 10:38 Yes.
**Dmitrii Anoshin** 10:40 Okay.
Okay.
So we we need that one before we can merge this one.
And this will actually change the SDK.
by providing experimental feature. Right?
**Josh Suereth** 10:55 Yes, it'll provide the experimental feature. You have to specify an environment variable or a Java property, and then it will pull in the,
**Dmitrii Anoshin** 11:03 No, no.
**Josh Suereth** 11:04 Balenciag Oh, gosh.
**Dmitrii Anoshin** 11:07 This one, right?
**Josh Suereth** 11:11 My cat disconnected me, am I back?
**Dmitrii Anoshin** 11:14 Okay. Yeah. All right.
Okay, yeah.
Sounds good. Yeah, it's looks good for me. I can approve it offline.
And yeah.
I don't think we have more to discuss now. This seems pretty straightforward.
Cool, unfortunately, I have a pretty big say now.
another site, and I cannot allocate time to entities at all, like that week, and maybe this week as well, but I'll try to do it.
So not really much of this from my side.
at this point.
Do we have… Maybe anyone else has anything to discuss.
**RC Robert Cowart** 12:16 Yeah.
CLAB, I actually had a question more than anything else, more than a discussion.
I mentioned last week that on the, you know, on the network side, we have an effort going to identify network attributes and stuff.
And as we're starting to do that and think about relationships, I was wanting to find whatever relationship types had already been defined and I couldn't. I think the issue, and I see it already in this URL being typed, is that, like, once stuff hits the doc page, okay, you can Google it or other ways to search it. When stuff is buried in GitHub.
issues, it sometimes can be really challenging to find it, so I… I swear I had, like, 30 different tabs open trying to find this stuff, And I'm not just trying to ask a lazy question, so…
**Dmitrii Anoshin** 13:12 Yeah, the thing is is that it's experimental, and we don't really like the dance crew make it.
like publicly. easily available. Let's put this way.
So that's why it's after.
**RC Robert Cowart** 13:29 Oh, yeah, I understand the reasoning for sure. I just it was I was struggling to find it. So.
**Dmitrii Anoshin** 13:35 I don't And it's for the relationship specifically, it's something that really very experimental. It's the design doesn't have any implementations anywhere yet.
And it's just like, let's say, aspirational, some minimal addition, how we would consider relationships being represented in future.
**RC Robert Cowart** 13:57 So I guess what I was looking for is, beyond… like, I felt, even there, it says EG, like, for example. I'm thinking, okay, I get the examples, so where's the list?
You know, so no, but if, if it's not there yet, that's fine. I, I mean, and then what we'll, we'll do is.
Try to document the things that seem to make sense to us, and then… I will come to this group and say, like, okay, if there's something that already is roughly equivalent, great, then we'll adapt. Otherwise, we'll probably have some suggestions then, so…
**Dmitrii Anoshin** 14:33 Yeah, actually, initially, in this Pr, I I used to have like, let's say, standard relationships type. But given that it's like there is no planned implementation at this point yet. We decided to not introduce that list, because, like.
going through this semantic conventions and all the 6 that might change. So your work would actually help to define that list. Because right now it's yeah, it's it's just examples and everything. But whenever you have more additions and more entities, definition, relationship, definition in the next, let's say, non normative.
Docs on the network entity side.
we can use that as a learning as well, and create this like standard list going forward. If that makes sense.
**RC Robert Cowart** 15:25 Got it. Okay, sounds good. All right. That makes sense then why I didn't, why I was struggling to find anything. So I appreciate it. Yeah, I suspect it'll probably, we probably still need a few weeks before I would then take a slot here to share where our thoughts were. But, probably closer to early August, I would guess. But yeah.
**Dmitrii Anoshin** 15:47 Sounds good.
I mean, data set. But Okay, anyone else.
Josh, do you want to bring anything?
**Josh Suereth** 16:13 I think the… I mean, we have… we have two main things going on right now, which is just we're trying to get the SDK prototype stood up to start, to start really letting people hammer on this and try it out, right, with the collector and the SDK.
And then, the big thing in my mind is the host ID problem, right? This goes into… we chose using local IDs and wanted to figure that out, so if there hasn't been any, like, progress made on host ID in the past week, then I say we, you know.
put… put this on hold and… and keep doing some thinking and writing, because I… in my mind, that's… that's our number one issue right now, as a SIG, is let's… let's figure out what the design for host ID should be, so that it works both with SDKs and with the collector.
**Dmitrii Anoshin** 17:02 But for the first idea, it's not.
strictly about entities. It's also more like How we actually get that data, we'll say reliably.
from all the different like permutations that the most can begin.
And that's what we… in in the host in systems of anti-conventional seekers are working on. So there's us like, actually, it's actually actively being worked on. But there is no No, like significant progress yet.
Right. That's. We have one person to work on it. Yeah.
**Josh Suereth** 17:41 Yeah, the thing from an entity SIG that we need to think about is this whole, you know, I am a piece of instrumentation that can describe an entity, but I don't know which one.
I know the type, but I don't know which one. Like, I don't How do we want to support that? Right? And that's so I'm waiting to see more about what you guys decide with host ID to kind of figure out if we need to propose any changes the data model. But in my mind, that's like, I see all of our, okay, once we finish that, then it's kind of relationships.
right, and how we want to do relationship things, but I think they're kind of a little bit entangled, because, like, host ID you had the proposal, Dimitri, about the ID scope, and being able to say, like, this thing gets its scope for something else, right? That, to me, that's all kind of tangled up in this host ID question of, I want to see, like, a comprehensive, how do we want to resolve that problem that we think scales to other related Things, you know, For context, someone in semantic conventions this morning was asking for how to model cloud related resources, they were specifically worried about Azure. But then we were talking about Amazon, and we're talking about GCP. And there's some interesting things there, right, like we have this cloud that resource ID.
But then we also have a thing, do I know that it is a, you know, What's it called? And I forget what's called an Azure container run thing, AWS lambda, whatever their equivalent is, they have some name for it that I always forget that thing, right? How do I know it's that versus a container in in like, AKS versus a container in GKE versus a container in EKS, you know?
So…
**Dmitrii Anoshin** 19:35 I don't know I think we discussed that. Not sure if that's written anywhere, but we just need to have more entity types and more more entity types would have overlap. So it will be generic entity type with some more specific entity type for particular for particular cloud provider, for example.
even even cloud needs to be also associated with some entity or cloud resources, cloud attributes. I mean.
So it will be, like, cloud provider, one entity type, and let's say Azure is another entity type. Does that make sense?
That we we'll align on that right.
**Josh Suereth** 20:12 I… we… we did, but I think we need to start writing down proposals of what it looks like, and then getting a feel for that. So, like, you know, with that… with that, what… what is a cloud res… like, cloud resource ID, where does it live?
And when we say there's a type that's like a refinement or an ISA with that, you know, like a… what does it actually look like? What are its identified attributes? What are its descriptive attributes? I think, like, it probably makes sense for us to put a proposal together on that. I might… I can take a crack from a GCP standpoint, because, you know, that's kind of what I own and do all day, is, like, identity of GCP resources. But, it'd be… it'd be useful to… to kind of think about that part of our data model, in, I'm looking at it in light of host ID, how we solve that, and then I'm looking at light of cloud, and how we want to solve this relationship-wise. Like, those are the two… in my mind, most important relationships. Host ID is interesting because we have an entity where I can discover all the attributes about it, but I can't figure out its ID reliably.
**Dmitrii Anoshin** 21:15 I see.
Okay, yeah.
**Josh Suereth** 21:17 Yeah, yep.
**Dmitrii Anoshin** 21:18 All right.
**Josh Suereth** 21:20 Good.
**Dmitrii Anoshin** 21:21 Yeah, I just want to say I understand the question. So we probably… like using host as a as an example and learning exercise. We need to define that somewhere in the spec. So it will be like, let's say, 1st official relationship that we that we establish, and all of the mechanics around that like a specific generic entity types, even, like, it's gonna be a spectrum, right? More specific, and, like, is, how that relationship would connect them to each other, which identifying field would be chosen.
**Josh Suereth** 21:56 Yep. Okay. And then, this will determine, like, if we start… as we keep churning through things and adding entity support, right, eventually we're gonna come to a state where it's like, here's the resource that I want to be reported.
And all the attributes I'm gonna put in it, and what the entity associations are there, right? And then here's the relationship signal that comes out of the SDK, here's the relationship signal that I… that the collector builds when it reads, like, the Kubernetes API, or Amazon's, you know, resource… APIs, I forget what they're called. For us, it's called the Asset Inventory Server. You know, if I read that and turn that into a relationship chart, what does that look like? That sort of thing.
**Dmitrii Anoshin** 22:37 Yeah, sounds sounds good.
**Josh Suereth** 22:40 Yeah, okay.
Okay, but yeah, so… SDK proposal, I think there's still the one from Daniel, I don't know if he's here or not, or wants to talk through that.
**Dmitrii Anoshin** 22:52 You cannot join today.
**Josh Suereth** 22:54 Yeah, please take a look, because I'd like to get the review and the spec sig, get it through into Java, and then there's a follow-up Java PR I would make after the SDK proposal's done and the initial proposal's done in instrumentation. I need to update all of the resource detectors actually in a separate project.
So, service and, telemetry SDK, I think, are the only ones that are in Java's SDK itself, and the rest of them are in this Java instrumentation repo. But from talking with Jack, I think it's actually pretty trivial for us to go add entity support out there with this flag that we're planning to have.
I think that can work for all the other SDKs, but I'd like to Also, try this in Go.
I think GO's gonna be rather exciting.
Just because they, they're always exciting for some reason.
The Go SDK? Yeah.
So I'd like to try that, and then I think we're good on… Foundation, so…
**Dmitrii Anoshin** 23:55 Okay.
**Josh Suereth** 23:56 Cool.
**Dmitrii Anoshin** 23:58 Sounds good.
I think I'll look into that. I just, as I already said, I have, I'm struggling with having time dedicated to entities recently, but like this week, maybe I'll find some.
Hopefully.
**Josh Suereth** 24:13 Yeah, I think maybe what that means is we should really have a defined scope of let's get to what we think the most useful low hanging fruit is, so that as we have trouble finding time, the most important questions for folk are answered, you know?
**Dmitrii Anoshin** 24:31 -H.
**Josh Suereth** 24:33 Okay.
**Dmitrii Anoshin** 24:34 Yeah, I guess I agree with you that this ambiguity around host ID and is that relationship with between similar types is kind of something that we need to flesh out.
Right, well, the…
**Josh Suereth** 24:53 The other thing, Dimitri, let me know if you're wrong. I know that you and I have been struggling with stable-by-default work that's been ramping up for OpenTelemetry. I've had less and less time for entities over the past six months to just to get all the stability work going for semantic conventions and all that kind of junk.
what my thinking is, is with getting this prototype and proposal out, when you figure out host ID and we get the initial set of relationships done.
I think we have a core people can try. And so I want to let things bake for a while of getting feedback from people trying it out. And use the SIG for like Robert's questions of like using entities and anger, and how they feel, and kind of take a little bit of an implementation hiatus to try things out.
And then take all the feedback, and then do a second implementation wave, like, in the fall, or, you know, once we get enough feedback in.
**Dmitrii Anoshin** 25:47 Sounds good. Yeah, sounds reasonable.
**Josh Suereth** 25:49 Okay.
Cool.
Awesome.
I think I'm gonna drop for my next meeting, sorry I was a little bit late, everybody, but…
**Dmitrii Anoshin** 26:00 I think I'll wrap it up if there are no other questions in that case.
Cool.
Cool. Thank you, everyone.
Bye.
