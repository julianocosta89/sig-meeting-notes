SIG: Java SIG
Date: 2025-07-31
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/KhgsTm341NrzVCCxQt_90brZ0MGuiYkg1Aid8aI7NKt9qAXFQ4ibGNGc8mOkN29M.8q2LLh2L-gHiLW3f
============================================================

## Zoom Recording Transcript

Trask Stalnaker 00:01:16 Hey folks.
Jason Plumb 00:01:25 In March.
Trask Stalnaker 00:01:25 Either. I think we have the same color T-shirt on.
Peter Findeisen 00:01:28 Oh yes!
Trask Stalnaker 00:02:03 Alright.
Let's see, declared or configure. July 24.
Got it so we should.
I won't make everybody read. Let's see, I can leave names in. Who are I can do this.
Jay's here. I feel like a school teacher checking people in Jonathan Jason Gregor Trust Stasnaker. Wow!
I just typed my own name Peter Laurie.
John. Alright! And this is alright. Thank you. Whoever's updating dates?
Fantastic. We've got 0 topics.
What do people want to talk about.
Alright, I can add
John Watson 00:03:26 I've got a logistical thing. We should probably figure out with Jack out, who are we gonna try to do a release next week, because I don't know if anyone really knows how to do that. At this point.
Trask Stalnaker 00:03:43 Sorry.
Jason Plumb 00:03:43 You just follow. I'm sure you just follow releasing.md, and it's really easy.
John Watson 00:03:47 I mean, it probably is pretty accurate as long as nothing goes wrong.
The question is, who has time to do it?
Cause it does take. This does take time to make it all happen.
Jason Plumb 00:04:00 That's true.
Trask Stalnaker 00:04:05 Google Docs. Sorry the font is really annoyed me, and I can't do to fix it.
I'll give up I I mean, I think, can approvers make releases.
Jason Plumb 00:04:29 I don't think so.
John Watson 00:04:32 Yeah, I think it could be.
Jason Plumb 00:04:33 Be surprised if those actions allow it.
John Watson 00:04:36 Yeah, I think it would have to. They, they think, run by by maintainers.
Trask Stalnaker 00:04:42 So I you can run. Yeah, this is something I learned recently the cause. I had looked it up for something else. Actions to run dispatch workflow actions. You just need right access to the repo.
John Watson 00:05:00 Which would not include approvers, then cause it does.
Approvals can't merge, though.
Trask Stalnaker 00:05:08 No, but that's blocked in a different way. But they do have right permission.
John Watson 00:05:14 Huh!
Trask Stalnaker 00:05:15 I'll show you the setup, because it's interesting to know and of course I can see it because I'm a github admin. But normally, I wouldn't be able to see this on this repo so if we look at.
Jason Plumb 00:05:32 Oh, I need to set up passkey. Oh, I keep forgetting that.
Trask Stalnaker 00:05:37 So Java approvers have right access.
But the reason they can't merge is this restrict who can push to matching branches so on the main branch.
We restrict only.
John Watson 00:06:00 So what does right access mean?
If you can't merge like what is right, what does right mean? If you can't merge.
Trask Stalnaker 00:06:12 So the real thing that it means for us is that code owners work?
If you don't have right permission, then You can't be in code owners. It won't automatically assign.
The other thing you can do would.
John Watson 00:06:39 Right? Right? Doesn't right? Doesn't mean right, really.
Trask Stalnaker 00:06:44 I mean you can push to a random branch in the repo.
John Watson 00:06:48 But not to me.
Trask Stalnaker 00:06:49 Yeah, but it shouldn't really be doing that, anyways.
John Watson 00:06:56 Except the except that the actions release actions do that.
Trask Stalnaker 00:07:05 Because they create, they create pull requests.
But those those are not run. Yeah, those wouldn't be run under like my credentials if I ran the release action. It runs under the the actions github tokens secret.
Is yaml so it'll pull these secrets
John Watson 00:07:43 Those are Sona type ones that's not.
Trask Stalnaker 00:07:45 Yeah.
And then this is for choose to create Github release.
So these are using the permission. This is what we've been updating everywhere across all the repos is these permissions.
these permissions apply to the Github action the built in secret token secret that Github actions have access to except on Prs Prs. Don't have access to those that any secrets or that special token.
But this sets up what permissions that token is allowed to have.
John Watson 00:08:35 And right access also also allows running dispatch actions.
Trask Stalnaker 00:08:41 Yeah.
John Watson 00:08:42 Okay.
Trask Stalnaker 00:08:44 Yeah, I was a little like I was kind of surprised to I I was surprised to learn that because that was a whole extra.
John Watson 00:08:56 Yeah, that's surprise. That's that's that's somewhat surprising to me. I didn't know that our approvers were all basically allowed to run any action which runs as essentially a a user with infinite power, right.
Trask Stalnaker 00:09:18 Not quite infinite. But yes, okay.
Jason Plumb 00:09:21 Yeah. Approved.
Trask Stalnaker 00:09:22 You mean pretty close, though.
Yeah.
Now for the release process like you wouldn't be the release process generates a those 2 prs, the prepare release.
And so those have to be merged by a maintainer.
John Watson 00:09:41 Can they run dispatch actions on other branches, though, like using the using code from using the the workflow definition from another branch.
Trask Stalnaker 00:09:57 I see what you're saying. Yeah, to like, try to steal a secret.
John Watson 00:10:01 Yeah.
Trask Stalnaker 00:10:02 I think so.
John Watson 00:10:03 Okay, that's really good to know. I was not aware of that.
So our approvers do actually have significant amount of power that I was not aware of.
Trask Stalnaker 00:10:14 Yeah, Jason, maybe you can, because I have. Everything is skewed for me, since I'm a org admin. But if you go to release. You should see the run workflow button here.
and you should be able to pick the branch.
Jason Plumb 00:10:32 Let me verify.
Yes, I can do that.
Trask Stalnaker 00:10:41 Yeah.
Jason Plumb 00:10:42 Yup. So if those 2 Prs get created and a Maintainer merges them.
then, technically, yeah, it seems like an approver could do the release.
I don't have time for it. Unfortunately.
Trask Stalnaker 00:10:57 I I can, John, I can drive. I I'm very familiar with this release process, so I I can drive it and just ping you for merging the prs that are needed.
John Watson 00:11:09 Cool, cool, cool. It's not till next week, anyway, so like.
Jason Plumb 00:11:12 No, it's next week.
Yeah. I might be able to.
Trask Stalnaker 00:11:15 Oh, I'm out next week, Wednesday, through Friday.
Jason Plumb 00:11:22 Oh, my God!
John Watson 00:11:22 It's really good to have someone who isn't familiar, like Jason or somebody who, if they have time next week to go through the process and make sure our documentation is actually accurate.
Jason Plumb 00:11:31 Yeah.
John Watson 00:11:32 Because I think, like Jack when I was doing it I had done it a lot and was. Jack has now done it a lot like probably doesn't even look at the documentation. So probably be a really good double check to make sure that documentation is up to date.
Jason Plumb 00:11:45 I ran through it in contrib like whatever it was like last month, and I've been running it in Android, and it's very similar now. So.
John Watson 00:11:53 We have a I think Java has a few extra steps. Just because we there's a there's a lot of weird documentation stuff that we automatically update and things like that. So.
Jason Plumb 00:12:04 Okay.
Trask Stalnaker 00:12:05 Wait recently Consolidated that those post release steps should all be automated now in the core repo. They weren't recent until recently, though.
John Watson 00:12:17 Yup! Yup! Yup!
Trask Stalnaker 00:12:18 So, hopefully.
John Watson 00:12:19 Yeah, exactly. Exactly. It'd be good to run through, sure that it all works always good to have double checking.
Yeah, I'm gonna be. I'll be around so I can approve. And if there's release stuff that needs to be fixed, I can probably figure out how to fix it. Probably find some time.
Trask Stalnaker 00:12:40 But font does a Mac.
Jason Plumb 00:12:42 Every time. And we typically do those on Thursdays right.
Trask Stalnaker 00:12:47 Right change log on Thursday. Send the change log on Thursday.
John Watson 00:12:54 Prep. On Thursday release. On Friday.
Jason Plumb 00:12:56 Okay, that's cool.
John Watson 00:13:02 Although I mean there's nothing that's super super strict.
but that's generally the the timeline.
Trask Stalnaker 00:13:17 Right jay jay you want to share.
Jay DeLuca 00:13:27 Yeah, sure. Let's look at it.
Yes, I this. This shouldn't take too long. But I just wanted to mentioned that I started experimenting with weaver. I kind of just picked up a random example of.
I grabbed the Oshi instrument like long close my door one second.
Yeah. So I just wanted to play around with it and see kind of the capabilities and and start seeing where it may or may not fit in with the instrumentation repo. And so I took a lot of inspiration from Jason and Antoine's example. Stole their docker file and things like that but and created like a template that generates the the metrics with ginger which ends up generating this file here. And then I basically just went in and replaced where we were manually creating the metrics with the the new ones. Everything seems to to work pretty well. It's I don't know whether it's good or bad. To be honest, it was a lot of work to write the the ginger templates and to maintain them again. I kind of approached this as an experiment. And what I was thinking of doing next was to pick like maybe a more modern example that uses actual like semantic conventions that I can just pull in as opposed to generating them manually. Actually, some of these might even be available within, like one of the the semantic convention registries.
But yeah. So nothing really to no action here from anyone. But I just wanted to throw it on the radar that I'm just playing around with it in case anybody wants to take a look and has feedback. But the the next thing that I plan to explore like I said, I'm gonna try and see what it would look like for another module, and then see where I might be able to reuse some of this, because, as of right now.
like the model definition, and the templates and and things like that are all within this one module, and it would be really gross, I think, to have that all duplicated per module. So I want to try and figure out what it might look like to have some shared resources and see if see if I can get these ginger templates to work generically so that we can just use the same one for each one. But so yeah. And then I I brought the Metadata project to the Weaver Working group this week just to kinda demo it and and get some feedback and I got some some good notes there they like one of the things that I think also plays into. It is the declarative configuration project and defining our configurations with Yaml and it is on the the roadmap for Weaver to be able to handle some configurations. Nothing's there yet but I'm gonna try and follow along and see if there's anything I can do to help with that But yeah. So no, I just wanted to to let you guys know that I'm I'm playing with this. If anybody has thoughts or or feedback wants to review the Pr, that'd be great. But yeah, it's still kind of a work in progress. Maybe I should denote that, but that's about it.
Jason Plumb 00:17:00 I had a question about these metrics. Do any of them make reference to existing external semantic conventions like, are there any metrics that have attributes that are elsewhere. And how did you handle that.
Jay DeLuca 00:17:13 I I think so. But I didn't handle it correctly. So like I, I basically redefined everything but that like I said the next thing that I want to play with is pulling in the existing registries as dependencies, and and swapping those out and seeing how that all works.
Jason Plumb 00:17:28 Okay. Cool.
Trask Stalnaker 00:17:35 So if as far as the I I like that because it's all just implementation detail, like swapping out implementation detail, it's seems very like easy from to approve. You know the test all pass. We're not changing any public Apis and so we can move forward with the experiment.
What would. So it would, as far as the shared aspect across multiple instrumentations.
We would. There wouldn't really be like a shared code base because it would generate that there would be basically generated code in each module that each module uses.
Jay DeLuca 00:18:31 Yeah. So the the shared thing would just be like the the temp, the ginger templates.
So basically something like this that basically has the code to to take in the different types of metrics and emit, you know, the whatever the builders are for each one.
and I don't know how like I created this. It works great for the metrics produced by this project, but, like I don't know how it's going to scale. Once I try to use it for some other ones. So. But I would think that, like this, custom attributes ginger, template this metrics ginger template, and then these Markdown ones have just a lot of shared. So so that would be the the shared piece. But yeah, the the generated.
like actual metrics, would be based on the individual models within each instrumentation, directory.
Trask Stalnaker 00:19:29 And would we like, I think one of the visions for this generating from generating the code from weaver was basically to be able to generate, like something like our instrumentation. Api, but like a very simplified version that instrumentations could use.
Basically, you know what you've done. But making that something that people externally could use.
whether there's like a standard Http.
you know, generated library for Http or maybe it's just because then that's harder to experiment with because of public Api changing But with a code generator that could change, that was easy for external people to use and say like I want my Http metrics.
I don't know. I'm I'm babbling now.
Jay DeLuca 00:20:34 Redefine it all. I think I understand what you're saying. I haven't gotten too far into that. But yeah, we could. We could certainly play around with with seeing what kind of helper utilities, or or if it's if it's the instrument instrument or Api, or whatever the the only thing. I haven't seen much about spans.
so I'll just start with the the metrics and the attributes for now. But yeah.
Trask Stalnaker 00:21:04 Haven't seen much about spans.
What do you mean?
Jay DeLuca 00:21:09 Like in like I like. I'm not sure.
I I guess we would probably just use the the generated attributes. But like so so within this system, like within an instrumentation, you define the metrics that are used, but like there's no notion of like defining that there's going to be a client spans, or or something like that, at least, that I've seen.
Jason Plumb 00:21:33 No, and we don't generate constants or anything for the names either, like the span names. Just it's just in line in most cases.
Trask Stalnaker 00:21:47 And so for kind of these standalone metric, it does seem like a good target, the ocean. Other standalone metrics things because they don't really use the instrumentor Api.
Jay DeLuca 00:22:00 Right.
Trask Stalnaker 00:22:01 Cause anything. Yeah, that's true. Any tracing instrumentation we have goes through the instrumental Api. So we'll be.
maybe not. We may not be able to port that to the code generated usages.
Jay DeLuca 00:22:21 Yeah, I mean, I do wonder if we might.
I was just thinking we might be able to to do the attributes. But I think we're already pulling in those attributes from the simcomp jar, right? So we wouldn't need to necessarily re.
Trask Stalnaker 00:22:37 Yeah, I mean, we already sort of have a lot of the structure in the attributes, getters, and extractors as far as kind of mapping semantic semantic conventions into those instrumentations.
I do thing that it would be nice for other people outside of the project to be able to generate like I see being able to generate, create span like a simpler Api than our instrument. Api, that's just straight from these yaml files, and also that could lead to some kind of shared across language.
Something that works across languages a more simplified like start span. Here are the required attributes. Here are the optional attributes something like that.
Jay DeLuca 00:23:42 Yep.
Trask Stalnaker 00:23:47 Cool. Yeah, I think the the metrics seem like a great place. Maybe just mark it as draft or ping like as far as when you want it to be, when you're ready for it to be like really like to merged. But I think overall I I that makes sense.
Jay DeLuca 00:24:12 Cool. Yeah, I'll mark it as draft. And then, yeah, like, I said, I'm gonna try to do at least one more implementation on another one, and then we can review it kind of in that context, I think.
Cool. Thank you.
Trask Stalnaker 00:24:27 Yeah, thanks.
Let's see, I have the next topic.
More just.
Jason Plumb 00:24:41 That's okay.
Trask Stalnaker 00:24:42 A not sure if anybody else is interested in this topic, yet.
Jason Plumb 00:24:50 Android is.
Trask Stalnaker 00:24:52 Hey? All right.
Jason Plumb 00:24:55 Want to do context to a based filtering of all telemetry. So by context, I mean session based.
So if you have a session that's been sampled or not sampled, as the case may be. Then we wanna not generate spans and logs.
Trask Stalnaker 00:25:16 Got it. So you don't want these specific log record processors, but you want the piece that these are helping to drive. Stability of which is the is enabled, the enabled yes, yeah, like processes.
Jason Plumb 00:25:30 Yeah.
Trask Stalnaker 00:25:31 Which I actually did not implement here. Okay? They enabled. I gotta look at yeah, cause that is still experimental.
But yes, let me write a to do.
enabled also.
Jason Plumb 00:25:52 And can you.
Trask Stalnaker 00:25:52 Yeah.
Jason Plumb 00:25:53 Tr in the doc. Please.
Trask Stalnaker 00:25:55 Yeah.
Jason Plumb 00:26:00 Thank you.
Trask Stalnaker 00:26:01 So just as a short overview of what we're talking about. Let's pull up this back.
So this question of how to filter logs has been outstanding for a while, and the current direction is to leverage log record processors.
Which is a little confusing@firstst like I was kind of expecting to see like a log filter concept kind of like a trace sampler like a log sampler log filter that was separate.
But the way it works is you have this optional method on a log record processor.
and you can implement it and when you call is enabled on a logger. If you kind of like log for Jay, you check is enabled before you do something expensive.
It will check your log record processors. To see if there should be enabled.
Now that becomes very confusing, I think, because of the way our log processors are not telescoped. They're not chained by default. It's like we run one and and then the next, and then the next, and so like would they all have to return. That enabled is true.
What's going on?
So could be, do you way that the proposal here has been that we would basically have these processors be chained except a delegate.
So you would have.
you know, minimum severity filter processor, which would delegate to say trace based filter processor, which would then delegate to the batch processor.
And this way, you know, you're just checking. Okay, is enabled on this, and they can give you a fast response, or it can delegate to this down, downstream.
John Watson 00:28:45 So I.
Trask Stalnaker 00:28:45 One.
John Watson 00:28:46 I hate to ask this question, but what's what's the plan for events?
Trask Stalnaker 00:28:53 Events or logs.
John Watson 00:28:55 I understand that.
But they're not. They're gonna parities right.
Trask Stalnaker 00:29:03 They.
Yes, this is where have we? This has been a topic. What have we said?
I think we're recommending that they have a severity.
yes.
John Watson 00:29:35 I don't know what an event severity means.
Jason Plumb 00:29:38 Yeah, we definitely talked about it. I I think there was even, I think someone suggested that we get rid of it for events. But I think that never landed.
John Watson 00:29:48 I mean I don't. As I don't know what it means to have a I understand what severity means. I don't know what an event severity means.
Jason Plumb 00:29:54 Yeah, we're to have 2 events.
Same name, but different severities, right.
Trask Stalnaker 00:30:03 That's confusing.
The I think part of it is the what you are considering an event like, if you're considering event kind of the user events like that's harder. But like, certainly there's debug level events like Http logs are going to be modeled as events.
I hear you.
John Watson 00:30:30 Like events in Android, and things like that.
Trask Stalnaker 00:30:33 Yeah. So in Jen AI, for example, they're defining events. But some events are more like verbose. They're like, contain the payload of the whole prompt. For example.
so in some contexts it makes more sense than in other contexts. Certainly.
I think for and for like user events, what we would say is, well, those should be probably info as kind of like a default. Ish.
There was. What did we say here? This the discussion came up here because log rec the severity.
Discussion.
Yeah, here, I think this was the concession to events that you're kind of.
partly may address your concern, John.
which is so, severity number 0 is undefined is the undefined or unspecified So when comparing severity, you may want to have special handling for that, and I should add this here cause. That's a good point.
John Watson 00:32:18 We should just make all events at severity. 6, 6, 6, just to exactly.
Trask Stalnaker 00:32:31 And then, so the enabled is just an optimization essentially because you can't guarantee that somebody is going to call is enabled on something. And so you also in the on emit need to apply that same filter downstream cool. So maybe, since you're interested, Jason.
well, we'll probably chat next week about this. If you want to join the log, Sig.
Jason Plumb 00:33:08 Yep.
Sounds good.
Trask Stalnaker 00:33:14 All right.
Patrick. Welcome.
patrickpok 00:33:23 Yes. Hello, everyone. Can you guys hear me?
Trask Stalnaker 00:33:26 Yep, yep. So this is my 1st time ever like in in a sig like with all of you guys. So just thank you guys for welcoming me. I think what you guys before like, if not anything else like, I think what you guys are doing is super cool. So just wanted to say that.
patrickpok 00:33:41 And so I apologize for troubling you guys. I just have a couple of questions. So I've been like looking at the report. And actually, I have some slides to share like, really, quickly, I drafted something just to just have something to show. So I'm not this like Zoom. So I'm trying. I think there's a button share above.
Are you guys able to see like my screen?
Yes, okay. So just couple of slides. So why am I troubling you guys is so pretty much in my organization, we are trying to solve a problem. And I believe that what you guys are doing is one of the right way of doing it. So on the upper left side. And that is something that is like very common like in the industry.
like someone who would use, like a springboard producer to push some messages to Kafka and have a springboard consuming crop from it.
The observability from open telemetry is pretty good here already, from logs, from metrics, from traces, and that's because they did like, I think, an amazing work with, like the micrometer, all the open telemetry on boarding, etc.
So for the spring boot world, it's pretty good, I would say. I'm not an expert, but I would say it's pretty good on our side. We use spark a lot, and we don't use spark just for the data from the database. We use something called the spark streaming, the spark structured, streaming.
It provides like the ability to have spark as a Kafka consumer or as a Kafka producer. And so a couple of examples like, for example, we can have, like any producer, like a sprinkle producer, but any producer pushing something into Kafka queue with the proper headers for tracing as of right. Now, spark has no capability to propagate and continue to trace it. So that's the upper right one and replace the green box with like any languages or any framework, who has the ability to produce a message with proper header and with proper trace. Unfortunately, as of right now, there is no easy way for spark streaming to propagate it, and it's the same with the other way around. Spark can emit messages inside Kafka as well and as of right. Now there is really no easy way to properly instrument and have the traces as well, and obviously the lower right one, which is like when we have a spark to spark. Then I feel like it's like we are totally blind.
So that's why I was just wondering if you guys would think it makes sense. So yeah, Apache spark. So I know that in the repo you guys have something called spark already. But that's the tiny spark which is like a web app. I'm talking about the Apache spark, and for me, I think there is like a gap to fill and like a problem to solve the problem statement which is in Apache spark, the tracing for for all the messages, consumption from Kafka, or producing and consuming, is really like near 0. So that's something that I was wondering if you guys would think would be interested to address. So just what I would like to hope so I don't know how to do it, but definitely like, just so that I have a plan just to get some idea and get the discussion going is my kind of dream is to have this Java agent, because Spark really supports quite well the Java agent. It's like on the driver side or on the executor side, just to instrument and give the possibility to spark. The driver and the executor.
to combine with the Java agent and the Java agent will take care of the 1st of all, propagating all the traces from those consumers, like as a consumer, or from all those producers which produces messages with the proper trace for spark to do it from the Java agent side. It is possible to do it manually. And there's actually a lot of code online stack, overflow Github of people trying to do it manually. So, instead of having each and everyone doing their source of doing it manually, maybe it will be a cool idea to have it on the Java agent level. That's like.
really would like to hear your feedback on this. And obviously, if we do it, one way is to do the other way, which is, if one day like, we produce back to Kafka. That will be something interested if the Java agent can help us without having everyone rewriting the manual instrumentation.
and that is really for the future. And what spark is really good to do is write those data back into some kind of database, as of right now, is also really not observable. And so it will be cool also to help with that. But just to come back to this one. Which is this is really my question to this group, which is.
I really feel there is a gap right now in terms of spark which is widely used in the industry, the spark structure streaming a little bit less, but still use, but as of right now it has no really real ways to propagate and continue all those traces sent inside Kafka, while spark structured, streaming with Kafka, is like a giant topic. So I was just wondering if you guys would think that makes sense to enrich this project, this repo with capability from the Java agent to continue and propagate the trace as a spark consumer. This is my question to you guys, and I hope I was clear with my slides. I apologize. I'm from China. So right now you guys are talking to the future. It's already Friday. I'm half awake, but I still really wanted to say, Hi to you guys and to ask you the question.
Trask Stalnaker 00:39:26 Cool. Thanks.
maybe I'll open up the floor. Has anyone here? Instrumented spark in previous Apm incarnations?
Jason Plumb 00:39:49 I don't think we had one in new relic. I don't remember it.
It was probably manual. Patrick, are you? Pat? Pat? 1, 2, 3.
patrickpok 00:39:58 Yes, yes, yes, yes.
Jason Plumb 00:39:59 Okay, cool. I linked to your issue as well. That does the same request. So in the Doc.
patrickpok 00:40:05 I didn't. Okay, okay. But but I think, like I, I'm pretty sure I'm not the 1st guy who tried that. Maybe I like, I'm the first.st
Jason Plumb 00:40:12 No, we. We get this question from our customers as well. And there's definitely been confusion about spark support, because we have that.
Deprecated ancient Http library. So, yeah, this is definitely something people are asking for. And I think it's I think the short story is, we would love help building this. Yeah.
patrickpok 00:40:32 Okay, okay? And yes. So definitely. So I'm very new to the repo. And it's very like, it's imagine just a guy like he opens a repo, and he's like, Wow, what is that? But hopefully, with you guys, help a little bit. And oh, I can understand. And personally, I think this report is interesting because we use the Java agent for other things. And it's like in your talk in Youtube when you say, Hey, you just bind it. And then suddenly, it's magic, and it feels like magic. And already things that are instrumented.
I would think the community, especially the spark community, will benefit of having this magic, which is hey? We are using this spark structure streaming, which is a big thing in the spark world. Apache spark, not the tiny spark thing. And suddenly, if they start seeing those traces from Kafka, I think that will benefit. So just want to run this idea by you guys. And if yes, then I will start obviously asking technical questions, but not today.
Jason Plumb 00:41:28 Okay.
I also linked to the semantic conventions for messaging, because it sounds like you are kind of of the assumption that context propagation should always happen through message cues, and that is not always the case. It's certainly not like the default behavior. The recommended behavior is to use span links to link back consumer spans to their producer spans. So I just want you to be aware of that. I think in in some of our existing instrumentation we have feature flags where you can turn propagation on, or continuation, or whatever. I forget how we're phrasing it. But you can do full just trace propagation through the queue, but it's not turned on by default. I think.
Okay, that's that's all I got. Thank you.
patrickpok 00:42:10 Yeah. And same for me, that's all I got. And hopefully, I'm going definitely to start, you know, raising the Github issue like Antoine told me yesterday to do it, and then hopefully, we can take it from there. So at least, you guys have some context like, who is this guy like suddenly starts with this, and from there, like, I would definitely have a couple of technical questions. You know how to do it in the proper way. So I managed to do it already manually, and the Internet also has, like many stack, overflow posts, proposing solutions to do it manually.
but now making it something inside the Java agent, I think, will be beneficial to the overall community. So from there we will start proposing pis, etc. So just really wanted to run this idea by you guys, and thank you so much for listening to me.
Trask Stalnaker 00:42:52 Patrick. It could be interesting to if you could post like an example great like the example repo of how doing it manually.
Cause that's sometimes easier to read that code than reading the byte code instrumentation stuff. And then we can kind of see like how it like. Understand? Oh, what headers you're passing across, and things like that!
patrickpok 00:43:21 Understood no problem. I I can link that definitely. No problem.
Trask Stalnaker 00:43:25 Cool.
John Watson 00:43:25 And if you're in China it sounds like Trask, maybe you all should connect for the Asia Pac. Meeting.
patrickpok 00:43:32 I went.
Trask Stalnaker 00:43:33 Yeah.
patrickpok 00:43:34 The packet was empty, so I will understand. I don't mind staying up a little bit later in the.
Trask Stalnaker 00:43:42 Cool. Yeah, yeah, it would. Did get the last one was cancelled. But we do meet every other week.
And there's a a few fold like, usually like 3 folks from Alibaba who joined. So yeah. Welcome to join both meetings whatever you like. Yeah. Yeah.
Alright. Drew back to our agenda.
Antoine.
Antoine Toulme 00:44:23 Hey!
Trask Stalnaker 00:44:24 Hey! Welcome to Java! Land!
Antoine Toulme 00:44:31 So I'm not the initiative of this. Pr, but I think I'm listed somewhere down the road like I. I helped a little bit build this code. So I I want to make sure it lands.
It's been sitting there for a while. Took I took a month off. Came back.
I'd like to make sure we blend this.
So what's going to be the best way to lend this?
Do you want to talk about it? Is there a process that we're should follow?
Trask Stalnaker 00:45:05 It looks like it's got looks like it's got approvals. It should.
What will probably happen is, we usually sort of try to get things into like a release. I can go ahead and let's see, we don't have tag. We don't have the wow junk.
Antoine Toulme 00:45:28 Any of these? Okay.
Trask Stalnaker 00:45:33 So this the let's see, what's our next release over here? 1 49.
Antoine Toulme 00:45:45 Okay.
Trask Stalnaker 00:45:47 So I will go ahead and tag it now, so we don't lose track of it.
But I think let's take a look.
because I know.
thanks, Jason, for updating. Oh, there's a lot of this is a lot of lines of code. What is this? 8,000 lines of code.
like Github, is struggling on it.
Jason Plumb 00:46:15 Yeah. I'm sorry about that.
Antoine Toulme 00:46:18 Yeah, I mean, some of it is generated, as you can see, like there's a weaver model. We generate a bunch of crap. So. But there's actually, genuinely a lot of business code as well, because we we do some connections to an Ibm Mq. We get some things. We interpret them. So there's some expertise that goes into reading that code that I don't think this unless you've been very familiar with this type of systems. You're not going to know that off the bat.
So unfortunately, the review of this code at this time can be on correctness, or maybe the approach that this code is taking. But some of the choices it's making. We we need to kind of keep that open for discussion.
So it depends where you want that discussion to happen right once it's merged after it's merged.
Trask Stalnaker 00:47:08 I was mainly reviewing it from the semantic convention side.
Antoine Toulme 00:47:15 Yep, that actually requires a probably a spec with a. So it's interesting, right? We built this weaver model because we needed to kind of make sure we were consistent in what we were doing. There is some work that's done for Weaver, not just with this, but with everything I'm doing in contrib. I'm actually pushing a Pr in contribu for the collector to start to use a weaver model as well. And most recently we had a person who did the reverse. They went to the semantic Conventions Repository. They pushed the weaver model and then they said, Now, Collector, implement, my model. And we're like, wait. That's that's weird. What are you doing?
So? We.
If if you want, we can take this model right now and push it to Sem and have a discussion about the validity of that model, regardless of this implementation.
and start to have that in parallel. So we can speed up a little bit. The discussions.
Trask Stalnaker 00:48:14 I mean, I I like I like it over here like I know the simcom folks in general are overwhelmed with stuff, and so.
Antoine Toulme 00:48:25 Yeah.
Trask Stalnaker 00:48:26 I think it's good to be able to distribute the stuff out.
More. What I meant by reviewing from a some conf perspective was just the following, the semantic con. The conventions used over there.
Would like, you know, this is Jason's updated, based on my original round of comments here.
Already. So it's probably good to go.
everything is scoped to. Yeah, that was kind of my main.
Jason Plumb 00:49:07 Yeah, hopefully, I got them all.
Antoine Toulme 00:49:10 I, you know. Let's be clear, right? This is the 1st draft of something that needs to get some love.
Jason Plumb 00:49:14 Exactly.
Antoine Toulme 00:49:15 Just we're not going to stop there, and then, surprised that the.
Jason Plumb 00:49:21 Double dime.
Trask Stalnaker 00:49:23 Yeah.
Jason Plumb 00:49:24 Oh, it's impossible! How does that.
Antoine Toulme 00:49:29 Oh, my God! Who wrote this.
Trask Stalnaker 00:49:31 Catch this.
Jason Plumb 00:49:33 That is interesting. Yeah, huh?
Trask Stalnaker 00:49:35 Yeah.
Jason Plumb 00:49:36 What did it do? Yeah.
Antoine Toulme 00:49:39 Oh, you should see, Weaver don't care right? So Weaver.
Jason Plumb 00:49:42 Name.
Oh, no, it's the id.
Antoine Toulme 00:49:45 Id. The id is not the name. The id is just. Some waiver is just like interpreting your stuff into Yaml, and then you apply ginger template on it right. The validation of it is also probably for some reading. The.
Trask Stalnaker 00:49:58 I see it's not the metric name. Yeah, yeah.
Jason Plumb 00:50:01 Yeah, probably just uses the literal there and doesn't, doesn't matter. But that's fine.
Antoine Toulme 00:50:06 It's still about.
Jason Plumb 00:50:07 Yeah, it is.
Antoine Toulme 00:50:09 That's good.
Jason Plumb 00:50:10 I'm sure that's a find and replace problem is what that is.
Trask Stalnaker 00:50:20 This is interesting. Do like a you can, sounds like.
Antoine Toulme 00:50:26 So it comes from the the system itself, and if you go and read the the specs on Mq. They said they they offer that the the way it works is that when they report this metric they report it with 2 values which have different timelines, which.
so the 1st value is the time spent on the in the queue on a short interval of time, like in the last minute, on average, and then the second one is on a longer time. They don't actually specify what longer time is.
So you'd have to kind of interpret what that could mean.
And, you can't really do much about that. So you're like, those 2 metrics are actually different, and they don't mean the same thing.
Trask Stalnaker 00:51:13 Yeah, I was just wondering if so the the this would not be like a valid variable name.
In some, maybe.
Yeah, I was just thinking of
Antoine Toulme 00:51:35 So you would like it like maybe short. Instead of that one.
Trask Stalnaker 00:51:39 Yeah. Short window period
Antoine Toulme 00:51:47 Yeah, I mean, some, some videos.
Trask Stalnaker 00:51:49 Even window one just not starting with a 1.
Antoine Toulme 00:51:55 Oh, okay.
Trask Stalnaker 00:51:57 Right.
Antoine Toulme 00:52:00 Too right.
Trask Stalnaker 00:52:00 Yeah, I don't think, yeah, yeah.
I don't think we have a rule in some com about that, but I don't think I've seen any.
Some comp attribute.
Antoine Toulme 00:52:13 For what it's worth. Basically.
these are good feedbacks also for even applying back to all the way to weaver, because we run validate on this Yaml file.
and you know it doesn't barf, which doesn't mean.
Trask Stalnaker 00:52:27 Yeah, this. Why not?
Antoine Toulme 00:52:29 I would use that as a test case to push back on the weaver people and tell them, Hey, you need you should have caught this right. Let's use that as a as a great dog fooding exercise for ourselves.
Jason Plumb 00:52:41 Well, there's 1 thing I might have mentioned in the description, but I know that we did not. In this Pr. We did not include the golden set of Integration Test metrics like we have.
Antoine Toulme 00:52:52 Yeah.
Jason Plumb 00:52:52 This golden image, and I know, Antoine, you're doing some work over there to get that golden.
Antoine Toulme 00:52:56 I landed that yesterday. So you're now. Yes, no, you did the right thing.
Jason Plumb 00:53:01 Okay, so there will be follow up efforts required to like wire that up. But we've got like a huge set of like test data that we can run through this thing with a real queue, like running running Mq. And Docker, and then making sure the metrics come out correctly.
Antoine Toulme 00:53:16 So on that. So, okay, this is a massive pr.
would you, in collector, when people send us thousands of lines at once, the collector. Country people have built an immunity system that that is pretty much. If it's over 500 lines, you can go take a hike.
Would you like that to here, because this is also a way to do this is rather than 3 to jam through 8,000 lines. It's Java. So maybe it's more verbose. Maybe you're more used to having lengthy reviews.
but if you want, we can also break it down into like multiple smaller ones. And maybe that makes the discussion a bit easier overall because you don't have to toggle through 10 lines of 10 files to find what you need.
And I'm I'm not saying we close this Pr.
but we could also just take it in. You know, kind of thing I do is like, I take a big Pr, and we we just take a slice of it. And then, you know, we're just lending the the folder. We're just lending the build file. We're just lending the model. We're just lend. Do you see what I mean?
Trask Stalnaker 00:54:20 Yeah. I think if this were landing in the Java instrumentation repo or the core repo, we would.
Antoine Toulme 00:54:31 Likely. Ask for that.
Okay.
Trask Stalnaker 00:54:34 But over here. It's very decentralized ownership. And so basically, as long as you, the component owners.
approve it.
We will probably merge.
Jason Plumb 00:54:50 Yeah, I think, almost there. Yeah.
Antoine Toulme 00:54:55 Okay.
Jason Plumb 00:54:56 Who's who's listed as components like me and Antoine and.
Antoine Toulme 00:55:00 Well, we're the only 2.
Jason Plumb 00:55:03 Maybe.
Antoine Toulme 00:55:03 Members. I don't think Matthew is a member of a pendometry yet, but that's we need to fix that.
Jason Plumb 00:55:09 We do need to fix that.
Antoine Toulme 00:55:11 Because I think he would be a better owner. Peter also has, I think, some view into it at least. He reviewed a couple of things. So why, I would add, Peter, right, and and whoever else here like, if you've ever had this secret desire to do more stuff with Ibm. This is your chance. This is your once in a lifetime offer.
Don't take it now, take it now.
Jason Plumb 00:55:37 No one ever got fired for doing more stuff with Ibm.
Antoine Toulme 00:55:42 We all will retire rich and healthy. That's what I'm hearing.
Trask Stalnaker 00:55:47 Alright. So yeah, I think we're. I. I think this is on track to make the August release which is currently scheduled for the 13 slash 15.
Antoine Toulme 00:56:06 And if I may, so maybe putting a different hat on for a sec. If this lands, is it okay? If we go and make a blog post on that, just to kind of get some excitement from the vast Ibm crowd. Enthusiasts out there.
Trask Stalnaker 00:56:21 Of course, the blog, the the blog people are always asking for more more submissions.
Antoine Toulme 00:56:28 All right.
Okay.
Trask Stalnaker 00:56:34 Yeah, in general, that would be it for the whole group here. The the would be. It's a great practice to when we land something to send a short blog about it.
Antoine Toulme 00:56:50 Yeah, I mean, I I already told my bosses like we should talk about it at Qcon.
just even have some some level of understanding of like what this type of development means for open symmetry. How is it used?
Because this is a interesting application of it?
Then there is also the interest for Weaver. Right? There's there's a discussion there, and seems like this is like kind of coming together. So want to use that momentum as much as possible.
Jason Plumb 00:57:19 Cool. Thanks, Antoine. This last one I know we're out of time, so I'll keep it very short. But I just occurred to me earlier, when we were talking about the instrumentation Api or the instrumentor Api rather. That this is something I did. We have a bunch of events that are like 0 duration spans that we're in the process of bringing over to actual events, and some of that some of those spans are generated using the instrumentor.
and it becomes very quickly apparent how coupled to tracing the instrumentor Api is like it. It should have been named like a tracing instrumentation tracing Api, or something like it's not geared at any other any other signals. So this is like.
I made a different attributes, extractor, because the existing one has on start and on end, which don't make sense for events. And that's the long and the short of this is like.
and I guess a question that falls out of that is, are we giving any consideration to expanding the instrument instrumenter Api to include other signal types like, is there room for stuff like this in the instrumentor Api, that can be a topic for later. I just want us to think about it.
Trask Stalnaker 00:58:29 Yeah.
I don't think we we need more. Well, do you know, if I haven't looked at Honorog's gen AI Openai Prs have included events.
Jason Plumb 00:58:47 I also haven't looked at those.
Jay DeLuca 00:58:50 I don't think they well, they they are admitting logs.
So is that a maybe. Then.
Trask Stalnaker 00:58:58 Yeah, that's a, maybe.
Jason Plumb 00:59:04 Cool.
Trask Stalnaker 00:59:05 So. Yeah, I mean, I wonder if sort of this auto generation, the weaver generation for the simpler signals, like metrics and events that are like could work for that. Or if there's benefits to the if we even need sort of these, all these hooks that we have, that we need for the tracing stuff.
Jason Plumb 00:59:38 Yeah, that's a good. That's a good point. There's there's like, no life cycle. And that's really what the instrument helps handle is the life cycle getting stuff on request, getting stuff on response. Yeah.
Trask Stalnaker 00:59:51 The instrument or Api, I mean, it's great for our purposes, but it's a bit complicated for end user, like, like we had at 1 point thought that this would be something that you know everybody could and should use.
But it's a little complicated for that, which is what I like about the weaver generation.
Sorry. Just noticed the time.
Jason Plumb 01:00:21 Yep, thanks. Everyone.
Trask Stalnaker 01:00:23 All right.
Jay DeLuca 01:00:25 To be honest.
Trask Stalnaker 01:00:26 I.
Jason Plumb 01:00:26 Bye.
