SIG: Specification SIG
Date: 2025-08-05
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 01:29 Hey, folks, I'm a little late, the waiting for Zoom to catch up with me here on my computer. I need to close some tabs.
Okay.
Alright. Can you all hear me?
**Trask Stalnaker** 02:00 Yeah.
**Josh Suereth** 02:02 Good.
Alright! My turn to run this one today. So apologies for being a little bit late, feel free to add your name to the attendees list and your items to the agenda right now, we only have about 25 min. So yeah, if you if you need more time.
feel free to add it.
We'll give another like 2 seconds for folks to do that.
Okay, let me change this to fit cool while we do that, Robert, you want to start.
**Robert Pająk** 02:49 Yes, I can start so this is just a next call about the Pr. Which I think I presented 2 weeks ago. So it has. If you open it, it has like 5 approvals. I've addressed all the comments. I think it's also not anything is more like a clarification to make everything more obvious. So I think it's good to merge. And I also wanted to call out what are the next steps that we are planning to address. So basically, this is also a preparatory preparation or follow up. I don't know messages, communication documentation pairs, or whatever maybe blog posts that we want to extend these attributes, and if they'll be extended, then they will be then the proto will have a minor bump, basically that we see that adding additional attributes is a minor bump. But this is not the scope of this. Pr, I just wanted to add more context to this one.
And yes, and that's all. From my side. I saw that Grant was asking, can we repeat it only once?
We could consider it.
maybe in the definition of the key value. But I I didn't want to do it. The reason is that in the log record where key value is used this kind of language does not apply. That's why it's copied in all the places except the log attributes, where where all of these kind of byte arrays empty values array values, K values. Maps are allowed.
That's why.
**Tigran Najaryan** 04:42 Good good call. Yes, makes sense, I agree. Agree. Yes, ignore my comment.
**Robert Pająk** 04:47 No, I do not ignore it. Thank you.
**Tigran Najaryan** 04:50 By the way, Robert, you you, I guess, since you mentioned minor version bump, we all of the releases from the product report so far, or most of them have been with a bump of a minor version number, which is not an indication of, I think hasn't been consistently used as an indication of anything of significance. As far as I remember.
**Robert Pająk** 05:14 Yes.
**Tigran Najaryan** 05:15 Which I think is fine. I I just wanted to make it clear that this we we don't necessarily want to use that version change as a signal of something important. We probably need to indicate it by some other means, to to make it clear.
**Robert Pająk** 05:31 I see.
**Tigran Najaryan** 05:34 Like, if you look at the past releases, that is, there's there's all. Almost always. We. We were pumping the minor version number.
**Robert Pająk** 05:41 Yes.
**Tigran Najaryan** 05:42 In very like rare cases. If there were some typos and stuff like that, we only bump the patch version number. But normally minor version number increase was not used as indication of a of a significant change in the in the semantics or the meaning of the problem.
**Robert Pająk** 06:01 The reason we're in.
**Tigran Najaryan** 06:02 Let's make sure now we we also signal it by some of our other means. That's all I'm saying.
**Robert Pająk** 06:07 I see, because right now the specification says that extending the attributes requires a major bump. So it's about communicating this well that we do not see this as a major version. There is an issue which, if you go back to the to the docs, to the meeting notes, Josh.
which is about adding this new attribute types. If you have any ideas, proposals how to communicate the changes.
whether it's blog posts, whether it's in some concrete, you know, place in the documentation specification proto repository. I think any ideas will be more than welcome.
**Tigran Najaryan** 06:52 So communication wise. I think you need to consider 2 things. One is the external communication outside open climate to the users of open climate, and the second is inside, particularly to the maintainers, who have, if they need to reimplement anything inside the sdks and the Apis for the internal communication I found in the past that what worked well was to go and create individual issues in every single language repository, that essentially would be a repetition of the same thing, saying, this has changed in the specification make a corresponding change in the in the language implementation. Right?
I found that the Maintainers appreciated that you have to go create 10 issues of exactly with the, with the same wording essentially.
But that that helps track whatever is happening. And you can just reference, all 10 of those in in a catch, all sort of a summary issue at the spec report. You can even track progress by by looking at that. In that case.
**Robert Pająk** 07:53 Do you think an issue like prepare for adding new attributes? Types make sense like? Because right now there's nothing to do but just like kind of. I don't know validation issues. Or do you have any other proposal?
**Tigran Najaryan** 08:08 I'm not sure what exactly is expected of the of the implementations. They're supposed to add the ability to model the Yes flex attributes right.
**Robert Pająk** 08:18 Yes.
**Tigran Najaryan** 08:19 So that's I think that's that's exactly what you want the the issue to say, right?
**Robert Pająk** 08:24 Okay.
Thank you.
**Tigran Najaryan** 08:29 Sure.
**Robert Pająk** 08:30 Any other comments.
**Josh Suereth** 08:31 To jump on what Tigran was saying, though I think if we're if we're gonna look at the communication here.
the internal, I think the consumers of this data are is is the main thing you're trying to figure out how to communicate to. And so the internal one, the collector would be the most important one to communicate with, of saying, Hey, expect this data? I think they might already do. But to to the bug that you were reading, and the thing that I think makes me nervous about communication and thing to think about. How do we communicate to external consumers like, you know, people who support the open telemetry, protocol, or databases, or or all of that right?
yeah, that's that's the question. Here.
**Robert Pająk** 09:15 My only idea so far was the blog post.
**Josh Suereth** 09:19 Okay.
I yeah, I I don't have better for you off the top of my head. I just like to to the the bug and the thing you're saying, I just wanna make sure we're focused on that to me like it's it opening. The ticket stuff is fine and we can control that timeline. But I feel like the external one needs to happen 1st to make sure people are aware before the internal ones flow fast.
like, if you're gonna order the 2.
So yeah.
**Trask Stalnaker** 09:48 For external communication. your previous recommendation, which I think is what Robert's following here is to basically use the proto change log as that communication, mechanism.
**Josh Suereth** 10:07 Assuming that anybody who's consuming proto should be following that change log.
I I think that's a minimum. Yeah. And I think it's a good thing to do. I'm just saying like to your question, of what other communication should we use? I think you're doing all the right things so far it's more. Is that enough? We'll still have people not know what's going on, and that's not. That's not on us right. But but as long as you're using the right communication channels. That's all I'm saying is in terms of the 2 things I'm worried about. The external one is the one I'm far more worried about making it out and change log should be good. External blog post is good. The other thing I I heard Tigran say that might be worth another discussion is, what does a minor bump on the proto mean?
And do we need to start advertising to people that these happen right when proto, when profiling releases.
there will be a significant need for people to advertise. I support version X versus y.
and we don't like that's the that's the piece of this that is in my head, Robert of like, you know, Prometheus says they support Otop. What version does the Otlp ingestion have all the vendor list of supported Otlp. What version is that?
We don't really advertise that today. And then maybe that's something we need to start doing like part of your your ticket. Maybe we need to split it out and like make a place for people to advertise the version. They support that sort of thing. Anyway, I'm I'm derailing this conversation a bit, but just calling out my my concerns there, and not things that would block what you're doing now, because I think you're taking the right steps now.
**Robert Pająk** 11:48 I think there were important comments still, even for for as part of this issue.
they're just more common for other problems. One thing regarding external most probably I'll be also speaking at Kubecon and and I, so probably I can also give it during a presentation. I think it also, is it an opportunity? Yeah.
okay, I think we can move to the next one. Thank you for your all your feedback.
**Josh Suereth** 12:17 Cool. Trask. Do you want to take it away?
**Trask Stalnaker** 12:20 Yeah, yeah, grab the right screen here.
cool. So in the log, Sig, we've been moving forward with minimum, basically how to do log filtering, or like? What is the equivalent of sampling trace sampling in the log world?
and so the 2. There's been a couple of things that have come from that one has been the work of adding that enabled method to the log processors. And that can be used for filtering. Now that's still in development.
and so what I was trying to do here is take kind of the 2 most common at least in the SDK world. Filters that users want to apply to logs and figure out how to model those using our existing spec work.
So those 2 are minimum severity and trace based minimum severity is just what it says. Trace based is cap. Don't filter it out if it is part of a trace that has been filtered out.
And so we can get into the details of those 2. In particular, there's a couple of interesting questions about defaults, for what to do with severity. 0 and what to do with logs that have no trace. Context.
But the thing that I primarily wanted to get in front of this group is today is there's 2 different proposals I've written up.
One uses the the log processors and the enabled functionality on the log processors.
And so the way that the log processors work with the enabled flag. Currently right. Our processor list is a list. They're not chained but really, for this kind of to model these. Well, you need to chain them. You chain your minimum severity, filter, your trace based filter in front of your batch filter, and you can have, of course, then, you know, if you're exporting to multiple endpoints. You would have another one of these chains below here, and you could have different severities and decisions there.
So this works nicely. I have a Poc in Java for it.
But there's another option that I think is nice also.
And there's different trade offs, and I'm not convinced that they both. I mean, it's possible that both of them make sense, and in the long term we might want both of them for different trade offs.
but also I'm don't love having multiple ways to do something. So this is the other proposal on the table right now.
Which is not using the The log processors for this implementation. I do think this proves out the is a nice poc, and proof that the log processor enabled stuff does work and so if people want to do like custom filtering it gives them a nice way to do that with the enabled functionality.
This one, I kind of think, feels a little bit more user friendly to me.
Looking at the declarative config. It. Piggybacks on the existing logger configurations.
Allows you to do like wildcard logger support, which is something that's already built into the logger configurator and we currently have enabled and disabled on these.
But you could do something like this. Set minimum severity info for this logger.
or these, this sets of loggers different one for this sets of loggers.
Certainly, coming from the Java world, and log for J. etc. This very much mimics that behavior.
Which is, I think, nice.
the other thing that is kind of nice about this, as we have been exploring in the Java Sig dynamic configuration via OP. Amp.
Where we would, we will. We want to support dynamically updating certain things in the configuration and one of the 1st things that we will are are supporting is the tracer configurator, and enabled, disabled by tracer name and enabled, disabled by logger name and this I'm not sure that trace based is something that people would necessarily want to flip on or off dynamically. But certainly the minimum severity is something that would be very nice to be able to do dynamically.
yeah, Robert.
**Robert Pająk** 18:44 I have a question regarding this OP. Dynamic changes. Is the scope planned that it will be possible to change all the configuration, including processors or not, really? Or is it just a subset that will have dynamic support.
train support.
**Trask Stalnaker** 18:59 I'm yeah. I I don't think we know the answer to that. we're starting small with things that are easy to change dynamically, without needing to throw away the entire SDK and rebuild the entire SDK and, as Tigrin says in chat you know, there's potentially some both rough edges and maybe increased security worries, if you allow updating too much. Yeah, thanks. Tgreen.
**Tigran Najaryan** 19:39 Yeah, there's there's some wording in the spec of it that worries about not doing too much dynamically from the remote sources.
Oh, I think really revolutionary there, just common sense.
**Trask Stalnaker** 20:01 So one thing, as Robert points out, that you can't do over here is applied different decisions to different pipelines. So if you're doing if you have exporting to multiple pipelines?
And so that's where you know. Maybe also, having this could make sense. Certainly, in the multi pipeline case you could implement this, but I think Robert's point was like in the collector. For example, multi pipelines is a very common scenario.
And so would be nice for collector users to have something standard.
**Robert Pająk** 20:46 It will be good. Also, the Collector Maintainers pick up here because my, maybe what I'm saying is wrong somewhere, but it needs to validate. My, you know my comments and feedback.
**Josh Suereth** 20:58 So I'm going to jump in quick. But this reminds me a lot of Jaeger remote sampling.
if you will, and how that configuration looks the the this proposal. I like this a lot. Very use case focused. Very. I think this is way more user, friendly.
And so we should encourage this one thing that I would think about, for, like the collector.
is, instead of just being like logger based, have an overall override on the resource.
So like Jaeger, remote sampler, your sampling configuration right is on service which is akin to the resource.
So you you could say, like, instead of thinking, pipeline based. Think logs from this thing that match this filter should look like this right? And then that can actually scale both to Sdks and to the collector.
So if you're going to do declarative configuration, and we're going to think about the namespace and the the ways that opensometry thinks about stuff, we have resources, and we have signals on resources. So if you always have that hierarchy of resource, then scope, then signal.
I think you get you get a lot of configurability. So log name would be the scope right?
or or get logger. Whatever. Get meter, get that sort of thing.
Resource would be the outer one that most sdks don't care about. So that's why it doesn't show up when you have an SDK thing. But in the collector that might be a way to actually have this make sense a little bit where I could say cool.
I want to filter different resource things I want to say from this, you know, service. I get this data from that service. I get this other data.
But that could blend blend the 2. Anyway. I still like.
I think pipelines are a good concept.
but declarative configuration and pipelines can get very, very messy, very, very quickly.
And so you're starting to talk about an imperative configuration file format.
and you're trying to blend the 2.
I think it's fine to have both if we need both.
But if you engage with declarative, I think it should be fully declarative and solve a key set of use cases.
And if you need to degrade into like weird pipelining stuff, cool, you can't engage with the declarative anymore.
That's fine.
But anyway, those are just like 2 of my thoughts here, really like the direction. By the way, like, I think this, this is what I would love to see more of across the SDK. And the collector.
**Trask Stalnaker** 23:25 I'm really excited for the declarative config like driven spec work like, that's why I put this like up front and center, because, like, I like to start from that, and then we can drive out the other pieces.
Cool. Any other feedback on this. So far we'll certainly cycle back. We'll we'll discuss in log, Sig, and and bring something up for out of draft.
for the broader everybody to review.
**Robert Pająk** 24:10 There is one thing which I think is obvious, but I'm not sure like it's obvious.
but implicitly. It's not called explicitly.
I think that. No, there, I'm not sure if there's a place which says that what is the precedence be between the configuration logger configuration and the processors, I think that the logger configuration goes 1st and then the processing.
I'm not sure if it's called out anywhere.
That's just a neat, a neat comment.
**Trask Stalnaker** 24:45 Yeah, I I agree with your implicit assumption, but I'm not sure if we say that anywhere we have no more topics.
**Josh Suereth** 25:10 I also kept bad notes, apologies. I'm so used to AI doing it for me now. I forgot to type while we were talking.
Yeah, we have no more topics. Does anyone else have anything else they want to discuss? Thanks for presenting Trask. I can take over if you want, but I don't know if we have anything else to say here.
Anyone else have anything they want to discuss for the spec meeting or Maintainer meeting any maintainer related questions concerns that sort of thing.
**Tedsuo** 25:39 I just have, like a kind of like open, ended question that. What we were just talking about reminded me of is we now have this like configuration syntax.
we want to roll it out everywhere we have OP. Amp. We want to roll it out everywhere. But we don't really have any like practice or tooling around like having kind of coordinated initiatives across different implementation settings.
You know, the finger pretty much independent, and, you know, can choose to to pull things out of the spec as you know, make sense for their own backlog.
But I just wonder how much maintainers would appreciate having more coordinated initiatives around. Some of these.
Configuration, in particular, seems like something that really changes the way initialization happens for the sdks. So I'm just kind of curious how maintainers feel like around having a more project based approach to doing that kind of stuff.
Anyone have thoughts or feels about that.
**Antoine Toulme** 26:55 Sounds good.
**Josh Suereth** 27:03 Do you have a straw man? Oh, go ahead, Josh. Sorry.
**jmacdonald** 27:07 Since since the topic came up, Ted, I thought I'd mentioned that the collector, Sig, which I've been getting closer to for quite a while. Has raised some concerns about configuring metrics and the SDK for metrics. Now we all know the metrics. SDK has views. And we're struggling. There's there's like a hard, coded, hard coded piece of code in the collector service main function that's like, here's all the views that we've come together with to get us through 2 years of of like, not quite being sure about this And so each time you want to add a metric that's off by default. You have to also go edit this file and and modify the views. Definition for the for the SDK used by the collector, and it's the the complexity of this approach is just sort of like fraying us, and it seems like the the group there would would appreciate a simpler proposal that was much more user friendly for specifying or configuring the metrics. SDK the names of the metrics we use, and whether they're on by default, even naming is not such a big deal. It's really that I want to have flexible control over which are on and which are off.
So there is a there is an existing kind of convention there, which is called the scraper metrics configuration. So for all the components that the collector has that that read metrics from the system. Some way, you can actually configure them. And there's a simpler model.
So it's appealing to the collector group to consider an essentially a lighter weight user model for configuring metrics. That would be, is it on? Is it off? What level is it? On or off at by default? Lets you turn on scopes and turn off scopes, and so on. I think that that would be a a good topic for the the group here to talk about, because it seems like, you know, the the metrics views. SDK, is not succeeding. It might be the right solution for low level, but it's not for users, and I'd like to to see what we can do about that.
**Josh Suereth** 29:02 I wanna jump on that Josh, actually, internally, we've been discussing that as well of there's an internal proposal around a metrics configuration system that would configure on a per metric process. That's way simpler than views.
Or basically the same as views. But the syntax is much shorter, I would be a fan of doing what Trask showed for log configurator on metric configurator and using Prometheus scrape config as the foundational basis of what everyone does today, and then figuring out if anything needs to be different for push based.
like, you know, we have a reporting interval. We have to add right of how often we send data as a thing we need to configure somewhere. But other than that, like, yeah, I think.
**jmacdonald** 29:50 There's a proposal also to extend just the sort of bare minimum for configuring attributes like, I do want this attribute. It's high cardinality. I don't want that attribute. It's lower cardinality. That's that's something that's being asked for. Josh, is this the proposal by Braden that you're referring to? Okay, well, Brayden has made a proposal which is adjacent to this conversation, and I will leave it off out of this meeting. But but there's something Google's doing that I know about.
**Josh Suereth** 30:13 There, there's there's yeah. We have, like 3 different efforts around metric controls. One of them is still internal and hopefully will become external shortly, which is a more aggressive proposal.
in any case, I think, the point being, these controls are needed. They need to be targeted at use cases like, if we talk about principles, the fact that, like Trask is like, here's 2 common use cases for logs. Let's make configuration that optimizes those use cases, we should take that approach to everything we do in configuration. When we do this declarative style, right?
Jaeger, remote sampler, I feel like also targeted specific use cases. This log configuration. We have target specific use cases. We did not do that with metrics made a very flexible system.
and flexibility is great.
But let's target the use cases people actually have. So I think I'd like to continue that discussion. Yeah, go ahead, Trask.
**Trask Stalnaker** 31:07 Yeah, Josh, there were a couple of things that you brought up. One was the disabled by default metrics. I dropped in the link to the spec discussion about that which I think is a great proposal. I mean, we do have these advisory parameters.
that, and that I'm curious if that solves that aspect.
And then the other piece is for attributes specific attributes that people want on or off the way that we've handled, that in the Java agent is, we pass in all the attributes so like on a Http duration metric. We pass in all the attributes from the Http span. But when we define the metric, we use the advisory parameters to say by default, you should only pair it down to this set of you know that matches semcom.
and what that does is it allows users, then, who want some of those higher cardinality attributes to define a metric view and opt into those.
I don't know if that is helpful or not. In that case, that the collector is looking at.
**Josh Suereth** 32:50 Does does go have the hint, Api. Yet, because it might be that what you're using isn't something the collector can make use of yet does the go SDK have the hint? Api.
**Tyler Yahn** 33:07 No!
**Trask Stalnaker** 33:08 Not. Nobody has it for attributes, advisories I I that's why it's still not stable, because I can't get we only have one proof of concept or one implementation of it for Java.
I I really love the disabled by default. Metric advisory, parameter idea. We could leverage that in the Java metrics a ton right now, we have, like all these ones that are all these opt in ones. And it's kind of silly. We have to have different configuration parameters for people to opt into each one.
**Josh Suereth** 33:56 So it does sound like to me. We should probably push for a project around metric configuration that that is probably worth some dedicated effort and attention and focus at some point like it. You know these things. We need them. They kind of happen organically. But we should think about when we look at the amount of attention we're spending on things, and we look at our project plans. This, this is a big project just landing. The advisory stuff is worthy of a project in the open telemetry. Planning cycle is worthy of having dedicated people driving that. I think this is as big like what you're doing with log configuration. Is that big? Is this the configuration, Sig? Or is this like a separate sub project to that.
**jmacdonald** 34:43 I have a I have a question on this sort of the same topic, and and I'm I'm afraid, to widen this even more. But you've mentioned Jaeger remote sampling. And we're talking about enabling and disabling logs, because obviously we know that the reason why people want to do that is to save money. And actually, the reason why people want to turn off metrics is to save money, too. So there is a sort of like bigger question that I'm seeing. And I've been so again, working with the collector, you know, a while ago we had this open telemetry arrow project, and we needed to have some more strict memory limits inside the collector. So I started working on memory, limiting in the collector, and, as I propose, made proposals to the Collector Sig about like putting that into the sort of base of the framework. Questions came out about rate limiting. So now there's questions about how do you? How do you rate limit? Sort of like, generically speaking, in the collector? What are the mechanisms that we have? And before long you're also looking at Jaeger. Remote sampling. Because, like, if you if you step away from logs and you start to talk about traces, at least there, we're talking about sampling as the mechanism for limiting something. So you have rate limiting and sampling and the configuration models for these are starting to look very similar to I've actually raised my hand mostly to ask if anybody here would like to talk about this with me offline, and or if anyone here is familiar with the envoy model for rate limiting extensions.
Because I think that before you get too far into this this conversation, the configuration model for rate limiting and sampling will end up looking almost the same. And that's curious to me. I'd like to know if anyone else has some feelings there. And I think that we're going to need to to specify how you configure samplers. Obviously, that's sort of following on the current work in the sampling sake. So just opening the floor to that topic. You don't have to speak now, but it's a curious topic for me. Thank you.
**Trask Stalnaker** 36:28 Super interested in configurable samplers from the Java agent side. We've that has been like our number one user request forever. And we finally sort of have a solution. But standardizing that and making it open telemetry wide would be amazing.
**Josh Suereth** 36:58 Am I working now? Okay. Yeah, I I would love to talk to you more. Josh. The I will say that we reached out internally to the envoy folks and the the control plane folks there, and had a really good discussion, and they were very interested in open telemetry and what we're doing with our kind of control plane. And so I think there's an opportunity for us to engage with that that ecosystem as well and kind of discuss this anyway, I'd love to continue that discussion. I think that's a much broader, open, ended thing.
**jmacdonald** 37:32 Yeah, I've been trying to make a write up. But basically, I'm going to propose without better proposals that we take the Envoy v. 3 rate limit extension model and apply it widely inside the collector. But but it takes a lot of work to make that statement very coherent, and I'm still still at it. Thank you.
**Josh Suereth** 37:49 Yeah.
I'd be. I'd be supportive of us standardizing on control that that aligns with networking in some fashion. If there's if there's a standard we feel like is the industry standard.
We don't need to build a new one.
We should use whatever that is. So. I appreciate that.
**jmacdonald** 38:12 Thank you.
**Josh Suereth** 38:15 This was a good, open, ended question back to Ted's original thing of do we need tooling? I think the answer is probably yes. People would appreciate some kind of tooling. Do you have a straw man you want to discuss, or I'm happy to to continue open ended discussion with people, or end the meeting either way. Go ahead.
**Tedsuo** 38:32 I to be clear? I wasn't thinking I was thinking less around, like like tooling and more around, like, you know, we have a configuration, Sig. Right? And that's like a spec sig, and it's still ongoing. But there's like a tendency for these spec sigs to, you know, have their purview end that begin and end it like defining.
You know, like they have some target they're trying to hit. They design it, you know. They get it into the spec.
We try to prototype it in a couple of different languages, but it just seems like like configurations, kind of like a bigger, longer, more ongoing thing. And like potentially touches touches just like a lot of stuff. And so I'm just just curious, you know, more about like, like one way to keep doing. It is like, keep having, like the configuration, Sig, you know, continue on. And you know, maintainers who are working on that stuff to go to that Sig and just hash it out there. And it's fine. There's more just like interested in hearing from maintainers.
you know, what they were feeling there, if they're feeling like supported enough, or if we needed some other way of coordinating this.
I see, hands up.
**Josh Suereth** 39:48 Yeah. Is it Antoine or Trashnik? Sorry I didn't.
**Antoine Toulme** 39:51 Press transfers.
**Josh Suereth** 39:53 Good.
**Trask Stalnaker** 39:54 From the yeah. I think it was a really good question. And and we wanted I wanted to speak from the experience of the Http simcom sig where? We had this desire to, you know, finish the spec and then go. And you know, do what you're talking about of implementing the spec or, you know, coordinating the implementation. And that second part failed.
I think it was.
Ha! But I instead of focus on why, I think it failed. the idea that I had that I wanted to throw out was using this meeting as sort of a touch point of like, okay, we've got a we've got a coordinated effort, say, for configuration. And each week that that's you know, we are just checking in getting feedback from maintainers sort of as a touch point. To keep it front and center on people's radar and plan.
**Antoine Toulme** 41:10 So might take maybe a bit. I'm coming at it from a different point of view here. As you might have picked up. There's a new project called the Injector Project, where we would be using actually a lot of the configuration Sig output because we would need to package all the instrumentations and offer configuration for those.
So we might actually be the people we end up having to do a lot of that tuning around config or who could benefit a lot from whatever you you want to build there? And and we can also run a certain number of validations or help to kind of make sure that when the injector is leveraging this configuration it works across different languages, or it's easy to pick up or so there's some some reuse, or we can share the load a little bit. On this type of things. We can offer a testing framework for testing this type of configuration when it comes out.
I don't know if that's really helpful for you, but this is from a from an implementation point of view, right? Not from a spec point of view.
I think. A nice place to kind of go and work across all sdks.
Does that help.
**Tedsuo** 42:28 Yeah, yeah, right? I mean, I think it gives a good example of like the the kind of things right? Like we, it's it's like this long, ongoing thing. And I think we had a good discussion earlier in this meeting with Trask, pointing out like we're trying to add new things. And we're like, let's look at the different ways. We could configure this.
And of course, if it's SDK level configuration, then that's also gonna interact with, you know, the internals of these implementations in different languages may maybe just bringing things up, you know, here, and having encouraging maintainers to to participate in the config is is like just enough, and it's just fine, and it'll work its way out.
I see Ty Tyler. You're on the call. I saw you popped on earlier.
and I know you're you're both a maintainer and participating in like the config Sig. For a long time. I'm curious if you have any thoughts on on how the rollouts going.
**Tyler Yahn** 43:35 How the rollout of the configuration is going.
**Tedsuo** 43:38 Yeah.
**Tyler Yahn** 43:39 Yeah, slow.
very slow. I think that there's been an effort to try to stabilize it since Jack left for paternity leave. And so it's been more about like validation of what's going on there. And so I think we're talking about that second part of that conversation. And we're not really talking about anything related to the instrumentation configuration just like the core SDK, stuff.
So like whatever model this, you know, we can learn from this, I think that we could improve that process a lot. I do know that, like the configuration sync meetings have turn into very open ended. There's a lot of space in the agenda. So if Maintainers wanted to stop by and talk about things and talk about new concepts there.
I think that that's a great idea. I think that the Trass point, like we've always tried to have. Well, I've tried to promote like this like touch point here.
because I think that the configuration is not unique to this. There's a lot of other like working groups or things that splinter off and they come back and like, if there's no iterative cycles that come back to this really fast, like, there's a really good potential for conflict to like be created, because this is the broader community that it's gonna affect. So I like, I like that idea of like continual like integration back to this kind of a meeting.
But yeah, I think it's like also to to your point about like, what are the next steps there like? That's very open, ended.
I think that we were trying to get this like stabilization over the line and then come to that question. But like, maybe we can start thinking about that. Yeah.
**Tedsuo** 45:12 Okay. Cool.
Thanks.
Yeah.
**Josh Suereth** 45:20 I'm liking these open-ended discussions. I'm glad we had time for this.
I'm going to just freeze this real quickly for anyone. Is there anything that you're concerned about in opentelemetry that's significant enough to raise in specification maintainer Zig.
that you were uncomfortable, just raising initially, we just talked about. How do we roll out programs across everything? We talked about configuration? You know, in terms of like my top, 2 ease of use and open telemetry, configuration documentation. Those are big.
Those are things that I am glad we're talking about and are are raising to the top of the surface. Is there anything like that that folks want to raise in the next 15 min or.
**Antoine Toulme** 46:00 I do, I'd love to talk about that for a sec. So it's a it's a bit of a vendor topic, but I think it's relevant. So we're trying to. We're trying to reduce a little bit of duplication that we have between maintaining our own docs and what is open from open geometry. I'm not particularly interested in copying, pasting, content all the place anymore.
I'd like to make it easy for us to reuse what's in the open telemetry I/O website.
and maybe also marry that to some of the weaver stuff that we're doing like there has to be a way to make all these come together right? But that's that's a bit too ambitious. One thing I picked up is that our docs team might be open to reusing some of the content if we make it available in some specific doc format called data.
which is God awful to read. But I didn't pick up on that would that be something that we'd be open to? Is that to start to package our docs and to release them as if they were actual deliverables?
I know that we have a markdown generator that generates open Termitry I/O, which is great.
Is there a way for us to kind of? And this is a big, the we don't have the right crowd, I'm sure. But would it be okay for people to consider making this an artifact deliverable? That would be downloadable, consumable. But machines as well.
And as I've been, maybe this is actually a maybe I'm beating a dead horse been discussed before.
**Josh Suereth** 47:32 No, I I think you're you're about 5 years ahead of where we are. Possibly.
**Antoine Toulme** 47:38 Oh no!
**Josh Suereth** 47:39 But but the the thing, the thing that I'm gonna call out 2 things that I think are important in what you're saying to for us to think through, because they resonate with me. The ability for us to have machine readable docs that can reformat. If you look at how open telemetry I/O works today getting documentation to it. It's a heroic effort from a small number of people to make that work.
And it's it's you know, it's the thing where you just you put you paint a really pretty picture, and then you just make a giant reel of duct tape around a bunch of sticks to hold it up, and it could fall over at any moment. Right? And you just keep adding the duct tape, and eventually there's so much duct tape. It's never going to fall. But do you really want it held by duct tape? I don't know. Maybe if we had something a little bit better.
It. It's a thing that that you know. We're going through with Weaver. Specifically, we were talking with the Docs team about how do we get our docs into open telemetry. I/O, what's that process?
If you're aware of techniques and conventions around like producing documentation and consuming it. That is kind of cross language, friendly cross organization, friendly something that we could use to improve that process. That would be step one is, get open telemetry to use that for how we communicate between projects and docs.
**Antoine Toulme** 49:00 Yeah.
**Josh Suereth** 49:00 Then we'd be able to publish it externally. But like we have to take that step first, st I think, because right now, the way we publish docs the way things are done. It's it's we do what works and and we are trying to evolve it, make it better.
But it's in a very inconsistent state across all the projects. I don't know if you want to jump in, Ted.
**Tedsuo** 49:20 Oh, yeah, I mean, just one note. I think copy paste is a very powerful technique, and people shouldn't knock it but more seriously. I think the the thing you run into, I think. And this is very much a com sig question, because they maintain the website and the docs is, I think you have attention of, like what we really wanna encourage with our website and our docs is lots of community contributions, right? Like if you see something up in the docs and you want to change it. It should be like very, very easy for a human to just go tweak that edit. And I suspect that that desire designing for that goal, optimizing for that kind of runs in a different direction from optimizing. For, like machine. Kind of code. Gen, approach
**Antoine Toulme** 50:10 Sure.
**Tedsuo** 50:11 To maintaining docs right? Because you you'd end up with like some separation between what's on the website and what you know, where the docs come from. And and it is like a total mishmash right now, right? Like, like some things on the website like, get sucked in from other places.
But I just wanted to flag that that I think there's actually, you know, optimizing is choosing one thing over the other, and I suspect you will run into some, some challenges there about like, what's the goal here? Making it easy for community members to contribute to the docs? Or is it easy to have like machine produced, you know, versions sections of the docs that are easy to like put into different formats.
**Antoine Toulme** 50:54 Yeah, no. I agree. So to me, it would be that we need to find a way where we want to have the source material to like you mentioned as easy as possible for people to come edit, manipulate, and then we would want to have some tooling, some build that would make it available in a variety of formats that would be easier for machines to make sense of. And yes, this is the difficulty. You're right.
**Tedsuo** 51:22 Yeah.
**Josh Suereth** 51:24 I'm gonna throw in a glib comment because I can.
Why don't we just throw it all into an Llm. And have it regenerate the docs over time. Right? Isn't that the new? The new way.
**Antoine Toulme** 51:35 No.
**Tedsuo** 51:37 Yes, AI does the copying and pasting for us. That's.
**Josh Suereth** 51:40 Yeah, you're only allowed to sound like an AI going forward. That's the other rule.
**Antoine Toulme** 51:45 I would turn it around. So what I would say is that an Llm. Is an ideal interface for end users to quickly grasp the open telemetry topic, and we should definitely make some sort of a and I don't know anything about Llms, but I think it would be really worthwhile for us to control what data and Llm. Could use or or be inspired from, so that it can be actually of good authority, because one thing that I would hate and sorry to happen to me is people come to me and said, the Llm. Said X.
And the Lm. Is wrong, and it's been wrong, like in a very authoritative way, which creates a whole lot of grief down the line. And we we will want to have the source material to be really well created and up to date.
because otherwise we're gonna run into that repeatedly until we start just not being able to sustain. So. But that's that's another thing. But it's true that people do no longer use the search bar. They want to have a chat about some random need they have.
and we need to go with where people go on that.
and that's that's going to happen to us.
No, for here's here's my lever, right? I recently went to the collector config components. We have 220 some components in the collector contriv repository, which is nuts. It's incredibly complex.
And we do a lot of creation of those components, and I don't know if you pick up on that. But I push people into unmaintained status all the time I put people emeritus. I drive people out of the project or tell them they're not.
you know. You need to be there right? So people take hiatus and no longer there for 6 months need to go.
And recently I went to all the alpha components. We've been Alpha for a while and said, Hey, you need to move to Beta now, right? You've been there for a while. You need to start to publish your stuff. It needs to be tested, and you can no longer hide under a rock.
So next step is, you want to go stable? You want to get people to really like, rely on you for production usage. You need to have your docs in order. We can set requirements and set the standard for what it feels like for those components which are actually one of the most like end user focused things like it's, it's really.
actually very close to the chest. For some of those folks. Right? The the collector attracts a different type of end users than say, A go developer or Java developer. It attracts devops, people devops. People have absolutely no bandwidth.
They need this to work the 1st time when they copy, paste the yaml, and that Yaml better be well indented because they're not going to change in. Then they don't have time for this.
So when we move to stable, we can set a number of requirements about what that means, and one of some of those should be about documentation, ease of use, intuitiveness, these type of things.
This is where we can come in. We can actually apply that.
So we have a lot of power over this, and if we set up that stuff, then the rest of the projects will have a kind of a easier path moving forward, because we'll build the tooling for it. We'll make it easy.
This is where Weaver could come in where Weaver could be, providing us a little bit of a way right now, like a lot of hidden nuggets of information are in the readmes of those components.
As that mentioned, we want contributions. Great way to get contributions is in collector country repo, because people want to have karma in the repo, where they eventually want to become code owners or maintainers or whatnot. They contribute to Readmi. They're never going to contribute to open terminatory, I/O, because it doesn't give them any karma to become more active or get up the ladder of maintainership in a repository.
So we can have the river registries or repos or definitions inside those components. They should have all the metadata about the docs, and then we can generate docs from that.
**Josh Suereth** 55:58 I definitely like that proposal. I think that's a thing that really makes sense for a component like the collector contrib where you have tons of individual components. Probably almost all of our contribs could benefit from this.
I I also think, like to your Llm. Thing. I don't know how we do this, but effectively, being able to to provide open telemetry rag where, if somebody's using an Llm we can give them grounding on real docs that we've given them the Llm. To say, Hey.
like, here's how you make sure you don't lie. Read these specifically, you know. Interface.
You nailed it, you nailed it, you nailed it. This is exactly what you do. So you have an AI that checks the Lzra AI.
**Antoine Toulme** 56:43 That's the most wonderful. It's actually less work for an AI. You cannot put from some other AI, and say, No, that's no, that's not. That's not true.
**Josh Suereth** 56:53 Yeah. Well, I guess you get what I'm saying is like, I think this notion of machine readable docs is something to move towards. It's just where we're starting from is bare minimum. So it might make sense to found a system that works for collector contrib talk to the Docs team, go to the go to the communication sake and be like, hey, here's what we need from the collector.
Let's work on this together. Let's start and solve your use case initially, because I think the collector has the most pain. Let's get. Let's get something out the door, and then let's start talking around the community, like with all of us here, this is a good broad discussion. But let's start solving that problem and then work towards what would a general solution look like from that.
because I think this is one where we it's if we start talking, General, we might never do anything, or we might overtune on something where no one will use it. So it's better for us to really hit your problem initially and then expand.
**Antoine Toulme** 57:47 Yep, no, we. We're keeping it really close to the vest in in really real, because we have to. We, we're in the collector. We're used to having to move 10 lines at a time. That's the only thing we know to do.
That's the only thing that ever landed. So no worries.
**Tedsuo** 58:05 Just yeah, to to close it out on this subject, because we're out of time.
A good place to start rather than the docs, by the way, is, I think, semantic conventions right? Because we've already got like semantic conventions are already set up in this manner. Right like it is already set up into like we've got like these schema files. And like all of this other stuff and markdown and like blah blah so. And we're actually my team at Grafana is is very interested in exploring like, how we could use weaver to like what what you just mentioned is like, we've got this data. We want to figure out all the ways people want to use this data with AI and Llms, and like, what is the best way to produce training data or verification data, so that like people get the best answers right? Like, like, the the tooling can actually do its jobs. And it's probably multiple different formats depending on like, what kind of task we're talking about asking an Llm. To do but we're really interested in that on my team and exploring that. So if anyone else is interested hit me up on slack.
**Antoine Toulme** 59:20 Yep.
**Josh Suereth** 59:21 Cool. Thanks everybody for the open discussion. I'm actually really glad we had some time for that. And yeah, look forward to seeing you all next week have a great week. Everybody.
