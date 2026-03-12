SIG: Java Declarative Configuration
Date: 2025-08-14
Duration: 57 minutes
Zoom Recording URL: https://zoom.us/rec/share/BxC_Q4OQPKX5ZxdLgnJcBsKeZGaONH26LoHyOkKwlgiStLVk5hvvmfhuKNHnh3Oi.kzH44nc8BqhJtYQI
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 01:08 Hello!
Just wanted to write you, because I had an idea.
I created a pull request, only a couple of lines, and….
It should fix a problem that you're having.
**Robert Niedziela** 01:26 It would be great.
**GZ Gregor Zeitlinger** 01:29 Hello? I'll just send it to you on….
Slack.
**Robert Niedziela** 01:35 Okay.
**GZ Gregor Zeitlinger** 01:55 Let's see if some people are back from… application already.
Trask is back.
I saw… Hi, Jay.
**Jay DeLuca** 02:24 age.
**GZ Gregor Zeitlinger** 03:33 So I think the topic queue is still the old one.
Not sure why it… move down.
That's here.
Did we have a meeting last week?
**Robert Niedziela** 04:14 Yeah, we did. We were only two guys.
**GZ Gregor Zeitlinger** 04:18 Yeah, I remember. That's why we did not ride.
**Robert Niedziela** 04:21 Yeah, exactly.
**GZ Gregor Zeitlinger** 04:21 Anything.
Okay, yeah, 4 minutes in.
That's start, I guess.
… So if you have anything, then please also edit Otherwise, I'm just pulling down from the topic queue.
So the first one is something that, … Has come up based on the pull request review.
… And it's about authentication providers.
My initial implementation, set the… authentication provider for GCP to a static value.
But, … That is insufficient, because the API key rotates, and that is not supported.
So I created a new, issue in OpenTelemetry configuration.
And, … I have two possible solutions that I'd like to discuss.
So the first one is, that, We have a new syntax and a configuration file that pulls values from a secret.
In our case, the user would not write that syntax directly, but the first part is the… Running the customizer, and the customizer would add this, … … expression there. Not in the parse… not in this… with the curly braces, but it would, like, would be… Actually, I don't know if it would… if it would be with the curly braces or not.
And the other solution is a more dedicated authentication provider.
That already exists in the collector.
And because it… It looks very similar, I like that solution more.
What do you think?
**Jay DeLuca** 06:57 How does the first one work?
In terms of the dynamic aspect of it.
I'm gonna call the secret each time.
**GZ Gregor Zeitlinger** 07:11 Yeah, I'm not sure about that, so… I, I have another… This is a component provider… … yeah, that's the customizer provider that I was just thinking about.
Robert, but, … We can also take it as… As an example, so, in GCP, the… Customize a provider.
would add… authentication headers. Okay, I can just open up, the pull request.
Oh yeah, that's exactly how it is done right now, and the old style.
So the builder has a setter method, and that takes a predicate.
And that doesn't work, because… The new customizer provider works on YAML objects that That don't support callbacks, or anything that, … only things that can be serialized.
from, and to, YAML.
And… This is a new one.
So here, you get a list of name… String value pairs, and then you… N… Add one with a name, and the name is actually a string.
I know what the problem is. When the declarative configuration is parsed, environment variables are substituted When reading, … the YAML in the first phase, and in the second phase, callbacks are applied.
Salt.
If we would have, … A special syntax here.
That would not, be, … used at all, unless the schema, the way the configuration is parsed would be changed. The workflow would be changed, that's what I mean. I think this would not work.
**Robert Niedziela** 10:09 But anyway, wouldn't it be insufficiently dynamic, let's say, because the secret can expire during the application is running, right? And we have no, actually, way to replace it on the fly.
Where's this?
**GZ Gregor Zeitlinger** 10:24 Well, the idea would be that you would have another, object, that you get from somewhere, and then you would say, secret, see, correct.
Storage, and then you would basically, have the same… callback that you said here. But the secret storage could have the dynamic part.
would be, ….
**Robert Niedziela** 10:59 Okay.
**GZ Gregor Zeitlinger** 11:04 This, is more generic, but I could not think of any other use case.
Where this would be needed.
I like that.
Okay, … Just wanted to get your, feedback on that. Let's move on.
… I guess I'll, ask, in the, … configuration as sick.
**Trask Stalnaker** 12:15 Gregor.
Before we move on back on that, The dynamic, … Are you trying to find a way to model dynamic … config that dynamic update just via the YAML.
Cause I would… I was assuming that would be, like, a… It would need to be a component, a custom component.
kind of like a span… named span processor, a named sampler. It would be a named… auth provider.
that… would be referenced in the YAML, which would then be responsible for That.
Dynamicity.
**GZ Gregor Zeitlinger** 13:06 So you can, see how I imagine it would be in the second proposal. Here you have an exporter, OTLP HTTP, and then you add an authentication a snippet, like you can do, in the collector today. So I also used auth, as the same key.
**Trask Stalnaker** 13:30 Okay, and GCP there is a named authenticator.
**GZ Gregor Zeitlinger** 13:35 Exactly. This is the one that already exists today.
… It's just, … That, … you configure it differently right now. Right now, you have your system properties that are red.
And as soon as the GCP provider is in the ClassPass, it's used, and you don't associate it directly to an exporter.
the GCP provider looks for the exporter, so it works the other way around.
And I would say the new model is more, more explicit and easier to understand.
**Trask Stalnaker** 14:20 Yeah, and this works, or sorry, I didn't… I'm sorry for missing the beginning.
It's not working.
**GZ Gregor Zeitlinger** 14:28 Right now, it does not work, and I can show exactly here in this, snippet, … So… And the old, … provider, it works, because the builder, has a, setter that takes a supplier, and that is incompatible with the new format, because you can only set things that are primitive types, because if you modify the… YAML.
Just not on the file level, but you modify it in the parsed form.
**Trask Stalnaker** 15:06 Oh, and so the problem is that there's not, like, a set authenticator?
**GZ Gregor Zeitlinger** 15:12 There is not a set authenticator, because this concept does not exist, and it's also not possible to call set headers like it was before.
Okay. And those would be, solutions.
**Trask Stalnaker** 15:27 Okay, if it had an authenticator, like, if we had an authenticator class, interface, and… the GCP authenticator implemented that.
and was a named, you know, did our whole named component thing, then… and you had a set authenticator here, that would all work?
**GZ Gregor Zeitlinger** 15:47 Exactly, and this is basically the second suggestion. And because it is similar to the collector, I think it's a good way to go.
**Trask Stalnaker** 16:00 Yeah, yeah, that makes a lot of sense to me.
Thanks.
**GZ Gregor Zeitlinger** 16:04 Okay, cool.
**Trask Stalnaker** 16:24 component, yeah.
**GZ Gregor Zeitlinger** 16:27 Component, yeah. That's a better way.
Okay, … Yeah, before we pull up more, let's go to… Robert.
**Robert Niedziela** 16:37 Yeah, I want to show you something. Actually, I bring it once again.
I just wanted to show you, if this is not confusing, and we are okay with this approach. I will share the screen, if you don't mind, and show you what I actually mean.
It's, I guess, this one.
So, yeah, technically, we actually have possibility to, create, invalid, model using customized providers. We have no, actually, type of validators, and we can easily construct invalid, invalid model. So, that's just to illustrate the situation. We have very simple YAML, With a tracer provider that, has, one processor with exporter to the… simple exporter to the console, right?
But we also have Customizer. The customizer is created here.
I mean, sorry, it's here, where I just, at the first place of the processor, I set the batch, how it works. The model that we get from this, first element is the span processor… sorry, a span processor model, and it has two fields, one for batch, one for simple, and additional properties.
So, the note in YAML, the definition in YAML says that it can be either batch, or simple, or additional properties, because we have limit for one property only inside of it.
**GZ Gregor Zeitlinger** 18:33 But programmatically, we can do anything with it.
**Robert Niedziela** 18:36 So, I have a parsed model from this YAML, Right?
Gosh, sorry, from this YAML.
and I programmatically set another… one more option to it. And because the clarity… I mean, because the span processor factory first looks into the batch model.
We get batch, exporter instantiated instead of, simple processor.
So… And we have no, actually, warning, no information that such, thing happened.
we see a YAML where we have simple processor, but the output actually creates a batch processor, because underneath.
Some magic happens that is, modifying this model.
I know, this is some edge case, but maybe we could, at some point, think about the validations for these model classes, if they are still consistent with schema.
**GZ Gregor Zeitlinger** 19:45 Oh, you mean if you would write the same thing with simple and batch in the file, then you would get an exception, but you do not get an exception when you do it programmatically. Okay, got it.
**Robert Niedziela** 19:56 There is no information that there were another property set on this node as well, so… To me, it may be, in some scenarios, it may be extremely confusing to customers, to vendors, right?
That there is no, actually, information about this inconsistency of data.
**GZ Gregor Zeitlinger** 20:23 I mean, even, if it's, perfectly valid. The providers can change things, and it can be hard to understand.
….
**Robert Niedziela** 20:36 Yes, but, you know, the easiest solution would be, actually provide any validation even on the factory here, right? We can check if there's only one field set of these three.
And in case it's more than one thing set, we just throw exceptional.
**GZ Gregor Zeitlinger** 20:56 And what should you do if you want to change from a simple to a batch processor, maybe for a valid reason?
**Robert Niedziela** 21:05 Hmm.
If you want to change, you can set simple to null and batch to not null , right? But I created a situation where the data con… model contains both of them, simple and batch.
**GZ Gregor Zeitlinger** 21:24 Alright, so you could run a validation when all the providers are run.
**Robert Niedziela** 21:29 Yeah, because providers can do, you know, really… Nasty things with the data.
I mean, these customizers.
**Trask Stalnaker** 21:46 Robert, would it also work to… I'm not familiar with when the validation occurs. I'm guessing the YAML, original YAML is validated?
**Robert Niedziela** 22:00 I think it's done… I don't know where it's done, but the original YAML validation is done earlier, so we are not going into a customization phase when we have invalid YAML.
And the customization can make it incorrect.
**Trask Stalnaker** 22:19 Can we run that same validation after the customizers run?
**Robert Niedziela** 22:24 I don't know, maybe that's something we can explore.
**GZ Gregor Zeitlinger** 22:32 But it would also have a drawback, because then it would be harder to distinguish other Is the user file incorrect, or is the… programmatic configuration, creating something.
**Robert Niedziela** 22:47 It could be done twice, right? The first time when it's parsed, and the second time after it's customized.
**GZ Gregor Zeitlinger** 22:54 Yep, that's true.
**Robert Niedziela** 23:07 Yeah, there are some frameworks also for validating POJOS, but the issue is that it's generated code, right? These models are generated from YAML.
From Ski Mining.
**GZ Gregor Zeitlinger** 23:19 Yeah, and that's actually an advantage, because it makes it the same in other languages.
**Robert Niedziela** 23:26 Yeah, from general point of view, yes, it's an advantage, but in some cases, Other things it makes harder.
**GZ Gregor Zeitlinger** 23:34 Yep.
I would suggest just create a PR to, to, … the SDK repository for another run of validation. I think it should not be difficult to do that and then discuss there.
**Robert Niedziela** 23:54 Huh?
Nope.
Okay, so I'll try to… to do it.
**GZ Gregor Zeitlinger** 24:03 Yeah, cool.
**Robert Niedziela** 24:10 Sorry, stop sharing the screen. Thanks.
**GZ Gregor Zeitlinger** 24:15 Next, I actually want to discuss the current PR. Etrask, you've already reviewed it, and it seems like it's only… The question of what we do with this one common property.
… Maybe we can figure that out.
**Trask Stalnaker** 24:35 Sure.
**GZ Gregor Zeitlinger** 24:44 I think it's already in the pull request as a comment.
Quite a long pull request already.
**Trask Stalnaker** 25:09 hidden, my favorite feature of GitHub, the hidden comments.
**GZ Gregor Zeitlinger** 25:15 Oh, the open comment is in the hidden comment, okay.
**Trask Stalnaker** 25:18 Yeah, I hate that.
**GZ Gregor Zeitlinger** 25:27 Yep.
That's it.
So, the… situation is that, both the agent and Spring Starter respect the… A common enabled feature that we have right now.
And… Trasky said it might be confusing if we… If we keep it like that.
**Trask Stalnaker** 25:55 Yeah, just thinking of the declarative config is also… I'm supposed to work with… Library instrumentation.
Sort of bring your own SDK and library instrumentation.
So I worry that common… Putting that under common makes it feel like it would apply to all of those instrumentations as well. Native instrumentations, ….
**GZ Gregor Zeitlinger** 26:27 library instrumentations.
**Trask Stalnaker** 26:29 So, I like the idea of… putting it under, like, if we already have agent and spring starter nodes, is that….
**GZ Gregor Zeitlinger** 26:38 We have Agent, but we don't have Spring Starter so far.
**Trask Stalnaker** 26:42 Okay.
….
**GZ Gregor Zeitlinger** 26:45 But we also have common, so right now it's under common, and … we would, … Not have it together with the other common properties, … the other Java common properties anymore.
**Trask Stalnaker** 26:59 Yeah.
Yeah, so I feel like putting it under common is, … biasing too much towards the Java agent.
… So I like this other split out.
default… I'm still not sure what to call them, though, because, like, what does default enabled mean? Like, this is not descriptive, like, of, like… what it's… what it is, does that mean that… is that the same as Java Agent?
enabled? Don't we have a Java Agent enabled flag, also?
Yeah, but for technical reasons, you cannot do it, and ….
**GZ Gregor Zeitlinger** 27:47 configuration file, because we need it earlier than that. Oh, it's, … it's… No, it's not here, but it's OTel Java agent enabled.
**Trask Stalnaker** 27:59 Yeah.
**GZ Gregor Zeitlinger** 28:06 Yeah, it's here.
… So, more, like, default enabled as we had before.
**Trask Stalnaker** 28:15 No, like, instrument, right? It's… we're not saying… It's the default for instrumentations.
**GZ Gregor Zeitlinger** 28:26 Default instrumentation, or…?
**Trask Stalnaker** 28:28 No… I don't know, I don't have a good… Maybe agent… instrumentation… Do you understand my concern?
**GZ Gregor Zeitlinger** 28:47 Yeah.
**Trask Stalnaker** 28:48 Okay.
Maybe instrumentation, and then default enabled.
And it could be default, and they, like, it could be too stacked, or… Because at least this makes it, like, okay, this is applying to all the instrumentation within the agent.
**GZ Gregor Zeitlinger** 29:26 Well, this is creating a repetition, because the top note is already instrumentation.
**Trask Stalnaker** 29:31 Drat.
Honestly, I don't like this option anyways, of the default enabled.
Oh, I like… … It's… It's a pretty, use at your own risk.
… I would.
I wouldn't be so sad if we threw it away and it was only available via system properties or something.
**GZ Gregor Zeitlinger** 30:12 But that's a bit strict, just because we cannot think of a name.
**Trask Stalnaker** 30:16 Well, and also it's not… I mean, I don't… it's not really a recommended. We don't recommend users to use it.
We explicitly recommend that users don't use this setting.
Because it's too easy to shoot yourself in the foot.
Because people don't know what to eat.
**GZ Gregor Zeitlinger** 30:39 I actually used it to find out where an error is, so disabled everything, and then… enable….
**Trask Stalnaker** 30:48 Sure, for troubleshooting something, but… For production usage.
**Robert Niedziela** 30:56 Sorry, guys, I had to disconnect, because I have another meeting right now, so… see you, bye.
**Trask Stalnaker** 31:01 Cheer.
**GZ Gregor Zeitlinger** 31:02 Bye.
**Trask Stalnaker** 31:07 We can think of something. What… what would it be?
**GZ Gregor Zeitlinger** 31:21 So the best, I can think of is just to have the default enabled that we had before.
**Trask Stalnaker** 31:38 Oh, is Agent under instrumentation?
Is the agent node under instrumentation?
**GZ Gregor Zeitlinger** 31:44 Yeah, that's a… that's a requirement that we can change.
Because everything that is not SDK is instrumentation. That's the idea.
**Trask Stalnaker** 31:55 Okay.
Oh, instrumentation is top level, got it.
**GZ Gregor Zeitlinger** 32:01 Yeah, and Java is also….
**Trask Stalnaker** 32:03 Java. Yeah, yeah. Okay, Java agent… Can you add, in your example there, one of the… like, what does it look like if we say default enabled false for the agent, and then have another node below for, like.
I don't know, executor… instrumentation… enabling that.
**Robert Niedziela** 32:51 I'm back, the other meeting has been canceled.
**GZ Gregor Zeitlinger** 32:54 Oh, okay.
That's how it would look like.
**Trask Stalnaker** 33:00 Okay, so it's just enabled.
I'm… Does that… is that confusing, though? Like, let's take, something we have.
… library instrumentation for. Let's change executor to OKCDP.
Right, the… Doesn't this make it sound like the oak… it would… disable the OKHTTP library instrumentation.
Like, these nodes here should apply… equally to Java agent and library instrumentation.
**GZ Gregor Zeitlinger** 34:00 They should, yeah.
That's enabled by account.
**Trask Stalnaker** 34:06 But enable doesn't apply to library instrumentation, right?
**GZ Gregor Zeitlinger** 34:12 Yeah, this is a general observation, that depending on where you run.
you have a different set of properties. This is also true for agent versus Spring. Some… properties, don't work in Spring because it's working in a different way. I mean, we try to limit this as much as possible, but there are some edge cases where this is true.
**Trask Stalnaker** 34:39 What I'm wondering is, do we want to instead stick all those enabled flags, sort of the per instrumentation-enabled flags, under the agent?
node.
To be clear that these are agent settings.
**GZ Gregor Zeitlinger** 35:02 Oh, this, … would have an advantage, but it would also have the disadvantage that it would, not group together with other settings for OKHTTP.
Like, I don't know, time out… Something like that.
**Trask Stalnaker** 35:24 Although, if you're disabling it, I mean, the typical use case is gonna be To disable a couple specific ones, and in that case, you probably don't have any other Settings.
in your YAML.
**GZ Gregor Zeitlinger** 35:47 Yep, that's true.
Only if you use default-enabled faults, then… Right, and I said it were true, and… Also set other properties.
**Trask Stalnaker** 36:11 Can we see what it would look like if you put Okay, CTP under… Yes, ….
**GZ Gregor Zeitlinger** 36:20 So, are you thinking disabled or something?
**Trask Stalnaker** 36:31 That's true, I guess I… yeah….
**GZ Gregor Zeitlinger** 36:36 Is that what you….
**Trask Stalnaker** 36:38 That's an idea.
So, like, under… oh, I know, I can go to, the meeting doc.
Also… … I'm going to, … So… I know the instrumentation is redundant here.
… Neil what… … We could do something like… Enabled. Disabled.
**GZ Gregor Zeitlinger** 38:20 Yeah, that would also work, right.
Yeah, it's probably better than… Then, … Other suggestion.
I actually liked the one before.
**Trask Stalnaker** 38:43 Oh, okay, let's see… So… Instrumentations… Enabled… Like this.
**GZ Gregor Zeitlinger** 39:02 Yep, Yeah, I think that's… that makes it… Very clear.
**Trask Stalnaker** 39:21 So you can use one… Or the other….
**GZ Gregor Zeitlinger** 39:26 You can use both according to the… Usual semantics.
**Jay DeLuca** 39:37 Does this solve for the original property of, like, they enabled all of the defaults, enabled or disabled?
**GZ Gregor Zeitlinger** 39:47 Yeah, kind of, because, then, … Kask's original concern was that it's not clear What the scope is, and now… We can easily add here… Default… And it's clear that… what this applies to, we just have to figure out if this is the right… No.
**Trask Stalnaker** 40:13 Do we even… do we even need that, though? Like, if you want to… if you want to do default enabled false.
**GZ Gregor Zeitlinger** 40:23 Oh yeah, you just populate enable.
**Trask Stalnaker** 40:25 list.
**GZ Gregor Zeitlinger** 40:26 Right.
**Trask Stalnaker** 40:26 enabled.
**GZ Gregor Zeitlinger** 40:27 Yep.
**Trask Stalnaker** 40:27 So you, you can only use either enabled or disabled.
**Jay DeLuca** 40:34 So we just have to make sure that's well documented.
**Trask Stalnaker** 40:39 Yeah, ….
**Robert Niedziela** 40:40 Yeah, but it is intuitive as well. Yeah, I like this.
**GZ Gregor Zeitlinger** 40:43 Okay, Then let's do that.
**Jay DeLuca** 40:51 And we know all the ones that are disabled by default, so we could populate the… The configuration with that, potentially?
**GZ Gregor Zeitlinger** 41:04 Oh.
What… what are you trying to do, Jay?
**Jay DeLuca** 41:09 So, if we… there's, like, 15 or so modules that are disabled by default already.
**Trask Stalnaker** 41:16 I agree.
a good point.
**Jay DeLuca** 41:18 Like, we could pre-populate the configuration file with those, potentially, if that makes it… I guess I'm thinking, like, the user's gonna need a way to know that those are disabled, and then to be able to enable them if they want.
**GZ Gregor Zeitlinger** 41:35 I like that.
**Trask Stalnaker** 41:40 It just makes it the… config file, so… like, the… Large, and it doesn't allow us to, going forward, add a new Instrumentation that is disabled by default.
**GZ Gregor Zeitlinger** 41:55 No, I think the idea is that this would be the kitchen sink example. It's not that you have to put it in there. If you leave it empty, then you still get the same disabled modules that you get now.
**Trask Stalnaker** 42:08 Yeah, but how would you enable one of those? Say you're using just the vanilla, everything, and now you want to enable JDBC data source.
If you put it in the enabled one, for our… Prior thought here.
That would mean everything's disabled except that one now.
**GZ Gregor Zeitlinger** 42:32 So we would need to enable… Only… ugly name, but what we would have to do.
And the same, I guess, for disabled, if you just want to say, Just disable those… hmm.
**Robert Niedziela** 43:06 I think I'm not getting why we do it… why… why do we need this split for enabled only and enabled to… because my understanding was that if we specify anything in enabled.
It means we have everything else disabled.
….
**GZ Gregor Zeitlinger** 43:24 Right, but you could also say that you only want to disable one instrumentation that is disabled by default, but you don't want to change anything else.
**Jay DeLuca** 43:41 I think the fact that there are, like.
I think the fact that there are a handful of modules that are implicitly disabled makes it a little complicated to just have the binary option of… Enabled and disabled.
Unless we change that behavior.
**Trask Stalnaker** 44:01 Yeah, Robert, I just dropped a link, this is what we're talking about.
**Robert Niedziela** 44:08 Thank you.
I see.
**Jay DeLuca** 44:19 Yeah, there's more than that, too. If you go into the instrumentation list YAML file, all of the ones that are disabled by default are noted there, too.
**GZ Gregor Zeitlinger** 45:10 Yeah, if you have those three properties, then it works, because it would have the same semantic as it has now.
Or it could have the same semantic.
**Trask Stalnaker** 45:20 Right.
That seems okay to me.
I mean, this is not… again, this is not something that we're… That's too common… I would say the most common… … Most common would be… just disabling… 1… Or… disabled… … Noisy, noisy, be, something like that.
It's like… The other… although the other option is… Not making it a list, but, Noisy A… Enabled.
False.
I mean, this gives us the option to… if we do have… I'm just trying to think of, like, if we have more… agent-specific stuff, like, oh, this one should use the indie… … module, India approach, or I don't know, something else.
Possibly.
**GZ Gregor Zeitlinger** 47:26 Hmm… Yep, also, also fine for me.
**Trask Stalnaker** 47:33 This kind of map's probably most similar… to our existing… I guess the only downside of this is the… what you said earlier of… it seems a little duplicative of, like.
if you also have OKHTTP, at the… broader level.
**GZ Gregor Zeitlinger** 47:58 I don't think that's a big drawback, because this is not a very common property.
And it's true to the spirit that it's very clear, To where the properties apply, and so having it there.
I think it's a good argument.
**Trask Stalnaker** 48:23 Yeah, I think that's my… Favorite, we could, if you want to poll folks in the general meeting, see if we get any other Opinions, feedback.
I like it.
**GZ Gregor Zeitlinger** 48:42 Okay.
**Jay DeLuca** 48:43 Me too.
**GZ Gregor Zeitlinger** 48:51 Thanks!
I don't know if we have… Time for another one.
… Yeah, this is more, … Status update. Trask, you wanted to ask in the semantic conventions… What we do about… the known HTTP methods.
I'm wondering how we should proceed there.
Did you get around….
**Trask Stalnaker** 49:24 to me.
Getting that into the configuration… the official config?
**GZ Gregor Zeitlinger** 49:34 Right.
**Trask Stalnaker** 49:38 I mean, I think… Everybody is supportive of this approach.
Somebody just needs to, … Try to make it happen.
Oh, yeah, I did have a one.
… proposal here.
**GZ Gregor Zeitlinger** 50:06 So the… my question is also, if this belongs to semantic conventions or not. So far, the options are in the configuration repository, but not in semantic conventions.
**Trask Stalnaker** 50:22 Yeah.
We're just… I think… Lydmila, Jack, and I are all aligned that we like the idea of semantic conventions, like.
Synchronizing between semantic convention option names and declarative config.
… just… It's a matter of implementing that, … So… Hi.
Let's see… I mean, I don't know if we're clear, and maybe if you want to add it to… might be easiest to add it to the semantic convention SIG meeting, if you're able to join.
That, as far as… like, do we want to add it to the YAML, to the semantic convention YAML?
Or do we just want to mention it in the text, what the… name is… So, Jack, I think Jack is holding up on adding it to declarative config.
Until… we officially, like, bless, document it from the semantic convention side.
Does that make sense?
**GZ Gregor Zeitlinger** 51:46 This is the part I'm struggling with, because, does it mean all of the values and configuration have to be transferred, or only the new ones?
Because we don't have a parity right now.
**Trask Stalnaker** 52:02 Yeah, can we look at the kitchen sink and see what all… Would make sense to define in semantic conventions.
**GZ Gregor Zeitlinger** 52:11 Sure.
**Trask Stalnaker** 52:28 Maybe search for headers, or… or you'll find it.
**GZ Gregor Zeitlinger** 52:36 So it's in the general section.
**Trask Stalnaker** 52:40 Right, so let's look at the ACTP ones.
I feel like the ACDP ones… we… Could go ahead and document those in semantic conventions.
**GZ Gregor Zeitlinger** 52:58 Okay.
**Trask Stalnaker** 53:00 … So yeah, I would suggest maybe send a PR to, semantic conventions that covers all of the HTTP.
Configuration options, including the known methods.
**GZ Gregor Zeitlinger** 53:36 Okay, and where, would that go and semantic conventions?
**Trask Stalnaker** 53:41 I would… I'm… At least for a… to start the conversation.
I would just add it freeform into the, the notes.
For that property.
For that attribute.
**GZ Gregor Zeitlinger** 54:01 Where would that… Oh, wow.
**Trask Stalnaker** 54:04 Go ahead and go… yeah, go to the HTTP… … Read me?
Or HCDB spans, really, is what I want to look at.
But not the YAML, let's look at the… because I can't read the YAML. Let's look at the, markdown.
**GZ Gregor Zeitlinger** 54:28 And also called spends….
**Trask Stalnaker** 54:30 Http spans.md.
**GZ Gregor Zeitlinger** 54:33 Okay. Yeah.
**Trask Stalnaker** 54:37 So, let's look at, … the… what are we talking about? We're talking about headers is one of them, so let's look at headers.
attribute, HTTP… server header… It's in the attribute list below.
Yeah, the one at the bottom there?
Yeah, header.key.
And let's look at the note, so 11.
Footnote 11.
So here, it talks about instrumentation should require an explicit configuration, which… of which headers are to be captured.
**GZ Gregor Zeitlinger** 55:34 Alright, so it just added there.
**Trask Stalnaker** 55:37 Yeah. Yeah.
**GZ Gregor Zeitlinger** 55:39 Okay.
**Trask Stalnaker** 55:41 And basically, it, you know, said the recommended value is something, something, something. I mean, the recommended name is… Something, something.
And that'll get the conversation. I don't… I don't have a lot of confidence that's where it will end up being.
But at least that will force the discussion And to me, at least that would be the minimum place, like, at least if we have it there, then I think Jack would probably unblock the configuration side.
**GZ Gregor Zeitlinger** 56:24 Oh, I think I added some things here already in… in the PR that I opened originally.
So here it was next to Autel Instrumentation.
**Trask Stalnaker** 56:35 Oh, yeah, yeah.
**GZ Gregor Zeitlinger** 56:38 Okay, so it's similar, let's see what….
**Trask Stalnaker** 56:40 Something like that, yep.
Okay, I would just add the rest here, I guess. Yeah, add the rest, that way it's kind of… we can see, discuss holistically for… but just for HTTP.
**GZ Gregor Zeitlinger** 56:55 Okay, and then we'll discuss NSAMConf.
**Trask Stalnaker** 56:59 Yeah.
**GZ Gregor Zeitlinger** 57:00 Okay, thanks a lot. Time's up.
**Trask Stalnaker** 57:02 Cool. Yeah, see you soon.
**GZ Gregor Zeitlinger** 57:05 See you!
**Robert Niedziela** 57:07 See ya.
