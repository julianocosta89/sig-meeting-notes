SIG: Python SIG
Date: 2026-10-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Diego Hurtado (Dash0)** 03:27 Hello, everybody.
How's it going?
**Lukas Hering** 03:33 Nope.
**Pablo Collins (Splunk Inc.)** 03:35 Bye.
**Diego Hurtado (Dash0)** 03:36 Y's in the three, are we waiting still for someone?
**Lukas Hering** 03:47 Maybe you'll wait another minute or so.
**Diego Hurtado (Dash0)** 03:53 Alright.
**Lukas Hering** 04:00 I know, Tammy said she can't make it, so… does someone want to do triaging?
Otherwise, yeah, I can…
**Mekan Baymyradov** 04:17 Thank you.
**Lukas Hering** 04:18 They're triaging.
Okay.
Okay, yeah, I can just start with some of the, with traging for the… the main Python board.
Then go to contribute. It's well after that.
So… yeah, I guess… Yeah, starting… The bottom here… Yeah, this is one I opened. I have it in the agenda, so we can just skip it for now.
This one… Line, delta, and async.
Metric start timestamps… Oh, right, Yeah, I think I briefly looked at this. I think this part of this might be… irrelevant now with the cardinality limit changes in place?
Yeah, let me just ask them, Okay, next one… is catch exceptions from child processors and multi-automit. I think I added comments here. It's just, yeah, pretty much what the… Description says… I'm not really sure what this… propagate false loggers form out here, but that was added since I last reviewed it, but… This is the patch release that's going on… going out.
Logs enabled filtering… Let's see… you guys are doing some activity on this.
Yeah, I think… So this change just needs to be updated since we switched.
severity number to be an NEM, so these stop value calls, we need to go away.
That should be all there.
Maybe I can switch over to contribute quick.
Since… A lot more going on there.
Excluded spans… okay, so this looks like just a configuration type of change.
I guess, ASGI… Yeah, probably not much to talk about here.
This one… Just for adding async.
instrumentation support for AIO producer and AIO consumer.
do Kafka… okay.
Looks like there's already activity here as well.
We just put… let these run.
Fix for URLoop to add server address and port to client metrics.
Yeah, Relatively straightforward.
**Leighton** 10:11 Yeah, I can… I can take a look at this one.
**Lukas Hering** 10:16 Thanks, Leighton. Okay, we can probably go to the agenda now.
Okay, first topic from Diego is… The packaging dependencies… Right.
Let me just open… there's 3 PRs, I guess.
**Diego Hurtado (Dash0)** 10:48 Yeah, thank you.
**Lukas Hering** 10:52 Yeah, do you wanna, I guess…
**Diego Hurtado (Dash0)** 10:55 Yeah, just, okay, so… there is, a discussion in the Slack channel, where I was talking, I think, I think with you, Lukas, and also with Aaron, Ricardo, about the packaging dependency. So, The, as you know, we have been working with the injector and the packaging projects, And, these dependencies are… are an issue for us.
Now, I'm… I don't want to frame the… This, plan that we have to… do something about these dependencies as something that is injector-specific. It, it's not. I added it as, as a comment in the Slack conversation regarding how this is actually important.
for anyone who's, using OpenTelemetry instrumentation.
So… So far I've, proposed, two approaches. The first one I proposed was, implementing?
Reimplementing the specific part of the packaging code that we use, which is actually very narrow. The… we only use packaging to compare versions.
I think it's, something we do in the… in the bootstrap script, in the instrumentation, right? So, first approach I did was, to compare this, to… create this code that does this comparison. This comparison is, by the way, strictly defined in a PEP, so I don't expect it to change much. Now, then I received some feedback, I think, from Lukas and Ricardo regarding if it would be better to just vendor it, so that we can get, updates, and from Ricardo regarding the fact that if we vendor it, we… Who need a way to… Get something similar, like automatic updates for it.
So… I opened a new PR with this new approach that does that. It uses vendering, and even… That's also a weekly… Workflow that keeps it up to date.
Any of those approaches is fine by me.
I just, and, and I also wanted to mention that it's not my intention to… Do this for every single dependency that we have?
I am… I think we should, consider them on a case-by-case basis.
Packaging is, is something that is really… important, I think, for us to vendor somehow, because it's, extremely common And, yeah.
it's very possible that an application has it, right? So, this is a new approach.
I, if you prefer the old approach, that… Wasn't using Vandarin.
I'm multiplying by that, I can reopen those PRs.
I just would like, That we can hopefully make a decision.
On this topic.
**Lukas Hering** 14:39 Awesome, yeah, thanks, thanks for the explanation there. Yeah, I think… Yeah, unfortunately, Aaron and… Ricardo aren't… aren't here to discuss this. I don't know if anyone else has thoughts.
I guess a part of… So it's… it's mostly… so this is coming from… The instrumentation package, right, yeah, okay.
**Diego Hurtado (Dash0)** 15:09 Get rid of it.
**Lukas Hering** 15:10 So, I guess, like… I mean, if this is the only one that we want to vendor, I could see it being okay.
like, what… are there any other ones that we're eyeing on, like, vendoring? Like, I…
**Diego Hurtado (Dash0)** 15:30 But JSON schema is another one that is, actually pretty bad, because, the way that it interacts with the ATTRS dependency, but that's a separate topic, because I have found a way to… I found a library named FastJSON Schema that allows us to generate our own our own schema… JSON schema Validator, so it's… it won't be exactly vendoring, it'll be using something… using a tool that already can generate the code for us. I'm also eyeing that one, but actually, JSON schema, it's, because I found a case where just by installing JSON schema, we can break the… the virtual environment of the application, so that one is the… the… that's the only other one that, so far, I… I'm considering. But it's a separate topic, and It's, it'll use an approach that is not vendoring.
And also not writing the code by ourselves, so it's actually a pretty good solution, in my opinion.
**Lukas Hering** 16:51 Got it, yeah, thanks, Yeah, we can, yeah, discuss that as well. So, but as far as, like, contributors, like, packaging's the main one, then?
**Diego Hurtado (Dash0)** 17:00 Right, yeah, for contributors packaging.
**Lukas Hering** 17:05 Okay.
Yeah, I think… Probably would want.
since Ricardo and Aaron were… are also kind of involved in this.
I'd want, their thoughts as well.
Yeah, personally, I probably would prefer the vending approach versus… Hand rolling, just because it's… a little less… Maintenance burden.
Of having to worry about the correctness of the implementation itself.
Not that it is necessarily incorrect, but, Yeah, that's… that's… that's my view on this, so… Yeah, Leighton?
**Leighton** 17:56 Yeah, Diego, quick question, I might have missed this, because I joined late. Is the main scenario that you're targeting Auto-instrumentation interfering with the application's version of packaging?
**Diego Hurtado (Dash0)** 18:08 Yeah.
Exactly, right? The installation of instrumentation, open development instrumentations, That's probably not.
**Leighton** 18:21 Are we foreseeing a lot of, like, dependency conflicts with this? Like… I know… Previously, you proposed some vendor solutions for other dependencies that are much more strict.
Even to the point of, like, different major versions.
But this one seems to be, like.
Like, do you have examples of, like, this actually causing problems, and… or is this just, like, a… you foresee that this might happen?
**Diego Hurtado (Dash0)** 18:57 Yeah, I added the example in the… in the Augment Telemetry Python channel in the conversation. Regarding the… yeah, I think there's a general concern, and I totally understand it.
About how far… are we going to take this approach, right? If I'm gonna keep pushing to vendor every dependency that we use, I just want to… assure everyone that, I don't want to. I'm trying to keep this at the absolute minimum, and I am… and I'll be just, thinking about them, and on a case-by-case basis, right? Because there is, I understand the burden that it is, To… have to, you know… have this bunch of code in our repos, right? So, There is an example I added in the conversation for, This, server packaging, right?
And, yeah, for example, I was, also… concerned about Py YAML, but fortunately, we don't need to.
Pyaml, we can use, without much trouble, since, the… every version so far… It's compatible.
With, 3.10 onwards, right? So, as I said before, the… Of course, every dependency can be a problem.
But, it doesn't necessarily mean that Every dependency will be a problem. We… We have to evaluate them on a case-by-case basis.
So… so yeah.
I just want to… reassure you, it is not my intention, right, to… To try and render every single thing we use.
And, yeah, I also don't like doing this. I mean, I see this as a… as a necessary evil. Let's call it like that.
**Leighton** 21:27 Well, so my question was more about, like.
the comment that Lukas pasted, probably, forwarding what you're mentioning.
I wasn't asking for an example of how this could be. Like, I know that this could very well happen. What I'm asking is more, like.
Are you presented with, like, Evidence from the community that this is actually a problem in people's ecosystems?
Or is it more of, like, a hypothetical?
**Diego Hurtado (Dash0)** 21:57 Okay, yeah, right, okay, so this all started with, the… The injector project that, When… when we were working on that, we realized that, There are dependencies that are very common in the application that will collide with, the… the injector project.
like, ERPC, and protot, right?
protocol for us to… the thing that I started with. So… It is, we do have, Reasons… Sorry, what?
**Leighton** 22:46 What is the Injector project? What is that?
**Diego Hurtado (Dash0)** 22:49 Okay, so… There is a project in OpenTelemetry named the injector, right?
And, there is another project, also in OpenTelemetry.
called the Packaging Project, right? So, the packaging project is, The idea of this project is to make system packages, like.
DBM packages or RPM packages, right, that you can install, and just by installing them, you automatically Have automatic instrumentation.
So, I like to describe this as automatic, automatic instrumentation, even when nobody else likes that name. But, that's, that's what it is, right? So, the, it was, when we started working on this project that we realized the problem that it was, These dependencies that are super common.
And we can probably have application code so that, we could, definitely use a solution, right? Vendoring this, doing this approach, like vendoring, for example, is not an uncommon, In Python, pip uses it.
and, in the OpenTelemetry project, also Java has its own version.
Its own implementation of, protobuf, right? So, we're not doing anything that is, unusual here, right? Or new?
Maybe… the… The… the interest in doing this has just increased.
Since this project started, right? But at the same time, I don't want you guys to have the impression that… The only benefit, from vendering will be on the injector side. Now, this… this can actually, cause problems also for people who are doing just normal, regular instrumentation, so… This is also important for them.
**Leighton** 25:10 Got it, nice. Thanks for the context, yeah.
**Diego Hurtado (Dash0)** 25:12 In total.
**Lukas Hering** 25:14 Yeah, one… one more quick comment on, that specific Slack example?
That seems to be a constraint put directly Directly from the flask itself.
So, I wonder if… so, like, the instrumentation library just bounds by 18.0, And this has a higher version, I'm not exactly sure why this is the case, but… I mean… I'm not sure if it would just be easier just to fix this, right? Or try to make the version, Like, we could just try to have a more wide version range with which we accept.
If that's… I'm not sure if that's something you explored, but, like.
**Diego Hurtado (Dash0)** 26:01 Yeah, that's, that's another approach, actually. It's a good thing that you mentioned it. In theory, I think.
Sometimes, because there is no guarantee that this will work every time.
we can change our code in our instrumentations, and in the instrumentation package, and we can add a bunch of ifses and elsees, right? So, what we can do as well is that When… when we just start, we check for diversion.
Of a certain package, a certain library, and depending on which version it is, we do something different, right?
That's also something we can do. And by doing that, we can, as Lukas just mentioned, we can widen the range of versions that we support, we support.
It's also… more complicated on us, and it's also… I mean, of course, it has its advantages, of course, we don't… we won't need to version things.
The disadvantage, of course, is that our code gets more complex, and at the same time, there is no guarantee that we can do The… the things that we do… for all versions. For example, what I mean is that, let's say that there's a dependency on version A, and that dependency also publishes version V. And the difference between them is not only About what API they have, it's also about the features they provide, and B provides more features.
So, we cannot.
I mean, if… we cannot rely on using a feature on B, because It may also not be a feature in A.
See what I mean? Right, yeah. So, yeah, that approach… has the problem, and that's what I mean, that we need to evaluate them on a case-by-case basis, because there are some libraries where we could follow this approach.
And it may work for us, and some libraries worry.
Wouldn't want, right?
To be honest with you, I haven't tried.
this approach on packaging, I can also try this approach on packaging, and I can also give you a PR.
Before you make a decision, because this, this could also be a solution for packaging.
So, yeah, I can also totally do that, yeah.
**Leighton** 28:41 Yeah, I think we probably should timebox this. I think we've brought this topic up many times. It just pretty much just calms down and transfers the responsibility Of dependency management from the installer to the maintainers, and that's just… Pretty much it. So, We could probably.
**Diego Hurtado (Dash0)** 29:03 We do this.
Yeah, sorry, how about we do this? I'll explore this other approach that Lukas just brought up about, Widening the range of packaging support by, I don't know, like, fixing our code in the instrumentation.
And, maybe, hopefully.
That it's doable, and it's practical for us, and then it makes the decision easy for us.
So yeah, I agree with Leighton, we can just, discuss this, another time.
And I can bring you the results of what I… what I get.
Next week.
**Leighton** 29:49 Cool, thanks, Diego.
**Diego Hurtado (Dash0)** 29:51 Alright, thank you all for listening.
**Lukas Hering** 29:55 Yeah, the next one's from Diego again. Yeah, I know there's…
**Diego Hurtado (Dash0)** 29:59 Yeah, exactly. If you open the… just open the contribo, please.
Yeah, right there, there's a tab that says Security and Quality, up right there. So it says 1400… things, right? So, most of those code scanning vulnerabilities… oh, by the way, let me give you some context first. So.
A few days ago, I was just, you know, doing my stuff, and then I get a message in Slack from Alex Bowden. I think everybody knows Alex Bowden, right? A member of the TC.
And he tells me, hey, what's, going on? Seems like, You guys have a lot of, alerts there, then I took a look and, well, yeah, we really do have a bunch of alerts. Now, I looked into this, and most of these alerts, code quality and vulnerability alerts, are happening because, either Dependabot cannot update.
some certain files because of some issues we have in our infra. And the other ones, the code quality issues, are also… The vast majority of them can be fixed by just a few changes in… in our… I think it was the… I don't, I don't remember the name right now, but it's just, changes in a few files, right? So, I opened, many PRs, That, that will… that'll fix this.
And we'll drastically reduce the numbers of security and quality alerts that we have.
The, now… as I was doing that, I received some feedback from people, saying that, It'll be better to use or renovate than depend, dependable.
I don't know much about the difference between them, but, I mean, these people are probably right, and I agree with them. Let's switch to Dependabot. But, what I want to propose is this, let's first, Get this, issues that we have with Dependable fixed, so that we can just quickly bring down these, numbers of alerts, which are, like, raising eyebrows in the TC.
And then, let's, migrate to… to renovate. I… I'll be happy to… to do the work of the immigration to renovate.
I just want to, get this, fix… fix these alerts.
Because, yeah, it, it's, grabbing the wrong attention to interpret it.
**Leighton** 32:59 Yeah, I'm actually… I'm actually okay with that. I'll take a look at your peers.
**Diego Hurtado (Dash0)** 33:04 Thank you. Appreciate that.
**Lukas Hering** 33:07 I will take a look at these as well.
Last one from Diego is the new…
**Diego Hurtado (Dash0)** 33:15 Yeah, I'll be quick with this one. Some time ago, we just discussed about a policy for accepting new instrumentations. I got a comment from Media, I think.
the… I, I am not against what the media is proposing, but, I mean, I've already written down my position here. I'm just asking for other people to, To write down what they think, so that we can move forward with this issue that can bite us again during the moment.
Already taken a lot of time, so that's it. Thank you very much.
**Lukas Hering** 33:54 Nope.
Thanks, Diego. Yeah, I'll, take a look at this as well.
Okay, one from me, I'll just… I'll try to be quick here.
Can also discuss it next week.
So, yeah, this is PR that's been open for a few months now.
It's not particularly interesting, but the… what makes it unique is that it adds a new attribute on, Instrument creation?
So, the… what the changes are is it adds an attribute advisory on, like, what attributes should be applied, in the… when a view is not specified.
So, I guess, yeah, the… what I wanted to bring up here was… Let me try to find the actual… Where the functions… actually change… Some hints here.
Yeah, so… Technically, to add this, would be a breaking change.
For the API package.
Because requiring an additional, this additional, keyword arguments.
This function would break external API implementations.
The… really, the only scenario, like, that this can occur is when… if someone's using the new, Like, advisory attributes, Argument?
for an underlying SDK implementation that doesn't support it.
So, yeah, there's kind of two sides to this. We can either just go ahead with making this change, call it out.
Even though it's technically… It's technically, like, a very small break to semantic versioning.
Or, We kind of just accept that we cannot do this, and basically, that would… we could do something with, like, creating new functions, For this, but we would not be able to add any new, arguments to any of these methods until we do, like, a 2.x release.
So, just wanted to hear some people's thoughts.
Yeah, Diego.
**Diego Hurtado (Dash0)** 36:34 Right, if I remember correctly, I think I either opened up PR against that PR, or added a comment there, suggesting a way that we can do this without actually Making a breaking change.
**Lukas Hering** 36:47 So, that was specifically for the case when you have a proxy. Originally, we were forwarding everything, like, all these arguments to the underlying implementation, so even if you didn't use those new arguments, it would throw a type error. That's fixed now, so we only forward the extra keyword arguments that are actually passed in by the user.
the issue that I'm describing here is that someone may install, like, the latest version of API and see that there's these new, there's these new arguments that they can use.
But when they try to use it, it'll throw a type error, because depending on if they have, like, a custom SDK, it'll blow up.
Does that make sense?
**Diego Hurtado (Dash0)** 37:29 Okay, so then it's not breaking in the sense that you are not removing An argument that was there before.
**Lukas Hering** 37:42 It's breaking the sense that, like, like… You know, adding an argument to an abstract method would require implementation.
**Diego Hurtado (Dash0)** 37:56 your class.
**Lukas Hering** 37:57 Actively have that, right?
**Diego Hurtado (Dash0)** 38:00 Okay, okay, I see. So it's, it's about these, the classes that,
**Lukas Hering** 38:07 extend the API. So that's our case, like, 99% of the time, but there are… there are users that do use, custom. So it's very subtle, but yeah, I just want to bring up, Liudmila.
**Liudmila Molkova** 38:19 Yeah, it's… Very related to the next few… next topic that I have, but I… I'm worried about breaking API.
Like, this is… if there are users, and we know.
That they will be broken, they… who implement this class.
It's… a giant… Reputation loss.
breaking API, open telemetry API is awful.
**Lukas Hering** 38:51 Yeah, so I guess just to call out, it's still a really, really narrow case if you'd actually run into an issue, and I brought it up in this PR. We actually… we've already done this before, so this PR…
**Liudmila Molkova** 39:05 I'm a lost its word.
**Lukas Hering** 39:07 Which adds… Although this is a narrower… so we added explicit bucket boundaries to histograms a while, like, yeah, over a year ago.
And this is a… yeah, this is a… this is the same exact change. We added this argument, no one seemed to notice or complain.
So, that's where, like, I know Emilio commented on this, saying that it's, probably okay, just because of how rare. So basically, the only way it would break is if you tried to do this.
But you're using a custom SDK.
create counter, and you gave it this custom… so basically, the user will most likely know what they're doing. If you're using a custom SDK and using, like, new features.
You would probably need to make sure that the You'd want to make sure that your SDK supports it, right?
So, if you're using the normal API as it is today, nothing will, like, this won't break.
So, like, it's not like… So any existing code will never… it'll not break. It's only if you start using the new attributes we introduce.
**Liudmila Molkova** 40:26 Yeah, I hear you. Can we… estimate, like, I don't know, ask AI to find if somebody Actually… Craig.
writes custom SDK.
Or there are non-test implementations on GitHub?
Like, just to assess how narrow this case is.
**Lukas Hering** 40:50 Yeah, media link's another issue.
So, yeah, someone… we did do another… we had another regression a while ago.
that wasn't intentional, that caused external SDK implementations to break.
And yeah, someone did raise an issue,
**Liudmila Molkova** 41:09 Yeah.
**Lukas Hering** 41:10 Open.
I mean, again, this is a… this is a kind of a completely different case, but, The… this case… again, like, the only way… so, like, going back to, like, you know, adding the span type.
**Liudmila Molkova** 41:27 Guys?
**Lukas Hering** 41:28 The only way you'd run into the issue is if you tried using the new spam type functionality, and you're using a custom SDK, right? So, like, you'd have to be, like, actively trying to use this new functionality with an experiment… or with your own SDK implementation.
**Liudmila Molkova** 41:44 Yeah, I guess my concern is more… general, so that we promise API stability, we promise that custom SDKs are possible. We… break it, because in every single case, it seems okay. It seems not critical. And I agree with you, assessment is probably not critical, but, like, if we keep ourselves to high standards, then we shouldn't do this. We should figure out a way to do it in a different way.
But I'll…
**Diego Hurtado (Dash0)** 42:20 Or we should, release it in a new Mayor version.
**Liudmila Molkova** 42:24 Major API version, please, let's not. Let's figure something else out. The new class name, new metad name, something.
**Diego Hurtado (Dash0)** 42:32 I mean, but… Isn't this, what the major versions are for?
**Liudmila Molkova** 42:38 This is what major versions are for, but the OpenTelemetry API new major version.
would be the first, and I tell… nobody plans for a new major version for API.
the… everybody who did new major version for API got so much beating.
It's… like, there are so many ways to do it, like, we could have a new version of the meter, or, like, the crate.
counter, where there are so many ways to solve it without new major version for API.
**Diego Hurtado (Dash0)** 43:15 Well, I guess we'll… Need to see if there's a solution, or that…
**Lukas Hering** 43:21 Yeah,
**Diego Hurtado (Dash0)** 43:23 For this particular case, because, What I'm not sure is that there will always be a good solution.
That is not just, introducing a change that requires a new major version.
**Liudmila Molkova** 43:39 It does not require major version if it's done a backward-compatible way. If it's a new method.
**Diego Hurtado (Dash0)** 43:44 Yeah, what I'm trying to say is that there is… there is no guarantee that there will always be One of the… a solution of that kind.
**Leighton** 43:56 I think in general, if we're talking about new features, there's always going to be a way to… Provide accessibility to this new feature, albeit it might be an inconvenient way of consuming it.
Right? There's always going to be a way to do that. The trade-off is just whether or not the… Breaking someone is… more or less valuable than providing this new feature, and I think I'm on the side of the miller here, where it's like.
Especially on the API, I really don't want to do a new major immersion.
And also, like, I think the credibility… of… you know, because we have so much visibility now, I think the credibility of the OpenTelemetry is… Quite important, especially with our… Few mistakes that we've had in the past.
So… Just from the top of your head, like, yeah, if we were to even just say, like, okay, like, we'll have, like, a… I don't know, metric instrument that is, like, experimental or something, and, like, you want to use it, with any new features that come that Might defy the current, stable contract.
You can use that one.
And yeah, like, users would have to use two different, components, but, like, at this point, I think it's better than, like, suddenly, us getting angry issues like the ones that we had a couple months ago, so…
**Lukas Hering** 45:35 Yeah, one small thing to add. So, like, actually, Attributes Advisory is… is being stabilized.
So, assuming if we take a very, very strict interpretation of the semconf, we can never add it to the existing methods.
So, we have to add, like, create counterv2, or, like, create counter… like, that seems really ugly to me, like, so yeah, we can probably stop it here, because there's people that probably have other thoughts that aren't here, so…
**Leighton** 46:08 Yeah.
In a… in a similar note, though, I think there was some discussion regarding, maybe tackling it now, in terms of making our APIs forward compatible?
I believe there was, like, a related PR to that.
**Lukas Hering** 46:27 Yeah, that was for law.
Since we… we haven't.
**Leighton** 46:29 Yeah, okay.
**Lukas Hering** 46:30 I added a… I added this same kind of functionality to logs, so that we can always add new arguments.
**Leighton** 46:40 Right.
Right, right. Yeah, I think that was… I was looking at this, yesterday, yeah.
Yeah, okay. But yeah, along the same lines, I think that's a good… Good to keep note of in terms of, like, more designing… new APIs, so… lining because we have stabilized logs. So, you know, we have an opportunity to do this.
**Lukas Hering** 47:06 Yep.
**Leighton** 47:07 Lenovo, go ahead.
**Liudmila Molkova** 47:10 Yeah, on this note that, okay, the metric advisory is one thing we've added, and there are more things we need to add, but there will be more features.
And every time, like.
we need… we will need to provide the method with QVRX at some point, for every… pretty much everything.
So, let's figure out the strategy. There could be a create counter too, which sucks, or there could be a meter or two, which sucks just a tiny bit less.
And we can explore different options and decide, but I think we need to have a common strategy. And, like, it's funny that, Lukas your thing decides to break, and my thing decides to invent a new method. We should at least figure out the common strategy, otherwise it just feels wrong.
**Lukas Hering** 48:10 Yeah, I was just gonna, yeah, definitely agree there. So, yeah, did you want to comment anything more on this, Ludmila.
**Liudmila Molkova** 48:20 Not really. I think I've got a review from you, from Aaron, appreciate it. I addressed everything. This is a call for review, but I realized that we probably need to have a conclusion on how we do such kind of changes before we can like, let it in. Regardless, it's, the… essentially not the ask to merge anyway, because this is the… the… implementation, I'm, connecting to the spec PR, and the spec PR is not in yet, so I would appreciate reviews or even approvals, if you are ready to give one, but it's not something we can merge until the spec is changed and released.
**Lukas Hering** 49:08 Okay, yeah. I guess just for anyone who's, like, kind of wondering, this is what you'd have to do In a… to avoid ad… so, like, not touching the existing signatures.
**Liudmila Molkova** 49:21 Yeah.
**Lukas Hering** 49:22 I guess, like, I mean, the other concern is, like, if there's a new thing… I mean, you made this forward compatible, but, like, you know, it's like a… you know, now we need, you know, all different combinations, like start type span, start type span as current, right?
**Liudmila Molkova** 49:40 Yeah.
**Lukas Hering** 49:41 It's not too bad in this case, but it can get really, yeah, kind of nasty, but, Yeah, we can discuss it more offline.
**Leighton** 49:49 Period.
Maybe we can start a discussion thread for, board compatibility for new features.
And discuss it there.
**Lukas Hering** 50:00 Yeah, I can… yeah, create… either we can do it in the Slack, or create an issue, or…
**Leighton** 50:08 Okay, sounds good.
**Lukas Hering** 50:10 Okay, Dylan?
Yeah.
Okay…
**Dylan Russell** 50:20 Yeah.
There's this, like, PyPi GitHub attestation stuff that… Pretty straightforward to add to our, like, release workflows.
And… Yeah, it… Basically signs the… the wheels and the… TAR that we generate at build time.
And… saves it to, like, the attestations page on GitHub.
And then people can, like, verify the… File to install with, like, GitHub attestation verify.
And there's a… Similar workflow step to do the same thing.
in PyePy.
Yeah, it's kind of…
**Lukas Hering** 51:15 Gotcha. Okay. Yeah, if you, if you want to open a PR, that'd be… that'd be great. Or, yeah, whoever has capacity here.
**Dylan Russell** 51:26 Yeah, I did it on another repo recently, the Gen AI one, so I don't mind doing it here.
Nice.
**Lukas Hering** 51:35 Okay, next one, Leighton on the… to Cardinality, or this is our patch release.
**Leighton** 51:46 Yeah, no need to spend too much time on this, I'm just letting people know that I am doing a patch release today, it's just for two… to PRs?
Yeah, that's… Maybe need some reviews for the, following… release PRs, but that's pretty much it.
**Lukas Hering** 52:07 Okay.
**Leighton** 52:08 I'll link them in the Slack, once they're out here.
**Lukas Hering** 52:13 Okay, thanks.
**Leighton** 52:15 Yep.
**Lukas Hering** 52:17 Okay, last one, from Mekan?
Let's look at this PR… In the call, okay, This is a fix for SQL Alchemy, don't suppress… Pool connection count updates… Okay, let's see the original issue.
Oh, okay, yeah, I kinda… kinda see how this could happen. Okay, did you just want extra eyes on this PR?
Or was there something else?
That needs to be discussed here.
**Leighton** 53:24 Yeah, Mekan, you're in the chat, you just probably need some reviews.
**Mekan Baymyradov** 53:32 Can you… can you review the… hello? Can you review the two approaches?
**Lukas Hering** 53:38 Yeah, yeah, we can take a look, yeah. Also, yeah, apologies, like, we have a… quite a few PRs in Contrib, so… But yeah, I'll try to take a look at it, sometime today or tomorrow.
**Mekan Baymyradov** 53:51 Thank you.
**Lukas Hering** 53:57 Okay, and that's it, so we can… Unless there's anything else someone wants to add quick, we can probably, finish a little early.
**Liudmila Molkova** 54:07 I have a quick question to you folks, process-wise. I'd like to do something with OpenAI V2 package in the country pre-po.
We never formally deprecated it, there is some bug, and I kind of want to… Polish some… Things there, call it deprecated, and forward.
Thanks to the new package.
We did call it out in the README, we never released it. And it breaks with some new version, I want to apply some version cups.
Maybe even… Take a dependency on the new package, and, like, always have an opt-in flag for experimental things, and when it's on to… Proxy to experimental package.
But essentially just released the final version.
And I… including, like, some graceful switch to the new version and proxying, it might be a relatively big change that, like, a lot of code removals, but just a lot of files.
Would you prefer it to be broken down? Would you prefer one big PR?
**Leighton** 55:22 I would personally… Like, it to be broken down?
**Liudmila Molkova** 55:27 What's happening?
**Leighton** 55:27 Not too much work.
**Liudmila Molkova** 55:29 No, no, I mean, who's a guy?
**Lukas Hering** 55:32 Yeah.
**Leighton** 55:33 Yeah.
**Lukas Hering** 55:35 We got the stacked PRs, too, so that'll… that'll help.
**Liudmila Molkova** 55:39 Cool, I'll do stock PRs then.
Awesome, thank you.
**Leighton** 55:44 We can, like… we can, like, streamline this relatively quickly, because I think we have a lot of context on GenAI stuff, so…
**Liudmila Molkova** 55:55 Awesome. I appreciate it.
**Lukas Hering** 55:58 Okay, awesome. Yeah, thanks, everyone.
**Liudmila Molkova** 56:00 Thank you.
**Dylan Russell** 56:01 Stadios.
**Leighton** 56:02 This goes…
**Diego Hurtado (Dash0)** 56:05 The goop.
