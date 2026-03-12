SIG: Configuration WG
Date: 2025-11-10
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/s1h0T-TCwZg97Dj_g-aPMq3vArLPLc3nX-Ii37X2AO0DRHNNqpf5xeaQtZ1rKZwA.uwXSziGpeRa3vSXC
============================================================

## Zoom Recording Transcript

GZ Gregor Zeitlinger 00:00:27 Hi, Alex!
Alex Boten 00:00:30 Boom.
Don't know how many people are gonna show up today, but I guess we're gonna find out.
GZ Gregor Zeitlinger 00:00:38 I know, but Jack will most likely not join. He's, on the, in-person onboarding in Grafana this week.
Alex Boten 00:00:53 Alright.
GZ Gregor Zeitlinger 00:01:04 Yeah, just looking back, we had some calls with very few attendees over the last Months. Oh, Jack, you made it!
Jack Berg 00:01:14 How's it going?
GZ Gregor Zeitlinger 00:01:15 Aren't you going to be onboarding today?
Jack Berg 00:01:17 Yeah, I'm going to onboarding, but I don't travel until 6pm, so… Okay. I'm gonna get in a decent amount of a workday.
GZ Gregor Zeitlinger 00:01:28 Very good.
Alex Boten 00:01:30 Have your flights been impacted by the… Recent cancellations happening in your current location?
Jack Berg 00:01:39 That's a… that's a very, PC way to… to frame that.
Alex Boten 00:01:44 I mean, this call is being recorded, so…
Jack Berg 00:01:47 Excellent.
Alex Boten 00:01:47 I could have called it a shitshow, but, you know, I didn't want… I didn't want it to be recorded. I guess I did now.
Jack Berg 00:01:51 There you go It hasn't been affected yet, but I'm worried about it. Like, I'm anticipating delays and it possibly to be a long night, so I don't know what's gonna happen. Someone told me that, they read something that indicated that, they're more likely to cancel domestic flights than international ones, just because there's more, there's more overhead and, you know, fallout from canceling an international flight, so… Canceling domestic is just, like, low-hanging fruit, so this is an international flight, so I benefit from that.
Alex Boten 00:02:23 Low-hanging fruit. That's… that's nice. That's a nice way to think about it. It's low-hanging fruit to travel across, like, a continent.
Jack Berg 00:02:33 Yeah, New York to California, low-hanging fruit.
Alex Boten 00:02:36 Yeah, just cancel those, it's great.
GZ Gregor Zeitlinger 00:02:40 But wait, you're in Chicago?
Jack Berg 00:02:44 I'm going Chicago to Toronto, so it's a short trip, but it's still international.
Alex Boten 00:02:48 Have you considered driving?
Jack Berg 00:02:51 I looked it up, and I'm not looking forward to it. It would be eight and a half hours in the car.
Alex Boten 00:02:57 If only there was a train.
Jack Berg 00:02:59 Yeah, we have no trains in North America. We had all the trains, and now we have none that are effective.
Alex Boten 00:03:05 I was… I was following, Jacob's trajectory of New York to Atlanta via train, and it's an 18-hour… 18-hour journey, instead of, like, a, whatever, 1-hour flight, or whatever it is. Two-hour flight.
Jack Berg 00:03:22 Yeah, you might as well just… Walk to your destination.
Alex Boten 00:03:28 Yep.
I mean, from Chicago, you could just swim across the lake, right? That's…
Jack Berg 00:03:33 It's a couple of lakes. It's… there's two great lakes. Yeah.
Alex Boten 00:03:38 There you go. Straight shoot. Just to get a… get a canoe, and you're good to go.
Jack Berg 00:03:44 We have… we have no trains and no ferries in the United States, and I feel like there's lots of trains and lots of ferries in other countries.
We only have highways.
Yeah, yeah, Jamie, that's a song.
Alex Boten 00:04:03 Alright.
I guess… Guess we can get started.
I think Tyler said he wasn't going to make it because he's in… he braved the local and international cancellations to get to Atlanta.
Jack Berg 00:04:24 Okay, I can share my screen. Let me just make sure I'm in a place where I can share it.
Alright, the first topic is… I'm not sure who added each of these items.
GZ Gregor Zeitlinger 00:04:41 Oh, sorry, I forgot to add my name. I added all of them.
Jack Berg 00:04:45 Okay.
Gregor has a lot of topics.
GZ Gregor Zeitlinger 00:04:49 Yeah, I, like, I was saving up topics that are not strictly Java-related.
And I think I also didn't make it to… To the last meeting, yeah, that's why it has kind of… Saved up.
Jack Berg 00:05:11 So the first one, service detector by default, what's this all about?
GZ Gregor Zeitlinger 00:05:14 Right, yeah, this is, more an idea I had, when I found out, that by default.
You have no service detector at all.
But in the old world, without declarative configuration, you had service by default. And I know we have a different philosophy in declarative configuration, but nevertheless, I was wondering if it would make sense to have service in there by default.
I actually started out with a, PR that only adds it to, to the agent, to the Java agent, and then we ended up in, yeah, well, this is not in the spec, so let's put it in the spec first before we do that.
That's why we're here.
Jack Berg 00:06:08 Well… I can… I can articulate the why behind this, but, you know, every time one of these situations comes up, it's… it's… I'm not… I'm not fully convinced of this. You know, every time somebody brings up one of these things about, hey, we should do this thing by default, whether it's, have a bunch of instrumentations enabled by default, and this is the presets issue, I don't know if you've all seen that presets issue by Robert, or, you know, I think you have another issue in this… in the notes today, Gregor, about propagators enabled by default.
Yeah, this is similar, right? Right, exactly. So, like, you know, should the… should SDKs do something by default, or, you know, trigger some behavior, even in the absence of You know, that configuration being present in a file.
And so, we recently merged a PR to, configuration.
that… you know, I guess codifies this convention we've been operating under, which is You know, what I've been calling what you see is what you get.
And so, let's see, where is this?
Did this… did this get merged?
GZ Gregor Zeitlinger 00:07:29 You're looking for a headphone?
Alex Boten 00:07:31 I don't think so.
GZ Gregor Zeitlinger 00:07:32 what you see is what you get. I see it right in…
Jack Berg 00:07:34 Oh, yeah. It's at the wrong level.
Right?
GZ Gregor Zeitlinger 00:07:39 Oh, okay, that's why I.
Jack Berg 00:07:41 Yeah, I guess I missed it. And I forgot that I put it up at the top. I was looking at the bottom here.
Right, so this tries to articulate, that, you know, to the extent that we can control it, the, the SDKs should configure things according to what is specified in the file, and not do things in the absence of, you know, particular properties. And… you know, like, what do I say here as an example? I say, okay, in this example, we have a pretty minimalist schema, and I've commented out meter provider. So I say, in this case, like, what's the closest analog we have to, you know, the absence of a meter provider? And that's a no-op meter provider, and that's what the default semantics say. If you don't specify the meter provider property.
The SDK should install a no-op.
I go on to say that it's… it's not always possible to follow this philosophy, and, you know, the example that I give is about attribute limits. So, you know, in this snippet up here, we don't see the attribute limits property.
But we still have a default for, you know, the attribute count limit of 128.
Right? So, you know, this is the philosophy, but, you know, I guess we can't always follow it. There are cases where the what-you-see-is-what-you-get philosophy is in tension with a safe default experience and with, you know, what the specification says we ought to do. So there's, like, exceptions to this.
GZ Gregor Zeitlinger 00:09:12 Yeah, I think, the… Safe default experience.
is both something I agree, but also that I have… that I struggle with, like, making a clear decision from, because, you could argue either way. Right.
Jack Berg 00:09:30 It's subjective.
GZ Gregor Zeitlinger 00:09:32 Yeah, yeah, for the Java agent, we have already settled on that we should have the distribution provider, always.
Because, without it.
it's much harder to troubleshoot, because it has the version of the Java agent included in it, and we did not want users to to report bugs without it. Service is, kinda similar.
Without service, instance, you have metrics that are, unintentionally aggregated or replacing each other, depending on your backend.
But, it was not enough so that we made a clear decision to include that.
Jack Berg 00:10:26 And just to kind of add to what you're saying a little bit, there… there's cases where… or… you know, you're talking about, hey, should we include the service resource detector by default? And, another place where the SDK is doing something by default, regardless of what's in the configuration file, is with resource. So, not with service… instance ID, which is the primary thing that the service resource detector populates, but, you know, where is it? Where's the… you know, even if you omit any information about your resource, we're going to include the default resource, which includes the telemetry, SDK name, language, and version, and also a default name, right? Like, what's the default service name?
GZ Gregor Zeitlinger 00:11:17 It's unknown.
Jack Berg 00:11:19 Right. Java unknown or something. Unknown Java.
So, I think there's… There's some, like, wiggle room to… You know, to indicate that something like a service instance ID should be part of the default resource.
And therefore, you know, kind of… Be an exception to this normal philosophy of what you see is what you get.
Right? So, like, you know, we have prior art for that, telemetry, SDK, name, language, and version. Like, arguably, a service instance ID is of similar importance.
GZ Gregor Zeitlinger 00:11:58 The service detector is also looking at an environment variable for Yeah, here it says, alright, auto service.
Jack Berg 00:12:07 Yeah, so two of them. The hotel service name, and then it generates service instance ID.
GZ Gregor Zeitlinger 00:12:12 Right.
Jack Berg 00:12:18 So two other, kind of, just things to think about with this.
This philosophy is, of what you see is what you get, is… We kind of have some other ways of, of nudging users in the direction that we want them to go, and, you know, that's our examples, so we want to push the SDK config and SDK migration config as the… as the starting point for users, and so the idea would be they copy-paste this, and then they modify it to suit their needs.
And so, you know, we do things like we, we set the propagator to be trace contacts and baggage. That's, like, the later topic, but I guess, like, interestingly, we don't include the service detector here in this default config. That's, like, another tool that we could have at our disposal, is say, like, hey.
this SDK config here, we're going to reference maybe all of these detectors, services included in there, so that would be, like, another route. I think the one problem with that route is that resource detectors are experimental right now, and so, like, not all implementations will support them.
I mean, even if they were stable, not all implementations would support them, because, you know, this is still very much under active development, but… I guess it would look a little bit strange to see a, you know, the… What would this end up looking like?
It'd look like, it texts…
GZ Gregor Zeitlinger 00:13:50 You can look at the blog post where I… I tried to… Have a good starting point.
Jack Berg 00:14:01 Yeah, yeah.
GZ Gregor Zeitlinger 00:14:02 I think it's… yeah, you already got it.
Jack Berg 00:14:05 Yeah, right, so that's what it ends up looking like, so… You know, maybe we do something like OS, container, Post.
Huh?
And, like, you know, I guess, do we care about this? You know, if we're gonna say that the SDK config and these starter templates are our recommendation for users. You know, it's arguable that we should limit them to only stable properties.
And so this is kind of at odds with that, but, you know, on the other hand, it's very important to have good user experience, so…
GZ Gregor Zeitlinger 00:14:41 Now, let me actually double-check what I have in the blog post.
This really has the… the development part.
Yep, it has, yeah.
I mean, the blog post calls out that the entire thing is experimental.
So, is it…
Jack Berg 00:15:08 Yeah, I guess for now it is. Kind of.
GZ Gregor Zeitlinger 00:15:10 Double experiment, or not?
Jack Berg 00:15:14 Yeah, right, but, you know, we're trying to go stable, so… I, I think…
GZ Gregor Zeitlinger 00:15:20 Even if we are… Even if we are stable, then, like… declarative configuration in the Java agent would still be experimental. That would not change just because we have the specs stabilized, in my opinion.
Jack Berg 00:15:38 That's true, yeah, it would take some time after the spec stabilizes for any language implementation to stabilize itself.
And, you know, personally, I'm okay with this, because, you know, it has limited downside. I'm just thinking out loud here, but, you know, if a language implementation doesn't support Resource detectors yet, or doesn't support any of these named resource detectors.
You know, it's not like… It… it's not like it'll crash.
you just won't get those extra resource attributes, and I guess that can be… that might be a surprising experience for you, but, surprising, I guess, isn't the end of the world for me.
Alex Boten 00:16:22 Yeah, I guess the… I guess the inconsistency would be… Probably… shocking to an end user, right? Like, hey, you told me I can use this config file to get the same experience across all these implementations, but… I don't really get a… And I'm not really… I'm not really sure what to do about it, you know what I mean? Like, if I'm just an end user and I'm trying to enable these… It's… it's not clear what the next step is. I guess… Yeah, maybe we need to be more… more clear on… the output from parsing the config file, saying, like, hey, these… these things have been configured, but they're not supported yet, or something like this. I don't know that we have… Any guidance on this?
Jack Berg 00:17:07 I think that's really tricky to do, so if you can play this out, like, let's say you have an implementation that supports version 1.0, and, you know, sometime in the future, there's 1.5 out, and there's a bunch of new properties that the implementation doesn't know about.
Because it's only on 1.0. And, you know, so the user specifies these new properties in their file, and the implementation If, like, along the lines of what you're saying, it's expected to be able to detect when something is specified that it doesn't recognize, and then, you know, log a warning about it, or something like that.
And, maybe there's an easy way to do that in implementations, but it seems pretty… My intuition is that it would seem pretty cumbersome to implement in, I can't think of, just off the top of my head, a way to do that in a really easy way.
Jamie Danielson 00:18:01 I feel like at that point, you're almost just as well off doing the implementation if you're already looking at the… Properties that are missing.
Jack Berg 00:18:09 Yeah, like… I mean, but maybe, Jamie, there's a way to, like, you know, automatically say, like, hey, unrecognized properties. Like, anything that isn't in this, like, known list of properties gets this warning, but…
Alex Boten 00:18:24 Yeah, I mean…
Jack Berg 00:18:25 To me, it seems like it would clutter the implementation.
Alex Boten 00:18:27 The collector does this today, like, if you're specifying properties that the collector doesn't recognize, it'll just return an error saying this is not a recognized thing.
Jack Berg 00:18:36 Oh, really?
Jamie Danielson 00:18:36 So, like, it doesn't specify that this is, like, not recognized, but not something we haven't done yet. It just is straight up, I don't recognize this thing.
Alex Boten 00:18:44 I don't know what to do with this property.
Jamie Danielson 00:18:45 Yeah.
Alex Boten 00:18:47 So, I mean, that… that would not be ideal, right? Because then you end up in the case of… If you have, I mean, then we would still have to handle the case of… Some configuration only applies to certain languages, and then, you know, then you have to have, like.
A special case around, like, the experimental instrumentation configuration, for example, to say, like, alright, ignore… ignore these properties that you don't know anything about, but under this other part of the tree, like, if you're getting… at the top level, for example, if you're getting properties you don't recognize, then you should do something about it.
But it's still… Not super clear.
Jack Berg 00:19:24 You know, Alex, what we could… another, like, option… this is good conversation, but, like, another option would just be to… you know, work to stabilize resource detection, and at least, you know, we have a variety of people that are implementing this right now across different languages, and at least agree on this, you know, set of four resource detectors, and have implementations in them. I think there's, like.
you know, 3 to 5 different people that are implementing this across different languages, and, like, that's a lot of momentum to go and say, like, hey, we have these 4 resource detectors all implemented in, let's say, 5 languages, let's mark the spec as stable and move on.
Alex Boten 00:20:05 Yeah. And then we just, like, you know, avoid this whole question.
Yep.
Jack Berg 00:20:12 yeah, so, like, I guess… this… we have this philosophy, what you see is what you get. It's… it seems like a good, you know, base philosophy to have, to… but, you know, I think there are some exceptions where it doesn't really… or at least I find myself questioning it, and, you know, propagators and resource detection is part of that, so I'm not exactly sure what to do about that. I still lean on the side of, you know.
Of this philosophy, but, You know, maybe there's a case to be made that we should relax that or change that, so…
Alex Boten 00:20:53 Yeah, I mean, I… I also like the idea of stabilizing with as much of this philosophy as we can, and if we get feedback from users that, hey, you know what, I'm tired of adding 3 lines of YAML to every one of my configs, and can you make it better? Then, you know, we can We can do something fancier in… 1.5 or 2.0 or something. Like, we don't have to solve all this before we get to… Stable for the 1.0 stuff.
Jack Berg 00:21:22 Yeah, and just… In case other people haven't kind of been following this conversation, so… in this… this comment here about what you see is what you get in the philosophy. There's, I note that, like, one of the ways that you can solve for the shortcomings of this is with higher order abstractions, like Helm. So… For example, if you go to… let's take the collector, for example, and host metrics. To configure the collector to collect host metrics, it's like 100 lines of YAML.
And that's really verbose and error-prone for users to, like, to specify. And so, how we sort of solve this with the collector is with standardization in Helm charts. And, you know, we published this OpenTelemetry collector Helm chart, which has, a variety of… what are they called?
called presets, and that's, like, exactly kind of what we're talking about here, right? So they have these presets where they have simple Boolean flags, which, when flipped, like, you know, the Helm templating engine spits out much more complex collector configuration.
Right? So, you know, I could imagine us in the future, you know, potentially when this is integrated into the operator better, because this is, like.
you know, declarative configuration is a great fit for the operator. That's what, like, people using OpenTelemetry instrumentation tooling without the ability to modify source code, this is what they want, is more expressiveness with how to configure things. And so, like, I could imagine us having Helm charts in here that allow you to, you know, flip you know, really simple Boolean flags to do, you know, common situations.
Like, maybe there's a Boolean flag for, you know, enabling all resource detectors, or something like that.
GZ Gregor Zeitlinger 00:23:15 Yeah, I see how we can use yet another tool to solve that problem, but I'm wondering… if it is actually a little bit too fast, if we declare it stable without having enough user feedback. And the public documentation that I have created is hopefully an avenue, to get such feedback.
But if we already declare it stable, and then everyone has to live with that until 2.0, then maybe we have given up an opportunity to clean things up based on user feedback.
before 1.0.
And my… My feedback is only just one, because I missed the propagator myself.
And it's probably more valuable to have feedback from users that have not been working on the topic extensively.
Jack Berg 00:24:16 Yeah.
you know, I mean, my thought on this is I hope that users are not… Writing configuration files from scratch.
Right? So, like, I hope they're always using one of these templates as a starting point, because there's all sorts of sharp edges if you're writing one of these things from scratch.
So the copy, paste, modify, I hope that we can, you know, push that in a way where it actually sticks.
I think the feedback from users, if we ask people point-blank, will be, like, no, I don't want to write all this. I want to write less, and I want, like, more magic to happen. But that's, like, at odds with other kind of goals, and so… Yeah, I know.
GZ Gregor Zeitlinger 00:25:00 This is not the question I would ask. It's more like, here is our documentation.
Instrument your service? What did you run into?
Jack Berg 00:25:13 Yep.
GZ Gregor Zeitlinger 00:25:14 And this documentation, that I created is something that, Can also be improved. But without it, there is, like, no starting point.
Jack Berg 00:25:26 Well, there's…
GZ Gregor Zeitlinger 00:25:26 I don't think any user has looked into The configuration repository, because it's… it's not really end-user documentation.
Jack Berg 00:25:37 Yeah, I… so, when you're talking about your documentation, you're talking about, Were you talking about, from the Java?
GZ Gregor Zeitlinger 00:25:47 You can also look into language and APIs. There are two entry points.
An SDK config.
This is, like, the general documentation, and then it has a link to the Java-specific part.
Jack Berg 00:26:06 Yeah, so…
GZ Gregor Zeitlinger 00:26:07 Right.
Jack Berg 00:26:09 I think what I would do for this specific thing is I would… You know, you have a recommended configuration file here, like.
GZ Gregor Zeitlinger 00:26:17 I would…
Jack Berg 00:26:17 directly embed.
And I know I had the opportunity to engage on this, so, like, sorry for not, like, engaging on this, but I would directly embed those, those starter templates in this documentation.
And so, you know, for example, OpenTelemetry.io has the ability to reference snippets, Right?
GZ Gregor Zeitlinger 00:26:38 Yeah, yeah, yeah, I know how this works.
Jack Berg 00:26:40 Yep.
GZ Gregor Zeitlinger 00:26:41 This would… this would, lose half my audience if I did that, to be honest.
Jack Berg 00:26:46 Well, there's the tension. It's like, you know, so, you know, you want something short and terse, right? But that's not what declared and Config is. It's like, it's… it's… exhaustive. It's, it's like, Kubernetes…
GZ Gregor Zeitlinger 00:27:02 Yeah, that's not true. The only thing I missed Really is to contact the propagator.
Other than that, it's complete. I mean, unless you point me to something concrete that I'm missing.
Jack Berg 00:27:15 Well, so, like, what it doesn't provide is a good launch point to configure additional properties, right?
GZ Gregor Zeitlinger 00:27:22 That's what I'm explaining below, that if you need more, then go to those, and then I'm actually pointing to those Both… two of those files.
Jack Berg 00:27:32 Well then, maybe there's… maybe there… so, okay, so maybe there's something to this. So you want something that is… That is the absolute bare minimum.
Because you don't want so much content that the user has to scroll for a long time and get intimidated. So maybe this is, like, a third starter template.
Right? So this is like the… it's like the bare bones, or like the absolute minimalist. And, you know, we could have that still in the configuration repository in examples, and we.
GZ Gregor Zeitlinger 00:28:00 Yeah, I think that's a good idea, yeah.
Jack Berg 00:28:02 And reference it as a snippet still over on OpenTelemetry.io, so everything stays in sync as well, because that's, like, the benefit of snippets.
GZ Gregor Zeitlinger 00:28:10 Pride.
Jack Berg 00:28:14 But yeah, like, you know, I think, just to go back to something else you said, you know, I don't think… you said, I don't think a lot of people are coming over to open telemetry Configuration, because it's not meant to be end-user facing.
I agree. It's not meant to be end-user facing. I'm sure… I've talked to you about this, but I'm sure other people have been following this as well, so I've been working on this… this schemaDocs, this thing called the metaschema.
And the meta schema is just, like, you know, a place where we track other bits of information that don't fit cleanly into the JSON schema. And one of the outputs of the metaschema is, you know, generated markdown, so human-readable form of all the information that is packaged up in the JSON schema and the metaschema.
And so, like, this is the type of thing, I'd like to see this synchronized to OpenTelemetry.io, too. You know, it is a long page, because we have lots of types in our schema.
But it's, you know, it's navigatable, and it's a very complete reference. So maybe it doesn't live on this, you know, this homepage in here, but maybe it's like a, you know, another page that can be referenced for… for users to navigate around there. So that's kind of my vision there. But, I'm working in the same angle, Gregor, of trying to Have more user-facing documentation.
GZ Gregor Zeitlinger 00:29:46 I guess you're leaning towards not… Adding a service detector.
As default, then.
From summarizing the… last half hour.
Jack Berg 00:30:00 It's… that… that's my position, so, like, here's what… here's what… I'll just write it down in notes, Jack's position.
you know, I would… Add, detection, development, To all the starter templates.
And include standard detectors, which are, you know, resource, OS, host, and container. So I would, you know, those aren't stable yet, but they're really important, and I, you know, I would include those in all the starter templates. I would add, a minimal… A minimalist starter template.
Two examples.
And reference this.
in the OpenTelemetry… dot IO docs.
And then, what else would I do? I guess I would also… That minimalist starter would include the standard detectors as well as propagators.
And then, you know, also, publish… schema.
docs.md to opentelemetry.io.
As supplementary information for users.
So that… that's… that's how I would handle this, but, We don't all have to have the same.
GZ Gregor Zeitlinger 00:31:46 for me, then, then I'll close this pull request and… Can always come back to it, based on user feedback.
Jack Berg 00:32:02 So, do we want to talk about propagators, or did we kind of cover that in the first topic? Because… We kind of went down the rabbit hole.
GZ Gregor Zeitlinger 00:32:12 I guess it will be the same. I still think it would be good, but yeah, we had the discussion.
We don't need to repeat it.
Jack Berg 00:32:24 Maybe it makes sense, like, I don't know, like, you know, the… the place where this… Actually, where the defaults, you know, are documented is… We have the… the metaschema file.
And then we have propagator.
And this is the exact… this is, like, where we talk about the defaults.
So we say, hey, the values that you can talk about are, you know, trace context, baggage, etc, etc.
If it's empty, a no-op propagator is used.
Like, we could change this text to say, if it's empty.
Trace contacts and baggage are used.
Jamie Danielson 00:33:12 I was gonna say, I almost have a stronger opinion with propagators than I do towards the service detectors mentioned before, the resource detectors. Like, propagators have been kind of a thing, especially since so many people don't actually understand what that is.
And I feel like that has been a default in everything, is to have, like, trace contacts and baggage.
Because of the W3C headers.
So I would be in favor of that. That's all my data point is there.
Jack Berg 00:33:38 It is the recommended default for the environment variable configuration as well, right? So, like, this is another case where the what-you-see-is-what-you-get philosophy is in tension with the defaults from the specification. And so, you know, what do you do in that situation?
do you rigidly use your… the… what you see is what you get, or do you, you know, make an exception for this case for improved usability? I think we're gonna… this is gonna be a recurring concept.
Alex Boten 00:34:07 I mean, in this… in this particular case, the… there's some text in the specs, specifically around, like.
Platforms may pre-configure an out-of-box propagator. If pre-configured, propagator should default to, like, the W3C and baggage.
I guess… I guess the question is, you know, do we… do we consider a config file The same as pre-configuring things.
And, I guess… If we're gonna be pedantic about wording, I would say no, because this is exactly what we're doing here. We're configuring things.
So, I mean, I guess what I'm saying is if we wanted to change the default here, we should also consider making a note of this in the spec itself. This is the part I'm reading about.
propagators.
Jack Berg 00:35:06 I'm not… I'm not… You know, opposed to changing the defaults on propagators in principle.
I think whoever opens that PR, if you're gonna open it, you know, what you need to describe is, you know, how a default, which is non-empty.
interacts with the fact that we already have two ways to specify the propagators. We have this, like, composite list.
Which is, you know, available for backwards compatibility with the hotel propagator's environment variable. So it's just like a string property, and, you know, the expectation is that implementations parse the comma-separated string.
And then we have this sort of structured approach, which is consistent with, you know, declarative config and YAML and all that. And so, like, you know, we already have two properties which are merging together to, you know, spit out the resolved propagators, so, you know, what you'll need to specify is how A default of non-empty interacts with these.
And it'll be a little bit tricky to word, but I think it's possible.
Maybe it'll be confusing for users, but…
GZ Gregor Zeitlinger 00:36:16 There's another possibility I had thought about, that is if you leave out the entire a propagate a block, then you would say, if the block is left out, then it defaults to the block that has the composite composite.
Filled with the two default propagators. That would, still allow users to have no propagator at all.
If they really wanted to.
Jack Berg 00:36:45 Yeah, yeah, exactly. So that's, like, another way to handle it, is maybe to say that, you know, the… and this is the open telemetry configuration, the top-level type. So, you know, if you omit the top-level propagator property, then, you know, what you just said is the behavior trigger. But if you include it.
As soon as you include it, you have to specify your actual list of propagators, or else it defaults to empty.
GZ Gregor Zeitlinger 00:37:10 Yeah, I think this would also match the… what you get is… What you see is what you get philosophy, because if you set something to an empty list, then it really is an empty list.
Jack Berg 00:37:23 Yeah, maybe that might be a way to have our cake and eat it, too. To have it both ways.
Alex Boten 00:37:29 Right, but if we don't have… But then the behavior will be inconsistent with other blocks, right? Like, if you don't include a logger provider, you're gonna get a no-op logger provider, not a…
Jamie Danielson 00:37:40 Default, hey, it just works, longer provider, which…
Alex Boten 00:37:44 Again.
Jamie Danielson 00:37:45 Consistency is pretty good here, but…
Alex Boten 00:37:48 literally, as we're talking about it, I might have just walked myself in a circle, also. Right.
Jack Berg 00:37:57 Well, if anybody wants to open that PR, I think we're all kind of up to speed and, you know, all know of the different things to be aware of in sharp edges, so, Yeah, open a PR, make the case.
GZ Gregor Zeitlinger 00:38:12 I think I like that, yeah.
I was still thinking about the analogy to… to exporters of that… If I… Believe that it's different or not.
If you leave it out, it's a no op.
Exporter… How is that different?
Isn't the noop exporter not the default?
Jack Berg 00:38:40 Noah, if… if you omit meter provider, logger provider, tracer provider.
we're going to give you a no-up, one of those providers. We will not configure a functional meter provider with a periodic metric reader with an OTLP exporter.
GZ Gregor Zeitlinger 00:38:57 And does this spec say what the default exporter is?
Jack Berg 00:39:02 The… It's… It says it in the context of, like, the environment variables.
But, like, I don't think it's opinionated about This type of thing.
like… if you initialize, and let's say, like, what do you think the spec would say about this? I'm initializing an SDK, And, with the programmatic Configuration API.
And I don't specify anything. I don't specify a resource, I don't specify readers, I don't specify, like, an OTLP exporter. And I'm using the programmatic API.
like… is the expectation that if I don't do any of those things, that I still get a, you know, a functional meter provider with an OTLP exporter.
I mean, I know our interpretation of that in Java is no. Like, you have to explicitly configure a processor with an exporter. You have to explicitly configure a metric reader with an exporter.
GZ Gregor Zeitlinger 00:40:09 Other languages take a different stance. Do they? If I remember correctly.
Jamie Danielson 00:40:14 I thought Java did too, actually.
not talking about strictly meter providers, I think that's a little bit more complex, but at least in terms of, like, I thought that became the default for everything. If you don't specify one way or the other, everything is enabled by default, with… used to be OTLP gRPC exporters, now is OTLP HTTP.
Jack Berg 00:40:35 Now, if you just do this, like, if you just, like, build a tracer provider, and you don't explicitly specify anything, it's a complete no-op.
Jamie Danielson 00:40:44 I think thinking of, like, zero-code config in various languages. Like, if you're using the agent.
Jack Berg 00:40:51 Right, exactly. And so, like, you know, where does this fall? Is it closer to the programmatic configuration API, where you have to explicitly, like, add a processor, or is it closer to environment variables, where there's lots of defaults in Magic that are, you know, automatically imposed on you?
GZ Gregor Zeitlinger 00:41:11 Yeah, I guess it depends on whether you see this as a replacement for environment variables or not.
which I kind of, like, Like to explain it to users, but that's not… An argument that beats everything else.
Jack Berg 00:41:30 Right.
Jamie Danielson 00:41:36 So it might just be what we said at the start of, need a little more time to think about it, and if someone opens an issue or PR, then… We talk more on that, because I feel like… I keep going in circles anyway, and I don't know if other people feel the same, of there's valid… opinions all over. There's a lot of subjective…
GZ Gregor Zeitlinger 00:41:56 I think, Jamie, you had a good point about propagator being a little bit different, because it's harder to understand for users.
They might not even know what it is, but an exporter is something that is That is, like, closer, because you know that data has to go to your backend somehow. So I still think we can defend changing propagators, even if we leave exporters as they are, or if we don't Know exactly if what exporters are one or the other.
Jack Berg 00:42:39 Yeah, let's, if you want to open that PR, let's see what the other people think.
I do feel, you know.
it's sort of a slippery slope situation. Like, once you compromise a little bit on this what-you-see-is-what-you-get philosophy, you start wondering why you're not doing it in other places as well.
And then, you know, you end up with a configuration interface which is extremely terse. You don't have to specify anything at all, but there's all sorts of magic attached to it. And so, like, I think when you play out that.
You know, you end up with a user experience which is Full of magic, which… and ends up being not… is intuitive, even if it is less verbose, but I'm just one person's opinion.
GZ Gregor Zeitlinger 00:43:31 So, knowing what we have in the, and the current form of the documentation, I… I'm not afraid of this slippery slope.
Because I… I think this is somehow related to lists.
That… that are hard to get, and propagators is also a list.
But it's a very special list.
Also, only my opinion, of course.
Jack Berg 00:44:01 Right.
Alex Boten 00:44:06 Looks like there's a spec issue that needs attention.
GZ Gregor Zeitlinger 00:44:10 Yeah, I actually didn't know if I wanted to include that, because this is not the only one.
That, I have not gotten around to, because I was working on other parts of declarative configuration, but I… wanted to ask if someone wants to work on it. It's not the only one, but I did not want to include A bigger list of things to distribute.
This is… one is particularly thorny, because it has a very long history to it.
The spec issue… Either that one or one that links to it is multiple years old.
Jack Berg 00:44:51 Oh yeah, this is… this is gonna be thorny for sure.
I think, you know, the problem with this, in a nutshell, is that for us to have authenticators in declarative config, you need to have an… in the spec, a new concept of a new, like, SDK extension point.
called Authenticator. Like, that concept needs to exist in the spec. And for that to exist in the spec, you need to get everybody to agree on what the API is for an authenticator.
And, you know, it has to be an API that makes sense across all the languages and ecosystems, and I think there's… like, the thing going for us is that there's something called an authenticator in the collector, and it's been around for a while, and there's a lot of examples of it.
So that's good. You know, we could lean on the collector for prior art, but, you know, I was actually just digging into the collector's code about this yesterday, or it's Friday.
To see how they did this, and… the collector benefits from being built on top of Go, which has a, you know.
you know, there's an HTTP client, which everybody uses, and so, you know, they can expose an authenticator leveraging this concept called a roundtripper. And this roundtripper is built into the Go language. And, you know, it's essentially an API for something like an authenticator to be able to influence a request and a response.
It's very, very nice.
like, what's the language-agnostic equivalent of that? That's, like, the question that's going on in my head. Like, what…
GZ Gregor Zeitlinger 00:46:29 I have one, I have one.
Jack Berg 00:46:31 gut.
GZ Gregor Zeitlinger 00:46:32 It's the prototype implementation.
that I have that is delegating all the work to the user, so it doesn't actually do anything.
But, if you have, someone taking advantage of it, like the gRPC authenticator, then they can, do anything with it. It's basically just a callback.
Jack Berg 00:46:59 But what does the callback have access to?
What can the callback influence about the request and the response?
GZ Gregor Zeitlinger 00:47:06 Let me… open that. It's not linked here, I don't see it, but I still have it.
Around… Let me edit to the book.
Alex Boten 00:47:22 At the very top.
Of the, the possible now?
That second sentence that you just highlighted, Jack, it has a link at the end.
GZ Gregor Zeitlinger 00:47:35 Here, it's the one. I don't know if it's the one that I linked.
Jack Berg 00:47:41 Did you send it in chat?
Yeah, okay.
GZ Gregor Zeitlinger 00:47:43 To the document, I edited it right there.
Jack Berg 00:47:45 To the document, okay.
GZ Gregor Zeitlinger 00:47:51 It's, it's a really small one, so it, Not difficult to understand, but I might miss something, of course.
Jack Berg 00:47:59 Yeah, so this… this is the… this is what you're saying the interface is, is, like, an authenticator has the ability to add headers to a request.
GZ Gregor Zeitlinger 00:48:09 Yeah, I think that was it.
Jack Berg 00:48:11 And is that sufficient? Like, is… would all the authenticators in the collector be able to be expressed just via this API?
Is that all they're doing, is, like, you know, providing headers which are appended onto requests?
GZ Gregor Zeitlinger 00:48:28 I would suspect no. Yeah, I think this is how the specification issue evolved before I, did not follow it anymore, and that there is use case X, Y, and Z that people have also tried, to argue before, and, Then I was wondering… Can we really… have a spec for every possible use case, because that seems, like, really hard to do, or is there some way that we can start with something easy, like in this PR, and then evolve it over time?
Jack Berg 00:49:09 Yeah, I… I mean, I like that approach of iterating, just landing something simple, and then, you know, having people open issues and say, like, look, this is insufficient, we need more.
So, you know, Yeah, if you want to lead that approach, that'd be great, right? I would support it. I would give my thumbs up if you proposed an authenticator in the specification, you know, that just had a simple interface.
GZ Gregor Zeitlinger 00:49:41 I had tried it, and, I… Was not able to navigate the maze.
But, I would be glad to team up.
Jack Berg 00:49:57 Yeah, hey, we can coordinate now, we work together.
GZ Gregor Zeitlinger 00:50:00 Right.
Jack Berg 00:50:06 Alright, So, let's talk about that offline, Gregor, and if anybody else is interested or has feedback, watch out for the issues and potentially PRs on this. So, lend your opinions.
Alex, you wanna jump in front of me?
Alex Boten 00:50:25 Sure. Shouldn't take too long.
I know at some point in the past we decided against using the JSON schema field of description.
I'm trying to go back in the other direction.
I can see you have opinions already, but I'm gonna finish saying the thing that I'm gonna say about it, so… Yeah. Two reasons I really want to use the description field. One, I want my code generator in Go to be able to use it to generate the doc strings, because it just works.
Jack Berg 00:50:53 Yes.
Alex Boten 00:50:53 And also, I want my IntelliJ to be able to, like, auto, tell me about things like description fields from the JSON schema itself.
So, these are the two things that I'm, excited about.
And that's kind of why I'm proposing going to add description back into the schema. I'm… I have a bigger PR than this, but I haven't included it here. That also updates, like, the tooling that you guys created, Jack, around the meta… meta schema.
docs, so, I think… I think it can all work together, now that we have all these tools in place. But I just wanted to collect feedback on whether or not this was a good or a terrible plan, and Before I do any more work.
Jack Berg 00:51:36 I wonder if you and me are actually thinking the same thing, because… so this was, this was something that, Tyler brought up when I was, like, initially talking about the meta schema, like, a couple of weeks ago. It was just him and I on this meeting, nobody else showed up.
And he was like, yeah, it'd be really great to be able to leverage this metaschema information in CodeGen. And I'm like, yes, it would. Of course, that'd be fantastic, because, you know, the artifacts that you generate using CodeGen.
They end up being, like, you know, something that users interact with, and they read their property descriptions and the, you know, the comments on there, and they're gonna… Expect those to contain useful bits of information.
And… and so I was thinking about this, like, how do we make this work? And, like, you know, just, like, a week ago, I was thinking, like, hey.
What if we… Like, okay, so this, you've illustrated perfectly the issue with embedding all this information in the JSON schema. It's an editing nightmare.
Alex Boten 00:52:36 Right? You have to, like, you don't get the nice typing that you get with YAML and, like, line breaks and things like that.
Jack Berg 00:52:44 so, how can we get the best of both worlds? Like, what if we output a JSON schema where the metaschema information has been enriched into the JSON schema.
So we get the best of both worlds. We maintain the descriptions in YAML, so we have, like, you know, all of the nice properties about, you know, enforcing that certain bits of information are there, like the default semantics.
and that the description is there, and things like that, and we get, like, nice line breaks. But we also get the ability to leverage its information in CodeGen by, you know, generating an alternative JSON schema, which has been enriched with whatever else we want in it.
Alex Boten 00:53:26 Yeah, I mean, I guess I could see it going both ways. You know, I could see the… Yeah, I agree that the downside of maintaining this is that the line breaks are not the way you want them, and that's… that's unfortunate. The downside of maintaining it through like, a description field through the metaschema is that anyone who's familiar with JSON schema has no knowledge of what metaschema is, and so for them to have to learn, like, a whole new… Tooling set, just to be able to edit, like, a file inside a repo becomes a bit tedious.
Yup.
I… I don't feel strongly one way or the other. All I feel strongly about is I want this description field to exist. That's… that's my only… that's my only outcome that I want here. So if… if, you know, if people agree that we want to… generate this from the metaschema, I'm okay with going in that direction. If people feel they want to take the description out of the metaschema, I'm okay with that direction. Like, I don't really care one way or the other at this point. I just want the feel to exist.
Jack Berg 00:54:31 So, so I have a PR that's open, which… I think is important for this conversation, and the PR is… is about splitting out the default behavior from the description field in the metaschema. And so, like, you know, if we look at metaschema types.
Every type in here goes from… Like, where's a good example?
Every type in here goes from having, you know, a description, To having a description, and… at least one additional field, which is the default behavior, and, you know, for… there's details in the PR description, but there's a second optional one, which is null behavior. If you want to differentiate between, like.
the property is omitted altogether, or it's present and null . Sometimes you have different, behavioral semantics you want for each of those cases.
And the tooling that I've added, forces you to specify a default behavior if a property is optional.
And this is really important because, like, if you go look in this, like, when you just add this description in here, you know, you're… as part of this description, we have default semantics here.
But it's just… it is completely unrealistic for us to… Be error-free on always ensuring that we've talked about the default behavior, without tooling.
Like, we are going to make mistakes, and this PR shows all the places where we have made mistakes, because there's, like, a million places where we haven't described what to do by default, and we need to articulate that.
Alex Boten 00:56:11 Yep.
Jack Berg 00:56:12 And so, build tooling can help give us more rigor around, like, ensuring that we, you know, define all these things, and then, you know, what I could see us doing is you know, producing a combined description. You know, a description that includes, like, you know, the content in the description and the default behavior.
whatever else we want to talk about, and, you know, renders it into, with, like, line breaks and everything, into the JSON schema, so it can be leveraged in… in code generation.
Alex Boten 00:56:42 Yep.
Jack Berg 00:56:43 I agree with what you're talking about with, you know, it's frustrating for users to, you know, come into this repository and have to learn a new bit of tooling just to edit a description.
I don't know what to do about that. That's definitely, like, a true statement. But, you know, it's also true that we absolutely need to have rigor around making sure we define default semantics for all of our… I don't even know how many properties, but it's got to be in the hundreds, so… and build tooling is the only way we're gonna, you know, have that.
Alex Boten 00:57:20 Yeah, I mean, they, you know.
We're gonna be running out of time soon, but… So I'm okay with continuing this conversation asynchronously. I think it's… I think it's really important to have, And we can kind of go from there. I'm… like I said, I don't feel strongly, one way or the other, about how we implement this. I just want to make sure that people are on board with adding this field, and then I will… then I'll continue to work on getting this PR in a good place, and… apply whatever review, feedback I get, so… Do you wanna… do you wanna talk about snippets? We have 3 minutes.
Jack Berg 00:58:00 just really briefly, I want to get this idea in people's heads. I have some… some code that I've been messing around with on my local machine, I haven't pushed it yet. But, the, You know, right now, we overuse kitchensync.yaml.
it's, like, it's in everything, right? Like, it's our way of verifying the schema, you know, is doing what it's supposed to, it's our way of documenting all of the surface area of the schema.
And it's just a terrible user experience to have to go look for your property in the kitchen sink and, you know, just to see how you might actually use the configuration interface to do a particular thing.
And by definition, like, in certain cases, it's incomplete. Like, we can't articulate all of the configuration surface area in the kitchen sink. We cannot demonstrate all of it.
And so, what I'm suggesting in this PR, and I have some code that does this, is, like, a new concept called snippets, and a snippet would be just, like, a tiny bit of YAML that demonstrates a very, you know, small, you know.
piece of configuration in isolation. So, like, you wouldn't have to show the entire, you know, configuration interface, you could just show one sampler, or you could just show a view that does a particular thing, or how to configure an exporter to do a particular thing.
And, you know, I've got some ideas about how we can link these snippets up into the meta schema and the docs generation, so we can, you know, have these part of the user experience of discovering you know, the schema and how to use different things, and I think it would improve our that didn't… a variety of things from the user experience standpoint. Maybe, Alex, maybe this could be another thing that got dumped into the description field, and could be leveraged in CodeGen as well. Like, if you could have… how cool would that be if your code gen could show, like, a little embedded snippet of YAML on how you can actually, like, you know, like an example of this thing?
Alex Boten 01:00:05 Yep.
Jack Berg 01:00:06 cotton.
Anyways, that's the rough idea.
I got some code, I might, like, push a draft PR, just so I can, you know, start to articulate some of these ideas and get some feedback, so look out for that.
Alex Boten 01:00:20 That sounds great.
I fully support that we can explain use cases through snippets, as opposed to just saying, oh yeah, don't worry, go… you want to configure a propagator? Go check out Kitchen Sync, it's got one. Go look for it.
Jack Berg 01:00:33 Yeah, just go scroll through 2,000 lines of heavily commented…
Alex Boten 01:00:38 Yeah, I grabbed through the code.
Jack Berg 01:00:40 YAML slop, and find the thing you want.
Alex Boten 01:00:44 Alright, we're out of time.
Jack Berg 01:00:45 Alright, thanks, everyone. Thanks, everybody. Good talk.
Jamie Danielson 01:00:47 Thanks, all.
