SIG: Policies SIG
Date: 2026-11-23
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Jacob Aronoff (Cribl)** 00:35 Hey, Jack, how are you?
**Jack Shirazi** 00:38 I'm good, how are you?
**Jacob Aronoff (Cribl)** 00:40 I'm doing alright. It's a beautiful day here in New York City, so nothing to complain about.
**Jack Shirazi** 00:46 Oh, well, it's sunny here in London, but, cold.
**Jacob Aronoff (Cribl)** 00:51 Yeah, same here, but… I, I do like the cold. I yearn for the cold, so… That is, like… I always look forward to it every year.
**Jack Shirazi** 01:06 It gets… Colder where you are than where you are.
**Jacob Aronoff (Cribl)** 01:12 Yeah.
Let's see, I think… I think, Josh can't join, but I think David should be able to.
**Jack Shirazi** 01:22 No, he sent a message, I think, on the channel, just saying he couldn't join.
**Jacob Aronoff (Cribl)** 01:26 Oh, no! Oh, bummer, bummer.
There's really only one thing that I wanted to talk about today, let me, The agenda set here… Hmm…
**Jack Shirazi** 02:45 Yeah, you were gonna add something to the event.
**Jacob Aronoff (Cribl)** 02:47 Yeah, I was just finding the PR. Stateless… second… I'll call it a post-transformation filter.
So, yeah, but basically, if you want to pull up this PR check… I don't know if you've read through this already, or if… David had mentioned this to you.
**Jack Shirazi** 03:23 I haven't looked at this one.
**Jacob Aronoff (Cribl)** 03:24 So, the idea that he had is that, basically, like, we should be able to run a second pass, filter after an initial transform.
And I had a few concerns about this.
So… He says that all transforms are run once per val.
There is no loop, log filter policy, transform policy, or separate definition types.
All transform matches are evaluated once against the pre-transformed record.
Oh, oh, I see why he needs… why this is the way that he wants to do this.
Oh, okay, this is a lot less controversial than I thought.
In my view, I was opposed to this because, I was going off of my previous… mode of, of doing this, where all… Transforms are… it's… it's a log policy, not a log filter policy, not a log transform policy. It's like, you put them all together.
But I now see what he's doing here. This is probably fine, and it makes sense. The reason for doing this is that, like, so previously, when I was defining a policy, you would be able to do something like, You would have the transform in the… you would have a filter and then a transform in the same, like, block?
And so it wouldn't make sense to be able to do a second pass filter, because anything that you would want a second-pass filter post-transform, you should know, going into the transform, that you're, you know, that you're going to filter that out eventually. In this case, what you're trying to do is… You don't have that guarantee anymore, because we've separated those definitions. And as a result, you want to be able to run a filter after you've… after transforms have run, to see that if any data has changed, then you are making the guarantee that the filter is accurate. Which I think is fine.
Can you transform, modify the record, reevaluate all…
**Jack Shirazi** 05:56 This is a separate policy, or it's part of the… Same filter policy.
**Jacob Aronoff (Cribl)** 06:01 It's part of the same filter policy. It's basically, whatever logic.
**Jack Shirazi** 06:06 Okay, to verify, verify. Gotcha.
**Jacob Aronoff (Cribl)** 06:09 Yeah, whatever logic we use for the initial filter pass, we then do again as a post-transform pass.
Which I think makes sense.
Let me just double-check what the protos are looking like.
To confirm that this is what I think it should be.
Yeah, I think this makes sense.
So, I think this is fun.
**Jack Shirazi** 07:00 Okay, I'll have a look afterwards.
I'm not going to be able to go through during the session.
**Jacob Aronoff (Cribl)** 07:06 Yeah, no worries. So that was one of them. Let's see… Then there's some safety stuff here.
That I can merge. I already reviewed this.
And then the enablement stuff, I think we're still working through. Jack, if you don't mind… oh, you did? Great, I just saw your comments.
**Jack Shirazi** 07:38 Oh, no kidding.
**Jacob Aronoff (Cribl)** 07:39 I was about to ask you if you could take a look.
**Jack Shirazi** 07:44 Yeah, the enablement, I've put the comment on the PR.
Cool. I just added a couple of items to the agenda. The first one, I saw that you… Discuss policy delivery.
in a… at KubeCon in a later session.
Yeah.
So this… So, one of the things with the OTEC was that we didn't have the definition of the policy And… in the policy.
And now we do.
Which is fine, that's an improvement, I think.
But we don't… we don't have a definition of… delivery structure.
So, for example, currently, my implementation says I'm gonna, go to the op-amp.
structure, and I'm gonna use the… the config map.
And we'll use a defined key to find the body.
I'll take the body of that… against that key, and I'll say that's where the… where the policies are And it'll be a policy list.
But that's just… a… a choice that I made.
There was a specific reason for making that choice, which is that if you… if you do it… if you do it that way, then the key… Allows you to have multiple different… Keys from different vendors without them colliding.
So… I would say that we… we probably need to define Whether that is the implementation method.
Because otherwise, there's no… there's no definition. There's… OpAMP doesn't give you this, right? So we have to decide.
Where the, the body is gonna be.
And how that's, how that's read and interpreted.
**Jacob Aronoff (Cribl)** 09:44 Totally agree. I think that that's pretty close to what my expectation was. I think we just have to decide on what the key structure should look like. One thing that I've always had with OpAmp that is frustrating is that there's no way to, like.
Specify a type of config that you are transferring, which is very frustrating to me.
So… we might have to get a little bit creative in the way that we specify op-amp usage, meaning that, like.
In the identifying attributes part of the op-amp message, we might want to say that we have some special Top-level key-value pair for… Defining the type of config that is being transferred, so that, a policy-aware backend knows that this is a policy-aware, implementation that you're talking to.
Right.
Meaning, like.
I think that what you said about the actual config body is mostly correct, and we just have to figure out those keys, but we need a way for a vendor to know that that is the key structure that it should send back.
Right. And so, in the op-amp agent-to-server message, we should just specify that this specific key-value pair, which is, like, typed and versioned in some way.
or, you know, has some constant and some version, will determine that this is the expected delivery mechanism using op-amp.
Right, such that… In the future, we can, like, change… if we need to change the semantics for whatever reason, we can do that.
**Jack Shirazi** 11:26 Okay, I just… I mean, we're agreeing that we need to specify that.
That's… and that's really the point I'm making here, more than… Actually deciding on the…
**Jacob Aronoff (Cribl)** 11:38 Huh.
**Jack Shirazi** 11:38 On the structure of the specification.
**Jacob Aronoff (Cribl)** 11:41 It's easier.
**Jack Shirazi** 11:41 And the quest… question for the other two… transport mechanisms that we support, which is the HTTP one.
Are we assuming that the body of the HTTP is purely… That is it, that is the… The set of policies.
**Jacob Aronoff (Cribl)** 12:00 Like, the body of the response?
**Jack Shirazi** 12:03 Yeah.
**Jacob Aronoff (Cribl)** 12:04 Yeah, I mean, in my mind, like, I don't know… how much people are gonna use just, like, a raw HTTP provider?
**Jack Shirazi** 12:14 They'll definitely use it for testing.
**Jacob Aronoff (Cribl)** 12:17 We're testing, for sure.
**Jack Shirazi** 12:18 Yeah.
**Jacob Aronoff (Cribl)** 12:21 Yeah, I mean, I had written, like, sort of a… Call it a minor… it's sort of like a… subset of features that OpAmp gives you.
For my HTTP version of this.
Where I just specified, like, you know, you should send some stuff about stats reporting, and the backend should be able to specify, Should be given some context about which implementation it's sending, which implementation it's getting messages from.
But… We might just need to specify, like, you know, add these headers to do this thing.
**Jack Shirazi** 13:01 I just took the body, and assumed that it's a… A set of policies.
**Jacob Aronoff (Cribl)** 13:07 Yeah, well, I think that on the response body, yes, but I think that we should maybe also say that the request contains Certain headers, or certain.
**Jack Shirazi** 13:18 Yep.
**Jacob Aronoff (Cribl)** 13:19 Request body payload.
**Jack Shirazi** 13:21 This is all stuff we need to specify.
Yeah. And funnily enough, The one that I had the most trouble over was the file.
Really? Because… Because… I have this problem where you could put in multiple different… Structures, data structures in there, in the file.
For example, you could put in protobuf and JSON.
And then deciding how that's interpreted.
And whether it's… it's… it's part of the same policy list, and… yeah. So… What I'm saying here, mostly, is that we've defined three delivery mechanisms. We should just define the structures that we expect those 3 delivery mechanisms to provide, and any additional, like you say, the metadata.
The headers and so on.
**Jacob Aronoff (Cribl)** 14:21 Yeah, I mean…
**Jack Shirazi** 14:22 It's consistent.
**Jacob Aronoff (Cribl)** 14:23 I agree. I can write up a PR for this, because I already have… I think most of that figured out, and I'll add it into this This proto-spec in this section.
For file, I think we should only accept JSON. Like, proto-files are, like, time… like, proto… like, serialized proto file… is not super common, and I don't expect a bunch of people to, like, be doing that. It's, like, kind of a pain in the ass to do that already, and I just don't think people are gonna do that.
**Jack Shirazi** 14:53 Yeah, but even, like, I mean, JSON is okay, but do we accept YAML? It's, you know, as an option, do we accept… I don't know, there's simpler structures than JSON as well.
Especially if we look at the most simplified Policy structure that we can accept, so…
**Jacob Aronoff (Cribl)** 15:12 Yeah.
I think JSON and… I think JSON is fine. I'm just thinking in terms of, like, language, in terms of, like, language support, JSON feels pretty… feels like the easiest thing, and YAML feels slightly harder.
**Jack Shirazi** 15:27 I agree.
Okay, I'm fine with Jason there.
I'm just trying to think, because the… in my examples, I've also implemented, support for just key-value pairs.
But…
**Jacob Aronoff (Cribl)** 15:46 So, this one.
**Jack Shirazi** 15:47 For my ones, that works, but for the outset, that worked.
Because you have to specify… the policy type.
it wasn't part of the policy. But now that the policy type is part of the policy, I'm not sure that you could do it. You could still do it as a key-value pair, but the value would be a bit… structured. It'd be a comma separated, or some kind of a structure, which might still work. It's more readable than a JSON.
the key would be the ID, and the value would be… Type, and then value.
Interesting.
**Jacob Aronoff (Cribl)** 16:29 Interesting. I think that that's probably too… I think JSON is going to be fine. I don't think we need to do…
**Jack Shirazi** 16:34 Yeah, okay, I'm fine with Jason.
**Jacob Aronoff (Cribl)** 16:37 And then your next one is existing implementations. Like, is this in terms of who has a… who has a thing out there?
**Jack Shirazi** 16:43 Yeah, so this… this was… this is me asking, really, because… A lot of what we do is very theoretical, and I know I have two implementations out there, which is the Elastic one and the Contrib one.
Yo… And… and my implementations are customer-driven, so they're actual… Requests by customers to have these Features in there.
And I'm just wondering… Where everyone else is.
**Jacob Aronoff (Cribl)** 17:18 I'll let Raphael take his first.
**Raphael Menderico** 17:20 No, no, yeah, I thought that was a haze rant. Okay, anyway, so I remember one problem with JSON when I was looking last year, which was merging Policies from different sources.
JSO does not have a standard for merging, so maybe that's one thing we want to specify. I mean, I don't have anything against JSO, just to be clear, but if we do go for JSON, then we… I think we need to figure out what to do with the merges.
Or consider something like it, because this… This is something that could be problematic if we have two clients that merge in different ways, the policies.
**Jacob Aronoff (Cribl)** 18:00 I think it's actually kind of similar to how we would do the HTTP and the op-amp stuff, where these should be keyed off of a, an ID, right? Like, of some… like, a top-level ID.
Such that you can merge them in a way that Well, also, each policy idea… I have to think about this a bit more, but…
**Raphael Menderico** 18:22 Because, yeah, the scenario where I think about merges, let's say, if the binary comes pre-configured with a policy, and then you want to override from the server.
So we needed to tell, like… I remember when I looked at JSON, was not exactly clear what was going to happen in that scenario. I… at the time, I came up with some special rule, but… Yes, I think we need to put that on the specification, like, or just say that they never merge. That's also an option.
**Jack Shirazi** 18:50 Did we retain… did we retain the policy, the priority?
**Jacob Aronoff (Cribl)** 18:56 I think we should retain the, like, the hierarchy of overrides.
**Raphael Menderico** 19:00 So then it drops everything, and that would be the merge.
**Jacob Aronoff (Cribl)** 19:04 I think that if… I think it's that, like, file is the lowest level priority, and then off-amp is the highest.
And so if OpAMP specifies the same policy ID, the same policy ID that had been loaded in a lower priority provider, then it gets overwritten.
**Raphael Menderico** 19:20 Yeah, but the full policy, let's say, because the policy might have multiple aspects, so we don't have the concept of a delta policy, it's always a full override.
**Jacob Aronoff (Cribl)** 19:29 It is always a full overhead, yes.
**Raphael Menderico** 19:31 Perfect.
**Jack Shirazi** 19:35 But even with priorities, there's still merge conflicts. There's a…
**Jacob Aronoff (Cribl)** 19:41 Good.
**Jack Shirazi** 19:41 Go to an issue somewhere.
**Jacob Aronoff (Cribl)** 19:43 There's, I'm gonna write this down. There is a possibility Of, two of the same priority… Providers provide, responding with a policy of the same ID.
I mean, one thing that we could do is just say that's an error, and respond back over op-amp to say, like, hey, you know, two people are trying… two people of the same priority are trying to override the same thing.
Figure out your semantics. And then just give that to the… give that to the user.
is an option. I'm not saying it's a good option, but it is an option.
**Raphael Menderico** 20:25 I think what's most important should be consistent here. I'm okay with the error, provided we… like, one of the goals is that the policies always converge to the same state.
So I think we need to be consistent to guarantee that, like, even if that happens, either it's an error, or that we make sure that they all convert to the same state.
**Jacob Aronoff (Cribl)** 20:50 Yeah.
**Jack Shirazi** 20:54 Yeah, there were…
**Raphael Menderico** 20:56 Okay.
**Jack Shirazi** 20:57 There are lots of concerns about… When you have policies, even… Even if you consider the priorities, You might still have… to, two conflicting ones, even from… Yeah, anyway…
**Raphael Menderico** 21:17 I guess I need to read this.
Take a look.
**Jacob Aronoff (Cribl)** 21:21 Yeah, I'll read through this, Jack, thank you for sharing it again.
Now that we have things that are more concrete, we can actually have a better discussion about it, so… Cool. Well, yeah, existing implementations, so, I have some, Google has some, I think they're all kind of disparate, though, and they're all gonna have to change, but… from my usage, it's like… I mean, mine were a bit different in that I was, like, writing a bunch of Lower level, like.
Clients using my hyperscan tricks.
And those will all have to change, but that's okay. But yeah, we are gonna work, Jack, through the… once we have this merged.
David and Raphael are going to update their, proof-of-concept collector implementation, and then that'll be the first one that we get merged in. And then that can be the sample that we go off of for everything.
**Raphael Menderico** 22:33 I mean, David Ash pole, right?
**Jacob Aronoff (Cribl)** 22:35 Yeah, yeah, yeah.
**Raphael Menderico** 22:37 Okay, yeah, he might be doing that more than I am. Okay.
**Jacob Aronoff (Cribl)** 22:42 No problem.
**Jack Shirazi** 22:44 The reason for me asking this is because I know, from my experience, the… the things that I've implemented are things that customers have requested, and I'm just wondering whether everything else out there that's being worked on Is customer driven, or is it… just, these are nice ideas, and let's do them. And it worries me.
**Jacob Aronoff (Cribl)** 23:09 I mean, I'd say all of my stuff was customer-driven, in that it's like, these are all features that we… Had been asked to implement From customers, and then things that we were also skating where the puck was going, type of stuff.
You know? Whereas, like, we know that… customers are going to want to be able to do this type of transform, and we should have support for that, or we know that a customer wants to be able to do sampling in this way, and we should support that. And then, like, months later, a customer is like, hey, you have this thing, great. You know, so it's a little bit of both.
But I don't, I don't think, I don't think, certainly in this… version of the spec that we're writing, I don't think that there's a lot of bloat. If anything, we've, like, scoped it down too much.
So, I think it's okay.
**Jack Shirazi** 24:01 So, in the current version, I've been working through… the things that I need to implement.
and at least half of it… I mean, they're all stuff that… it's nothing new. It's all stuff that I've already put into the, the comments.
And at least half of it doesn't… isn't specified at all, which means I'll have a lot of custom, policies, which is… I mean, it's fine, but… I kind of… I guess my question… the reason I'm raising this as a question is because This is stuff that I have in production.
it's working, and I just wonder… whether… the approach that we're taking is customer-driven enough. But you're saying that you're one that is, so that's fine.
When I say customer-driven, it's not just… So, we… we spent a lot of time with our customers.
Narrowing down what they needed to be able to change dynamically.
Rather than statically. Because a lot of the things that are available are… you can do it statically.
And… And if you just ask the customer, do you want this dynamic? They say yes. It's the simple answer, right? But when you focus on, actually, you tell them.
We can do this or this, you know, then it becomes more of a, oh, okay, we want that and not that.
And then you find out that a lot of the stuff that they want to configure, they're fine configuring it statically, and there's a few things that they really… really want to configure. Like, for example, the one thing that's… heavily requested is being able to turn off individual instrumentations.
And changing routes that are ignored.
And those are already, I think those are now supported with the, the PR, number 8.
**Jacob Aronoff (Cribl)** 26:09 Yeah, the equipment stuff?
Yeah, I think once we sort that out, that will cover that use case well.
**Jack Shirazi** 26:15 Yeah.
But there's other ones that, about half the stuff is unsupported, and I just… I kind of… I kind of think… Yeah.
I'll just… I'll just focus on adding those.
**Jacob Aronoff (Cribl)** 26:32 Yeah, I think we will continue to have things that we, are missing, that are gaps, but, like, I would rather we… Keep a very tight scope initially, and then can continue to add features, rather than trying to get the spec to have everything that we want before we even get started on implementation.
And that's what's more important to me, is just that, like.
The first implementations we have can… Do the basic stuff, you know?
We can continue to add things, but, like.
the point of this is that also, not everything is going to be able to implement every feature, right?
And so… that… taken together, like, I think that it's fine to continue to add things, but we should also not… Hold off on implement… on getting the spec just out there, so we can begin Like, official implementation stuff, you know?
**Jack Shirazi** 27:30 Okay, yep.
**Jacob Aronoff (Cribl)** 27:32 But we will definitely be missing plenty of things, like, that's just… that's just a given. But that's okay, in my view.
We will, we will continue to add stuff.
Like, I would almost be okay to… Hold off on, merging the, like, the enablement stuff.
Until after we merge the base… the existing PR.
that into the proto, so we can get the protos released, and then get the collector implementation out there, while we sort out what we want for the enablement policies, and, like, understand that scope better.
But… not saying we have to do that, more of just, like, I would like to… get the larger PR merged.
So that we can have Better discussion on smaller things.
Anyway, that's… that's all I got, for ya.
Do we have anything else to go over?
You're all good, Raphael? None?
**Raphael Menderico** 28:43 Yeah, no, I have to go, buddy, yes.
That's good.
**Jacob Aronoff (Cribl)** 28:47 Does that all sound good for you?
**Jack Shirazi** 28:52 Yep.
**Jacob Aronoff (Cribl)** 28:53 Cool. Yeah, I really just want to get this merged sooner rather than later, so that we can unblock the collector work, and then we could also begin… like, I was gonna write up a… take… I have a whole, like, conformance suite that I wrote for my proof of concept that I will rewrite based on this spec work.
that we're doing here, and then I will probably add that into a… maybe we'll make a new repo in OTel or something for that, called Conformance? I don't know. But I want to write that up such that a, it can do, like, the full loop of, like, send the OTLP data.
or, you know, Prometheus data or whatever it is, run a bunch of policies, and then check the output, and then check the stats.
from the op-amp, from file, from HTV, whatever it is, and then verify that all of these implementations do the thing that we expect.
Is the goal.
Such that as we at our companies, like, write the implementations, we can just use this as the sample.
To know that we are all doing the thing that we expect.
which no one… right now, OTEL doesn't have that at all anywhere, so I want to make sure that we do that, because that would be… for something like this specifically, it's going to be, like, vital that we are all consistent.
Cool. Well, anyway, that's the reason I want to get this merged in, is all I'm saying.
**Jack Shirazi** 30:31 Cool. Good evening. Thank you.
**Jacob Aronoff (Cribl)** 30:34 Yeah, thank you. Bye.
