SIG: Resources and Entities SIG
Date: 2026-07-27
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**krajo Krajcsovits** 01:45 I don't.
**Josh Suereth (Google LLC)** 01:48 Hey!
**krajo Krajcsovits** 01:49 Okay, I sh… Maybe I should have stayed in the old one and told them to look at the link. Let me see if I can join both at the same time.
**Josh Suereth (Google LLC)** 02:00 Oh, no worries, yeah. I was like, where the heck is everybody? Alright.
**krajo Krajcsovits** 02:06 Yeah, there's two more people there. Let me make sure.
**Michele Mancioppi (Dash0 Inc.)** 02:59 Hey, Josh.
**Josh Suereth (Google LLC)** 03:05 Hey!
**Michele Mancioppi (Dash0 Inc.)** 03:06 Is it only… only us?
**Josh Suereth (Google LLC)** 03:09 No, Half the people are in the other Zoom meeting invite, because we just changed to the CNCF one.
**Michele Mancioppi (Dash0 Inc.)** 03:16 Alright.
**Josh Suereth (Google LLC)** 03:20 Yeah, if you weren't aware, apparently we're switching our Zoom accounts, and as such, it's chaos where, if you had, like, your own meeting invite with the Zoom ID, you're on the wrong one.
**Michele Mancioppi (Dash0 Inc.)** 03:35 Yeah, well, still better than when I… when we found the arrows SIG cyber-squatting.
On the link we were supposed to use in packaging.
**Josh Suereth (Google LLC)** 03:45 Oh, really?
**Michele Mancioppi (Dash0 Inc.)** 03:46 And they were 2 hours late.
**Josh Suereth (Google LLC)** 03:50 That's funny.
Anyway, I put it in the notes the new Zoom link, so hopefully folks can take a look at that. But, why don't we get started here? Kreo, you want to talk us through?
**krajo Krajcsovits** 04:03 Yeah, it's just, like, a practical question. I'm thinking about how to do the left-hand navigation.
You know, eventually I want to get to demo or prototype.
And, I was wondering what it would actually show, because I understand that entities eventually will give me a kind of hierarchy, like, you know, what contains what, or what the context is.
However we're going to call that.
And so I will be able to show something like, you know, host entity, VM entity, content entity, or whatever, in a kind of a tree, right? Because I have Some knowledge on how they are fit together.
And then, yeah, and then, like, the obvious question is, like, okay, so then I want to filter on, like, a host.
Or something.
I click on host, and then I can start selecting something, but what is that something that I'm selecting? Because… There's going to be an identifying attribute, one or a couple, but those are, like, numbers that people were not… probably not recognize, I guess? And then you have a bunch of, descriptive attributes.
And, like, looking at the examples, it's very tempting to just say that you know, host.name is the thing that I'm going to offer as the thing to select.
And the thing to filter on.
But, like, I don't actually know, because that's not part of the… part of the spec. So, I don't know if you had any thoughts on You know, how did this would work in practice, and whether we should have a rule saying that there should be something called name, or display name, or something like that? I don't know. You know, any thoughts?
**Josh Suereth (Google LLC)** 05:56 I can talk about what we've mentioned before, which is, like, I think it's important that we have a display name, like, this is a thing we absolutely want to solve, and there is nothing written down in the spec yet.
Oh, okay. The… my thinking is, at least when we talked in the past, we want OTLP to kind of contain the data that has to be sent on OTLP.
So, that might not… Send a display name every time, if you can infer the display name from the type.
So, one of the ways to think about solving this is, like, the definition of the entity. Somewhere will say, this type has this, like, two-string method, where it says.
you know, for host, like, use name. For container, it might be, again, it might use the name for container, because I think container name makes sense. For, for service.
it might be, like, use the namespace and the name together, you know? It depends how we want to… because service, you have instance ID, so it might be, like.
Show the service and the instance ID, Or show just the instance ID, because there is no name to a service instance.
it could be that for service instance, we say, find an ID from somewhere else, I don't know, but the idea would be, like, there would be a… external to OTLP thing that says, for this entity type, here's how you make a display name for it, and here's the attributes you use.
That's… that's kind of like the… the strawman proposal there.
Just so that we're not overloading OTLP with a whole bunch of data that is synthesized from other things. That said, that's not, you know, set in stone or anything. Go ahead, Daniel.
**Daniel Dyla (Dynatrace LLC)** 07:56 It seems to me that, like, display name may even be something that we might not want to specify at all.
To me, that almost seems like a product decision for backends.
like… Some products may use the term host to refer to physical hosts and virtual hosts, and some products may want to call it a virtual host.
And, like, that's just a… you know, I don't want to pick on that.
Examples specifically, as much as, like.
It seems like display name is a… I'm not sure how useful it is, especially as something to be sent across the wire.
I could see display name being something that's, like, recommended in some cases, or just the names… we will need something to call it in prose, in the SumConv and stuff like that, so having a consistent naming scheme might be less confusing.
In that regard, for, like, documentation and blog posts and what OTEL calls a thing.
But as far as what a back-end product calls a thing, they may use the same term OTL does, but they may choose not to.
And I think we may not want to be, like, overly prescriptive about that.
like, the… If we say the name can be derived from the attributes and the type, and we're only going to send the attributes and the type.
Seems like a backend product can do with that information what they will.
**krajo Krajcsovits** 09:37 Will… I mean, that's part of the information. The other part is how do you derive that?
But then, I mean, for me, the simplest… Things seems to be that… if there's an entity type.name attribute, I'm just going to use that, like, a simple heuristic, because… Like, I've been in products before where we tried to encode Oh.
Like… stuff outside the spec, you know, naming conventions, and such, like… I worked in secular logging, and there was always discussion, okay, how do we call the user? Is it username, user, or whatever? And it's always a pain to keep Track of that, and try to cover the whole world, and all the various products that produce username.
So, yeah, I don't know.
**Daniel Dyla (Dynatrace LLC)** 10:36 Yeah, but my point was that that's a product decision, like… that's not… open telemetry, you may not want to make that decision for you. And sending a name across the wire Is just one more thing for… the JavaScript SIG to do something subtly different than the Python SIG and introduce weird bugs.
In my opinion, this was a mistake we made with spans.
But, yeah, we don't need to go too deeply into that, but, I would say… the… the… OTEL should be consistent with the naming and the words we use internally.
But… like, Google Cloud Trace might call something differently than we do, and that's okay.
And if we send a name across the wire and they don't use it, that's just useless bytes.
Potentially, it's even confusing to users.
If, you know, they… modify the name in an OTLP processor, and then it's displayed as something different in the product.
That's, again, that's a product decision. If a name comes across and your product wants to use it, great.
But I… I am not entirely sure I see the value Of producing a name… the… Like, telemetry capture point.
**Josh Suereth (Google LLC)** 12:10 So… One thing I want to add here, just to… so we understand where we're both coming from, Krajo's, you're Prometheus, and Prometheus is a product, you are a backend, you have to discuss, like, you need that as a decision.
OpenTelemetry is back-end agnostic, and so we have, like, best practices, and we're trying to give you the best out-of-the-box experience, but if you want to diverge, you can. So if you take that as the principle here, I think, Daniel, what you were saying was.
We could provide a default somewhere for you to use, right? That we would recommend for Prometheus, and Prometheus could just pick that up and use it for their product. And we would call that, like, the default experience that we think is good.
But… but, you know, two things would be true. One is, people don't have to use that. It's just we're going to recommend it. Eventually, people will probably standardize great. Second, we don't think we want to send it over OTLP. Like, it, like, that's… I think the main theme here is, like, we don't want it in the protocol itself.
There's a lot of things in the protocol itself I think would be better outside of the protocol for efficiency reasons, like sending unit and descriptions and stuff every single, you know, time we call and make metric calls in OTLP, they're included. And they have to be right now, because we have no other way of communicating them. But as part of this entity's work, we're looking for a way to communicate that data outside of the OTLP channel.
And so that's where we'd want this to live and be.
And so… Okay.
Yeah.
**Daniel Dyla (Dynatrace LLC)** 13:45 I, I have a different… I… I… when you… when you mentioned krajo is from Prometheus, that triggered something different in my… am I… So… Prometheus probably doesn't want to maintain a big mapping of types to names.
I would say we should provide… to me, I think we should… provide guidance that the ID, like, the type encodes the name with some, you know, just provide, like, humanization rules, or whatever it's called. So if it's, like.
host is the entity type, you know, maybe host is a bad example. Something with multiple words, right, that's separated by underscores, just like… Title case it, and use that as the display name by default.
**Josh Suereth (Google LLC)** 14:36 I think it can be really dead simple, too. Like, take the entity type, use the name if it exists, if it doesn't, use the ID.
**Daniel Dyla (Dynatrace LLC)** 14:45 Yeah, exactly.
**krajo Krajcsovits** 14:48 So, yeah, that's what kind of what I arrived at. Looking at the examples on the Entities page, I see that you actually put in, you know, host.name.
Kates.node.name. So basically.
all the examples have this name, so that is why I wrote it's very tempting to… for probably to just take that, and if… and if it's not there, then we'll pick the first one, and we'll have to let the user pick any attribute to filter on anyway, because they might… they might not want to filter on the name. They might want to filter on something else. But we need to pick something first that makes kind of sense.
So… Yeah, I mean… Especially since you put this name into all the examples, it is… probable that most people will do something like this, and will probably have the name. So I can live with that. And… I understand you don't want to have a dedicated place in OTR before that, that's fair. It could be very redundant, very fast.
So… Yeah, I think as a first approach, I can… I can live with that, and then we can… Maybe have a… Some side channel that… that gives us… more information. I mean, eventually we'll want to, you know, Cash and use the… Semantic conventions and the schema.
Yep. For transformations on the fly in the queries and stuff, so we will have a place for… for this kind of information as well, probably.
But yeah, this is good enough for now. Thank you.
**Josh Suereth (Google LLC)** 16:31 I am thinking we can put it in the semantic conventions long-term, too. Like, we can… so we could have a better… like, if the default that you choose isn't… isn't great, we think there's a better one.
we could have a, like, two-string annotation in semantic invention that says, here's how you can make display names, and then if you're already consuming and interacting with them, you can leverage that, you know, for, like, how I display things.
It's still, you know, there's still this whole, like, how do I consume the schema URLs, and ingest them, and make them serveable, and fast, and all that kind of crap. So it's not, you know, what's the… when you have a hammer, everything looks like a nail, right? When you're a semantic conventions maintainer, everything looks like semantic conventions config. I don't necessarily want that to be the case here, but yeah, let's work together, you know?
**krajo Krajcsovits** 17:23 Yeah, I mean, to be fair, in the first iteration, we would just store the URL, or some other conversions and serve it.
Because, obviously, we are not going to start, you know.
Synchronously tried to fetch it during ingestion, so that it has to be Kind of an add-on later.
And then, yeah.
Cool.
**Josh Suereth (Google LLC)** 17:48 Yeah.
Okay, cool.
That was an awesome discussion. I think the only other topic we have is just going through the latest spec. So, Dimitri's on vacation for quite some time, I think? Like, 2 weeks or something?
So I'm expecting not a ton of collector work to get done.
But just wanted to call out, Daniel, I think you updated your PR? I didn't have a chance to get to it… yet.
Is there anything you want to call out here?
**Daniel Dyla (Dynatrace LLC)** 18:20 No, I just did exactly, what we talked about, so instead of having a separate entity detector, it's now a resource detector, I called it an entity-aware resource detector.
My… it's not a new technical name, Entity Aware, that's just the… what I used in the pros, I guess.
I have not yet updated my prototype to match this model, but, I mean, there's nothing about the entity detector that Prevents us from just smashing two pieces of clay together and saying, here's this thing.
**Josh Suereth (Google LLC)** 19:00 Yeah, yeah.
And we do have… we do have a prototype in Java you can use, actually.
If you want to grab the Java one. It's like a combination of Jack and I. I did a bunch of work, and then he hates how I write Java, which I don't mind, because I don't think… I hate the way I write Java, too. So he went and fixed it all up and made it look prettier, and that's the current prototype.
let's, let me open up the other one, because I made a few updates from, like, Jack's comments. So Jack opened a PR… oh, he approved already. Jack had a PR that was, trying to fix up some of the configuration for resource, so we agreed to merge everything together, and I asked him if he wanted to merge mine into his, or he wanted me to merge his into mine, and he picked his into mine, so… more work here, but, the, the TLDR, I think we talked about this last week, there's an OTEL Experiments… OTEL Experimental Entities Enabled config flag.
That would be an end variable, and we are adding this into… config. So there's also a PR that Jack has on the config repo for the same thing. I'll go find a link and put it there. This would enable the entity-aware resource detectors.
And then the… the link that you have, Daniel, We have a… in Resource SDK, where it talks about the specific, like, resource named resource detectors. We update them… no, we update them to just say they populate the particular container entity with a link to SemConf.
on that.
By the way, this link might break and change with the latest SimConv. I'll… We're changing around how registry works, to be, namespace, so instead of Registry Entities Container, it'll be registry containers, Registry container, and then Entities.
Just so everything's namespaced at forward.
Anyway, we can fix that later in case you notice a breakage. But it just says that, and then this line is consistent everywhere, where we populate the entity or all relevant attributes of the entity if entity support is not included yet. This is so that we can kind of stabilize the named resource detectors in the spec for folks.
For context, this part of the specification is not considered stable yet.
The named resource detectors. That came in with configuration, and since configuration hasn't fully stabilized everywhere.
certain pieces haven't stabilized, this is not stable spec, this is still experimental.
Okay.
The other thing is Dimitri's concerns here around this end propagation.
The idea we have here is that you specify an env detector. When you specify the env detector, that means that we use OTEL Entities as a propagation technique for your resource identity. So if you specify in config that you're going to use environment variables.
then it looks at OTL Entities. If you don't specify it in config, it doesn't read the environment variable, you only get what you've hard-coded.
Right?
Dimitri has concerns about how we're going to make this work with OTIL resource attributes.
and what that means, if this is default on. I'd like to consider this out of scope for this PR, and just something we're going to address with further spec work, because I think that specification lives elsewhere.
But I wanted to run that by the SIG quick.
**Daniel Dyla (Dynatrace LLC)** 22:38 I guess I'm not entirely sure that I… is it a prioritization concern? Like, which attribute wins if you define it at both places?
**Josh Suereth (Google LLC)** 22:49 What I want to propose, and what the spec currently reads as, is LTEL resource attributes occurs in the same place it happens today, which is outside of the scope of configuration.
It's literally just hard-coded that we use OTEL resource attributes.
in resource detection. It's just, like, a mandatory part of the spec somewhere.
So what would happen in this world is actually, as specified.
ENV would always happen before OTEL resource attributes, because of the way the spec uses resource detectors. OTel resource attributes always happen after your configured resource detectors in the spec.
**Daniel Dyla (Dynatrace LLC)** 23:29 You're fine.
**Josh Suereth (Google LLC)** 23:30 read it correctly. If you want, I can expand this and we can look at the details.
Cause I, I might be misremembering.
But… Yeah.
**Daniel Dyla (Dynatrace LLC)** 23:43 No, I think I understand the concern, like, the specific details are not, I think, important right now.
Well…
**Josh Suereth (Google LLC)** 23:51 Are we willing to make a break and change to it? Go ahead, Kelly.
**Michele Mancioppi (Dash0 Inc.)** 23:55 Because I have used auto-resist attributes to override the DM detector. Are you sure it happens before?
**Josh Suereth (Google LLC)** 24:04 No, hotel resource attributes happens after all of the resource detectors.
**Michele Mancioppi (Dash0 Inc.)** 24:08 Good.
**Josh Suereth (Google LLC)** 24:09 Yeah, yeah.
What we could do is we could have something to disable it.
But again, I don't think there's any way to reconcile these two without making a breaking change to a stable part of the spec about resource detector attributes.
**Michele Mancioppi (Dash0 Inc.)** 24:27 No, I think that the contract is… resource attributes go last.
So, I would resolve all the entities before resource attributes.
**Josh Suereth (Google LLC)** 24:36 Which is what we would currently have here. So, N will happen first, and then outside racist attributes are next.
**Michele Mancioppi (Dash0 Inc.)** 24:42 You also mentioned another environment variable, auto underscore Entities.
**Josh Suereth (Google LLC)** 24:47 Yeah.
**Daniel Dyla (Dynatrace LLC)** 24:48 Yeah, that comes from the EMV detector.
**Josh Suereth (Google LLC)** 24:51 you have to configure an environment detector, and that will use OTEL Entities.
And the order that you pick in your config determines where that happens. Otherwise, you don't get OTL Entities.
**Daniel Dyla (Dynatrace LLC)** 25:01 Yeah, I think that's fine.
**Michele Mancioppi (Dash0 Inc.)** 25:03 Yes.
**Josh Suereth (Google LLC)** 25:04 Yeah.
**Daniel Dyla (Dynatrace LLC)** 25:04 And then you can use OTEL resource attributes That apply after all the detectors to override certain attributes if you need to. Right. And if you overwrite something that's in an entity, don't do that, you know? Right. Open doors before you walk through them.
**Josh Suereth (Google LLC)** 25:21 Dimitri's concern is around migration, how about how we won't get people to stop using hotel resource attributes and start using hotel entities?
**Daniel Dyla (Dynatrace LLC)** 25:32 I think it will become… I'm not sure we need to make people stop, I think.
**Michele Mancioppi (Dash0 Inc.)** 25:38 if…
**Daniel Dyla (Dynatrace LLC)** 25:38 If there's compelling reasons to use entities, they will.
And if they're getting along just fine with using hotel resource attributes, like, do we.
**Josh Suereth (Google LLC)** 25:48 Continue.
**Daniel Dyla (Dynatrace LLC)** 25:49 care to stop them? Like, if they're getting what they need out of it.
**Josh Suereth (Google LLC)** 25:54 Yeah, I think that.
**Daniel Dyla (Dynatrace LLC)** 25:56 Like, their back-end vendor may tell them, like, hey, you should do this because you'll get better, you know, views or whatever, like, that any given vendor may… may give their customers whatever carrots they want to, to switch, but as OTEL, as a project, like, do we care if people switch?
**Michele Mancioppi (Dash0 Inc.)** 26:16 Hey, I think…
**Josh Suereth (Google LLC)** 26:18 We shouldn't care, no. There's a few things that we're gonna… planning to do here that would be nice if people can interact with it, but again, if they're already using no-tail resource attributes, they're already self-servicing. Like, we don't care when they move.
**Daniel Dyla (Dynatrace LLC)** 26:30 Yeah, and I would just call that, like, a last resort escape hatch, like, in the documentation, documented as, like, a, if you absolutely must override something that came from your earlier config, here's how you do it, which is how it works today anyways, so that's not breaking, it's just a… Reframing of the prose.
And then, you know, We put in the documentation entities as the expected happy path.
Anything that's already working continues to work.
And new users, when they onboard, they will read the docs and do what we tell them to do, most likely.
**Michele Mancioppi (Dash0 Inc.)** 27:12 But also, do we really believe that every resource attribute is going to be part of an entity?
Because I don't.
**Josh Suereth (Google LLC)** 27:20 a pure resource attribute? I… I… I don't think… I don't think so. I think you're gonna decide whether you're an entity or not, and move it.
If it makes sense. Like, there are things… so, like, the OTEL, operator today is throwing in all the Kubernetes IDs. I think that can move to OTEL Entities, and it can specifically say, I'm a Cates container, I'm whatever. That… that's kind of the thing I want to change. I actually want, in GCP, I want us to do this by default, like, I want to encourage teams now to say, cool, we will give you an end variable of OTL Entities that gives you your ID, so you don't have to write a detector, you can just use env, right? Great. I think that makes sense, but where users are using it to add in their own crap.
I… it might not be an entity, you know, and it's a label, yeah.
So…
**Michele Mancioppi (Dash0 Inc.)** 28:07 Technically, you could do all the injection of the IDs yourself right now with resource attributes instead of auto entities. There is a… the injector is actually doing that by looking up some environment variables for the pod UID, for example, on Kubernetes.
**Josh Suereth (Google LLC)** 28:22 Yes.
But the… we do want them to move to OTL Entities just so that we don't get the schema URL conflict. I'll walk into that in a second, because that's actually, I didn't add this on the agenda, but I… we need to talk through it. There's an, Yeah, if you're not aware with the resource merge algorithm.
The way it's specified, no SDK implements except Python, and Go used to implement it that way and deviated from the spec on purpose, the way everyone else did. If you implement the specification as designed for resource attributes.
you drop resource attributes all the time, and it just doesn't work for users. That's one of the reasons the SIG exists. Like, it's literally a broken specification.
And I need to show you a comment thread that Robert and I had on this, and some… some thoughts there, but, schema URL and resource is 100% broken today. So, that's why this gives us a schema URL that we can use to do, like, compliance testing with Weaver and that sort of thing. This one does, and that's okay, it's just, it can never be validated. Yeah.
**Michele Mancioppi (Dash0 Inc.)** 29:29 Okay, take a step back. You're talking about the, resource schema, right? Resource schema version.
**Josh Suereth (Google LLC)** 29:34 I'm talking about resource schema version, yeah.
**Michele Mancioppi (Dash0 Inc.)** 29:37 What is broken about it? What happens is…
**Josh Suereth (Google LLC)** 29:40 If you… if you specify this.
and someone specified something with a resource schema version, technically, if you read the spec in the way that things work today, you would reject all the attributes.
In very… like, there's ways that you can reject all attributes, it's kind of awkward as hell.
I'll show you in a second, there's a bug open about it. So… Nobody's actually doing that because it's stupid and impractical. Except for Python, which implemented the spec exactly as written, and Go used to implement the spec exactly as written, and then had a bunch of users complain about it and then fix it.
So, we need to fix the spec, and Entities is meant to fix the spec, because the whole resource schema URL disappears, and only Entities have schema URL.
And so if you throw on raw attributes, these are schema-less, by default. We don't know what the schema is, so you can't, like, validate them, they're just extra, right? Whereas OTL Entities have schema on everything, and if you don't specify one.
we assume that you're in conflict with anything that is the same type with a different schema, right? It's because we know that you would have one.
Anyway, okay. I'll show that in a second, just, just so that you know.
Daniel, to finish where we started with this, NC wire resource detectors are called out here. The thing that Jack wants to do, and this is what we should talk about, is how the SDK is responsible for stripping NC information from a resource detector Before we give them to a provider.
In… if, this is not set to true. So, the idea here being that we can update resource detectors with entities in a non-breaking way.
They all get updated. If the user opts in, the SDK is responsible for getting rid of them so they don't show up in OTLP.
If the opt-in is true, then entities start showing up. But we can update the code without breaking users, because they can decide whether or not they have entities. I think this has implications on merge and things, but I just wanted to run this by you. This is… this is the phrasing, so please.
**Daniel Dyla (Dynatrace LLC)** 31:43 Amazon.
if we're doing this, what was the… what was the reason to make it all backwards compatible in the first place? Like, we jumped through a lot of hoops to make the whole thing backwards compatible. Why do we need to do this? Why can't we just commit them?
**Josh Suereth (Google LLC)** 31:58 So, Splunk doesn't think that we are… not Splunk, I should say Robert doesn't think we are backwards compatible.
And I'll, I'll show you that.
**Daniel Dyla (Dynatrace LLC)** 32:09 So, if we're not backwards compatible.
Personally, I would rather be completely not backwards compatible. Like, the data model could be a lot less convoluted if we're gonna call it breaking.
I thought that that was, like, the whole reason we did that.
**Josh Suereth (Google LLC)** 32:29 Yes, and I think we are backwards compatible for prac- practically. Let me see if I can find this resource.
URL… I forget who opened it. Oh, resource merger, here it is. This is the Go issue, right? So this is the issue. We pulled this into Entities SIG back then, April 2023, right? This is the merge algorithm that's problematic.
And just some examples of, like, deviations, right?
Java always warned on the spec issue and never actually implemented it. Erlang warned Python actually errors and returns an old resource that doesn't merge.NET, C++, and Ruby did look into, but if I recall correctly, none of them actually Follow the spec there. Go actually returned an error, users complained, and they updated it, and JavaScript also didn't really support this, and then merged resource without schema returned. Like, this was the previous schema URL issue.
**Daniel Dyla (Dynatrace LLC)** 33:35 Didn't support what? Like, hold on. Didn't support…
**Josh Suereth (Google LLC)** 33:40 didn't support, this particular part of the spec. So, if the old resources schema URL is empty, then the resulting resources schema URL is empty.
or we set the schema URL the updating resource. If the updating resource URL is empty, then the resulting schema URL will be the original schema URL. This is the problematic one.
Oh yeah, if the schema URL of the old and the opt-in resources are the same, you can merge. This was… if you have two different schema URLs.
It's considered a merging error. Like, if one's not empty, you would consider it a merge error, and you would issue a merge, and the resulting resource is undefined, and its contents are implementation-specific.
**Daniel Dyla (Dynatrace LLC)** 34:25 Okay.
**Josh Suereth (Google LLC)** 34:26 You're supposed to actually issue an error.
Basically, people issued warnings.
they would actually return an empty resource and go, and, like, consider it a complete failure, which is problematic. For context, how this happens, if I have… if I'm using semantic conventions, and I have a schema URL, and I have a resource detector defined.
And that resource detector is in library A, and then I have another resource detector in library B.
And now my semantic convention version differs, and the schema URL is different. Suddenly, things that used to work no longer work, because I updated. It's like, it's terrible.
Doesn't necessarily make a lot of sense, and that's why, you know, we're changing this. So, the proposal here was update the merge strategy to have the SDK upgrade downgrade resource in the process of merging. We decided we can't do that, because that means every single SDK has to have access to schema URL and all the Semantic convention stuff, and that's just impractical.
Add additional recommendations. So you can see there's a back and forth between Robert and I. He came up with a proposal for how to fix this.
Where he shows the current behavior of everyone and what they do. Oh, right, Ruby and Swift don't support schema URL, returns a merged attribute with no schema URL, no diagnostics in Rusts, JavaScript admits a warning and returns normally merge, etc, etc. You can see the behaviors of all the No. Robert was not a fan of our… current entity prototype, because he considers it a breaking change. So he and I had a, a discussion here.
He wants to resolve the issue by specifying merge attributes plus empty resource URL as preferred, recovery behavior, keeping diagnostic language specific, blah blah blah blah blah. Basically, from what I understand, there's a, like.
he has concerns about some Splunk-specific SDK that sets resource URL, and I think in our merge algorithm.
we would actually remove the schema URL, And he wants to keep it.
is the TLDR, of, like, the effective behavior.
and we're trying to figure out the principles behind this, but our current merge algorithm, if you read the spec, I consider it non-breaky.
Because we say the behavior's undefined. Where was it?
The resulting resource is undefined and its contents are implementation-specific, right?
**Michele Mancioppi (Dash0 Inc.)** 36:57 Oh, wait a second. Resulting resources undefined is different than the scheme is undefined.
I read that as the resulting resource doesn't exist, nothing is returned.
**Daniel Dyla (Dynatrace LLC)** 37:07 Yeah, I read this as there is no definition for what should happen.
undefined behavior in the C compiler sense.
**Josh Suereth (Google LLC)** 37:15 Just means you do whatever.
Yeah.
**Daniel Dyla (Dynatrace LLC)** 37:19 Not… not undefined in the JavaScript sense. Undefined in the C compiler sense.
**Josh Suereth (Google LLC)** 37:24 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 37:25 Notify me.
**Josh Suereth (Google LLC)** 37:26 Here, not undefined, yeah. So basically, there's no definition here.
But the proposal here from Robert is, where was it? Right.
he said there's two ways we can treat an empty schema URL, right? We can either treat it as an unknown schema, or I don't care and I'm safe to merge as a schema.
And… You know, my… my… Stance here is the only safe thing to do is to always treat empty schema as unknown. We don't know what the schema is. Like, there is a schema, someone just didn't bother to write it down.
And so…
**Daniel Dyla (Dynatrace LLC)** 38:07 Otherwise, you would never put it in the… Yeah. Even if the contract is implicit, you would never insert data if you didn't have some idea of what it was.
**Josh Suereth (Google LLC)** 38:15 Right, so to me, the failure scenario is if we start building out, like, Weaver compliance testing that uses schema URL.
Right?
and someone is using OTEL resource attributes or something with empty schema URLs.
and I pretend like it's SEMCOM, and then you get a whole bunch of warnings about attributes that don't exist, that's a worse experience. Then I say, oh.
you don't have a schema URL here for your schema. If you define one, I'll validate it. Otherwise, I can't validate this as a warning instead of an error.
Right? So, that's why I would prefer… like, I think the absence of a schema URL means I didn't bother to write it down. If I merge something that has one and something that doesn't, I remove it, because I don't know what the result means. And I don't want automatic compliance tests to be broken. That's my proposal.
Robert's not a fan of that, he's gonna open some tickets for us to talk through and change, and you can read, like, our thoughts here in this thread. I'll put this in the notes. But feel free to take a look.
Standard.
**Daniel Dyla (Dynatrace LLC)** 39:18 Okay.
**Josh Suereth (Google LLC)** 39:19 Yeah, there's, like, some links and stuff. You can see our conversation on the Entity SDK PR, which is now merged because he decided not to block it, and Tigrin approved it. But, yeah, like.
I think we're gonna have to resolve this, and what I want to make sure of is that we get some principles around what's important.
I don't think the important thing is keeping a schema URL that's invalid. I think the important thing is giving someone a schema URL they can use for automated validation, if they care, and if they don't, like, if they have decided not to care about schema URL, not write it down.
don't make the automated validation, yell at them for that, or yell at them for the attributes, make them yell at them for not having a schema your own. You know, like, hey, you want automated validation? Write your schema down, we'll validate. Otherwise… You know, don't.
Go ahead.
**Michele Mancioppi (Dash0 Inc.)** 40:12 At the risk of causing a tangent of infinite length.
Why don't we get rid of the schema URL at all?
**Josh Suereth (Google LLC)** 40:22 Why do we get rid of it?
**Michele Mancioppi (Dash0 Inc.)** 40:24 Yeah.
Because my point is, the, the schema URL, I always thought it was at the wrong level.
It's, in, in proto, it's at the level of the resource, where in reality, for me, it's at the level of the attribute, because in my resource, I may want to mix any numbers of schema, which is precisely the whole point of Weaver.
**Josh Suereth (Google LLC)** 40:47 Yeah.
So, that's… that's… we… we with entities are going to deprecate schema URL at resource.
In the long run. We have a new schema URL that is at the entity level, so I can say this set of attributes is a schema.
**Michele Mancioppi (Dash0 Inc.)** 41:02 Yes.
**Josh Suereth (Google LLC)** 41:03 And that's why, like, from my perspective, Schemia Outlet Resource is just best effort. Of, let's give people a decent experience if they're still using it.
But let's… but we don't have to go much further than that.
**Michele Mancioppi (Dash0 Inc.)** 41:18 Or, we say… Don't care. I leave it entirely undefined. That thing is gonna go away from the proto.
It's gonna be super mega legacy, then use this.
**Josh Suereth (Google LLC)** 41:31 I'm personally okay with that, but I know that Tigrin asked us to try to do best effort to keep it, and we have an algorithm we defined that he approved that I think keeps it around if it can be the same, and gets rid of it if it can't be, and I think that's a reasonable thing. It's not hard for us to do. We can still deprecate and get rid of it, and then it's not a big deal later, long-term.
But in the interim, it's still there.
**krajo Krajcsovits** 41:57 But, sorry, so… If I understand correctly.
you're suggesting we are kind of migrating away from the resource level schema to entity, That little schema, but… I haven't seen that in the… in the… Hmm… in the spec yet. That's… that's coming, right? Or…
**Daniel Dyla (Dynatrace LLC)** 42:19 It's in the data model spec.
**Josh Suereth (Google LLC)** 42:21 Yeah, here, I'll show you.
If you look, this… because, again, we took… we took so long to get this through.
But in the data model spec, we have, Where's the merge algorithm? We have a schema URL in here.
Yeah.
So we talk about schema URL in Entities, and we talk about how to merge with schema URL. We give you some examples, but I think that's actually the one call-out for.
**Daniel Dyla (Dynatrace LLC)** 42:49 I think there's, like, a definition of entity that has, like, ID… it's, like, the first… table there.
**Josh Suereth (Google LLC)** 42:56 Yeah, I don't know.
**Daniel Dyla (Dynatrace LLC)** 42:57 No, it should be in there.
**krajo Krajcsovits** 43:00 Yeah, that's what I was referring to, because, I mean, again, some people are quite excited about the schema for Prometus to be able to, you know, migrate metrics.
which is always the biggest pain in the ass to migrate something. And I know, like, Bartek and… what was it? Somebody else as well, was, you know, doing even, prototypes with it. So… I mean, I'm not going to, you know, lose sleep over not having to support something, but, like, it would be pretty nice to have.
**Josh Suereth (Google LLC)** 43:34 Yeah, we call it out the data model, because, again, if you look, if you look, where is it? Here, common… Our Entities are here, yeah.
**Daniel Dyla (Dynatrace LLC)** 43:43 Yeah, it's definitely in the proto.
**Josh Suereth (Google LLC)** 43:45 The proto has it.
**Daniel Dyla (Dynatrace LLC)** 43:47 Yeah, and it should be in the table on that Markdown file, just as a… I would have expected it to be there.
**krajo Krajcsovits** 43:54 I can open a PR. I've been opening PRs on the Prometus Auto compatibility anyway, so…
**Daniel Dyla (Dynatrace LLC)** 44:02 My point, and, like, I don't know, Josh just said this took forever to get through, and he was right, and I… I almost feel like I shouldn't say this, but… If we're going to have some, like, experimental opt-in attribute, Why would we not go… Whole hog with it, and have a separate top-level Entities field.
And the attribute would be… opt-in, like, the same way we do the SEMCOMP migrations, you would have an opt-in attribute that double emits.
And then, in version… the next major version, you would change the default behavior, And… Like, then we deprecate.
Over time.
**Josh Suereth (Google LLC)** 44:44 OTEL owns everything.
That's reasonable. But where there are backends that consume the data.
The opt-in attribute for entities would, like, change resource to be entity aware, but any system that's still resource like, non-Entity aware, still works.
With the way we've done this, right?
**Daniel Dyla (Dynatrace LLC)** 45:05 what the double emit would be. If you detect all the entities, the double emit would just scrape all those attributes and copy them into the resource.
It would be inefficient, and that's why you would want to eventually fully migrate, but you would have that, escape hatch there, and probably you would want to… have that ability long-term. Like, we may have… you know, some component that could do it, or, you know, I'm not sure, some ability to… to say, I'm not migrating everything.
But just double omit it, and… Copy it all into resource, and say, this is… if you don't like this inefficiency, you should upgrade your path.
**Josh Suereth (Google LLC)** 45:54 I mean, yeah, I…
**Daniel Dyla (Dynatrace LLC)** 46:00 That obviously goes… it walks us back, like, two and a half years, so…
**Josh Suereth (Google LLC)** 46:05 It does welcome back two and a half years. I do think we should start Keep going with the experiment where we are today, and we should make decisions on that based on what we find from, like, size.
And, and, protocol issues, I'm still worried what we have today is too large, proto-wise, and too, like, too expensive a payload cost for what we have today. And we went with something kind of in the middle.
So, like, what you're suggesting, I think, is entirely too much.
To… it's gonna bloat things. Like, when we… when we're talking to profiling, it's… it's apparent we… I think we need to spend more of a performance effort on our… Our protocol and how we send things. Because if… yeah. Anyway.
I'll leave it there, just that our protocol is rather inefficient. It's starting to show up in certain cases. I really don't want to say, shove all this data two places, and ignore it if you want to ignore it, you know what I mean?
And I also don't think it's practical for us to say, hey, every backend that exists.
you can't be used anymore if someone's using entities. I think that's… that's broken in a different way, right? What we want instead is… is a path where we can start migrating people to be entity aware, As they find value in entities.
You know? So, don't break them. Let them use the Entity Aware resource detectors. All the OpenTelemetry things can leverage the data and do intelligent things with it. The backend doesn't need it, doesn't care. Just keeps progressing as it did today. It still gets a bundle of resource attributes, it still uses them. Backend wants to engage with entities, it gets better data.
It knows more.
You know?
But it gives us a compliance regime for instrumentation, because with with entity-aware resources, we can actually do compliance on resource, because we can look at bundles of attributes instead of all of them, right? So it gives us a path forward for a lot of things we need to do.
If we want to say something is, like, hotel compatible, or hotel native, or whatever.
So, I'd rather focus on, like, the set of problems we have in front of us. This, like, how do I preserve schema URL? As far as I know, I think only Splunk uses schema URL from resource at all, because everyone else decided it wasn't reasonable, because it's so horribly broken, including Weaver. Like, we… We actively aren't using schema URL to enforce attributes in Weaver because it's broken.
Instead, we make the user tell us what the schema is, and we enforce it kind of completely independently of what's in OTLP.
**Daniel Dyla (Dynatrace LLC)** 48:52 So, why don't we then… Wouldn't it be… it fixes the backwards compatibility concern if we… Don't… change anything with the resource level schema URL, right? If we say, if you're doing something with this already, continue doing what you're doing, whether that's a good idea or not is up to, you know, that's between you and your deity of choice.
And the schema URLs in the entity We will make assertions about those.
Because that's new from whole cloth, so it… Doesn't need backwards compatibility.
**Josh Suereth (Google LLC)** 49:33 I see, so basically we say, like, Weaver, for example, won't interact with Schema URL and Resource.
**Daniel Dyla (Dynatrace LLC)** 49:38 Yeah, essentially just won't… we'll pass it through in the collector if we see it there, but, like, we're not gonna do anything special with it.
**Josh Suereth (Google LLC)** 49:46 And we could probably make a call out about, hey, this is the algorithm that's used for schema URL. We can get rid of the thing about dropping the resource completely, because that's horribly broken.
**Daniel Dyla (Dynatrace LLC)** 49:55 Yeah, and nobody does it anyway. Well, not nobody, but…
**Josh Suereth (Google LLC)** 49:59 Well, nobody… it's undefined behavior, so everyone defined similar behavior, because that's what makes sense.
**Daniel Dyla (Dynatrace LLC)** 50:06 And there will always be people that want to just tack on a resource attribute, because they're trying to tag something with, like, you know, Team A, and they just want that to be there. They don't care about the entity that it's in, or the schema, or anything like that. They just want to be able to filter their backend.
**Josh Suereth (Google LLC)** 50:22 And that should be allowed, and it shouldn't ding you when you do a compliance test in Weave or LiveCheck, right?
**Daniel Dyla (Dynatrace LLC)** 50:28 Yeah, and I would say the schema URL is just…
**Josh Suereth (Google LLC)** 50:30 Cheer.
**Daniel Dyla (Dynatrace LLC)** 50:32 like, it was never that useful to begin with. That's why there was… that's why you went through the whole schema V2 thing, was because the old schema URL was just not working for what people needed it to do.
**Josh Suereth (Google LLC)** 50:44 Yeah, we couldn't implement tooling around it, yep. Okay, so… maybe we can make some comments on here, and when Robert gets back, he's on a forced holiday, but when he's back, We can talk… we can flesh this out, but if someone wants to write that down… By the way, your comments on the PR, like my PR and everything, please get those in GitHub.
But for next steps for the schema URL thing.
why don't we make our plan of record to be… we can keep the previous behavior, we can update the merge algorithm to say it keeps the previous behavior, but we'll also update the documentation to say, ignore schema URL at the resource level. Like, this is what it does, but we don't think it's useful, and it exists for backwards compatibility only.
And so use entity-level schema URL.
Yeah.
**Daniel Dyla (Dynatrace LLC)** 51:37 I agree.
**Josh Suereth (Google LLC)** 51:38 Okay, go ahead.
**Daniel Dyla (Dynatrace LLC)** 51:39 Let's make sure to document all this, because we… nobody can access recordings right now.
**Josh Suereth (Google LLC)** 51:45 Oh, that's true. Okay.
**Daniel Dyla (Dynatrace LLC)** 51:48 I think you can get them from the CNCF if you send an email. You have to have, like.
a TC member email CNCF to get a recording for you.
**Josh Suereth (Google LLC)** 51:58 Oh, that's fun. Yeah.
**krajo Krajcsovits** 52:03 Yeah, indeed.
**Daniel Dyla (Dynatrace LLC)** 52:04 Oh, you wanna say something?
**krajo Krajcsovits** 52:05 Yeah, I wanted to ask two things. Like, one of them is that I very optimistically wrote in the… in our native metadata design doc, you know, we'll just have the semantic convention URL, That was the input I got from somebody. And then I realized that, wait a minute, the protocol doesn't have it, it only has the schema.
For resource and scope.
But what I'm hearing is that I shouldn't bother with… with the resource.
Level, actually.
And also… like, the real, deal will be V2. And when you say V2, you mean the one where it's not only the changes, but the whole… Schema plus changes from the previous one, right?
**Daniel Dyla (Dynatrace LLC)** 52:54 When I say Schema V2, I mean Josh and others.
Did, like, a whole rewrite of the schema file definition and processing and merging and all of that stuff.
**Josh Suereth (Google LLC)** 53:10 Yeah, you can… Ludmilla's been driving the latest part of that, but you can look at, like, Laurent, he's also from LTel Arrow, if you're familiar with him, did an initial, like, diff merge algorithm for Weaver, where we can diff two schemas.
and, like, figure out what the differences are. But what we found was actually, if we just update the deprecation status of every single signal in SEMCONF, the deprecation status has a merge, a, sorry, a, transition block of, like, what you do. So, like, this is renamed from here, which means I just rename A to B to, like, merge to the thing. So, that is how we're actually planning to do a lot of these transitions.
**krajo Krajcsovits** 53:54 I'm sorry, I'm not looking for the transitions, I'm just… I was just asking if the V2 will… have… Like, all the information… That describes the semantic, meaning that the current schema URL just has the changes, but V2… so that OTAP is going to be in there, right?
**Josh Suereth (Google LLC)** 54:14 Yeah, yeah, have you seen the Ultra? If not, I'll get you the link, but it's… it's a… it was a full-up specification. I think it merged.
already. Let me take a quick look.
**krajo Krajcsovits** 54:26 Yeah, it was, I know I, I looked at…
**Josh Suereth (Google LLC)** 54:30 Yeah.
**krajo Krajcsovits** 54:31 Or some… 400-something, I don't know, I don't remember.
**Josh Suereth (Google LLC)** 54:35 It's, it's this one, 4E15, yeah. That's…
**krajo Krajcsovits** 54:40 Yep.
**Josh Suereth (Google LLC)** 54:40 Yeah, we, we, We have the publishing working for this. What I was working on recently, and the latest Weaver resolver does, is resolving dependencies across schemas, and then handling, like, version conflicts and all that kind of crap, so… I can go into, like, the nitty-gritty detail of what we've been doing.
**krajo Krajcsovits** 55:01 No, no, no, I don't… I just wanted to make sure that we're talking about the same thing, but yeah, okay, thank you.
**Josh Suereth (Google LLC)** 55:06 the, the 2.X… series of schema URL will have all the definition in the schema URL, not just the diffs, yep.
So all your entities will be in there, too. Okay, I think we're out of time. We have a set of action items here. That was a good discussion.
So, Daniel, I'll review your PR, please review mine and make comments, and we'll see if we can get those in. FYI, I'm on vacation starting tonight through Friday, so I probably won't get a lot done until next Monday, but I promise to, like, look at GitHub comments every once in a while.
**Daniel Dyla (Dynatrace LLC)** 55:47 I was supposed to be out all this week, and I'm not entirely sure. On any given day, I might be gone.
**Josh Suereth (Google LLC)** 55:53 Okay.
**Daniel Dyla (Dynatrace LLC)** 55:54 I'll be back next week.
**Josh Suereth (Google LLC)** 55:57 Okay.
Cool.
Then if you can make those comments today, that'd be great. Alright.
**Daniel Dyla (Dynatrace LLC)** 56:03 Okay.
**Josh Suereth (Google LLC)** 56:04 I'll see you guys all later.
**krajo Krajcsovits** 56:06 Okay, my bad.
