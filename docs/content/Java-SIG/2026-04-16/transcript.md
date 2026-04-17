SIG: Java SIG
Date: 2026-04-16
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Trask Stalnaker 00:02:25 a.
John Watson 00:02:31 Good morning.
Jack Berg 00:02:41 Hello.
Chas, did you have a good, I don't know if you went somewhere, or if you just took a couple of days off, but did you have a good break?
Trask Stalnaker 00:02:50 Yeah, yeah, I went to Boston, college. Visiting.
Jack Berg 00:02:56 That's a quick turnaround for going across the country.
Trask Stalnaker 00:02:59 It is, yes.
All business, no, yep.
Cool, Jay, let's, kick it off.
Jay DeLuca 00:03:37 Yeah, so I was just, I was just reviewing, this PR, and I don't… I was wondering how we should think about when we add new configuration options to Contrib components, if there's any… Rules we should be following now.
Jack Berg 00:03:58 Sorry, can you repeat?
Jay DeLuca 00:04:01 Yeah, so when we add new configuration options to contribib components, if there's anything we need to keep into consideration in terms of, like, the way that we're… Or formatting them, or… Like, just think of a declarative configuration in mind.
Jack Berg 00:04:19 Yeah, interesting question. You know, I think of Contrip components as, sort of, Independent, things that, you know, just take advantage of some shared Publishing rails and shared build rails. Provided by the contrib.
repository, and… But, like, you know… to what extent should they follow the lead, the guidance of what we're trying to do in the core repo and in the instrumentation repo? That's kind of what you're… you're tugging at, I think.
Jay DeLuca 00:04:58 Yes.
Trask Stalnaker 00:05:13 What's our story for declarative configuration in… Contrib… I think a couple of things we have… added support, but I think those are things that are… more intended to be used inside of the Java agent.
Jay DeLuca 00:05:38 Yeah, like, I think the resource detectors?
Trask Stalnaker 00:05:41 Yeah…
Jack Berg 00:05:42 There's also, a sampler, the rule-based sampler, which is integrated as well.
Rule-based routing sampler.
It registers itself… registers itself as a component provider, so you can reference it in your… Config YAML.
Trask Stalnaker 00:06:02 Yeah, I guess I would… the first thing I would ask here is, can we… Does it not also support… is it one of these things that it's supporting both declarative config?
And system properties, or we're not supporting declarative config at this point.
Over here, and if so, could we…
Jack Berg 00:06:29 I mean, the core repo basically has a policy right now where, you know, we're pretty judicious about adding new properties for system property and environment variable configuration, and if we do, because we do have some examples of that, we… are always sure that there's equivalent configuration options and declarative config. Like, we don't want… we want declarative config to be a strict superset of what is available via system properties and environment variables.
Trask Stalnaker 00:07:05 And we've done the same in the instrumentation repo at this point. Everything… Is basically declarative configuration first.
We use the declarative configuration.
API to… Read things, and the… The difference there is that we installed that bridge.
in the Java agent, so that we are still supporting system properties via the bridge.
Jack Berg 00:07:37 -
Trask Stalnaker 00:07:40 And so, I don't know if we want to take the same approach in Contrib and say.
That you have to install if you still want System properties support.
Over there, you need to install the bridge.
Although, I would guess that this… This one, I would assume, and Sylvain, maybe you know, that this is primarily intended to be used in the Java agent And so… We probably don't… we probably could just do straight declarative config here.
Sylvain Juge (Elastic) 00:08:22 Unfortunately, I haven't been following what Jack is working on.
Trask Stalnaker 00:08:26 No worries.
Sylvain Juge (Elastic) 00:08:27 I can't answer.
Trask Stalnaker 00:09:09 Alright, yeah, good question.
Jack Berg 00:09:14 I'm, opening a new issue, by the way, that… And that declarative config should be a strict superset of sys properties and environment variables, and then at least we'll have, like, an artifact to point out.
And I'm not super opinionated about whether contributen to what we're doing in the core repo, but, like, you know, I minimally want to have that policy documented for Core.
Trask Stalnaker 00:09:48 Cool.
Jay DeLuca 00:09:49 Awesome. Thank you.
Yeah, so this… this next one's me too. I was just sketching out another idea about, Since we have the metadata, if we wanted to try and use it to create kind of a kitchen sink For all the different instrumentation options. I did something similar in the Explorer project that I'm working on, but I figured it would be potentially useful to have, just as an artifact within this repo, too, where someone could just copy and paste it if they wanted. It's still… there's some… I need to do some quality assurance, I think there's some… stuff that isn't quite right, and I had an open question about if we decided to do this, if we thought it would be useful to also include, like, the… SDK getting started, snippet as well, but… Yeah, I just wanted to get some thoughts on whether this was something worth pursuing.
Trask Stalnaker 00:10:47 Instrumentation slash development.
Jay DeLuca 00:10:50 Right, that's one of the things that's… Yeah, I need to… I need to fix some stuff, but… .
Trask Stalnaker 00:10:57 I love it.
Jack Berg 00:10:59 Yeah, I like it too, One of the things I ran into when we maintained a kitchen sink, example file in the OpenTelemetry configuration repo was that, There were certain, like, cases where… it's not clear, like, what you should actually include in the kitchen sink. Like, so imagine, for Tracer Provider, you have… you have the opportunity to set a sampler. And the kitchen sink, you're supposed to, like, demonstrate all the samplers, but you can only set one. Like, what do you do there? Which do you choose, and why?
And, like, which go undocumented because of this requirement that you have to choose one. And, you know, like, kind of a similar thing is, like, so sometimes properties have, like, natural default values, like, like, span limits, for example. Like, you know, the max number of attributes that you, that you can set, you know, the default is 128. And… but the default for, what the max length of an attribute is, is unlimited.
And so, like, what do you set for the default value where, like, the semantics of the property are, like, such that, like, if it's unset, you do some behavior that you can't actually, like, encode in a default?
Like, how do you set unlimited as the default?
Trask Stalnaker 00:12:34 Jack, what do you think of, like, if you put… if you commented, like, included all of the… basically, make everything commented out, essentially?
Jack Berg 00:12:47 There you go. Yeah.
if you could some… but, you know, I assume… given that this is Jay talking about this, this is going to be generated, and not manually curated, so, you know, you just have to do something like, you know, generate it, assuming you know all the properties, and then somehow selectively comment things out based on whatever you decide.
Trask Stalnaker 00:13:08 Comment out everything.
Jack Berg 00:13:10 Oh, okay.
Trask Stalnaker 00:13:12 That's what I was wondering, kind of, like, what if we just comment out everything I don't know if that works, like, if some of these have required… Like, if they require at least one thing under them.
Jack Berg 00:13:29 I still think you probably have to come, like, make some decisions about, like, what to set as the value, even if it's commented out for certain properties?
But, like, it definitely, you know, sidesteps some of the problems I was talking about.
Jay DeLuca 00:13:47 Yeah, so right now, it uses… it basically just uses the default values that are set. But… but one… so one thing that I'm thinking about next steps for this is, right now, all of our metadata tracks all of these properties as system properties, so I have to do… some gross stuff to kind of reverse that. So what I want to do is… but once I get that algorithm tightened up and accurate, I would like to then go back and convert all of our metadata the way that we track it to be declarative configuration first, and then I can just generate the system property equivalent in another doc, as well.
But yeah, so that's kind of the direction that I'm thinking about going, but… and I say that, so we'll have this in metadata if we wanted to add additional attributes or ways to annotate specific instrumentations that would be very easy to incorporate in the metadata schema, and then we could just use that as we process. Because, yeah, this is… this is entirely, generated, so overnight, presumably, as we keep our metadata up to date, this would just update automatically.
I still have intentions of eventually going even a step further to see if we could then take that metadata and generate the code that is used to then scaffold out the declarative configuration API and all that, but, yeah, baby steps.
Jack Berg 00:15:10 Right.
One more thing to think through, or I guess maybe that, I want to get your thoughts on. So, I'm thinking of… what is it? The JMX stuff.
Where you, like, this is a natural fit with declarative config, where you can encode that, the JMX YAML for how you want to map those metrics to the you know, metrics in OpenTelemetry. And, like, I'm only talking about JMX because it has this characteristic where it has, like, an array of objects.
And the default for the array is probably, like, empty. But the point in your kitchen sink is you want to be able to, like, describe these data structures.
Like, you want… you want to give, like, an example of, like, an entry in this array, so that you can, like… so people can have a starting point, and then go and edit it. And so, like, what do you… what do you do in that type of case, in a kitchen sink example?
You know, like, what… what… there's no default. The default is empty, but, like, you still… part of the kitchen sink is you're trying to describe this… this data structure, right? So, like, what do you choose?
Jay DeLuca 00:16:23 Yeah, so at the very least, it sounds like when I go back and do the, kind of, the metadata reverse engineering, we should have an examples, or the ability to embed an example and just have that, kind of.
Put as a comment above it, just, like, as an optional attribute.
Jack Berg 00:16:43 That'd be a good way to solve it. That's kind of how I solved this in, in, in the OpenTelemetry configuration repo. We have, like, these examples which you can copy and paste in, but then we also have these snippets, and the snippets are, like, they're not… They're just supposed to, like, be this kind of thing, where they're, like, you can take inspiration from them, but we're not recommending you copy and paste this into your environment wholesale.
Right? So that's what we're trying to articulate in this case. Like, you know, if you need to, you know, model one of these rules for the JMX thing, you know, here's an example of this, but, like, you know, don't copy and paste this into your default config.
Jay DeLuca 00:17:23 Yeah, and maybe that would make sense to be something separate, like a snippets tool, but that's good food for thought.
Trask Stalnaker 00:17:30 Do we… are we expe… yeah, I guess kind of a question of how this would be used, Do we think a lot of people would… Just copy-paste this in as their starting point.
Jay DeLuca 00:17:47 Yeah, so my initial thought was… I just had it all as the default values, so it would be… the idea would be… to start out, it would be a no-op, essentially. Like, you use the config file, and it's going to give you exactly what you would normally get by default.
And then if you wanted to customize things, you just, you at least have… You know, the starting point.
Trask Stalnaker 00:18:08 Yeah, so the, the… one thing that I have always struggled with the kitchen sink type of thing is that It drifts over time, and so if the user, you know, copies it at one point, it then becomes, like, unclear.
What they've intentionally changed, or what they've not gotten updates for.
And so a couple of options there worth considering. One is, the commenting out thing, like, if you do Essentially, then, like, it's like, it's clear what people have opted back into.
The other is if we… If… if it's valued, like, if having the kitchen sink could just be, like, an HTML, you know, a Markdown file that has the different, again, the snippet idea of each one you have. It's basically a kitchen sink of snippets.
That you can copy-paste to the snippet that you want to create your… YAML file.
Jack Berg 00:19:27 So it's sort of, like, decomposed into snippets for each instrumentation, which makes you, which kind of, like, discourages this pattern of wholesale copy-pasting and uncommenting.
Trask Stalnaker 00:19:39 Yeah.
Jack Berg 00:19:40 Yeah.
Jay DeLuca 00:19:43 Yeah, and that's the approach that I've taken with the Explorer project, where it's like, you can select the instrumentations that you actually want, and then they're dynamically populated into the file. But, Yeah, I'll explore… I'll explore the snippet idea a little bit further, and I haven't… I don't think the JMX stuff is even included in this so far, so, I probably haven't even thought that through.
but, yeah.
Trask Stalnaker 00:20:09 Yeah, this…
Jay DeLuca 00:20:09 stop.
Trask Stalnaker 00:20:10 Yeah, the snippet piece could be, would… Yeah, let's see how many of those kind of, JMX and maybe sampler, kinds of things that we have, because that could lean us in the direction of snippets that are more flexible and having multiple snippets that kind of describe different pieces.
Jack Berg 00:20:33 It's not just JMX, like, it's… you see it right here on line 8, like, request captured headers, right? So, like, what's the format of those?
like, is it uppercase? Is it lowercase? Does case sensitivity matter? Like, anytime you have an array where the default is, like, empty, and you have some semantics around that, it's nice to show some example values of that array anyways.
Jay DeLuca 00:20:59 Yeah.
Trask Stalnaker 00:21:13 Core PRs…
Jack Berg 00:21:18 Yeah, I just saw a light agenda, so I thought I'd bring up some topics that have, you know, had PRs open for some time.
Just to get through the conversation synchronously.
Trask Stalnaker 00:21:31 Yeah, I couldn't… yeah, this kind of rings a bell, John, but then couldn't…
John Watson 00:21:41 I thought…
Trask Stalnaker 00:21:42 Doctor.
John Watson 00:21:42 What I… I mean, what I remember, and again, this is just sort of a vague Recollection is that we didn't want to add these until we actually had like, a real need to. So if you… if, like, instrumentation has a real need for it, then… I'm not gonna block it, but I want to make sure we actually have a real need for this.
Jack Berg 00:22:04 We're gonna have the realmade, because it's sugar.
John Watson 00:22:07 Right, and I think we didn't want to encourage people to be using these things, because it's not… they're not ones that are commonly… In the, in the semantic conventions, right?
Sweet.
Except for a few… except for a few small cases, so that's… I just wanted to make sure I threw it.
Trask Stalnaker 00:22:30 So, I did actually, this, want to use this, which is why I opened the PR. The context was… is that, I was prototyping some Gen AI semantic conventions.
And… I want to just… Yeah, so it was kind of confusing to me why it didn't work.
Because the GenAI semantic conventions does, use value objects And I think in my prototype, I wasn't using the constants, which, of course, would be A sensible thing to do.
So, we did add it to… And that's the other thing. We do have it on Attributes Builder already.
Jack Berg 00:23:45 It can't not be on attribute… oh, oh, oh, we have the sugar method on attributes builder.
Trask Stalnaker 00:23:51 Yeah.
Jack Berg 00:23:53 Yeah, so at that point, we're just… we're just inconsistent. Or at this point, we're just inconsistent, because we have the sugar methods in some places, but not all.
Trask Stalnaker 00:24:06 I think that's where I… landed.
John Watson 00:24:09 Well, I mean, we have… is that… is the one on… the one on the attributes builder isn't sugar, like, you have to have that one, right?
Jack Berg 00:24:17 That's the same case where you can always use the attribute key, version instead of the one that accepts a string key.
John Watson 00:24:26 True, true.
Do… but do we have the… we don't have… Do we have on the… On the ones that Trask was adding to.
Do we have the key… the attribute key version?
Already?
Trask Stalnaker 00:24:41 Yes. Yes.
John Watson 00:24:44 Okay.
As I said, I'm not gonna… I'm not gonna stop it. I just wanted to make sure we… because I do have a recollection that we decided we didn't want to do it until we actually had demand, so… that… that's all.
Jack Berg 00:24:59 I'm leaning towards merging it, just because of this inconsistency problem. I think if we would have had the, the foresight, or, been scrutinizing enough to avoid this sugar method on Attribute Builder, then, you know, I could say, like, hey, we're gonna avoid this everywhere, but now we got a… we got a split brain thing, so… We kind of already… We're stuck. So… If you're… if you're neutral on it, John, and Trask, if you're still in favor of going forward with this, then I think we should go forward.
John Watson 00:25:38 Yeah, I mean, I'm… I'm neutral on this side.
It's more like, I just… I still think these are gonna be… these methods are gonna be really confusing for actual non-maintainer users to understand what the heck they're supposed to do with them.
So, I still feel that way.
That this is… this is kind of a weird, wide-open thing without a lot of guidance.
for end users about why you would want to use this under what circumstances. Like, throwing this completely, just throw a map in… essentially throw a map into the data.
So I still, I still feel like this is kind of a footgun in our API.
Trask Stalnaker 00:26:22 So, I can give you a little bit of context, around… in the semantic conventions.
John Watson 00:26:28 No, no, no, so Trask, it's not a semantic invention issue. It's a… users are going to see this API when they look at our Java docs and not know what to do with it and when they're supposed to use it.
not a, like, people who are really deep in the code… deep in the semantic conventions and understand why it's used won't know how to use it. It's for the rest of the world who are not deep in that, and are gonna see this method, and like, what the heck is this for? What is this value thing? Like, I just feel like it's a… it's a… it's the equivalent of having a method on your API that takes map Object, object.
Which is like, what do I do with this? Like, what's this for?
Jack Berg 00:27:11 app string object.
John Watson 00:27:13 Yeah, I mean, again, it's like, what do I use this thing for? It's really hard to understand how to… like, for someone who's not deep in the project.
to know what to do with that API.
Trask Stalnaker 00:27:27 Yeah, I guess what I was trying to get at with the Gen AI SemCon is, I mean, we… I mean, that is a… We have users who are, trying to emit GenAI, someConf-compliant data.
And, what we're doing there to help make it clearer is we're actually using JSON schema To define in semantic convention what that blob is supposed to look like.
To provide, sort of, some more guidance there.
I wonder if you…
John Watson 00:28:07 I wonder if there's something we could do in our Java doc on those API methods that are… potentially… not ones that people who aren't specifically working on… like, if I'm not working on that, and I do just code completion in my IDE, I'm like, what is this… what is this thing for? Like, I wonder if there's some… something we could do on the Java doc to make it clear that these are pretty specialized cases that you wouldn't want to.
Jack Berg 00:28:36 That's exactly what I was thinking, and I just sent a link in the chat, and I… because I was going through this Javadoc and looking for these warnings, because I know we had, like… we had thought about this thing before, John. Like, how can we help, you know, reduce the foot gun? And it's with Javadoc.
And, we only have it in one place, which is on the attribute key method.
If you… And that's not, like, quite good enough. So, like, maybe any place where we add these sugar methods, you know, the sugar methods, essentially, you're never exposed to this, this is the sort of comment that we need, right? Hey, use simple attributes whenever you can.
Right? That's what we want to convey to users. So, like, if we have the sugar methods, you know, duplicate this warning on all of them.
John Watson 00:29:26 Yeah.
Trask Stalnaker 00:29:27 That makes sense, because, yeah, we couldn't add it, really, to the… generic method.
Because it wasn't specific enough.
Jack Berg 00:29:38 Yeah, there's a typo here on line 75, so I'm gonna go fix that, too.
Returns an extended attribute key, yeah.
John Watson 00:29:47 Less a typo and just some copy-paste that didn't get corrected, yeah.
Jack Berg 00:29:50 Yeah.
John Watson 00:29:53 Okay, yeah, I mean, I'd be fine, that sounds good to me, at least it's a good start.
And if we get… we get reports and people of confused users, we can always… you know, increase the messaging from…
Trask Stalnaker 00:30:06 Size of… the font size of the, warning.
John Watson 00:30:09 Yeah, exactly. I wish you could do… can you do font? Like, you can put some rough HTML there, can you make, like, a… Extra font size attributes, style, put some style into the Java doc.
Cool, thanks.
Jack Berg 00:30:26 Cool.
Rasky's adding a comment.
Trask Stalnaker 00:30:34 Adding a comment to add a comment.
Jack Berg 00:30:37 Yeah, perfect.
Trask Stalnaker 00:30:41 Alright, next.
Jack Berg 00:30:44 Alright, so this is, this is something we talked about a while ago at this point, and it's about, like, splitting out or mitigating some of the confusion, some of the issues with OKHTTP, and the fact that we have a single OKHTTP sender module that effectively works with two different major versions of OKHTTP, and so it has this weird, sort of.
You know, dependency resolution issue where it can, you know.
give the impression that it's forcing, you know, libraries to upgrade from V4 to V5, even though it's not strictly necessary. Like, you can use… continue using V4 OKHTTP, even with this sender, which has a dependency on V5, and so… you know, how do we resolve? Well, we split apart our sender into a V4 copy and a V5 copy.
And what I do in this PR is I, I use Gradle build tooling to actually just create an exact copy of the code, so we don't have, like… because it really is the case that the same code works with V4 and V5, you know, I don't want to deal with the drift bit from maintaining two copies of the code, so we make this we embed the copying, task in the Gradle build itself. So, the only reason not to do this And I bring this up now because, you know, it looks like Gregor is poised to approve this, and so then it would… you know, I don't want to merge this, even with an approval, unless we talk about this, but this hasn't come up again.
like, since it came up a couple of months ago, there's been no follow-up on… on this PR or the related issues. So, like.
Is it actually urgent?
Or is it, like, fine, after we've sort of clarified more forcefully that this OKHTTP sender is, in fact, compatible with V4 and V5?
you know, another thought that I have, and I left this in the… the notes document is, like, maybe we do this pattern, but we just wait for OK HTTP v6. So, like.
you know, we sort of made a mistake with OKHTTP v5 by having a single artifact that tries to target multiple major versions, and whatever. That's water under the bridge now, but come V6, we do introduce a new V6 sender.
Trask Stalnaker 00:33:16 And leave… our OK TDP, our base artifact at V5?
Jack Berg 00:33:24 That's a question that we'd have to encounter as well. So, like, when a V6 comes out, what's our decision about what our default sender is?
I think people have different philosophies on this, whether you, like… do you pin to, like, the oldest version, which is known to be okay, or do you pin to the latest version? Where the latest version is, like, you know, guaranteed to be bleeding edge in terms of security updates and things like that, and the older version might be okay from a security update standpoint, but it might not. You just don't know.
So I tend towards pinning towards to the latest, not towards the oldest, but I know, for example, that maintainers in .NET, like, chose the opposite approach.
My old colleague, Alan West and I talked about this a lot, and how .NET, like, you know, will… for all their dependencies, they use the oldest dependency, which is known to be safe.
So, it's a different philosophy.
Lauri 00:34:27 How does it work currently, if you want to use a different sender?
You have to.
Jack Berg 00:34:34 Yeah, JDK1, you have to instruct Gradle to exclude OKHTTP sender and include a dependency on the JDK one.
Lauri 00:34:46 So…
Jack Berg 00:34:47 Or, or if you want both, and you just, like, you have to set a system property or environment variable to select which one to choose.
Lauri 00:34:56 So… If you… If you have multiple OK HTTP dependencies, then the user would need to exclude the default one and choose another one.
Which raises the question, like, why they can't just exclude the OK HTTP itself.
And, include whatever version they want.
Jack Berg 00:35:20 Exactly. That's what I was trying to articulate to the person who raised this issue a couple of months ago.
Lauri 00:35:26 I think there was some sort of, explanation that it's… Too hard for them to do because of… Some understandable reason.
Jack Berg 00:35:37 I think the only thing that this, this, this user would have been happy with were, like, really, truly happy with would have been, like, us pinning to OKHTTPv4.
as the default. And to me, that's just… that's a non-starter.
I'm not gonna pin to a dependency that, like, has had zero updates in, like, the last two and a half years, or whatever.
So…
Lauri 00:36:05 I think… I think the user should, like, work a bit harder for us to make that kind of, Changes for them.
I just continue using the OKHTP latest, whatever.
Unless the users can articulate some sort of reason why we should have a separate sender implementation.
And why, like, documenting that it actually works with older versions isn't enough for them?
Jack Berg 00:36:48 So I'm happy enough to, I guess, close this PR and keep this type of strategy in our pocket.
you know, come V6, or if there's additional feedback from users.
So… I just kind of want to reach a conclusion one way or the other.
Trask Stalnaker 00:37:15 Is it a non-starter to… Not have a transitive dependency To any of them, and force users to pick one.
Jack Berg 00:37:31 That's been in the back of my head. I think that's the one thing we haven't talked about.
So.
Lauri 00:37:40 Will that be a braking change?
Jack Berg 00:37:43 Well, it's a breaking change that we are allowed to do, or we've convinced ourselves that we're allowed to do.
In the past, we've done things that, like, despite stable artifacts, like, you know, we allow ourselves to require users to switch their artifact dependencies. We rename things, we'll split things up, we'll merge things, we'll delete artifacts, things like that.
So we've given ourselves some leeway in terms of What we're allowed to do from an artifact standpoint.
Trask Stalnaker 00:38:23 the ripple effect.
The number of people that that would affect.
That would need to go and add… an explicit dependency. I mean, we can give a nice Error message on startup.
Lauri 00:38:40 We aren't going to get any more… any new friends with that kind of change.
Only pure hate.
Jack Berg 00:38:53 Yeah, and it's… like, I think with, the thing that comes to mind is gRPC. gRPC Java forces you to choose your, like, your backing implementation, Netty or OKHTTP, or NetE shaded.
And, it's a similar thing there, but I think from the start, they had the foresight to, to force the user to select the one. Like, there's no default.
And, you know, we didn't. We built on top of OKHTTP from the start, when these modules were stable, and only later added the sender abstraction, because OKHTTP was insufficient in certain cases.
Lauri 00:39:37 Actually, did we? I thought we used, Netty, at least for gRPC.
Or maybe the gRPC library itself.
But, you know.
Trask Stalnaker 00:39:49 Yeah.
Lauri 00:39:49 depended on many.
Trask Stalnaker 00:39:51 Before we, hand-rolled everything.
Jack Berg 00:39:56 And before, like, so, yeah, my memory's kind of hazy, because at one point, there was only gRPC OTLP exporters, and then we added the HTTP variant as well.
And so I'm not sure if the OTLP exporter module was, like, stable before we added the HTTP variant.
Trask Stalnaker 00:40:19 Yeah, it may have been pre-1.0 days, I can't remember.
John Watson 00:40:28 I hope.
Trask Stalnaker 00:40:29 Yeah, it's good.
John Watson 00:40:30 I don't remember either.
Trask Stalnaker 00:40:32 I do like that, I mean, that pattern that GRPC does, I mean.
Feels like it would have some… At least it would be super explicit here about our one… Third-party dependency.
And would probably encourage more people to use the… throw in the JDK one.
But… I don't know how we… get there.
Jack Berg 00:41:01 We could add it to a list of to-dos for an SDK 2.0.
And, like, come that, you know, we just be sure to include this type of more, you know, impactful change.
Not that an SDK 2.0 is… is happening.
Trask Stalnaker 00:41:22 happening.
But… Yeah, never say never.
Jack Berg 00:41:27 Alright, I'm gonna close this, and in my closing message, I'll say that, like, I'll talk about, you know, the things that we discussed here today. So, more user feedback that this is important, be proactive about this pattern come OKHTTPv6, Consider requiring a sender to be explicitly set, in a 2.0, so… Oh, this one's fine. Oh, friend.
Trask Stalnaker 00:41:56 Yeah…
Jack Berg 00:41:58 Yeah, so, okay, so… What's, you wanna share?
You can share, but I can just, you know, frame this up, so… I… this PR improves the performance of metric record operations when there's contention.
But the additional, there's some, like, minor additional, like, tracking overhead that, slightly reduces the performance If there is no contention. For example, if you're recording these single-threaded or something like that. So, you know, like.
the thing that motivated this is I was hearing from Prometheus maintainers that open telemetry was way less performant than Prometheus Client Java. And I was like, I've done the benchmarks, it's not that different, I don't know what you're talking about.
And I went and found their benchmark in Prometheus Client Java, where they show this, and the Prometheus Client Java benchmark, it really indexes on the things that Prometheus Client Java excels at, which is bound instruments, which OpenTelemetry doesn't support, and high contention.
Right? So if you combine those two factors, Prometheus Client Java just, like, it blows open telemetry away. And, you know, So, you know, I argue that, you know, it's… it's… it's… it's not… the majority of metrics cases don't actually have those two conditions, where you… where, you know, you could get by with bound instruments, and where they actually are under high contention, but, you know.
The point stands, which is, like, for the most performance-sensitive applications, Contention is likely.
And, you know, the bound instruments is likely, and I'm trying to solve bound instruments separately from this, but, Yeah, so, like, in my head, I am willing to tolerate a slight reduction in performance in single-threaded in exchange for higher performance under contention.
John Watson 00:44:13 So I'm gonna throw a crazy idea out there, I have no idea if it's possible. Is it possible to dynamically switch if we detect contention? Can we detect contention and switch our… are locking modes.
Jack Berg 00:44:27 Yeah.
We could have some heuristics in place, we could track whether, like, the lock was held, we could… we could do some fancy stuff that, you know, increased the complexity and, and also made it more difficult to benchmark deterministically, but…
Trask Stalnaker 00:44:46 Tuned to the benchmark, yeah.
John Watson 00:44:48 No, for sure. I mean, one of the things that I think Maybe I… maybe I'm the only one who has had this in my head.
is that OpenTelemetry, the default SDK, The intention is not to solve every use case in the world.
Like, there are going to be… super ultra-high-performance real-time applications that just should not be using OpenTelemetry, or not using the default SDK.
And we… because you can't solve, like, I think trying to solve every possible Use case, and every possible… way that someone might decide to use it is going to be… it's going to be tilting at windmills. Like, we're never going to be able to win that game.
So… I wonder if… And maybe, like, a third… a third way is… Maybe have two implementations, and if a user… like, like we do with the memory, like the, the memory performance mode, where you can reuse the memory… the memory structures, like, maybe do some… something similar here.
Where you could turn on high-performance high contention mode.
But it's not what's used by default.
Jack Berg 00:46:06 The Go folks have had some interesting thoughts here. Tyler Jan was, he was, like, really unhappy with this language and the specification that talks about how, like, you know, APIs have to be concurrent safe.
And he's like, why? Like, sure, like, a concurrent safe metrics API should be the default, but, like, if you know that your application doesn't need that concurrent safety, then you're going to pay some additional overhead for that coordination.
And it should be possible, and maybe desirable, to have an implementation of the Metrics API that doesn't have any concurrency guarantees, and reaps, like, performance benefits as a result.
And, yeah, I was thinking about that type of thing. Like, that's kind of a different version of what you're saying. You know, you could take it in a couple of directions. You could have a different implementation of the metrics API, which gave up that safety.
Or you could do something, like, where you can, like, an advisory parameter type of thing, where, like, we could have an API where you are instructing or giving a hint to the SDK that, like, hey, you're going to take, concurrency guarantees into your own hands, like, and, you know, go on a fast path that gives up all of this locking.
Or whatever, the techniques that we use to guarantee safety under concurrency.
And, you know, as for your other comment about, like, you know, the OpenTelemptra APIs aren't suitable for all applications, like, I agree.
But I want the set of applications for which OpenTelemetry APIs are not suitable to be, like, as small as we can reasonably achieve.
John Watson 00:47:58 Sure, of course, of course.
Jack Berg 00:48:00 And with reasonably achieve is where we get subjective. Part of me thinks that, like, maintaining heuristics and, like, stats within the metrics SDK to, like, choose one path or the other is outside of that reasonability clause.
John Watson 00:48:19 Boom.
Jack Berg 00:48:19 getting unreasonable.
John Watson 00:48:21 So this particular… I mean, there's a lot of data in this benchmark. So, let's say I was a user who knew I had a… Who had already optimized my application to make sure my metric recording was single-threaded?
How much pain would I feel with this change?
And I was, like, a high throughput, and I… I shunted all of my metric reportings into a separate thread specifically to work around this contention issue.
Jack Berg 00:48:52 It depends on your case, and so the… it depends on your, The instrument type you're using, counter or histogram, are, like, engage are, like, the most important things. Temporality, cumulative or delta, we have different code paths for those already, because they have different tracking requirements. And… I think those are the main things that would impact it.
So, like, the examples at the top are… are…
Trask Stalnaker 00:49:24 But we're…
Jack Berg 00:49:25 For the worst.
Trask Stalnaker 00:49:25 Whereas.
Jack Berg 00:49:26 Exactly, so 40% reduction in throughput.
But if you go down, you get some really awesome improvements on the concurrence and the contention side. So, trade-offs.
John Watson 00:49:42 Yeah, because I'd hate to get this merged and then… get a bunch of complaints from those users who had… who want… really want to use OpenTelemetry and have worked really hard to make it work for them.
And then we would just… Make it… make their lives less pleasant.
Where they'd have to go and undo all of their optimizations.
That's my… I mean, I think that's kind of my main concern.
how… I haven't looked at this PR at all. There's not very many lines of code. How difficult would it be to have this be, System property option to flip over to.
Jack Berg 00:50:23 That would be quite easy.
And maybe we do something that's the opposite, like, maybe, Maybe we, like… so, back when we were introducing the… The custom exception, stack trace resolver that was more performant. You know, I was tossing around the idea of, like, I think we did do this, like, you could, By default, the SDK used this new FastPath that I implemented, but you could set me a system property to revert back to the old JDK one in, like, if you really ran into an unknown, unknown issue. And we could do something like that here, where it's like, by default, we prioritize this new change, which improves behavior under contention, but you can revert back to.
You know, the old behavior, if you wanted to.
If you wanted to… if you, for some reason, knew ahead of time that you don't need concurrent safety.
And maybe that property could, like, you know, grow over time in terms of, like, what it does from, like.
because if you really do want to guarantee that you're… if you can make the guarantee as a caller that, like, you don't need this concurrent safety, we can get rid of a lot of overhead. Like, we can really, really improve the speed of these things.
Trask Stalnaker 00:51:52 I don't… I want to be really clear here that this is about contention, not about concurrency.
Jack Berg 00:52:01 Yes.
Aye.
those words interchangeably, but I understand your point.
Trask Stalnaker 00:52:08 Yeah, because concurrent applications like, that is just the de facto stand, I mean, in Java world. I don't really see much point in a non… thread-safe metric API for Java.
If you need something like that, Build it yourself.
Jack Berg 00:52:35 Concurrent recording to the same series is the contention that we're talking about here.
So, like, that… like, the contention is, like, a subset of concurrency. It's like, you know, yes, we're operating in a concurrent situation, but it only matters when you're concurrently recording the same series. That's when you get contention.
Trask Stalnaker 00:52:55 Yeah, so it's gotta be, you know, like, in this… in the… this benchmark, right? You have 4 threads That all that those four threads are doing is hammering on this one single Or a little metric instrument.
Like, not even, like… in your application, you may be emitting, you know, 50 metrics. You've got 4 threads all completely hammering on one poor little metric.
So… I… I… at the same time, and I don't… I don't love, like… Being like, oh, well, there's some external benchmark that, you know, we want to improve on, even if we're not Sure, like, the real… realisticness of it.
And if it's going to be a net benefit for… many of our users. At the same time, you know, I do… I would be okay with the change, I think… That those kinds of benchmarks and that kind of perception is something that's important.
has its own value, and I… I… I don't want to… It's more work to try to explain, like, some… why maybe it's not the same versus trying to just conform to the… External benchmark, and be like, oh yes, more performance under more contention is… is good.
Yeah. So…
Jack Berg 00:54:43 You kind of hit the nail on the head with how I'm thinking about this, so, I…
Trask Stalnaker 00:54:49 I… I mean, I left… I left the… I left a comment a while ago, That, you know, I… Wasn't super thrilled with it.
But, I would… I, I, I would… Give it the… Stamp of approval, just… For that sake.
Jack Berg 00:55:14 Yeah.
it's like… but I don't think the story ends here. You know, this is… I view this as, like, a temporary… trade, like, I think we're kind of probably under-indexing on contention.
And… like.
Trask Stalnaker 00:55:35 Would be nice to be… see the two threads here.
Jack Berg 00:55:39 Okay, yeah, I can definitely do that.
Trask Stalnaker 00:55:43 Cause I'm kind of curious, Yeah. The other… the other thing that would be interesting, I think, would be, because there is… Like, if you had 4 threads, but they're not hammering on the metric, but they are 4 different threads… Doing a certain number of operations per second.
There's… That could still…
Jack Berg 00:56:13 Exhibit 100.
That's, like, the 100 values. That means the 4 threads are distributing their activities amongst 100 different series.
Trask Stalnaker 00:56:22 Oh… oh, that helps me. I didn't catch that.
Jack Berg 00:56:27 So, it's like, that's sort of simulating your two-threads situation a little bit. It's, like, some contention, but not all the contention.
Trask Stalnaker 00:56:36 Wow, and that's really this… much improvement there.
Jack Berg 00:56:43 I definitely did not type these numbers in myself, so I had a computer calculate them.
John Watson 00:56:51 You know, one thing that's, you know, and we're almost out of time, we're out of time.
But the thing that always gets me with this kind of benchmarking is that the real… almost every… not every, but almost every real-world application, this is going to be noise in the overall, overhead that's going on in their application. Like, you make one database call.
In your stack, and it's going to be a thousand times more than any of one of these metric recordings.
Jack Berg 00:57:23 I mean, even the… even the overhead for, you know, request response is just, like, yeah, 1000X.
John Watson 00:57:28 Yeah, exactly. So this, I mean, in a lot… in a lot of ways, this is kind of… in almost every case, this is just silly. Like, we're optimizing something that doesn't matter to anyone except someone who cares about benchmarks.
Jack Berg 00:57:40 But people talk about it at the spec so much. They talk about, like, nanosecond performance.
John Watson 00:57:46 I mean, there are use cases out there.
Jack Berg 00:57:48 Yeah.
John Watson 00:57:49 But that's… this is where I'm saying, like, should we be solving those use cases?
I… I… like, I don't know. It just doesn't seem like it's that important to me, but…
Trask Stalnaker 00:58:02 The… I would be interested in… Your theories for why… This… the 100 has similar…
Jack Berg 00:58:18 Yeah, I have a theory about that. Like, why is it not as pronounced of an improvement versus the Delta?
Where Delta is getting, like, 300-400% increase.
Trask Stalnaker 00:58:30 Sorry, no, I'm okay with that difference. The difference that I don't really… Understand is the 1 to 100… Here, and they're kind of… they're pretty similar.
Improvements.
And I would have thought, with it being distributed across a hundred different time series, like, is there a lock on… is there any kind of locking on the instrument itself versus the time series?
Jack Berg 00:59:03 Yeah, so there… there's locking at both levels, So, and it depends on whether we're talking about cumulative or delta. So, for delta, you have to lock at the… not lock, but you have to do coordination overhead at the instrument level, and then down at the time series level.
For cumulative, you only need to… Do coordination down at the instrument.
food.
you have to do, like, a minor amount of coordination at the instrument level, but most of the coordination is down at the, the time series level. So, like, you know, if you look at, for example, the…
Trask Stalnaker 00:59:46 Right, so…
Jack Berg 00:59:47 Okay.
Trask Stalnaker 00:59:48 Why… yeah, so why is it… why is this one getting such good benefit from your… optimization… If the… because these ones shouldn't be seen nearly as much contention at the time series level.
Jack Berg 01:00:11 Yeah.
Well, not as much as the 1, right, as when the cardinality is 1, and there's still 4 threads.
Right.
Trask Stalnaker 01:00:21 But the improvement seems to be about the same between.
Jack Berg 01:00:27 So there is…
Trask Stalnaker 01:00:27 100.
Jack Berg 01:00:28 There is variance, and we've talked separately about, like, looking at the visualization of the metrics benchmarks over time. Like, we're not happy with, like, the variance. There's too much. So, like, some way, shape, or form, we gotta dial that in. So, but, you know, I can take that offline and investigate this a little bit.
I have some ideas, I just don't.
Trask Stalnaker 01:00:51 Yeah, I'll ping.
Jack Berg 01:00:52 how to turn.
Trask Stalnaker 01:00:53 Yeah, I'll ping you in chat, I have one other… thing I'm kind of interested in seeing.
Jack Berg 01:00:58 Okay.
Trask Stalnaker 01:00:59 But yeah, this helped. Thanks for bringing it up.
Jack Berg 01:01:02 Yeah. Pranav, you have an item on the agenda we didn't make it to. Let's… let's follow up with that async. I'm sorry we didn't get to it.
Pranav Sharma 01:01:12 No worries, sure, thanks. I just had a couple of quick questions, actually, regarding the expected behavior, for exporting the batches.
So, actually, just, like, if you have a batch of metrics that require 10 export calls, depending on your batch size, how should those calls be scheduled? Like, should they be asynchronous, or should I wait for each call to finish before starting the next one?
Jack Berg 01:01:39 I have answers for you, but we have to call time.
Trask Stalnaker 01:01:41 Yeah, and this is not an easy question, and I think Jack and I may disagree on the answer.
Pranav Sharma 01:01:47 Okay, got it. I'd be happy to discuss it again, or on Slack.
Jack Berg 01:01:51 Slack, please.
Pranav Sharma 01:01:52 Alright. Thank you.
Jack Berg 01:01:53 Bye.
