SIG: FAAS WG
Date: 2025-07-02
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/AL1FQVgsUF1mRupHCJZVxaEVjrYdxKRkqWKvj_UzIu248xNOFBDTAvV-q5E-1IxZ.aICtyQisp1eZou7j
============================================================

## Zoom Recording Transcript

**Tyler Benson** 04:33 Hello! Everyone.
**Maxime DAVID [AWS Lambda Runtimes]** 04:37 Hello!
**Warre Pessers** 04:40 I.
**Tyler Benson** 04:45 So I I think we can get started here soon.
Does anyone have anything they'd like to add to the agenda today?
**Warre Pessers** 05:02 I can quickly give an update in a minute, so I'll add that to the agenda.
**Serkan Ozal** 05:57 Hello! Everyone. Sorry for being late.
**Tyler Benson** 06:06 No problem. We're just getting started.
**Serkan Ozal** 06:12 Okay, I think we if we are all here
not sure Ivan will be able to join. But we have worry. And Max, I think can start
for for this meeting. I don't have any specific agenda to discuss. I just wanted to mention that there are 2 dependent, both Prs failing one for the I think the Java agent and one for the the python python layer
so I will be looking into that if there is no volunteer to to to take them.
**Tyler Benson** 06:54 I do look at the Java, one.
**Serkan Ozal** 06:57 Yeah, okay.
**Warre Pessers** 06:58 Yeah, if you want, I can look at the python one
**Serkan Ozal** 07:02 Okay, sure
and other than that. I mean because of I mean some some personal plans. I mean, I have. I had, I mean, vacation plan and some other things. I couldn't find time to to think about the distributed tracing issue over Sqs. And the Sns.
But I am.
I mean.
if there is any update from Vori or from from anyone on that to to discuss, as of now, I will be happy to to discuss as of now.
**Warre Pessers** 07:43 Yeah. So I'll real quick. Give you an update. I've been looking into this. I already discussed this a little bit with Tyler as well. So it basically, for Nodejs has to do with using a lambda event source mapping that the
Sq. Sqs instrumentation you would normally use is, of course, not happening when you use an event source mapping. So I tested it
with like, actually receiving the message using an Sqs client. And then you can see. Okay, the spans are properly being linked to their producer span. So
it feels like, that's something that's missing in the Aws lambda instrumentation. Possibly. I've opened an issue for that on the Js contrip repo. No response as of yet. But I'm already looking into building a small own version to test this myself, so we can
do the propagation properly.
**Serkan Ozal** 08:58 Yes. Yeah.
**Tyler Benson** 08:59 Not exactly very familiar with event source mapping. Maybe you could explain a little bit how that's different from regular Lambda invocation and and why you would want to use it if you don't know. Maybe, Maxine, maybe you could explain. I don't know.
**Warre Pessers** 09:16 Yeah. So I don't know. Maxime probably knows a lot more about this than I do. But for me, how I see it is just like a normal pattern to use in lambda where you can create a trigger for a lambda function based on an incoming Sqs message. So
I call this an event source mapping, because that's how it's called in terraform. But I'm not entirely sure if that's the correct terminology. But basically, what it does is when
there are incoming messages on Sqs. Sqs. Will trigger your lambda with an event containing those Sqs records.
So you don't have to call, receive message on the Sqs. Queue yourself.
**Tyler Benson** 10:09 Okay.
**Warre Pessers** 10:10 That's clear.
**Maxime DAVID [AWS Lambda Runtimes]** 10:11 Yeah, yeah, this is exactly it. So lambda function is event based. So you need an event to trigger a lambda function. And you can pass like S. 2 events. So every time you put something in a bucket, this will trigger your lambda function, or it can be as you just described Sqs, events, and and you can. You can configure this as a batching so you can, receiving. You can receive one message at a time, or you can receive like N message at a time, or you can do a mix of receiving
end message or a deadline. Let's say, if I don't have like 10 message in 30 seconds. Just send me an event with what is inside of those 30 seconds, so it can be a mix of of different parameters.
**Tyler Benson** 10:59 So how is that different from the, I guess, like.
I'm just having a hard time understanding how that's different from the other part of it that you said was working.
**Warre Pessers** 11:15 Well, so what I tried just to do like a sanity check, let's say, is, I didn't add an event source mapping to
a lambda function. Instead, I invoke this lambda function manually, but inside the lambda function I sent a receive message command to Sqs. To like
manually retrieve the messages right and doing that, you get the usual Sqs auto instrumentation which will take care of your spend creation and context, extraction and span linking.
**Tyler Benson** 11:57 Okay. So on the Java side, I think that there is. And maybe this is where I'm not quite
as familiar. I believe that there's a a wrapper function that so like. If you write a Java lambda invocation handler, you can extend the this wrapper function
this class that kind of does all of that for you. And then you
you can invoke that. I don't think that it's a automatic instrumentation is maybe the problem.
but yeah, this is where, like, it's been a couple of years since I've done this. And so my my recollection is getting really rusty.
My! My day-to-day job doesn't really deal with aws as much as it used to, but
my my recollection is that there there was some way for this to to work with Java at least.
**Warre Pessers** 13:08 Okay, that sounds interesting. But I don't know if you might be able to still figure out where
that code is is at, because I did scheme quickly through some other language specific implementations. But I wasn't familiar enough with them to really comprehend it quickly.
But if you can link it later on.
**Serkan Ozal** 13:34 Actually one of the I mean one of the points I have been thinking on that as of now. The the lambda handler
wrapping and auto instrumentation is handler, I mean, in the upstream Js repository and the All. All the logic is there and then. When we start working on the I mean custom. I mean some by by introducing some custom logic to to extract trace context from from different
types of lambda events like the Sqs. And Sns. It might be. I mean a little bit harder for us to
to apply all these changes to the upstream Js repository. Maybe we, we might think of introducing a new kind of
I mean a wrapper concept or something like that on the
upstream Gs Repository, so that we can
handle some of such such logics on our side in the layer layer repository, because I mean, as of now, the sip and creation logic is there and then once we decided to create the.
for example, for the Sps message processing spans. We also need to control the the invocation span which is created by the upstream Gs Repository. So what I believe is that I think we might 1st
find a way to
to have the control on the span creation logic which is managed by the upstream Gs Repository. Just to to find a way that we can. We can all write or customize that logic in our site, because otherwise we will have to move many logic to the upstream Gs Repository. And and also it might mean, take more time to to update and just just introduce new
new improvements for for the different event types.
**Warre Pessers** 15:39 Yeah, that sounds good to me as well.
I'm down with doing it that way.
**Serkan Ozal** 15:45 Yeah, actually, currently, we have an Aws lambda instrumentation object, which is.
and some some of the configurations are passed through. These instrumentation object to the to the upstream Js Repository, where the the core of the instrumentation lives there.
So maybe we can introduce some another property to to the existing aws from the instrumentation
to hook into that I mean span creation or span customization process in the upstream Gs repository. So we will be, I mean.
move faster, or will
have our own. I mean custom logics on our side through these new, I mean, who point, maybe.
or the instrumentation object aws the instrumentation object, because I mean, as of now, there are already some some properties and functions to be customized, some some behavior. I think we can also use
that approach, for I mean
for the extraction, I mean at least context extraction and some other I mean customizations like customizing or ignoring the rule. Span the invocation span.
but just just I mean very rough ideas of now. I mean in my mind, as I said, just couldn't find time to to think about in detail, but just I'm feeling that it might be
but the best way to to deal with. I mean.
with these, I mean context, propagation issue.
**Warre Pessers** 17:21 Yeah, that sounds like a good idea to me. I did look into the current options, the current configuration options. And I concluded that they didn't seem to be sufficient enough. But I think if we can add something to that, we might be
good to go here. Yeah. So I suggest we look into that. Then I think that's a good idea.
**Tyler Benson** 17:44 Did you see on the chat or in the the the the notes. I included a link to Java's Sqs. Handler?
So there's actually a library that gets published as as a jar that you can have as a dependency, and then extend the the tracing message handler, and it will give you, I think, the functionality that I've been talking about.
**Warre Pessers** 18:15 Yeah, I see. Yeah, I'll look into that one as well, then might be interesting to
maybe draw some parallels from this one. Thank you.
Yeah. I don't know if you need to talk about this issue further, or is this has been
discussed enough? Then.
**Tyler Benson** 18:40 Okay.
**Warre Pessers** 18:41 Think we can move forward with it.
**Tyler Benson** 18:44 Cool.
Max, I think you're next.
**Maxime DAVID [AWS Lambda Runtimes]** 18:50 Yeah, so I've created a pr, like 3 or 4 weeks ago in the open telemetry collector contribute
to reduce the number of allocation made by this, this.
this package. It has been merged, and it has just been released. So I will create a new Pr on our repo to bump to that, and I suspect that we will see
quite an interesting performance gain in the course. Start duration. So I will do some some benchmark, and if we have an interesting number, I might create like a small blog post about that, because I think it's it's interesting to
to explain how go in it is working, how the allocation has been detected, and just talk about the like open source fashion of how to to deal with this kind of issue. So let's see how it goes. But I am really looking forward to to see the numbers. So yeah, just just a heads up that I'm going to create a Pr to bump this package.
**Tyler Benson** 20:01 Nice job.
**Serkan Ozal** 20:02 Yeah, sounds sounds really good. And really, I mean, we appreciate for your report. And Max, actually, I mean, I think months ago, I mean
we actually, I mean, I have been discussing with Tyler and Ivan, after the nodes called start improvements, whether we should, I mean, write a blog post on on those improvements. Maybe along with your improvements on on the collector, I mean, we might just, I mean, write some some kind of blog post series on the All. These calls start improvements.
**Maxime DAVID [AWS Lambda Runtimes]** 20:37 Yep.
**Serkan Ozal** 20:38 SDK side and and the collector layer side, and so some other further, I mean plans we can do like. I mean, maybe I just mentioned about in the previous meeting, about the kind of lightweight proxy layer in front of the actual layer to to register.
Yeah, I think that might be interesting for for all the comment in the service world, because, I mean, you know, the call start is
one of the most famous, maybe the most I mean the famous issue, I mean challenges actually in this world.
**Maxime DAVID [AWS Lambda Runtimes]** 21:10 Yeah, it would be great to have like a multi author blog post talking about different optimization. You've done in the past. So yeah, I'm definitely looking forward to it. Yeah, let me let me see the number, because I hope we will gain at least 2 or 3 ms, maybe a bit more. But let's see how it goes.
**Tyler Benson** 21:31 Nice job, everyone.
**Serkan Ozal** 21:33 Yep.
**Tyler Benson** 21:37 And then once that's since that's merged was that included in our latest layer release as well, or do we?
Oh, so their release.
**Maxime DAVID [AWS Lambda Runtimes]** 21:47 Oh, so no. What I meant is this, Pr has been merged on the upstream collector. Contribute go package, and 2 days ago these Prs has been included into the release. So know that the new go module is ready. We need to bump this dependency to V, 1, 1, 2, 9, and then we need to create a new layer release. It's a bit long, but we will get to it.
**Tyler Benson** 22:16 Okay, is that something that we need to do manually, or should depend about pick up that update.
**Maxime DAVID [AWS Lambda Runtimes]** 22:25 That's a very good question. I can check the dependable config. Yeah, that's that's a good point. It has been released 2 days ago. So maybe it's too soon. I don't know how frequently depend about is checking the release for for go. Yeah, I can. I can check that. Yeah. Let's see how it goes.
**Tyler Benson** 22:45 Okay.
**Maxime DAVID [AWS Lambda Runtimes]** 22:50 And yeah, just last thing, I think the I fixed the all the comments on the node. Gs samples. Pr, I think you all approved. Maybe we want to to merge that. I don't know if you if you have any outstanding feedback, but maybe let's let's merge it.
**Serkan Ozal** 23:09 Yeah, actually makes. I mean, I saw that I just forgot to merge your peer. And then there are some- some conflicts.
**Maxime DAVID [AWS Lambda Runtimes]** 23:16 Okay. No worries.
**Serkan Ozal** 23:17 And just just message you in the Github. So if you are just resolved the conflicts I am, I mean, okay.
**Maxime DAVID [AWS Lambda Runtimes]** 23:25 Okay, no worries. I'll check after work. And I'll resolve the those. I guess it's like package, log or pages package, Jason, or something like that.
**Serkan Ozal** 23:33 Yeah. Sorry for forgetting. I mean to merge your Pr. In the just after the I mean.
**Maxime DAVID [AWS Lambda Runtimes]** 23:38 Yeah, no worries, no worries at all. Don't worry. I I know that we all taking our free time to to.
Yeah.
It's so. Yeah, no, no stress.
**Serkan Ozal** 23:51 Another topic to to discuss for minimum.
**Tyler Benson** 23:56 Serkin. You've got the last one, I think.
**Serkan Ozal** 24:02 Sorry
**Tyler Benson** 24:03 So you I added your earlier in in the chat you asked about changing the meeting time. So I added, that agenda for today.
**Serkan Ozal** 24:12 Yeah, yeah, actually, guys, I mean, the the current start time for for the meeting, I mean
is a little bit I mean harder for me to attend, because I mean because of some personal stuff like I mean, I have to pick up my my kid from from school, and then just
came to home and then joined the meeting, and I would be happy if we could move it to I mean, half hour or 1 h earlier. The meeting, if I mean it, works for for everyone, so it will be easier for me to attend one time just one time. Otherwise I mean
time to time. I might be
a little bit late to to the meetings.
Just wanted to ask everyone whether it works.
**Tyler Benson** 25:03 Maxim, what time zone are you in.
**Serkan Ozal** 25:06 Yeah.
Please. Go. Ahead. Thanks.
**Maxime DAVID [AWS Lambda Runtimes]** 25:09 Oh, sorry you asked me. Tyler.
**Tyler Benson** 25:11 Yeah.
**Maxime DAVID [AWS Lambda Runtimes]** 25:11 Yeah, I'm in Dublin, but I will relocate to Montreal actually, in September.
**Tyler Benson** 25:16 Oh, okay, yeah.
I wasn't sure if you were in the West Coast or something. But.
**Maxime DAVID [AWS Lambda Runtimes]** 25:22 No, I'm in Dublin. Yeah. I'm in Dublin.
**Tyler Benson** 25:25 Okay, I I'm in the the Us. East coast time. So it's not so bad for me either. Either way. I just I don't know how many people we've been having. It sounds like it doesn't. We haven't had any one attend from the West Coast but moving it earlier might be difficult for West Coast folks.
so I don't know if it's possible to to go slightly later and target a later time, but
like maybe 30 min later, we could potentially just do a 30 min meeting and start 30 min later.
**Serkan Ozal** 26:09 I don't know if that would be enough of a time change for you actually
30 min letters, I mean becomes a little bit, I mean later for me. So if it is.
can be 30 min before I mean earlier, it might be better. But if not,
let's keep it as is. I think it. It will be better for me.
**Tyler Benson** 26:34 Okay. So later would be worse for you.
**Serkan Ozal** 26:37 Yeah.
**Tyler Benson** 26:38 Okay, so we could see about moving it 30 min earlier. I I think that would be okay.
Is that what you're asking for?
**Serkan Ozal** 26:52 Yeah, I mean 30 min early, I mean will be better for me, but not sure about for
for that. I think he's okay for for Max and worry, but not sure about the Ivan.
Maybe we can wait for his response, and then.
**Tyler Benson** 27:07 Okay, do you wanna ask Ivan? And and then we can go from there.
**Serkan Ozal** 27:12 Yeah, sure.
**Tyler Benson** 27:14 Great sounds good to me.
And are we are we due for another release here soon?
Let's see.
Yeah. Looks like the last set of releases was the end of May. So I'm probably due for doing the releases myself.
Correct.
**Serkan Ozal** 27:44 Yeah. The the previous one was was at the end of May, and I think we can. We can have another release.
**Tyler Benson** 27:54 Okay.
**Maxime DAVID [AWS Lambda Runtimes]** 27:55 If if I can ask you, Tyler, to just wait for the bump of the the country. Collector, that would be great. Yeah, I'm going to try to check whether or not dependable, but will pick it will pick it up today or tomorrow, otherwise I'll create it manually. No worries.
thank you.
**Tyler Benson** 28:16 We can also, Trigger, depend about to run manually as well, to like to scam, to see if it picks anything up. I but I think that circuit just merged a bunch of dependabot Prs recently. So.
**Maxime DAVID [AWS Lambda Runtimes]** 28:31 I'll check.
**Tyler Benson** 28:31 If any of those are covered already.
**Maxime DAVID [AWS Lambda Runtimes]** 28:34 Okay, maybe it has already been done. Yeah, let me check right now.
**Serkan Ozal** 28:37 Yeah, last night, I mean, I have merged. Actually.
today, I think maybe earlier today, I have merged, I mean.
Pr from from dependable, and there was from from collector, too. So maybe I mean
your improvements, I mean has already merged into the dependencies.
**Maxime DAVID [AWS Lambda Runtimes]** 28:58 That would be.
**Tyler Benson** 29:00 I do see some collector contrib dependencies merged. Do you know exactly which dependency it was.
**Maxime DAVID [AWS Lambda Runtimes]** 29:08 Yes, it's ottl.
**Tyler Benson** 29:17 Okay.
**Maxime DAVID [AWS Lambda Runtimes]** 29:27 collector depths, 45 updates. Let me check Ottm.
**Tyler Benson** 29:37 I don't think we have. I mean, I don't see it in the list of this dependencies.
**Maxime DAVID [AWS Lambda Runtimes]** 29:43 Actually sorry I did not want to interrupt.
Fine change.
Yeah, I can. I can check offline. I don't. I want to be respectful of your time.
**Tyler Benson** 29:55 Yeah, just let me know, and then I will work on a new set of releases this
this week, probably to to probably tomorrow.
**Serkan Ozal** 30:07 Either. Will you handle the new release, or should I take care of.
**Tyler Benson** 30:13 I can. I think you did the last one so it's I think it's fair to switch back and forth unless you like doing them. I'm happy to let you do them.
**Serkan Ozal** 30:24 Okay.
**Tyler Benson** 30:26 So great sounds like it was taken care of.
**Maxime DAVID [AWS Lambda Runtimes]** 30:32 Yep. Awesome.
**Serkan Ozal** 30:38 Okay. Also. I mean, I will work Max Pr. About the nodes template once, I mean, he resolved the conflicts.
and then I think we, we will be ready for for the new release.
**Maxime DAVID [AWS Lambda Runtimes]** 30:52 Sure. Yeah, I'll resolve the conflict like a bit later today.
**Tyler Benson** 30:58 Okay.
**Serkan Ozal** 30:59 Thank you. Everyone.
**Maxime DAVID [AWS Lambda Runtimes]** 31:01 Thank you. Everyone.
**Tyler Benson** 31:03 Bye.
**Warre Pessers** 31:04 My.
