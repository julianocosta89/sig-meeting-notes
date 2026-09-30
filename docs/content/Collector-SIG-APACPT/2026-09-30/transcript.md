SIG: Collector SIG (APAC/PT)
Date: 2026-09-30
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Antoine Toulme (Splunk Inc.)** 01:31 Hello.
**Paulo Janotti (Splunk Inc.)** 01:33 Hello.
Since the quorum is low.
I have a PR for you.
**Antoine Toulme (Splunk Inc.)** 01:43 Okay.
Okay.
Sure.
Good.
Drop it in the chat or something. Oh, hey, Josh.
**Joshua MacDonald (Microsoft)** 01:59 Hey.
**Antoine Toulme (Splunk Inc.)** 02:00 The Borneo.
**Joshua MacDonald (Microsoft)** 02:03 What'd you say?
**Antoine Toulme (Splunk Inc.)** 02:04 It's a party now.
**Joshua MacDonald (Microsoft)** 02:06 It is.
**Antoine Toulme (Splunk Inc.)** 02:07 I was worried.
**Joshua MacDonald (Microsoft)** 02:10 I… yeah, this is usually pretty sparse. Good to see you.
I do have a couple open PRs that I'm interested in getting approvals for, so it reminded… I remembered to come today.
**Antoine Toulme (Splunk Inc.)** 02:23 Cool.
Okay.
Free drop in the chat, or whatever.
Have you been through?
Okay.
The notes doc is here.
I'm putting you… I put Josh and Paulo in there. Feel free to put yourself in there.
And then if you have anything you want to talk about, let's go.
**Joshua MacDonald (Microsoft)** 02:54 Alright. I have 2 topics. I'll put them in.
First one, yeah, second one, yeah, coming.
Cool.
And There… oh, jeez.
Yeah, something's going on here.
**Antoine Toulme (Splunk Inc.)** 03:15 Yeah.
**Joshua MacDonald (Microsoft)** 03:16 The next one is 64.
So… My god.
There we go.
**Antoine Toulme (Splunk Inc.)** 03:28 Alright.
**Joshua MacDonald (Microsoft)** 03:31 Off to a good start.
So in order, this is about the batch migration.
Both of these are, and the first one is to get metrics out of the exporter helper into the QBatch processor.
So, it means.
they're, like, I've gone through 3 ways of doing it now, but I think this one's pretty solid, and, like, the smallest we could do. Most of this, and most of the code is internal.
So this… Ads, a lightweight metrics dispatcher. You get an enum that tells you which metric it is, you get a number. you have to go ahead and do, like, call your specific instruments. So we generate instruments for each of the components. The exporter helper gets its instruments, QBatch processor gets its instruments.
And then, the dispatch goes both directions. You get two sets of metrics.
**Antoine Toulme (Splunk Inc.)** 04:30 Okay.
**Joshua MacDonald (Microsoft)** 04:31 So that's the first one. Really boring. So many ways to slip up. No real functional change.
And… We have one set, review already on that one. Pretty good.
Yeah.
So, if I may, the second one, this is probably more impactful and more interesting.
I could, pull it up, maybe, and share my screen.
Hmm. Maybe.
**Antoine Toulme (Splunk Inc.)** 05:03 Sure.
**Joshua MacDonald (Microsoft)** 05:06 Let's see… under tabs, this is the one.
Israel has been doing code review for this, for both of these, and he's done a great job, so I think it's ready for more, more eyeballs. So this… But then… Adds to the metadata.yaml to facilitate the batching migration. So the big deal is we're going to change the default.
batching property from disabled With a bunch of defaults in the config optional, to enabled, with a bunch of defaults turned on.
And this has been planned. We're in Phase 1. This is one of the major steps remaining in Stage 1, Phase 1.
what I propose looks like this thing here on the screen. I can make it a bit bigger. So, so… If you are overriding the default, and from the contrib repo, there are about 45 exporters.
Half, almost exactly half.
just give you the default. So those are the ones that are just gonna automatically change to the new behavior. And the others, you need to put in an override in the metadata YAML to clarify what your intention is and to document your default with a rationale.
**Antoine Toulme (Splunk Inc.)** 06:26 Okay.
**Joshua MacDonald (Microsoft)** 06:27 So.
Not too… it's not… not super exciting, honestly, but.
There are 3 exporters in the core repository, so you can see what happens to them.
Now, this is… Font size is not working for me anymore.
So.
What are they?
What you'll see is that each of the, exporters gets a new documentation file.
That has the sending queue. The support is given, so there's 3 ways you can go. Default, omitted, or, has overrides. If you have a… Whether you have overrides or not, you're going to get one of these sections. If you're the default configuration, you're going to get this feature flag reminder that says that the feature flag controls the value for enabled.
And if you're an override, let's see, we have one of those, too.
Http exporter is standard. So it has the feature flag.
And then, where's the debug processor? Debug exporter is the one… It has overrides.
So it will override the, sending queue to be disabled, as well as the batcher to be disabled, but both of those features are there if you turn them back on. So, this is your reminder, and note that there's no feature flag here, so when you're in has overrides, you don't get the default feature flag anymore. You have to pin it down, basically. So this is how you pin it down, using a sending queue.
In the metadata, let's show what one of those looks like.
Metadata YAML.
**Antoine Toulme (Splunk Inc.)** 08:13 What's the motivation for this work, Josh?
**Joshua MacDonald (Microsoft)** 08:17 This is to… to safely, Change the default.
And I think it's important… so this is… I think you're probably asking the right question, this goes a little further than we need. Putting the documentation there makes it front and center, like, automatically generated code that tells you what the default batching configuration is.
**Antoine Toulme (Splunk Inc.)** 08:38 Yes, no surprises, okay.
**Joshua MacDonald (Microsoft)** 08:40 And the kind of behind that, the reasoning, I think, is… Among those 23 with overrides, we've looked at them, and it's a variety of explanations. I would say about 10 or less have a.
like, a good reason to be doing something fishy. Or at least it was well-intentioned, and it's… now would be a breaking change to change it.
And something that was, like… or, like, in the case of some weird stuff, I'll just say Azure Exporter. Azure Monitor Exporter has a secondary batching that goes on, so, like, they're gonna turn off the… they don't even use the, you know, QBatch, and it's intentional.
Yeah, but for most components, if they're old enough, the the Q batch configuration didn't exist. It's evolved a tremendous amount since it those exporters were created. And the feeling is that they might want to just reconsider whether they want the defaults.
Or whether they have a good reason to have the defaults overridden. So it's a chance for everyone to review their defaults before we flip the default on everybody.
**Antoine Toulme (Splunk Inc.)** 09:53 That makes sense. And, I mean, one missing thing in there is that… If I remember properly, the batching does not really do a good job of having custom Custom sizers, custom motioning.
We size according to the OTRP protocol, and then there's been some efforts to do a better job of that, but… Quickly don't batch by custom… by custom marshalling, right?
Supported.
**Joshua MacDonald (Microsoft)** 10:27 Why am I linking to this? This is the wrong link.
The… so, as far as I know, the problems that you're imagining are behind us, and the batching migration, which I was trying to find a link to.
We'll see if we can find it here…
**Antoine Toulme (Splunk Inc.)** 10:48 You can offer, okay, go ahead.
**Joshua MacDonald (Microsoft)** 10:51 This is the document.
Yes.
So… The sizers used to be a problem. The old batch processor, the original legacy batch processor, only supports items, so its defaults were, like, 8,000 items. The new support is you have to choose.
The sizer is going to be items, or… Well, there's… there's two sizer choices, one for the queue, one for the batch. That's… the queue will be sized in requests by default.
And the batcher will be sized in items by default, but you can change both to be bytes. And that's all, I would say, new, but it's not new-new, it's two… two years old or so.
**Antoine Toulme (Splunk Inc.)** 11:39 Yeah, it's feasible.
**Joshua MacDonald (Microsoft)** 11:40 And so that's what we're doing, is taking out the old batch processor and installing these new defaults, which should be enabled for most users.
**Antoine Toulme (Splunk Inc.)** 11:49 My understanding is that we… a good reason why there's a lot of overrides, at least for the Splunk HAIC exporter, we have our own way of marshing and compacting the, the request out. And the problem we've had is.
I mean, when QBatch was introduced, one of the promises that the Ministry made to me is that it would… the batcher would be able to take a custom marshaller to marshall to bytes, and then we'd be using that.
And he's done that only for Sizer, and he's actually not using that for… the actual batcher or something. So it's it's it's backfiring a little bit, and it was not completed.
And now you're moving towards making that a bit more hardened, but the first thing that's gonna happen is that all those custom… all those components have done custom things in the past, like this BlockAC Explorer, they're going to look like big culprits even more, when really what's missing is that we did not finish the job in QBatch.
Did I… am I missing something?
**Joshua MacDonald (Microsoft)** 12:50 I… fully understood your criticism, I think, because I remember making similar sort of statements.
**Antoine Toulme (Splunk Inc.)** 12:59 Yes.
difficult.
**Joshua MacDonald (Microsoft)** 13:01 There was a moment when I felt that the premise or the promise that you said, like you said, was that, well, we're going to make things complicated and slow us all down for a few years, which is sort of what I was complaining about.
So that we could have this new request type, which allows you to supply your own marshaller and unmarshaller, but then for years, it kind of creaked along without making much progress, and I said to the authors, including Dimitri, like, why do we have no examples of how to use this fancy new functionality?
Yep. Because there's no one using it, basically. And I'm wondering, like, are you vendor behind the scenes doing this? So I asked a few people.
I don't know the answer, but my… but…
**Antoine Toulme (Splunk Inc.)** 13:49 No, we're not. I mean, maybe… maybe there's some exp…
**Joshua MacDonald (Microsoft)** 13:53 But it's there now.
**Antoine Toulme (Splunk Inc.)** 13:55 Is it?
**Joshua MacDonald (Microsoft)** 13:57 Fair. Yeah. So I don't, I would definitely ask Dimitri this question now.
**Antoine Toulme (Splunk Inc.)** 14:03 It's.
**Joshua MacDonald (Microsoft)** 14:03 Because.
**Antoine Toulme (Splunk Inc.)** 14:04 Let's get some Zoom.
**Joshua MacDonald (Microsoft)** 14:06 You should, in theory, that's the way I understand this whole elaborate setup.
Be able to provide a function that is a splitter merger.
And, you know, as… as a plugin of… as a… as a user or instantiator of the exporter helper, you give your Marshall function, and if it knows… it gives you a way to combine or split.
Which is part of the complexity, honestly. So… Okay. Yeah, I just haven't seen anyone use it.
**Antoine Toulme (Splunk Inc.)** 14:41 I've seen it used, but only for the person queue.
So, the code referring to that marshaller ends up being used only for the person Q, not the rest of it.
That's what I saw. And I might be wrong.
In any case, it's somewhat orthogonal to your work. I don't mean to discourage you. I just want to understand because I think in a sense you're lighting a fire under us because you're.
**Joshua MacDonald (Microsoft)** 15:06 the.
**Antoine Toulme (Splunk Inc.)** 15:07 Pretty bad.
**Joshua MacDonald (Microsoft)** 15:08 I… Don't mean it to be that way. I have held that feeling, though, and I think it's good to remind ourselves of it.
Yep.
**Antoine Toulme (Splunk Inc.)** 15:23 On words, right?
I mean…
**Joshua MacDonald (Microsoft)** 15:26 Yeah, yeah. And So the batching migration, which is up in front of us, will go forward, I think, and will help to get the rest of Phase 1. The only thing else is this blog post.
The two that I have get us through the remainder of this First 5, and then… I was thinking about a blog post with Dimitri.
I would invite Bogdan to come do it, but he seems a little bit… Distant right now.
**Antoine Toulme (Splunk Inc.)** 15:57 I don't know. I haven't heard about him.
for a while. I think also, the CFP for Kipcon EU is still open, so… That's an option.
**Joshua MacDonald (Microsoft)** 16:08 We are going to present this work at one or two spec SIGs from yesterday, or this morning, actually, proposing after the RFC on V1 that this is happening, this stuff here. So I will speak about it again.
**Antoine Toulme (Splunk Inc.)** 16:26 Okay.
**Joshua MacDonald (Microsoft)** 16:27 I would say also that.
your point, or the idea behind Splunk… do you say HEC, H-E-C, whatever you… however you say it? Yeah. The HEC protocol is, valid, and… in…
**Antoine Toulme (Splunk Inc.)** 16:49 It's pretty stupid for two.
**Joshua MacDonald (Microsoft)** 16:50 What I… well, what I… What I, aim to say something about is that in the Hotel Arrow project, which I've been involved with now for a few years, we are building this Rust pipeline Yep. And, one of the features of that design, which is responsible for so… some of its, I guess, optimization, as well as its code bulk, is that it has a dual data path, where you can either be arrow, and never mind what arrow is, but the point here is that you come… the data comes in, and you can either be OTLP bytes, or you can be this other complicated representation.
And we have a way, therefore, to pass undecoded bytes, like.
as presented to the RPC library, here's your protocol buffer.
If you want to dissect it.
then you should probably turn it into objects. But if you just want to pass it through.
maybe you should just pass it through. And then what it does is it gives us a lazy or an on-demand transition between those two types.
And there's a lot of interest now in Sort of supporting, like, arbitrary types.
Because anything can be a byte array, and you'd say, here's a chunk of data that's in some other exporter format. Effectively, you're providing a way to do this marshaling and unmarshaling.
We call it a Kodak, and this is coming soon.
the idea that you could carry data through your pipeline in any old protocol that kind of makes sense. If there's a translation into OpenTelemetry.
Ideally, both directional… bi-directional translation and open telemetry.
And so, what I'm trying to say is that we've sort of validated this design, where you can carry data and, like, not… force it into OTLP, And maybe never force it into objects either, just, like, however it comes, make sure you can translate it as needed.
But then, the final step would be putting it in Splunk Heck before it goes into the Batcher.
Bytes, count, or whatever.
**Antoine Toulme (Splunk Inc.)** 19:01 Yep, yep, that's…
**Joshua MacDonald (Microsoft)** 19:03 Get your advice on that.
**Antoine Toulme (Splunk Inc.)** 19:04 I mean, I saw the… I saw the lines, the contours of the solution last time I tried, and it took me… to me, a couple hours to get to this hiking, and I'm… at this point, I guess, I'm actually very perturbed where we were, because There's a lot of really good ideas in Explorer Helper, which just did not pan out, and have been abandoned throughout.
I pointed at Dimitri the other day, there is even a way to, in the queue, to do a ref, ref counter.
So we could do more there, like in terms of using memory management or something like that. We just don't. Anyway, okay, so I'll review your PR. I'm happy to review that. That's great.
**Joshua MacDonald (Microsoft)** 19:47 Thank you.
I agree with the exporter helper. You know, I sort of agree, and I don't agree anymore. Like, I think it's mature code now, so…
**Antoine Toulme (Splunk Inc.)** 19:59 Yep.
**Joshua MacDonald (Microsoft)** 19:59 Let's ship it.
**Antoine Toulme (Splunk Inc.)** 20:01 I'm going to.
Oh, that's good. Sure.
**Joshua MacDonald (Microsoft)** 20:06 And then, and then I think the, the… Ideally, the future is we, allow a little bit more flexible conversion between data types and you won't have objects, and then this design of Exporter Helper, which is prevent… is to sort of… help you batch outside of the objects should be a little bit more orthogonal. You could just have a translation from PData to Splunk Heck, and then it would go straight into your exporter, or something like that.
**Antoine Toulme (Splunk Inc.)** 20:36 So we talked about that.
**Joshua MacDonald (Microsoft)** 20:37 2.
**Antoine Toulme (Splunk Inc.)** 20:38 How we do this? Interestingly, I think there was some state associated with some of that. So we we will we will look into it. It's it's not there yet. It's been interesting because there's too much commute. Yeah. But we I do.
**Joshua MacDonald (Microsoft)** 20:52 I can't imagine…
**Antoine Toulme (Splunk Inc.)** 20:54 We built some codecs before, I think.
I don't know if the one for the,
**Joshua MacDonald (Microsoft)** 21:00 The Oto Arrow… Go exporter component is an example, right… right where it doesn't… where the model breaks down, actually, where you want to, like.
That one's hard to explain, but… but the… because of there's a persistent stream inside of the exporter itself, how you do batching kind of matters.
I'm not ready to talk about that.
But thank you for agreeing to look at those PRs.
I saw yours as well on the dialer. Looked very good, thank you.
**Antoine Toulme (Splunk Inc.)** 21:39 Yeah, I'll put this at the end of the agenda. First, there is a discussion from Paulo. Paulo, you want to promote the Windows event log receiver to beta.
What is that about?
**Paulo Janotti (Splunk Inc.)** 21:50 Yeah, That's… the PR itself is not interesting, it's just, more of an announcement, that we think it's in the right spot to be, beta. Actually, customers have been using for quite some time. I put one here in the PR because I'm sure at least one year, but I think, like, two.
**Antoine Toulme (Splunk Inc.)** 22:17 At least, yeah. Okay.
Yeah, it's great. In general, like, anything we can promote, we should, just to increase the comfort level of people.
when it's wanted.
So, I just approved it for the 4th.
Maybe we keep it open for a couple more days if you want, just because… This ceremony, or anything else?
**Paulo Janotti (Splunk Inc.)** 22:37 Yeah.
**Antoine Toulme (Splunk Inc.)** 22:38 Okay.
So… Let's talk about the dialer for just a sec. So, I've, had a use case that was communicated to me, which is kind of intriguing in the first place. I mean, I don't know, it's nerdy, so… I love nerdy stuff. WireGuard is a VPN that's kind of new, allows you to do all sorts of communications, connections via.
UDP, TCP, it's actually UDP-based VPN, and it's all software-based, and it has a Go SDK, which allows you to embed connections to the VPN straight into your software for a specific endpoint.
And you can do that for a HTTP server or a HTTP client.
So this, even if we, lend this, we still need to do it for the server part.
The client requirement is that you override the dial context function in your transport to, instead of calling to the classic TCP stack of Go, you will be passing through their library, which will do some random stuff to the TCP connections until such time that you get to where you want to be.
And, so I pretty much copied the page from your book, Josh, where I use Config Middleware for what it was, and then extension middleware to do that.
I ran into a bit of trouble about how I'm going to surface that in Config HTTP. So, unfortunately, or, I mean, it's… it's… the timing is a little awkward, in spite of the feedback I got from maintainers. They want to stabilize Config HTTP, and the feedback I gave them is that Right now, there is no way for Configure HTTP to actually be pluggable.
You cannot have an extension.
there isn't any… any means to… to do that. So, either we add a dialer field that points to a component ID, just like we have for the middleware stuff, and And after that, he gets less… Weird.
Or we have to find a really elegant way of making the Config HTTP stuff extensible.
And the maintainers, specifically Alex Bolton, when I talked with him.
was a bit ignorant about this. It's like, why don't you just use XConfigHttp? It's just gonna work, right? I'm like, no, that means every exporter has to now change the way they do their config Http stuff.
This makes no sense. I cannot work with that.
So… If we… if we learn this, that's great.
I hope we learned this.
If we don't lend this.
I… my point back to the folks who want to stabilize this is that they did not make it any… It's pretty risky what they're actually trying to do here.
**Joshua MacDonald (Microsoft)** 25:15 Yeah.
**Antoine Toulme (Splunk Inc.)** 25:17 So Unless there's, like, some really good idea how we do this, I think.
Yeah, hopefully I can land this in time, but then we're shutting the door on ConfigHTTP being actually pluggable and extensible.
In the way that we might like.
So that's what I have.
**Joshua MacDonald (Microsoft)** 25:38 Yeah, they were speaking about this on Monday and I was confused at first.
And disoriented by the… by the PR.
Or Alex mentioned it.
**Antoine Toulme (Splunk Inc.)** 25:51 Yep.
**Joshua MacDonald (Microsoft)** 25:52 Yeah, that was… there was, like, a doesn't… hasn't anyone solved this problem kind of discussion, and hasn't Kubernetes solved this problem?
**Antoine Toulme (Splunk Inc.)** 26:02 Well, no, no, no, no. This is not a discussion for Kubernetes environment, unfortunately. We're not here doing a network on… so I think what they're talking about here is, like, a mesh network, an Istio or something like that, where you have a software-based network, that.
**Joshua MacDonald (Microsoft)** 26:17 have.
**Antoine Toulme (Splunk Inc.)** 26:17 receive.
**Joshua MacDonald (Microsoft)** 26:18 Typed configuration…
**Antoine Toulme (Splunk Inc.)** 26:19 Yeah, yeah. No, that's not this case. We are having a standalone distribution of a collector in a quote-unquote air-gapped environment, and you need to be able to extract the data to some to something without opening too many ports, and… nope, sorry, no escapes here. I actually just like that this is something that even went into the discussion.
**Joshua MacDonald (Microsoft)** 26:40 I… Thought your approach of using the component ID was fine.
**Antoine Toulme (Splunk Inc.)** 26:49 Yep.
**Joshua MacDonald (Microsoft)** 26:50 And I don't quite see a problem… I don't see a problem with adding optional fields that are just component ID references.
Because then you can use an unstable.
Then, if you… you're right, that leads back to the config… XConfig HTTP, where to use an unstable feature, you have to… We can only add stable extension interfaces right now.
**Antoine Toulme (Splunk Inc.)** 27:24 How would that… yeah, this is the thing, it's like, so you have the OTLP exporter, you want to change the dialer on that thing. How would you do that?
how do you make config Http somehow extensible? So you could add a dialer field without breaking the config Http module. In the 1st place, I don't see it.
It doesn't work.
you would need to have an XConfig HTTP, HTTP client options, or something like that, that you would then have it embed the stable one, and then you have the OTLP exporter has to use the unstable config options to get to where it needs to be. And then you just defeated the whole purpose of stabilizing the collector in one cell swoop. So, I don't… I don't see the point.
**Joshua MacDonald (Microsoft)** 28:08 But wait, let me play the counter argument is.
We've complained… we've hemmed and hawed about interface extensibility, where adding a method can break everything if you don't lock it down just right.
And I thought the rules for structs were much simpler, because the config object is a struct, therefore adding fields is safe as long as you have an anonymous field somewhere that forces you to name all the other fields.
**Antoine Toulme (Splunk Inc.)** 28:39 The yeah.
**Joshua MacDonald (Microsoft)** 28:41 Like an underscore field, or an uninitializable field, a no-default field, or… I can't remember.
**Antoine Toulme (Splunk Inc.)** 28:47 And yet when Alex brought it up to me, he said, you know, we're trying to stabilize this, so we're not looking to add additional things.
**Joshua MacDonald (Microsoft)** 28:54 Hmm.
I guess I would have… my interpretation of it was that you're looking to stabilize it. We will only add backward compatibility thing things, where the default is safe and off, or whatever it is. Like, optional features can be added. And then where the conversation went, let's find… I think we can find some sort of solution. Conversation went towards talking about a feature flag potentially being per component.
And it made me think of the batching migration itself. Like, I just went through an entire explanation for you about how this metadata YAML override can be done, where you declare your overrides, partly to get through a feature flag migration.
**Antoine Toulme (Splunk Inc.)** 29:37 Okay.
**Joshua MacDonald (Microsoft)** 29:38 And what they were talking about for this dialer override was that it was in your PR, it's an optional, which we're comfortable with now.
But what I was thinking was to make, like, a new feature flag optional type, which would be called config feature, or something like that. So, config feature optional would be like optional, but Would be controlled by the feature flag, so that you were… you would be able to add a flag that was off by default and featured off Until you turn the feature on, and then you could maybe use it.
Okay.
**Antoine Toulme (Splunk Inc.)** 30:15 That's cool.
**Joshua MacDonald (Microsoft)** 30:16 That was half of an idea, and Nobody had any strong opinions by the end of the conversation this last Monday.
And I wasn't up to speed. I came… came in on.
**Antoine Toulme (Splunk Inc.)** 30:27 Monday morning. It's a convenience thing, right? It's a convenience layer that you're adding where you would be able to do this by hand as well, where you could have the config optional, and then you would just have the feature gates check at that point as well. So you could also get away with just… what you're referring to here is a construct that it makes it a little easier to define these type of features.
Yeah, but I mean, in general, like.
**Joshua MacDonald (Microsoft)** 30:49 You could have it, like, a global, as you say, or you could… then you could extend it in the direction of having per-component features.
**Antoine Toulme (Splunk Inc.)** 30:57 Oof.
**Joshua MacDonald (Microsoft)** 30:58 Nobody wants that.
**Antoine Toulme (Splunk Inc.)** 31:00 Imagine what your command line is going to look like.
**Joshua MacDonald (Microsoft)** 31:02 I.
**Antoine Toulme (Splunk Inc.)** 31:03 I'll see it. No, I… Also think this is a bit of a… The only reason this is ever so slightly contentious is because of the stabilization efforts, and it's got itself… I have horrible timing.
That's what I'm thinking.
**Joshua MacDonald (Microsoft)** 31:23 Perhaps horrible timing, but I think it's… And it could end up holding you up for a while. I will try to help you. I can add that I'm… I've seen this need before.
The, like, I'm a vendor, and I have very particular ideas about the network, and therefore I want to change how gRPC works, which means I want to install some custom gRPC widget.
**Antoine Toulme (Splunk Inc.)** 31:47 Yep.
**Joshua MacDonald (Microsoft)** 31:47 And…
**Antoine Toulme (Splunk Inc.)** 31:48 Definitely.
**Joshua MacDonald (Microsoft)** 31:48 So it was a multi-connect feature where honestly, I wish gRPC was less opaque and easier to use and set up and it wasn't necessary to do this, but it is the way it is.
So… but you've shown a nice case for HTTP as well, and I think it's good.
And I don't really want to provide… that was my first question when I saw your PR, was like, let's hope he has a good motivation here, because I don't want to see this if… unless it's necessary. But yeah, WireGuard was a good reason, I thought.
The one my old company did was terrible, and I didn't want it.
**Antoine Toulme (Splunk Inc.)** 32:25 Yeah, wireguard is pretty cool. I think it would also be a nice security layer. It's a selling feature for photometry, if we can make it happen.
Okay, so, on that note, so… Look, I still want to pursue having some sort of a way to make everybody a little bit more easy with this, and there might be a way for us to… Expose.
So, another way I can think of is that we have a… We define the dialer as an unexported field in the struct.
And then we have… but no, that sucks. No, I can't do that, right? The problem is, like, I like the XConfigure HTTP struct, then to have a way to set the dialer, but… No.
Yeah, No, I need to really think through how.
**Joshua MacDonald (Microsoft)** 33:17 Another… another workaround, this is not pretty, but you could.
There's already a list of middlewares, and just put your dialer first, and have a…
**Antoine Toulme (Splunk Inc.)** 33:28 Yeah, but I mean, I think you would hate that and me too, right?
I think this is not… this is not suitable, right?
Another way to do it is that we could have, you know, a map of string component ID, extension middleware, and you say, go at it, your hot contents, and the strings are magics, and they're somehow keys to some external behaviors that, you know, we don't know.
And then you can… you can kind of, Explain that.
Those keys, over time.
For a little while.
**Joshua MacDonald (Microsoft)** 34:03 Yeah, I would probably call those capability key, or capabilities, or something like that. You could just, like, hear them, you know.
Pizza.
**Antoine Toulme (Splunk Inc.)** 34:11 Advanced, whatever, whatever you want.
Weird.
**Joshua MacDonald (Microsoft)** 34:16 Okay, this is an important one. I think we've all realized it, and I will continue trying to help or think about it.
I don't quite see the problem… that Alex is referring to.
**Antoine Toulme (Splunk Inc.)** 34:30 Interesting.
**Joshua MacDonald (Microsoft)** 34:31 Supposed to be the easy case.
**Antoine Toulme (Splunk Inc.)** 34:32 So, you make a very point, and I did not think of pushing back on Alex with that, so maybe that's also a discussion to have with Alex. It's like, you're… you're punting on this because you think it's going to affect stability, but this is not actually affecting stability at all. And here's why. And here are the backward compatibility requirements. You are not actually in any…
**Joshua MacDonald (Microsoft)** 34:52 Let me think about it some more.
**Antoine Toulme (Splunk Inc.)** 34:54 Yeah.
**Joshua MacDonald (Microsoft)** 34:55 Crazy.
**Antoine Toulme (Splunk Inc.)** 34:56 Where is that? Where is the stability requirement?
Umm.
Docs.
Stability… Component stability.
Not many…
**Joshua MacDonald (Microsoft)** 35:21 I feel like a feature flag tied to an optional field is… just right.
**Antoine Toulme (Splunk Inc.)** 35:27 Sure.
**Joshua MacDonald (Microsoft)** 35:28 I can't see a reason… I mean, I… I think the…
**Antoine Toulme (Splunk Inc.)** 35:33 some.
**Joshua MacDonald (Microsoft)** 35:33 Nothing.
**Antoine Toulme (Splunk Inc.)** 35:34 completely.
**Joshua MacDonald (Microsoft)** 35:34 Dependencies allowed, but this is just a metadata… an extension ID.
**Antoine Toulme (Splunk Inc.)** 35:43 Just keep your mind.
**Joshua MacDonald (Microsoft)** 35:45 dependency on…
**Antoine Toulme (Splunk Inc.)** 35:46 Keep in mind it needs to also evolve. So you put a feature flag on this thing, then six months later, what do you do? Right?
I think it's the timing of the… of the components lifecycle by not match 1-1, the feature flag lifecycle you'd like to have.
So you're… you now got customers, they want this, they're like, why is this still behind a feature flag? Why is this not GA?
what do we explain that to them, right? I'm like, oh, I'm sorry, we… we were doing that at the same time we're stabilizing the components, so you have to wait, like, another year until we get $2 out.
Not cool.
**Joshua MacDonald (Microsoft)** 36:26 This is tricky.
I don't… I feel like I just still don't quite see the problem, so I look forward to seeing other people express the problem in the ongoing conversation.
**Antoine Toulme (Splunk Inc.)** 36:39 When, do we have this, if you have your backward compatibility thing.
I just don't. I… the documents I have are very fluffy, and there's nothing about APIs.
I don't know… Yeah, Dr.
**Joshua MacDonald (Microsoft)** 36:57 the.
**Antoine Toulme (Splunk Inc.)** 36:57 We landed… I know it's somewhere, but.
The Docs folder doesn't have it.
component interfaces, component interfaces.
**Joshua MacDonald (Microsoft)** 37:07 Yeah, it's component interfaces is the one I wrote. And it's But it's mostly about interfaces, not structs, because they're supposed to be simpler.
But it does mention it, I think.
**Antoine Toulme (Splunk Inc.)** 37:18 No, it does not. So… Now, looks like we need component structs.
**Joshua MacDonald (Microsoft)** 37:24 Well… So that was probably an omission. I did look… like, the GoReleaser tool has a set of formal rules that are harder to enumerate.
and about structs, and I thought that there was a recommendation, at least.
if I didn't write it, there should be one that says.
You must have an anonymous field entry in your struct, because that forces you to name your constructor initializers. And once you've named your initializers, it's safe to add new fields.
**Antoine Toulme (Splunk Inc.)** 37:59 Now we've done that. That was actually the offer of the tool that actually checks that you're doing that properly. And even first CIA, someone was to add the struct without that anonymous struct field.
**Joshua MacDonald (Microsoft)** 38:09 Yeah, that's there, so you can do what you want, I'm pretty sure.
**Antoine Toulme (Splunk Inc.)** 38:14 Maybe I can find the origination of the motivation for the tool as a way to link back to the docs that actually, you know, propel the whole thing.
What was it called?
key, something.
It's been a while.
**Joshua MacDonald (Microsoft)** 38:31 our key…
**Antoine Toulme (Splunk Inc.)** 38:34 I mean, there's, Let me do a blame on some of that stuff. Sorry, Paulo, hopefully it's not too boring.
Http config.
**Joshua MacDonald (Microsoft)** 38:49 Bye.
**Antoine Toulme (Splunk Inc.)** 38:51 Alright, so, no blame here.
prevent and keyed… literal initialization.
**Joshua MacDonald (Microsoft)** 39:03 What is it? The Golang has a blog… Golang team has a blog called Working With… Modules…
**Antoine Toulme (Splunk Inc.)** 39:14 Hmm.
**Joshua MacDonald (Microsoft)** 39:15 It's like the Go Mod.
Like, when GoMod was new, they had to teach us how to use it, and we all got it wrong.
At first.
**Antoine Toulme (Splunk Inc.)** 39:26 I remember those days.
**Joshua MacDonald (Microsoft)** 39:28 Yeah.
**Antoine Toulme (Splunk Inc.)** 39:29 That's like 10 years ago now or something.
Issues…
**Joshua MacDonald (Microsoft)** 39:38 going…
**Antoine Toulme (Splunk Inc.)** 39:39 We have a…
**Joshua MacDonald (Microsoft)** 39:41 Accountability.
**Antoine Toulme (Splunk Inc.)** 39:42 Here we go. So… There is actually something from Bogdan back in 22 here.
which was the reason why I built the thing on top of it afterwards.
Here we go.
There is a message here from Dimitri, it says, it looks like we're trying to go beyond Go 1 stability guarantees. They have this particular exception. Struck literals.
For the additional features in later point releases, it may be necessary to add fields to exported structs in the API. Code that uses unkeyed struct literals to create values of these types would fail to compile after such a change. However, code that uses keyed literals will continue to compile after such a change.
So, it's okay to add additional fields.
**Joshua MacDonald (Microsoft)** 40:32 I got into, an email thread with one of the Go team members that I knew, on this topic. I put a link to the Go blog that I was thinking of. This is almost the best reference there is, which is kind of sad because it's not very good, or it's not complete.
It's complete enough.
what I felt like was missing from this document is what I put into that component interfaces document. Like, like, I felt like they don't tell you how to handle interfaces, but they do tell you how to handle structs.
And, that's, I think, where I first learned this rule that you just described.
**Antoine Toulme (Splunk Inc.)** 41:10 Don't add non-comparable if you can write this for that to really prevent comparison in the first place. I don't think we care about comparison that much for a config struck, do we?
**Joshua MacDonald (Microsoft)** 41:19 But it's a compatibility issue. As soon as one person in the world puts it in a hash table as a map key.
Then you're gonna break them. So if you put it there from the start, they will never be able to do that.
**Antoine Toulme (Splunk Inc.)** 41:35 Okay.
**Joshua MacDonald (Microsoft)** 41:36 So, yeah, an anonymous function prevents people from using it as map keys, and it makes it easier to make safe changes, yeah.
Maybe you can use this to get what you want.
**Antoine Toulme (Splunk Inc.)** 41:50 Yeah, thank you for the reference. But I.
**Joshua MacDonald (Microsoft)** 41:53 I guess that… The risk that may be concerning people is really why I was proposing a feature flag tied to an optional, is that mainly it's a risk that, like, this is unsafe, this is untested code. We released 1.0, and, like, now you add this new thing, and maybe we're gonna make it be off by default until 1.1.
And that will do.
**Antoine Toulme (Splunk Inc.)** 42:16 Can separate those decisions with feature gates and whatnot in a way that does not impact the config struct signature.
In a way that is… Painful.
But sorry. Go ahead.
**Joshua MacDonald (Microsoft)** 42:30 Cool. This, this, I think this, you can use this link to your advantage.
**Antoine Toulme (Splunk Inc.)** 42:35 But what I need to do probably is just the same way you wrote something about interfaces, I would like to write something about structs too.
**Joshua MacDonald (Microsoft)** 42:41 Yeah, I think it was… you could put it in the same place, or rename the document and add a paragraph or two, but this, this blog post is… the most important companion. The Go team I was… argument I was… I was going back and forth with, with… I was basically saying, like, wouldn't it be nice if you guys published this article so I don't have to write my own document for my own repository?
They didn't… they didn't seem to buy it. Like, it was too opinionated.
And they, they talk about the, kind of, with… there's other ways to do this, and I kind of like what we've done in the Collector, and I… I've said this before, but I, like, Bogdan, in my opinion, he invented this new thing, and, like, we should blog about this. Like, GoTeam should write it up.
It's not…
**Antoine Toulme (Splunk Inc.)** 43:25 The the the the end key check. Yeah. Absolutely.
**Joshua MacDonald (Microsoft)** 43:28 Well, the Go team has written the unkeyed struct check, but what it was is the stuff in component interfaces about using a function type for every member.
of your interface with a no-op, and, like, the pattern… that pattern is, like, not documented by the Go team anywhere.
**Antoine Toulme (Splunk Inc.)** 43:49 Yeah.
Okay, so… Hmm. Okay, I'm gonna go and do what I can for this particular use case here, and hopefully put a lot of things to bed on that.
I thank you for the approval on the dialer thing, and I'll follow up on your review. I saw you put a comment with some changes, so…
**Joshua MacDonald (Microsoft)** 44:11 Paulo, thank you for the Windows exporter event.
**Paulo Janotti (Splunk Inc.)** 44:14 That's fine.
And thanks for this conversation that I was trying to catch up in the background, reading stuff, interesting stuff. And remind me a bit, because, I kind of don't like to go… to do these things in the collect.
**Antoine Toulme (Splunk Inc.)** 44:32 Go Park!
**Joshua MacDonald (Microsoft)** 44:33 Yeah.
**Antoine Toulme (Splunk Inc.)** 44:35 Go can be hard. Yeah.
**Joshua MacDonald (Microsoft)** 44:37 Alright, you guys, thanks. I'll see you next time.
**Antoine Toulme (Splunk Inc.)** 44:39 Okay, have a good one, bye.
