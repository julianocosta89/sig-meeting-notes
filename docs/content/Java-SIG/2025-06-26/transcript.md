SIG: Java SIG
Date: 2025-06-26
Duration: 71 minutes
============================================================

## Zoom Recording Transcript

Trask Stalnaker 00:15:23 Hey, folks.
how are you.
Steve Rao 00:15:29 Yeah. Hi. Trustee.
Minghui Zhang 00:15:32 I trust.
Huxing Zhang 00:15:33 Don't trust.
Trask Stalnaker 00:15:34 Okay?
All right.
we've got attendees and topics.
Yeah, let's kick it off.
Steve, support distinguishing different types of instrumenters by span kind.
Steve Rao 00:16:18 Yeah, yeah, this is a subsequent questions about yeah, about original. Pr.
yeah, I can introduce something about the background.
Yeah. As we know, we support extension for instrumentation to add some attribute extractor, something like that. But I found in some corner case, in some instrumentation. They are a client or server, or producer, or consumer.
Trask Stalnaker 00:16:56 Oh, I see!
Steve Rao 00:16:58 How to apply it.
A different extension for different instrumental. Yeah, that is a question.
so.
Trask Stalnaker 00:17:08 Is this you said you're a later Pr, but this isn't.
Oh, this is your repo. Got it? I understand.
Steve Rao 00:17:16 Okay, yeah, I I just want to. Yeah, show my idea.
Yeah, I add, a, get a spend calendar to solve this question, but it yeah, it can solve all questions, because, in some scenarios if user do some customization for span candle extractor.
it will return the result according to the request.
But in initialization we can get the request.
So in that corner case that is a question. But this Pr. Can cannot solve that corner case. I just want to support some constant span candor in majority of scenarios in our current code base.
Trask Stalnaker 00:18:20 Right.
Steve Rao 00:18:21 Yeah.
Trask Stalnaker 00:18:22 So this solves your yeah mead.
Steve Rao 00:18:28 Yeah.
Trask Stalnaker 00:18:29 Okay, yeah. So let's talk about yeah, it. It makes sense to me. In the same way that you know, you might want to have behavior based on the instrumentation name. You may want to have behavior based on the span kind.
Steve Rao 00:18:47 Yeah.
Trask Stalnaker 00:18:52 Let's see, do we?
When we call build.
Steve Rao 00:19:03 Yeah. Here you can see.
You can see this this cross.
Trask Stalnaker 00:19:10 Apply customizers to the builder builder.
I see what you're doing. Okay? Okay, yeah.
So let's see where this is called from.
Steve Rao 00:19:32 Yeah. Code from here, build an instrumenter.
Yeah, I also discard this question with Laurie. Yeah, he think. Yeah, it's a bit hard to support all scenarios. Maybe we can. Delayed this question and don't support it. Currently. Yeah. But I I guess that is a important part of this pr, I want to support some majority instrumentation in our code base code base. Currently.
Trask Stalnaker 00:20:15 Right? Does it? I mean, most of our instrumentation calls build client, instrument, or build, server, instrument or.
Steve Rao 00:20:26 Yeah.
The.
Trask Stalnaker 00:20:27 Gotten.
Yeah, so potentially.
you can. Yeah, I mean, check. There.
let's see to do it dynamically. The extractor.
Let's look at your original pr here.
Yes, cause we're customizing the builder. So it's gonna be too late.
Steve Rao 00:21:04 Hmm.
Trask Stalnaker 00:21:07 But.
Steve Rao 00:21:08 Yeah. In fact, it's yeah. It's okay in a lot of scenarios. Yeah, because a lot of instrumentation, they just use the the constant a span candor extractor.
Trask Stalnaker 00:21:54 So you're adding, like custom attributes extractors.
Yeah. So the question is to Laurie's point about to do it. I was trying to think what it would take to do it accurately.
We don't know the span kind until span kind extractor runs.
Where is that kind extractor? Yeah, here. And then we'd have to dynamically on every request.
Ask for the custom attributes extractors for that span kind.
And then you start talking about.
Steve Rao 00:23:04 Yeah, you you can check. Yeah, you can check out a span candle extractor class.
You, yeah, you can click on the class and.
Trask Stalnaker 00:23:21 So tell me, what is what's like? The use case is this for something like Nettie, where we have both client and server with the same instrumentation, name.
Steve Rao 00:23:36 Yeah.
And like, in messaging like, yeah, they are a producer and client with the same instrumentation, then. But yeah, maybe sometime, we need to add a different instrumentation for different Enter.
I guess that is a common scenarios. Use case.
Trask Stalnaker 00:24:07 Yeah. So I think I wouldn't do this.
Yeah, you can call.
Steve Rao 00:24:15 The class, spank, handle.
Trask Stalnaker 00:24:19 Yeah.
So you would just look at if the span kind extractor is always client or always server one of these, then you could populate it, based on that.
Steve Rao 00:24:36 Yeah, yeah, we can support that scenarios.
Trask Stalnaker 00:24:42 Yeah, that seems reasonable to me.
So the other thing that I wanted to look out with you on this with just the Api design.
Steve Rao 00:24:59 Hmm.
Trask Stalnaker 00:25:03 So the customizer you're going to implement a customizer.
Steve Rao 00:25:12 Yes, yeah. For users. They just need to. Yeah. Achieve. In, yeah, achieve instrumental customizer provider something like that.
Trask Stalnaker 00:25:32 Oh, okay, right? So provider.
The provider. So you you implement the provider. It calls.
Steve Rao 00:26:10 Hmm.
Trask Stalnaker 00:26:12 You instrumentor, customizer.
Steve Rao 00:26:50 Yeah, users can. Yeah, define their own customizer.
And to set the instrumentation name and all. Kind of attribute extractor something like that.
Trask Stalnaker 00:27:10 So did they a user implements? Is there a test that shows how this works.
User would use it.
Steve Rao 00:27:21 Yeah, sorry. I I don't write the example in this. Pr, yeah, I want to. Do a do that in follow up pr,
Trask Stalnaker 00:27:30 Is there? Is there a test, though.
Steve Rao 00:27:32 Yeah, yeah, you can check out the test.
Trask Stalnaker 00:27:34 Yeah.
So we've got a provider.
What is
Steve Rao 00:28:05 Yeah, to see the yeah, this is a design to sell. Yeah.
Laurie's advice is, we should move the Api to incubator module. Firstly, so by this desire to achieve the target.
Trask Stalnaker 00:28:39 Okay, so this is the static list.
Steve Rao 00:28:45 Hmm.
Trask Stalnaker 00:28:49 Set, so you call?
Are these not getting loaded via spi.
Steve Rao 00:29:06 yeah, you can check out the test class. Okay, let me introduce.
Trask Stalnaker 00:29:11 Yeah, so it looks like you, you programmatically call this.
Steve Rao 00:29:15 Yeah.
Trask Stalnaker 00:29:17 Okay, I was imagining it would be an spi and loading using normal spi class loading.
Steve Rao 00:29:31 Yeah for users. They just need to care about the instrumental customize the provider. They just need to define the yeah, their own provider. And yeah, in the master, they can. Define some instrumentation. Yeah, you can check out the Api in. Yeah, in this they. They can implement the the class and define their own behaviors in in customizer method.
They they used a instrument.
Trask Stalnaker 00:30:10 Yeah, but you're saying it's a spi here, but it's not. I'm not seeing that it's loading. Oh, it is sorry I missed this.
Okay, so we are loading.
I see. So this was just the package protected for testing.
Okay. So the spi is loading that.
Okay? So you wrap provider.
So they give you one of those providers. Then let's see, why is it wrapped in this implement internal?
So is this all? Just because you're trying to split things between the incubator and.
Steve Rao 00:31:28 Yeah.
Trask Stalnaker 00:31:29 Okay, yeah, yeah. Things get.
I usually recommend people to do that as a last step.
Steve Rao 00:31:36 Okay.
Trask Stalnaker 00:31:38 Because once we approve the the design cause, it's hard to Yeah, it's hard to follow with that package splitting. It makes things a lot messier. Yeah.
Okay, so let's look at your test again.
So provider customizer, okay.
setting customizer, your customizer and attributes extractors.
And so what do you do with how does instrumentation?
Let's see, get instrumentation, name test, get instrumentation name shared that.
Let's switch this equals test.
It's like customizer builder.
Okay? So you're building this with the instrumentation name building. Okay? And so then you wanna check that customizer was called.
And you're asserting that customizer.
I see customizer get, okay? So there's an implementation of.
I see, okay, okay, this is, yeah. So apply customizers, your getting populating that. Okay?
And if somebody calls you if somebody calls.
Oh, I see. So the user calls add attributes, extract mentors.
Steve Rao 00:34:44 Yeah.
Trask Stalnaker 00:34:46 So what the Api design question that I was trying to get to is in one direction, this customizer, your populating things, and then the other direction. You're asking if is not a bad approach.
I was just trying to think if there's like, add.
Steve Rao 00:35:23 Yeah. I also discussed this question with Laurie. He think, yeah. Used to add attributes. Extractor. It will be consistent with current instrumental builder.
Yeah.
Trask Stalnaker 00:35:42 Right?
Yeah.
So let's look at your test again. Here.
So a typical customize would implement this and they get one call back, and they get to do stuff, and you get to do stuff with the customizer you get. Add you get one call back. So let's look at the provider cause the it's great to customizer writer customize. Okay, so you're getting to customize.
Steve Rao 00:36:49 Yeah, okay, yeah, maybe I can. I can show yeah. Use case how to use this Api and I sent it in in chat. Yeah, I send it the code and you can check.
Trask Stalnaker 00:37:08 Okay?
Yeah. So what I was kind of wanted to just discuss pros and cons of changing it to be something like this.
Steve Rao 00:37:22 Hmm.
Trask Stalnaker 00:37:27 Where this is just like a callback.
Steve Rao 00:37:33 Yeah, I also discard a similar question. Yeah, before with Laurie. yeah, he think. Maybe it's look very. Yeah. A clear look, very beautiful, like the Api in in Java. SDK, jia is a a similar api in Java. Sdk project, and it's use similar dessert.
So this pr, just follow. It is a desert.
Yeah.
Trask Stalnaker 00:38:28 Yeah. The difference here is that this is these are only callbacks. There's not. There's no getter.
Steve Rao 00:38:35 On this.
Yes.
Trask Stalnaker 00:38:37 Right.
Steve Rao 00:38:38 Yeah. Anthony.
Trask Stalnaker 00:38:38 So. So it's a little bit. That's the part that is different to me. You pass in.
Steve Rao 00:38:44 Okay.
Trask Stalnaker 00:38:45 Well, let's see the what the provider.
Steve Rao 00:38:48 Yeah, you can check the provider cost.
Yeah, they just want parameters. So, yeah, Laurie.
Trask Stalnaker 00:39:01 Yeah.
Steve Rao 00:39:02 upgrade.
Trask Stalnaker 00:39:03 So.
Steve Rao 00:39:04 Add more parameters in that method.
So we just achieve it like he no.
Trask Stalnaker 00:39:18 Yeah, so it's a little different, though, like this one, this is a let's see, what could we do?
customers are.
See, these are all like your calling it with things that then get further callbacks, which So if we don't do this, I won't. Actually, I'll just leave it pending there.
Steve Rao 00:39:52 Yeah. I sent. I sent a a cold sleep in the meeting being, yeah, you can. You can check out.
Oh.
yeah, something like that.
Yeah, for users. They can. Yeah, they can on do their customization like like this, use this spi
Trask Stalnaker 00:40:30 Yeah.
Steve Rao 00:40:37 And they need to. Yeah, achieve their own.
Trask Stalnaker 00:40:41 They like it, I mean, I think it's.
And so it's going to get.
Steve Rao 00:40:54 Yeah, cool.
Trask Stalnaker 00:40:55 Hard once or each.
Yeah.
So another option.
Well, I do like this.
This is extendable, like, if we decide that we want more getters like more things to differentiate on in the future.
Steve Rao 00:41:41 Hmm.
Trask Stalnaker 00:41:43 So that's good.
Another option.
Steve Rao 00:41:55 Yeah, yeah, you can.
Trask Stalnaker 00:41:57 Another method.
I'll do. Here.
Steve Rao 00:42:57 Yeah, that is a extra line.
Trask Stalnaker 00:43:10 That's an option.
But if we wanted to add more later, that's less flexible.
Steve Rao 00:43:23 Okay.
Trask Stalnaker 00:43:32 this one is super these auto configuration. One is pretty complicated because it you, basically, each one of these is a function which then can decide, based on the inputs.
Steve Rao 00:43:47 Hmm.
Trask Stalnaker 00:43:47 If it's gonna do something.
Computer customizers.
Oh, yeah, looks like those are customizers. But let's look at a simpler.
I mean, that's kind of what? That's another option over here is customize. Oh, not here.
Oh, this is the provider. Sorry.
Writer, customer.
instrument, or customizer.
Where do we go?
So if we were really following this pattern would be.
yeah, Ab would be adding a customizer.
So we'd be adding an instrumentation customizer. This would be like would have a instrumentation customizer.
let's see another and then instrumentation customizer would be like auto configuration, customizer and instrumenter customizer would be like these other ones, like resource customizer.
So let's flip that so add resource. Customizer would be in our case, add.
Steve Rao 00:47:07 Add attribute.
It's a chapter extractor.
Trask Stalnaker 00:47:18 This one is customizing. Let's see, taking simple span exporters lets you wrap each span exporter. What about just adding to add a single?
I see. Yeah, to add a single span processor, you have to add a tracer provider customizer, and you customize dot.
So it's not really. It's add ins instrumenter customizer that takes instrumentor, builder and returns instrumenter, builder.
So it would take a function.
One of these do we need config properties?
Probably may as well.
Steve Rao 00:48:55 Okay.
Trask Stalnaker 00:48:57 Let's say by function, instrumental builder, config properties.
instrumenter, builder.
Problem here is that you only want to.
There's lots of these instrumentor builders, and you can't query that. So you want to know the instrumentation name instrumentation scope.
Yeah, I think this is all getting too complicated. And I like the I mean, I think you're This add attributes, extractor instrumentor builder.
I mean. Let's see, what else would we have to pass in here.
Steve Rao 00:50:31 Hmm.
Trask Stalnaker 00:50:32 In order for you to make a decision. It's like we'd almost need.
Steve Rao 00:50:38 Documentation. Then you mean so, or spam calendars like, like, yeah, into.
Trask Stalnaker 00:50:51 What do we mentor? Builder?
Yeah, I mean, we could pass all these into a the function along with it.
Instrument builder.
Eradicate.
Yeah, you end up needing, I think, almost like a instrument or some kind of struct that has instrumentation, name and span kind that you can pass in to your function to make a decision based on.
Steve Rao 00:52:05 Yeah, okay.
Trask Stalnaker 00:52:08 I don't think that's really better than what you have, though.
alright! And it sounds like you've talked through some of this with Lori already.
Steve Rao 00:52:34 Yeah.
Trask Stalnaker 00:52:35 Okay. Did he have sorry I didn't notice. Has that been here?
Steve Rao 00:52:49 No, yeah, you can.
Yeah, yeah, you can check this. This one.
Trask Stalnaker 00:52:55 Okay.
Similarly to, you could have, okay. Okay.
Steve Rao 00:53:06 Yeah, so we achieved to pr like, like, here.
Trask Stalnaker 00:53:13 Okay, yeah. Sorry I missed that. Laurie had.
I mean, if Lori's on board, I'm on board.
Steve Rao 00:53:21 Look.
Trask Stalnaker 00:53:22 Yeah, you don't need my, you don't. Yeah, you don't need me.
Steve Rao 00:53:27 Yeah. So I want to discard the question is about this, yeah, is about the spend. Yeah, today.
I just, yeah, I just want to support the majority of instrumentation to distinct with a different type of instrumental. I want to hear your voice. Yeah.
Trask Stalnaker 00:53:48 Yeah. So I mean, I would go ahead and update your Pr.
Steve Rao 00:53:53 Hmm.
Trask Stalnaker 00:53:54 With that with your proposal, and get Laurie's additional feedback. There, mom.
I think it. It sounds okay to me.
So do the I wouldn't do the like. You had the passing null to the span. Kind extractor.
I. Instead I would look to, and I would look to see if it is the at the known one of those known span kind extractors.
Steve Rao 00:54:32 Hmm, okay, yeah, yeah, this is my question. I also.
Trask Stalnaker 00:54:39 And see. I mean Laurie. Laurie may have different opinion.
Steve Rao 00:54:44 Okay, okay, yeah. I will. Discuss with him yesterday.
Trask Stalnaker 00:54:51 Okay.
Steve Rao 00:54:52 Thank you.
Trask Stalnaker 00:55:07 All right. Minghui.
Minghui Zhang 00:55:14 Yeah.
I have updated this pr, and we now based on our before discussion, we we remove remove the complex inheritance, and we now have the messaging process. Request the interface for the manual Api and the built-in request for the for the pre-built, for the pre-built implementation.
I have left some. Yeah, I have left some comments in our in my, in my pr, you can see that I don't know.
Think in the end of the Pr.
Trask Stalnaker 00:56:24 Okay, so have to define their own app.
Minghui Zhang 00:56:34 Yeah, here it is.
Trask Stalnaker 00:56:37 Attribute extractor.
Yeah. So what?
Let's look so right now.
So without this text map getter.
now, we have an implementation that mirrors the one used in instrumentation define their own message. Request?
Oh, yes, yes, I remember, I think. Yes, I yeah.
I think that this I support not having this because and then each right, the key part. The the key part is this the attribute getter? That's the bridge from into.
And then this, maybe like a Kafka, even just a Kafka native class. It might be like, in some cases we can use those and you don't need to have anything.
And so, yeah, there would be no default. In that case, right?
Minghui Zhang 00:58:43 Yeah.
Yeah. Yes. Yes.
Trask Stalnaker 00:58:47 Yeah, yeah, I I think that aligns with the that aligns well with the existing attributes extractors.
Because this is kind of duplicative of the we only kind of need, one or the other.
Minghui Zhang 00:59:09 Hmm.
Trask Stalnaker 00:59:15 Should we catch exceptions here?
There may be unchecked exceptions. We didn't do that in the instrumentation, right handle and extractor.
So handle. And have you looked to see what?
I don't think our library instrumentation suppresses things generally.
Have you looked.
Minghui Zhang 01:00:20 And I I remember the library instrumentation is just the add a wrapper simply so good.
I'm sure it. And I'm sure the library instrumentation don't do this.
Trask Stalnaker 01:00:42 Okay, yeah. I would say, don't yeah, not don't add exception catching, you know, everywhere. If there's certainly sometimes we have, like a bug reported. That's like, Hey, this Api, that you're calling sometimes throws an exception.
And so we will add, if there's kind of a known issue, we will.
Minghui Zhang 01:01:14 Yeah.
Trask Stalnaker 01:01:18 Add a try, catch around it like if we know the underlying library fails. Sometimes.
Minghui Zhang 01:01:23 Yeah.
Trask Stalnaker 01:01:32 right? And then this one, you wouldn't need that cool. Yeah, yeah, thanks for doing all that work to align it with the attributes extractors.
I think that'll make it a lot easier to bring into the instrumentation.
Repo.
do we? Was there some? I forget. If there was a an issue, any issue you were having that we needed to bring it into the instrumentation repo.
Minghui Zhang 01:02:13 I have, I have. I have not created this issue. And but- but I want I want to remove this Pr to the instrumentation because of the the test and the.
Trask Stalnaker 01:02:34 Oh, the tests. Yeah. I remember.
Minghui Zhang 01:02:38 under the receive contest that we can't. That we. We can't access in the in the Java country, but we can access the receive contest in the Instrumentation Library.
Trask Stalnaker 01:02:53 Receive? What's the receive context?
Minghui Zhang 01:02:57 We Sometimes we we record the we record, the receive, spend, and we will use this span as a parent choice contest as a process span. So if you want to create a process span, you should access the receive span, and it's hard in here, but it's more easier in instrumentation.
Trask Stalnaker 01:03:31 Okay, cool. Yeah, I think that this is I think this is good.
I support moving this to instrumentation. Because it solves. It solves the problem that we've had. Multiple users ask about.
Minghui Zhang 01:03:51 Yeah, and nowadays. I'm working for the instrumentation in a spring rabbit, and I found it's harder to add a batch add a batch instrumentation in in it. If we don't have the messaging wrapper, and I think I think this company is component is important.
Trask Stalnaker 01:04:24 Cool.
Yeah, that's great. Since you're looking at messaging instrumentation, it may be worth following. I don't know if you've seen this pr, been working on it for a while.
Trying to update to the latest messaging semantic conventions.
There may be something interesting in there.
and we could certainly use help looking at it, or or understanding what's going on in all the messaging it has been actually making good making progress again. Yeah, it kind of stalled stopped for a while.
But yeah, maybe just follow it.
Minghui Zhang 01:05:14 Yeah, I will check it.
Trask Stalnaker 01:05:25 Cool anything else to chat about today.
Minghui Zhang 01:05:30 Yeah, I have no known no more, no more scenes.
Steve Rao 01:05:37 I have no more questions.
Trask Stalnaker 01:05:41 Hello, yeah, I'm I'm Jose, finishing.
Huxing Zhang 01:05:44 As I think. Steve has already reached out to you that we actually we were planning to open source our Travel agent for the next couple of maybe very soon, and we will build build this project based on the proxy agent. Architecture that Steve has already proposed before. And we just want to know that we are.
We're working very closely with the upstream. And we, this is actually kind of of distribution of the open telemetry is will be open, sourced just the Internet to know about that.
Trask Stalnaker 01:06:33 So the I know the proxy piece will be open source. Will you? Are you gonna open source? Your code, your distro also.
Steve Rao 01:06:44 Oh!
Huxing Zhang 01:06:44 Yeah. And the the main main frame of that project will be open source that we we still will have maintain a commercial version of that agent.
and we will split. Some of the features may may not be open, sourced, and but we we want to like keep the main framework. And then the agent.
the main agent, open, sourced. Yeah, that's why the current anyone will sync.
Trask Stalnaker 01:07:19 Yeah. So I think the that proxy 8 J.
Is a good idea. I would just keep that proxy agent as like small of a diff to the upstream as possible.
Huxing Zhang 01:07:36 Okay.
Trask Stalnaker 01:07:38 And.
Huxing Zhang 01:07:39 I did.
Trask Stalnaker 01:07:40 Yeah, I was sharing. I shared with Steve that I did something very similar with our distro for the 1st couple of years. Because I needed hooks in there. And it was yeah painful. But yeah, having that at.
it's a good way to go. And it also will allow us, like Lori and myself, to see what hooks that you all are actively using, that we might then be able to suggest ways to upstream that those you know I mean ideally. And then in 2 or 3 years from now, you won't need the proxy agent.
Huxing Zhang 01:08:29 Yeah, that's what we want to achieve.
Great.
Yeah, just one thing that you know about this.
Trask Stalnaker 01:08:42 Cool.
Well, have a good one.
Huxing Zhang 01:08:46 Okay.
Thank you.
Trask Stalnaker 01:08:48 See ya.
Huxing Zhang 01:08:49 See you bye.
Trask Stalnaker 01:08:50 You!
