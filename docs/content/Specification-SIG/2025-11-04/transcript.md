SIG: Specification SIG
Date: 2025-11-04
Duration: 78 minutes
============================================================

## Zoom Recording Transcript

Bogdan Drutu 00:03:18 Everyone.
Pellared 00:03:22 Hello.
Trask Stalnaker 00:03:23 Aye.
Austin Parker 00:03:25 nodie.
Bogdan Drutu 00:03:30 So, I think we are ready to start.
Robert, you are first.
Pellared 00:03:38 Okay, I can share my screen. By the way, Bogdan, good to see you. I also… I'm waiting for feedback in one of the issues, but I will add it to our agenda later.
Yeah, this is the issue, by the way, but maybe I'll just add it later.
Bogdan Drutu 00:03:55 Let's… let's go in order, and then we'll talk about that.
Pellared 00:03:58 Exactly, exactly. So, first of all, I created APR regarding stabilization of logarith chord processor enabled.
First of all, I… I'm not in a rush, it does not have to be, like, even though they are already for approvals, because it's a stabilization, we can wait more, that's one thing. Also, I wanted to have approvals for all the languages that already implemented the feature, to make sure that I find of the way it's currently specified. So, basically…
Bogdan Drutu 00:04:30 have a tracking of which languages you are waiting or seeking approval, because otherwise it's gonna be hard for us to track.
Pellared 00:04:37 I think I… I edited somewhere, I'm just… Double checking, EHP? Yeah, so… Awaiting approval for PHP maintainer. If you want, I can put it to the description.
Bogdan Drutu 00:04:54 Yeah, move it to the description, which languages you are waiting for approval, which one you already got, and when all the boxes are checked, somebody can merge it.
Pellared 00:05:05 Okay.
Bogdan Drutu 00:05:06 Bingo.
Pellared 00:05:09 To be defined.
I'll put it later.
There were also some questions regarding this feature, even… so, if someone do not want to dig… make an archaeological dig, I also put some information here, as good as possible. What are the use cases where this feature is kind of helpful?
Any questions, or can we switch quicker to the next topic?
Bogdan Drutu 00:05:43 I don't think it's any question here.
Maybe if we have anyone from PHP, just a call for you to go and review this.
Pellared 00:05:53 Yes.
Alright.
Trask Stalnaker 00:05:56 I still have… concerns, but I have said my piece on the PR.
Pellared 00:06:02 Okay.
Regarding declarative config, I'm not sure…
Bogdan Drutu 00:06:07 So, Trask, is your concern blocking, or is it more like…
Trask Stalnaker 00:06:17 I won't block it.
But I think that… We should be thinking of features from a declarative configuration perspective first.
And this one is not thought through declarative Config yet.
I think that it can be. I don't think… I mean, I think that it… I just think the ordering is wrong, on the way we're proceeding here.
I don't object to this feature, per se, I just, think that we should… Define it from a declarative config perspective first.
And the… the problem is that This feature is not really useful without chaining. Like, you basically have to use log processor chaining for this feature to make sense.
And unfortunately, we haven't defined log chain processing, log processor chaining. We have a non-normative example of how you could ad hoc implement that.
But since we don't have that as a first-class concept, it's not… there's no first-class representation of that in declarative config.
And so, it creates a potentially awkward user experience and divergent behavior, how different people implement it and represent it in declarative config.
Bogdan Drutu 00:07:47 So, so you think, you think… You don't have a problem to stabilize this, but what your feedback is, we should first Define the configuration for this feature, and then stabilize this once we stabilize the… or do it in the same time, mostly.
Trask Stalnaker 00:08:06 Exactly.
Bogdan Drutu 00:08:08 I see. I think it's a fair feedback. Robert, do you think you are okay with that, or do you think we should decouple the two?
Pellared 00:08:15 I think that there's nothing that needs to be done in declarative config right now.
So, basically, the way it will be structured is the same way how it can be composed for the samplers. And I saw there are already issues regarding sampling composition.
And basically, the same patterns can be applied to any kind of processors.
The difference…
Trask Stalnaker 00:08:37 policy.
Pellared 00:08:39 Sorry, go ahead.
So I just wanted to say that, basically, there's a precedence in the samplers, and there's nothing… you know, the fact that there's… we added just a function.
To the component does not say that we will compose it any differently.
Bogdan Drutu 00:08:57 But how do users configure this? Because people will come and say, I want with this feature.
to enable or disable logs coming from a specific scope, for example. Or others may say, I want to do it by level. Others may say, I want to do it by randomly sampled. Others may say.
thousands of options, okay? So, there will be more and more features, and every language will go independently and do something that will diverge from the community.
I think that's what Trust kind of tries to… to tell you.
Trask Stalnaker 00:09:38 And the difference to me between this and the samplers is that, samplers are pre-existing.
Right? Like, now we didn't have declarative config at that time. Now we have declarative config, and I'm trying to push… Any new feature, any new spec feature that we add.
I think we should be thinking of it from a declarative configuration perspective.
Pellared 00:10:05 Okay.
Can I just ask a question? Because I think I understand right now, and if this is my understanding correctly, then I prefer the coupling, so you want just to propose having some concrete, filtering processors, like severity base, trace base, etc?
So that they can be used and have, you know, like, a standard way how to do it in declarative config.
So, a standard structure for filter processor, for, you know, severity filter processor, for trace-based filtering processor, and, I don't know, routing… routing… routing processor, or whatever else could be there.
Is this what you were asking for? Possibly.
Trask Stalnaker 00:10:48 I think what I was imagining, but I was trying not to be, concrete, like, too specific, was… I was imagining that what I would… I think what I would like to see is us stay in the spec. Here.
Is a chain… you can have log processors that are chained.
Right? We define chained log processors as a spec concept.
And we define in declarative config, this is how you… Put them into the YOW.
Bogdan Drutu 00:11:21 Yeah, yeah.
Pellared 00:11:23 So, for me, it's the follow-up.
Because, in my opinion, you cannot do… you could do it, even now.
Bogdan Drutu 00:11:30 You, you can do, you can have change right now.
Pellared 00:11:35 So right now, it's, right now, this concept is the, in the, in this… supplementary guidelines.
And I think the only way to put it further to the spec is just to add some concrete examples you know, log severity-based processor, for instance. Do you want to… but…
Bogdan Drutu 00:11:57 I think he's a…
Pellared 00:11:58 A separate concept still.
Bogdan Drutu 00:12:00 I don't… I think it's orthogonal.
But how do people configure this? So, right now.
In Go. You implemented this in Go, correct, Robert?
Pellared 00:12:10 Correct.
Bogdan Drutu 00:12:11 Okay, how do I configure this right now in Go?
Pellared 00:12:14 You're decorating. Basically, it's a decorator.
But it's not only for this. It can be even without this enabled method. If you want to make filtering, you still just, you know, the correct processors, even without the enabled method.
Bogdan Drutu 00:12:27 I understand, but how do I configure? Did you… did you implement something like, I don't know, scoped, filter scoped, or something like that. Did you implement any of those?
Right now, the function is there, I can decorate, but how do I, as a user of this library, how do I configure today Anything related to this.
Tyler Yahn 00:12:57 So, like, I'm a little confused on this one, because… So, so the way this is… this isn't actually defining configuration, right? This is defining a mechanism to turn things on and off.
Right? And then it's, on top of that, however you want to define configuration, you can use this to turn things on and off.
It's not necessarily, like, this is the configuration.
So, like, to Bogdan, to your point, like, the severity-based, like, tracing, if you wanted to, like, restrict the amount of, log records that are coming through, right? You can use, a processor Which is defined to use… uses this method of enabled to say whether it is turned on or whether it's turned off. And if you wanted to, say, like, take the configuration from, like, the OpenTelemetry configuration, right, and you wanted to implement the logger configuration saying, like, a logger is turned off based on scope, a logger is turned off based on some sort of tracing ID, What you do in the construct and parsing of that log… logger… er, sorry, in the processing of that configuration is you just build the processors that you want to wrap whatever the pipeline is.
So it's more… it's a mechanism than rather than it is, like… a… like, this has feature sets. Like, this is more like… this is the knob that you can turn.
Bogdan Drutu 00:14:13 I understand that, Tyler, perfectly understood that, but that is a useless feature unless we propose some implementations or some ways to use this, correct? Like, right now, you are telling me this is a model, this is the… model that we are defining, but I cannot use it unless I'm writing my own mechanism of filtering, correct? Unless the… so, is the SDK give me some Sort of implementation of this, or it's just the interface?
Tyler Yahn 00:14:42 So the SDK is just an interface. The contrib repository does, in Go, has implementations of this that uses, you know, useful, processors. But, like, say, like, in the Go-specific space, if we're gonna run the configuration file.
the configuration file is done through, some sort of, like, processing pipeline. That processing pipeline takes the configuration, and if it wanted to implement, say, like, a disabled function on, like, some sort of logger ID, it can just write its own processor and wrap whatever it builds there.
Trask Stalnaker 00:15:17 Right. How do you, integrate that into… how do you configure that via declarative config?
Tyler Yahn 00:15:25 So, you mean, like, the lager, Disabling of a particular logger with a scope trask?
Trask Stalnaker 00:15:32 Sure, like, if you wanted to change the scope name or the level that was configured in this log record processor.
Tyler Yahn 00:15:43 So… Oh, oh, oh, okay, so you're saying. I mean, you could use the standard, configuration, so the logger configuration from the YAML, that you would set there.
I don't know if we do a severity-based, on that one, but, like, definitely for, like, you can set whether you want to disable or enable a particular scope. You can parse that from the configuration file, and then just build the processing chain as you need it to.
Trask Stalnaker 00:16:13 Right. But how do you represent chaining, in the YAML configuration?
Tyler Yahn 00:16:21 So you could… we could update that to make it… there's chaining in the configuration, but that's not necessarily needed to be represented, right? Like, if the user is… is not necessarily asking you to chain, but you need to use chaining to enable the feature set that they're asking for, then, like, the library itself can do the chaining for them.
Trask Stalnaker 00:16:47 guess that's the part… I guess I'm not quite following that. Maybe in, to not.
Tyler Yahn 00:16:54 So, so, like, if you wanted to, like, a concrete example, like, you can specify, like, a batch processor in the configuration, right?
And in that configuration, there's also another section for the logger configuration to disable something with the scope of, you know.
OpenTelemetry.io, right? What you do is you see, like, oh, I have an ability to do… to, like, disable some scope here. I know I need to, like, wrap this batch log processor with this other thing.
And that other thing is the thing that's going to filter before it gets to the log processor.
Pellared 00:17:27 my screen? Or not really? Is this what you are describing?
Something like that, right?
Tyler Yahn 00:17:39 But, to your point, Trask, like, there is, like, like you're saying, like, I think, to Robert's point, like, I think this is usable today.
With, like, as a mechanism for turning things on and off.
But, to your point, I think that you could make the logger configuration, or the file-based configuration more expressive by having these additional, processing chains, included there.
things like this severity-based processor, things like the scope-based processor, something like that, so then it could be explicitly done in the processing chain. I think that that's a great addition. I do think, though, that, like, it can be used today, is what I was just trying to say.
Tigran Najaryan 00:18:20 I'm a bit confused here, guys.
You're discussing… sort of orthogonal concerns here, or they should be orthogonal in my mind, right? The composition of the processors And how you configure them.
is its own concern. If it's not its own concern, then we're doing something fundamentally wrong here.
The fact that the processor uses or behaves from the perspective of how it reacts to the enabled method.
One way or another has to be decoupled from the fact that it is composed by… with another processor.
Or how the composable processes are configured, right?
If that's not how we do it, then we're doing something wrong here.
Trask Stalnaker 00:19:06 The reason why I'm tying those two things together, why I see them very tied, is that the feature doesn't really make sense if you have, multiple parallel kind of processors. It really… this is enabled, really only works… makes sense with chaining. So it's sort of by… you have to use chaining for this feature to make sense.
Tigran Najaryan 00:19:33 Sure, yes, if you use… if you… if we provide… a number of built-in processors that use the enabled plug, and we tell the end user, use those, and they are composable, and here's how you configure them. Yes, I agree with you, trust. But today, that's not the case, and how you use it today is you write your own custom code, right?
You write your own processor, and it's doable today, and it doesn't require configuration, and it doesn't require composition, even.
Bogdan Drutu 00:20:05 So.
Trask Stalnaker 00:20:06 Yeah, but shouldn't we be thinking of… I mean, I guess that's my fundamental thing that I was… I would like to see us think of any new feature in the spec as declarative config first, from the usability perspective of declarative config.
Tigran Najaryan 00:20:25 I don't disagree with that. I'm saying… If the declarative config requires every single feature.
to be thoughtful before that feature can be enabled, then it's not implemented correctly in my event. It has to be orthogonal concern.
If it's not, then something is designed incorrectly here.
Bogdan Drutu 00:20:47 I disagree with you, because we, for the moment, have not… don't have a good story of how the user will use this.
not the user that wants to write code, but the user… like, the final user that shouldn't write code to use this. We don't… we haven't defined that story, and I think… That we have should have that, because otherwise, if you don't go until… to the point of how the user will use it, you may define something that is not usable by the user.
Does it make sense?
Tigran Najaryan 00:21:22 I think the story… yes, but I think the story today is that the only way for the user to use this is to write their own custom processor. You write code. That's the only way.
I agree with you, it's much nicer to have building blocks.
Pre-built processors which give you an interesting way to deal with the enabled plug or other plugs.
That should come in the future, and I agree with you that that's something we should do. All I'm saying is, if we're forced to do that today, then something is wrong with how we're thinking about declarative config.
Bogdan Drutu 00:21:59 So, so… I think… We need to… to start at least POC to make sure that the user knows… no, no, we need to POC to make sure that we have a nice way to give it to the user. Maybe it's not… this is not the final, this is not stable, but… Yes.
Tigran Najaryan 00:22:20 Some examples you're saying.
Bogdan Drutu 00:22:22 What?
Tigran Najaryan 00:22:23 Show some examples. Implement…
Bogdan Drutu 00:22:24 Here's some example.
Tigran Najaryan 00:22:25 Two implementations of a processor that behaves somehow differently for the enabled flag, and show that they are composable, show they are configurable. We don't have to standardize on the config, we don't have to have a stable definition of.
Bogdan Drutu 00:22:41 Correct.
Tigran Najaryan 00:22:41 But show that it's possible, at least.
Bogdan Drutu 00:22:44 Correct.
Tigran Najaryan 00:22:45 I agree with you.
Bogdan Drutu 00:22:45 It's a…
Tigran Najaryan 00:22:46 Yes.
Bogdan Drutu 00:22:46 we have to exercise the API to make sure that it's good for what we try to achieve in the future, and one of the things is this, Tigran, correct? Like, that's what I want to.
Tigran Najaryan 00:22:57 That I agree with. I'm saying yes, but I'm saying we don't need to make it stable and final before we allow this feature.
Bogdan Drutu 00:23:04 I'm okay with that, but as long as I know there is a path in the future, that we can have this.
Tigran Najaryan 00:23:12 Agreed.
Trusk, I think, and then Ludmila.
Trask Stalnaker 00:23:17 Yeah, I'm happy with a path forward. I think my one concern with Not, like, only example… only doing examples, is that, once this feature is out.
everyone's going to start implementing it ad hoc. Like, they're going to implement chaining ad hoc, and they're gonna, you know, use a different way of representing chaining in the YAML.
And so, unless we… You know, at least put out a… draft?
Of, the config… how can… how chaining should be represented in declarative config.
everyone's going to implement it their own way. Like, as Robert was showing in his… if you still have your notepad up, Robert.
Everyone see that this is… how chaining, so in this example, Roberts chained the batch processor underneath the filter severity processor.
by having a field called processor in that. Like, literally, that's all that I feel like we have to define.
to say, this is the standard way to do chaining, because right now, that is ad hoc, right? This word.
Pellared 00:24:37 Like…
Trask Stalnaker 00:24:38 Processor underneath there.
Pellared 00:24:39 this is also how samplers are proposed to be done, in my opinion. But I think it's just… I think it's… I think it's something that can be defined on the configuration level. I think at least, you know, having an issue there, maybe having some premature agreement.
Just before that is feasible, right?
But I can, yeah, I can at least describe it, what are the possibilities.
That we are not doing something which will be not then backwards compatible in the future.
Liudmila Molkova 00:25:12 So, I think you can have Both. You can have multiple top-level processors, and you could have chaining under.
And… It's some future that… or something that somebody can build today.
So, I think what we… what I'm worried about is that, enable this chaining and the programmatic way of implementing it.
it would result in a lot of surprises. So today, when you programmatically add processors, you don't chain them.
like, from the code perspective, you're right, they are not chained, even though maybe SDK changed them.
I'm not sure about Golang, but I think it's not the case in many languages, not in Java.
Trask Stalnaker 00:26:01 No, nobody changed them.
It's by spec, but they're not chained.
Liudmila Molkova 00:26:06 So the real problem here is not the line about the enabled, but that everybody uses, like, there are two flavors of implementations for chaining and not chaining.
And if we code things in the spec for chaining, it will be very surprising to anybody who writes Java code.
Pellared 00:26:29 So, first of all, this training concept is described here, this advanced processing. I don't think it's, you know, a scenario that most of the users need.
Another thing is that… I disagree.
Trask Stalnaker 00:26:40 Oh, now that we're introducing this feature.
This… this feature, to me, triggers this… this is no longer advanced processing, this is required processing if you want to use this new feature. And I agree, it's a very useful new feature.
Pellared 00:26:57 Okay?
The last thing I just, what I wanted to say…
Bogdan Drutu 00:27:07 Robert, let's take a break on this one. Let's move to the next topic, because we have multiple.
Pellared 00:27:14 Out of time.
Bogdan Drutu 00:27:15 And let's move this discussion to the logic, as Trask suggested. That's a great suggestion. But I think we need a bit more consensus here, because we… until we put the bit stable on this one.
Pellared 00:27:32 Okay…
Bogdan Drutu 00:27:33 For me, at least exercise the API to prove that we can do a lot of these things is the minimum required, even though we may not implement everything, but at least exercise the API to make sure we can do changing, we can do everything we want in the future with this.
Which I think we can, but let's make sure, double-check on that.
Pellared 00:27:55 Okay. Robert, you are next.
Bogdan Drutu 00:27:57 I guess.
Pellared 00:27:58 Yes, so next one is just, semantic conventions. So, this one is just refining… so we, we have this table event name.
But the semantic conventions about how using, what, what events are in development.
And the semantics for events are also, like, these are all… everything is in development. So, basically, I did my best to improve this… oh, this is what happens here.
I try to do as much as possible here to clean up these, these recommendations, and also capture some, some stuff which I think is non… is not controversial.
in a PR, just to have a little baby step towards stabilizing it.
I do not… I remember that we are also discussing whether, we should put the somatic conventions if body should be used. I remember that the recent discussion was that body should be discouraged.
But because I'm not 100% sure on this one, I propose to have it as a separate PR and discuss it separately. So I put this, basically, here, this kind of information.
Liudmila Molkova 00:29:15 Robert, you removed the line that discourages the body, so why? Why don't you give it?
Pellared 00:29:24 I will remove such time.
Liudmila Molkova 00:29:26 Yeah.
Pellared 00:29:28 So you… okay, so I can put it back, right?
Liudmila Molkova 00:29:32 Yeah?
Pellared 00:29:33 Okay, so I'll do it.
Liudmila Molkova 00:29:35 And aside from this, it's just refactoring.
Pellared 00:29:37 And the thing is that… I do not, so, it was not clarified, because in one… in one place, it was saying that it is reco… Okay, I'm fine.
If you say so, then I will… I will add it then, if there's… if it's not controversial.
Bogdan Drutu 00:30:01 Let's save time, then. Move to the next one.
Robert, still you.
Pellared 00:30:06 Yeah, this is just a little one, I'm just asking for reviews, because it's a very minor thing, it's just about reordering sections, so they are more, easier to read, because when you're talking about attribute limits, these attribute limits describe the attribute limits on attribute collection, so it's just about reordering and changing the nesting. I just have only one approval, it's just editorial, so just asking for more.
Reviews and approvals on this one, unless someone disagrees.
And… that's all from now.
And I will stop sharing. Thank you.
Tigran Najaryan 00:30:47 Yeah, I think I'm next, and this is about the proposed change to OTLP to introduce reference-based attribute values.
I don't know if we have Josh, we don't have Josh, so right here… Do we have… we have Florian here.
That's good. Bye, Florian.
So, in a nutshell, this… this makes a change to, obviously, a stable part of OTLP, the Initially, it was in the resource.
Now the current state is it's in the any value.
Maybe I should share my screen to show what exactly it's about.
One second… Which one is it? This one?
No, this one.
Bogdan Drutu 00:31:31 I can share if you want.
Tigran Najaryan 00:31:33 I'm sharing.
So this is any value.
stable, used by all signals, besides a string reference, which is an index into a dictionary, which leaves, Somewhere here in the resource.
No, not in the resource.
Anyway, the dictionary part we can discuss. The thing is, I believe that Because this obviously impacts the existing signals, we need to be very careful with this change, and to me, it means that we need to make sure that interoperability of the old and new versions, so before and after an exchange, is guaranteed. So if you have a sender and a receiver who, use dictionary-based or don't use dictionary-based attribute values, they should be able to work together.
For example, you update your sender, which can be the SDK or the collector, but you don't update your backend.
Your backend doesn't know anything about the dictionaries.
that should still work. Work in the sense that Somehow, the sender needs to avoid doing… avoid using the dictionaries if the receiver Has no idea how to interpret them.
I think it's very important.
OTLP's stability, and I don't think those aspects are discussed in the PR, so I blocked it so that we can have that discussion, and in my mind, this really warrants an appropriate.
The other thing that I asked about was to have benchmarks that show how this helps, and in what situations, and by how much. I think that work is in progress, we will see that.
But, I think that's, that's only one part of the… what we want to see before we make this change. The other part being we make sure that we're not actually breaking The protocol, in the sense we're not preventing interoperability.
Bogdan Drutu 00:33:36 Oh, yes.
Tigran Najaryan 00:33:36 Or I think Bogdan was first, Bogdan, correct.
Bogdan Drutu 00:33:39 Tigran, do we have any forward compatibility requirements?
Tigran Najaryan 00:33:47 What do you mean?
Bogdan Drutu 00:33:48 That's what you are asking for. Like, this is backwards compatible, but it's not forward compatible. Do you… Do you…
Tigran Najaryan 00:33:57 Yes, yes, I think for OTLP, that's extremely important. You can't break that.
You… it's a huge pain in the… backside, if you have a deployment.
A variety of senders and receivers, and you change the protocol in a way that some participants In this, network.
change the version of OTLP and upgrade, and… and you… and then they don't… can't work with the rest, right? So you have to do a coordinated update.
Or you have to do it in a particular order. That's… that's a complication.
Bogdan Drutu 00:34:35 is not coordinate. You can do it as long as you do.
Tigran Najaryan 00:34:38 In a particular order, that's… yes, a type of coordinated update, yes. Correct. I think that's… in my mind, that's unacceptable. I don't think that's… yeah.
Bogdan Drutu 00:34:49 But then, then, let me tell you something. Any change to the protocol, then, we cannot make anymore.
Tigran Najaryan 00:34:55 No, that's not true. You can make it in a way that is possible to do, right?
There's a proposal about how you can do that.
Bogdan Drutu 00:35:02 We cannot add entities.
Florian Lehner 00:35:04 May I chime in?
Bogdan Drutu 00:35:06 No, no, no.
Florian Lehner 00:35:07 I don't, to be a… to chime in on this discussion, I don't see the risk of having an older version that is not supporting this protocol versus a new version reporting it. The reason is, profiling is behind a feature flag, and, if you don't use this feature flag, you don't have profiling support at all.
By introducing the string reference in any value, we're giving… not only profiling the benefit of using this as a dictionary later lookup.
But we are also establishing the base for the other signals in the later step.
With all, with all the programs.
Tigran Najaryan 00:35:50 There's nothing profiling, though, Florian, this is in common parts. I have no problem with profiling.
Florian Lehner 00:35:54 Yeah, but, if someone ignores and uses string reference for logs or traces, then, the implementation is broken, I would say.
Tigran Najaryan 00:36:06 Sorry, I don't buy the.
Florian Lehner 00:36:07 it's due.
Tigran Najaryan 00:36:08 add a change to the protocol, people are free to use it.
That's how it works.
Florian Lehner 00:36:12 The status is declared as development, and it's clearly marked as exclusively used by profiling.
How should we have… Work around this otherwise.
I mean, the same approach is used in different ways as well. Yeah. I made a specific proposal on how, but let's hear… let's hear from others first.
Tigran Najaryan 00:36:35 Clasp was there, but he's gone. Daniel?
Daniel Dyla (Dynatrace) 00:36:39 Yeah, I just wanted to point out that this is a little bit different than the entities example, because in entities, you miss out on… any new information that's added, so, like, you don't know which, you don't know which entity is associated with particular attributes, but you still get all the attributes. If somebody were to use this, then theoretically they would have not you wouldn't also include a string value, because it would have no… this has no benefit if you are not… if you're just gonna duplicate the data anyways. So, any existing receiver I have no idea what the string is.
Tigran Najaryan 00:37:19 Yeah, yeah. There's no way to include both, then. This is one-off.
Daniel Dyla (Dynatrace) 00:37:23 Yeah.
Tigran Najaryan 00:37:23 Both the ref and the string right.
Daniel Dyla (Dynatrace) 00:37:25 Oh, because it's one of. Yeah, so you can't have both. So this… this would… if an SDK switched to use a string reference, receivers that aren't updated would be broken.
Tigran Najaryan 00:37:35 There you see no data, break all of it.
Yes, entities break nothing in the existing data.
trust your back.
Trask Stalnaker 00:37:45 Yeah, I just wanted to say I agree that the, the issue is around whether it's profiling-specific or not, right? Like, I agree that if it somehow was just scoped to profiling, the change would be okay. But it is… very… I also think it's very… Like, it's in the common… Proto, even though we're adding a comment there, and it does feel like something that's come up a lot, and I do wish, Josh Sareth was here, because he's… I know there's been discussions in the past of doing dictionaries just across all signals.
Which could be nice, but then, you know, we really get into what Tigrin was saying about how do we… how do we do that backwards compatible? We need to, you know, we need some protocol with the server of, do they accept this.
data.
Tigran Najaryan 00:38:46 Bogdan, this is the answer to the question you had.
It's in the spec.
That's a requirement.
Bogdan Drutu 00:38:54 But… It is… it is capable of talking, it's just, like…
Tigran Najaryan 00:38:59 You just lose all the data, great, right? It's capable of talking.
Bogdan Drutu 00:39:04 Yeah, but, so… so, for example, why is that different if I… clients start sending a new… a new metric type?
Is it not… you're gonna lose that metric type, correct?
If you do send anything new that the server does not know, you lose that thing. It's… for me, it's a bit similar. If I send new type of resource, I'm gonna lose it. But again, let's not go too much into…
Daniel Dyla (Dynatrace) 00:39:35 And you wouldn't… you wouldn't miss out on existing… pre-existing metric types, where on this, you would miss out on pre-existing strings.
Bogdan Drutu 00:39:43 Pre-existing strings, if you send them exactly the same, I will not miss them.
I will miss.
Daniel Dyla (Dynatrace) 00:39:48 Yeah, but if you duplicate the data, there's no point.
Bogdan Drutu 00:39:53 But the same story may be made at one point. I'm not sending fixed bucket histogram, I'm sending exponential histogram. We added those later. I'm missing on them now.
Are we talking about?
Trask Stalnaker 00:40:06 about profiling signal only, or across everything? Because I keep getting confused there, because it… is there agreement that if this really was profiling scoped, it would be acceptable?
But given that.
Tigran Najaryan 00:40:20 Yes. To me, to me, it would be acceptable trust, but there's no way that you can limit that. If you introduce this feature, it's in the any value, it's in the common.
I think… I mean, what are you going to do, keep this forever in the state that says it's just for profiling?
If that's the case.
I accept that it's okay from the compatibility perspective. I think it's a very poor design, then, in that case.
I don't accept it as a design.
Liudmila Molkova 00:40:49 We just spent several… Yes, sir, go ahead.
Tigran Najaryan 00:40:52 In my mind, string references are useful for other signals as well, and we should be adding them in a way that works universally across the signals. So this warning, to me, at best, is temporary. We should remove it at some stage. And if we remove it, then people will start using it. Using it means I implemented in my OTLP exporter.
Right? I can detect duplicate values and use dictionary encoding for that. What happens with the destinations, then?
they break, right? You don't see the data.
Sorry, Ludlina, I cut you off. Please go ahead.
Liudmila Molkova 00:41:27 No, no, no, I cut you off, thank you. So, we just spent several months discussing that any value is signal agnostic, right? And the API, the Prada, you can have whatever comments, but then the API level, it's the same.
And then, is it available through API to profiling and other signals?
I mean, it can be backward compatible. You can double emit, and you can have a feature flag that disables duplication.
It can be done in non-breaking manner, but I think that we need to think about the API behavior, and this change should have a counterpart in the spec on how it should work.
Tigran Najaryan 00:42:12 What do you mean by double limit? I don't think that's possible.
This is one of value. You can't include both string value and string graph, it's impossible.
Liudmila Molkova 00:42:22 Oh, right. Yes, you're right. So then you can have an opt-in, just a feature flag that didn't.
Tigran Najaryan 00:42:27 Yeah, you use one or the other, but you can't have both, there's no way.
Bogdan Drutu 00:42:31 You can… you can remove it from the one-off, Tigran. It's not a problem, if you really want, you can put it outside the one-off.
Tigran Najaryan 00:42:40 Which is then a different design, we should consider that design, and I'm not sure I like that design. But this is what we have in the PR, right?
Florian Lehner 00:42:50 And what could be possible alternatives? Sorry.
Austin Parker 00:42:54 Yeah, sorry, so, generally, I'm actually in favor of the current design. I think having… I think the comment about string value must not be set if string references used is kind of… Duplicate.
But… I… also think that because anything can use any value, you know, there's plenty of… there's use cases for this in non-profiling signals, right? Like.
Tigran Najaryan 00:43:25 It's everywhere, yes. Yeah, like, there's…
Austin Parker 00:43:28 Any of us can sit here and rattle off 10 things that you could use this for.
So, I really like this as an evolution of OTLP. In terms of compatibility, you know, ultimately, that's a decision at the… In terms of compatibility with consumers, There's obviously, you know, there's no problem with… wire formats, there's a… Perhaps an expectation thing.
But I think that that expectation would be set at the, you know.
SDK level, or the instrumentation level, and is something that needs to be managed with config and sort of better communication around, you know, releases and da-da-da-da-da-da. Like.
Which is… Sort of the point of… the… full effort that I'm… I wrote up around changing how we think about stability, right? Like… Yes in an uncoordinated, you know… Yes, we can't stop people… we can't stop people from using stuff that we put into OTLP. But what we can do is we can make it easier for consumers and implementers to sort of interpret what's happening when we make these changes. And so, I… I think we have to be able to make changes like this with the understanding that we're gonna do something on the other side to make it easy for people to consume those changes, and we shouldn't let the fear of things changing hold us back from, like, evolving OTLP or the spectrum.
Tigran Najaryan 00:45:12 Just to be clear, Austin, I'm not saying we shouldn't make the change. I see a way to make this change in a way that preserves the… what I'm looking for, the interoperability. It's doable, I think. It's just that this change doesn't do that. It's… I don't think… I think… I'm in favor of adding the feature. As a concept, I like it.
I think we should do it in a way that maintains the guarantees that we provided, right, in the spec, which says that interoperability is important, we should preserve it.
One possible way is through using capabilities, and the senders can just downgrade to not using the dictionary if the recipient can't accept it.
There's other ways. I mean, it's doable. I see ways.
Austin Parker 00:45:55 Yeah.
Tigran Najaryan 00:45:55 We need to make a bit more effort on this one.
Bogdan Drutu 00:45:58 Let's… okay, so what is the next step, Tigran? Do you suggest we should have an OTEP, and .
Tigran Najaryan 00:46:06 I think we should have an O-type that, yes, works in that direction. I'm happy to work together on that O-Type, I'm happy to help with that, and Again, like I said, I'm in favor of the feature. I would like to also see the benchmark results that show that it's actually useful, and it's not just something that we feel like it's useful. And we can work together with a profiling SIG on this one.
Bogdan Drutu 00:46:31 That would be great. Also, I think we should use it for… not just for resource attributes, but for all the attributes, because right now it's only working for resource attributes, but can be extended to support metrics attributes or other things, okay? Okay, so… how do we unblock profiles? Because also, profiling has kind of a blocking thing, and how do we make progress on the long term? Do you think, Tigran, there is a compromise here where we unblock profiling somehow, but still move Move towards the end goal, where is to support this everywhere.
Tigran Najaryan 00:47:11 in… in what sense is this blocking the profiling? This is a… this is a performance optimization, right?
It's not a functionality that blocks, prevents from anything in the profiling.
Or is it… so important performance-wise, that you can't live without it. It's essentially a blocker.
Bogdan Drutu 00:47:31 I don't know about profiles, every time when I ask about this, it's so critical every time, so…
Florian Lehner 00:47:37 For us, it's a blocker in the sense that, if we cannot get in these changes to the proto, we cannot get the changes into the collector and other sub-components and make use of it, and learn from it. And, I think the important part here, especially, is that, we as profiling can have the advantage that we are in development stage, and can be the learning playground for OTEL, and before it can be later, applied on other SGMAs.
I see the point that the benchmarks are important, and we will deliver them, probably next week. But… Yeah, we need some… Action or feedback, I would say.
Tigran Najaryan 00:48:24 Actionable feedback, I think I provided in the… in the comment there.
And again, we can work on it together, I'm not solely asking you to do all the legwork here for other signals.
In terms… I don't think we have a great way of making these changes in an experimental way, Bogdan, if that's what you're asking, to unblock the profiling signal, unfortunately.
I don't know what's the great, what's a good way to do that, to make it possible.
Bogdan Drutu 00:48:53 We… I mean, to unblock profiles, we can play a game here, duplicate this message in profiles, and we play some aliases and everything, if we really want to unblock profiles, but, how long… okay, let's… let's… let's then… So what is the next item? What is the next action item, Tigran, here? We need to provide the community clear understanding of what we'll do next. Are you… Florian, are you okay with working with Tigran to do this across all the signals, or you think you don't have that time or interest?
Florian Lehner 00:49:30 I would be happy to bring this forward.
Profile is… Want to get stable at some point, and This is now a block of ours.
Bogdan Drutu 00:49:42 Okay, Tigran, is that reasonable for you, the guys, to chat and start working on the OTEP, then?
Tigran Najaryan 00:49:53 Yes, if there is someone from the Profiling Seek who can help me on this one.
Bogdan Drutu 00:49:58 Florian just offered his help. Do you need anything else? Anyone else?
Tigran Najaryan 00:50:03 No, that's fine.
Bogdan Drutu 00:50:04 Okay.
Tigran Najaryan 00:50:05 We'll work together.
Florian Lehner 00:50:08 Cool, thank you.
Tigran Najaryan 00:50:12 Bye.
Bogdan Drutu 00:50:16 Could mean a lot.
Liudmila Molkova 00:50:19 Yes, give me a sec. Do you want me to present?
Bogdan Drutu 00:50:26 I can present, it's just, like, it's your topic.
Liudmila Molkova 00:50:31 Yeah, so it's a short one, and we had some good discussions offline on the PR. So, I am, based on the… Josh's question a few weeks ago, I'm proposing to deprecate Zipkin Exporters.
The usage is lower than the Jager exporter that we deprecated a while ago, and the proposal here is essentially to remove it from the spec.
But to, keep whatever exporters we have.
But new SDKs, like, would not need to implement them. For example, we have a donation of Kotlin SDK. Is it beneficial if they have to include Zipkin exporter? Maybe not.
So, in this PR, I'm deprecating the document, because it's out of date already, and nobody actually follows all of it.
And… I am, making Zipkin Exporter optional. The key question I have… I haven't heard anybody who is in favor of keeping Zipkin so far. The key question I have, do we want to actually remove the document, say it will be removed in one year, or do we feel, that Until we have a stable path, like Zipkin native OTLP support.
we would rather keep the document around. I think Josh raised the point that he would rather keep the Document around, but he's not here.
Bogdan Drutu 00:52:14 So, I think, personally, I think… We should probably keep the documents, but move them into an archived, deprecated directory somewhere.
more hidden from the main documentation, so that only if you are really looking into this, you are gonna find them. But otherwise, in the main documentation, it shouldn't be there, in my opinion. I feel like it is beneficial, the text is already written, everything is written, so let's keep it around for, you know, in a separate pa… in a separate directory somewhere, so that We have it for posterity and show people that we will… Good.
The people and had the support initially.
Liudmila Molkova 00:53:01 Sounds good. Then, if anybody, have any important feedback, anyone wants to keep Zipkein around. Let's keep this PR open for… for a little bit.
And make sure we have time to address it, but then, I'll remove the Do Not Merge, and maybe after the KubeCon, we'll come back to it.
Thank you.
Bogdan Drutu 00:53:33 Okay, next is Austin, sorry.
Austin Parker 00:53:39 Yep, this is just a real quick one for, maintainers, especially.
It may… I would like to get the, blog post announcing… Proposed stability changes and tips up this week.
Feel free to… Look at it.
Try to go through and make it more clear what is, sort of, negotiable versus non-negotiable.
And more clearly, Spell out where this will impact maintainers, and… End users, Obviously, nothing's done till it's done, but… The start, something, not the end.
Pass.
Trask Stalnaker 00:54:35 On the… I saw that there was a discussion about the stable RC Beta, the sort of SEMCOM… introducing SEMCOM beta.
I don't know, I just wanted to check in with some con folks, Lydnila, just… Josh isn't here, if that was… something that the SEMCON was agreed to from the SEMCON side, or if it would be better just to leave it more generic and work out that detail in the OTEP.
Liudmila Molkova 00:55:11 I think it's best to figure out the details in ATA, but my understanding, that we agreed that We care less about some kind of stability, does not matter.
as long as the instrumentation library guarantees stability through somewhere. So, stable instrumentation can follow any Semantic convention, there's any status.
Austin Parker 00:55:39 The daunting.
Liudmila Molkova 00:55:39 Want to tie them to each other.
Austin Parker 00:55:42 I think the… I think we do want to say that there is… I think the thing we wanna do, or the thing that the… The desired result here is… normalization, right? Like… We want to make it.
Liudmila Molkova 00:56:04 Thank you.
Austin Parker 00:56:05 possible for, kind of, three things to happen. One is we want SimConv to be able to… or I think two things. One is we would like for… the project, for SimConv itself to not be a blocker on SimConv more generally.
And part of that is… Being able to say, hey, sim comp stability levels should be a little more nuanced.
So that both for… maybe for the project, but certainly for other… for third parties that are doing their own SEMCOM, giving them the ability to kind of have that, to encode that nuance, right?
Third party…
Trask Stalnaker 00:56:55 Do that already, though.
Austin Parker 00:56:56 Well, but not really, because you have experimental RC and stable, right?
Liudmila Molkova 00:57:06 And we support all of them?
We support all maturity levels, so third parties can.
Austin Parker 00:57:12 But we only… SimConf right now only supports 3 levels, right?
Trask Stalnaker 00:57:16 I'm conv Repo, but that's where I wanted to, like, differentiate here, like… If we're, like, end up…
Austin Parker 00:57:24 This is the way people experience it.
like, right now, we only use Experimental RC and stable, right?
Liudmila Molkova 00:57:32 We only use them, but we… we can definitely use them more. It's just, it's not codified what it actually means.
Austin Parker 00:57:40 Right.
Liudmila Molkova 00:57:41 Instrumentation's key, really.
Austin Parker 00:57:44 And part of this is saying specifically, okay, across everything, here's what these levels mean.
And here's what you, end users, should expect at these levels.
And… Normalizing all of that stuff across the entire project.
Because right now, it's not… that's not necessarily the way it is. The second thing is, yes, like, we should unlink telemetry stability from instrumentation stability, and say, you can have a stable instrumentation library that's performant and tested and da-da-da-da-da.
And it might depend on unstable Semcov, but that shouldn't make the instrumentation unstable. That just makes the telemetry unstable, and we want to be able to… like… Say that, and… Going back to what I was just saying.
Let… Give… set the appropriate expectations with people about what that all means.
Liudmila Molkova 00:58:54 Yeah.
Austin Parker 00:58:57 Yeah, there's definitely details that can be worked out in the OTEPs here, but I… and that's why I kind of, again, I redid this with a focus more on, like, what are the goals that we're trying to achieve here?
And a little less about, like, the specifics?
Liudmila Molkova 00:59:13 Yeah, but I think… The moment we start to work out specifics of more nuanced levels, we would… get into… Hard problems, very hard problems to solve. One of them is… Okay, the moment we publish semantic conventions, the moment we release them, they are effectively better.
We released GenA conventions, and people immediately pushed back against breaking changes there, like, immediately.
So, you can… we can think about all of them as beta.
The second hard problem, if there are nuanced levels, how do you express it with the schema, URL, and on the telemetry? And how many versions of semantic conventions artifacts would languages ship? Like, 5?
Probably not, it's too complicated. So I think we need to think about some… something… More simple, that can… We could find answers through WhatsApp, too.
Austin Parker 01:00:21 Yeah, I think the… again, the goal here is to… The goal here is fundamentally… 1… We would not… we would like for… OTEL, the project, to have, and especially maintainers, to have a much clearer idea about, like, what is the scope of support for things that we are actually going to include in upstream instrument… in upstream distributions.
In order to… promote the idea that people outside of hotel should also be doing this, right?
We don't want… some comms… some comms SIG to be the be-all and end-all, and the… You know, the choke point for semantic conventions in general.
Trask Stalnaker 01:01:13 And that's what I'm worried you're cause… that's what I'm worried about introducing alpha-beta stability to SEMCONS, is that you're… is that that's introducing a choke point there, that everybody's gonna then… say, oh, I have to get my SEMConf to beta before I can do my instrumentation, and we want to unlink those two things and say, instrumentation can be stable, you don't need the choke point of SEMCOM repo.
Austin Parker 01:01:42 So the alternative there is just to remove the idea of stability levels entirely, and just say that, for some convin, say.
SemConv is just versioned.
and there's… you know, and we remove the idea of stable SimConv, and we just say, hey, we… whenever… whatever a published version of SimConv is, that's what it is, and you know what it is, because that's… this is the date on it, and we can communicate, like.
Do we expect this to change? But what we actually are gonna be working on is how do you safely transform between versions?
That, to me, is…
Trask Stalnaker 01:02:19 why that… why that? I don't…
Austin Parker 01:02:23 How do you stop?
Trask Stalnaker 01:02:23 conclusion.
Austin Parker 01:02:24 Because the second that you say, like, oh, this has a stability level, then consumers are going to… go back to, well, I don't want to use it till it's stable.
I also don't… I mean, I want people to read it, and if you have a huge problem with something that's in there right now.
like, let me know as soon as possible, because I really would like to publish this so we can start actually, like, making progress on it, and not… Try to debate it, the details of it, in this call.
I also.
Liudmila Molkova 01:02:54 So that…
Austin Parker 01:02:55 Have a different meeting.
Liudmila Molkova 01:02:56 Yeah, okay.
Austin Parker 01:02:58 Sorry, but if you have a specific comment on this specific thing, please go make it on that post, and I will change.
Trask Stalnaker 01:03:04 No worries.
Austin Parker 01:03:05 Before we, before it gets published.
Trask Stalnaker 01:03:07 Okay, thanks.
Austin Parker 01:03:09 Thanks, bye all.
Trask Stalnaker 01:03:10 Like…
