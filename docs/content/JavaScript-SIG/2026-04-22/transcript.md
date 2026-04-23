SIG: JavaScript SIG
Date: 2026-04-22
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Trent Mick** 01:09 Ew.
**Marylia Gutierrez** 01:13 Oh.
**Marc Pichler (Dynatrace)** 01:42 Hello?
I'll tag my own name today.
**Trent Mick** 02:31 I was just gonna say, I'm glad I'm not the only one.
**Marc Pichler (Dynatrace)** 02:39 Alright, let's jump right into it. Trent, do you want to get started?
**Trent Mick** 02:46 Sure, so there's a PR that came in for someone requesting That it be possible to opt in to turning on host metrics collection?
In Auto Instrumentation's note, I think, if you want to open that issue.
Then… so that one is proposing using an environment variable to opt-in, which would have always been the way before, but now is not the way, because… whatever, Disney quotes, I can't… quote the Mandalorian properly, but… The… That's not the way anymore, but there isn't a way in declarative config to really do this kind of thing. Marillie had started a review saying, you know, like, this would work if it were in instrumentation, but it's not currently.
So, a few things on there that soliciting opinions on. Would people be opposed to re… Jiggering the host metrics package to be instrumentation host metrics, because… I think it's not in instrumentation only by accident, because back in the day, the only instrumentations were tracing-based, and this is the first one that did metrics.
That's first question. Second question is… I guess I'd reverse, that was the second one that I had on there. The first one is, my understanding, and I'd welcome other people's understandings, is that… The general opinion in OpenTelemetry is that thou shalt, or thou should, not shalt, Prefer to use a… OpenTelemetry Collector, and… running as agent, I'm not even sure if in config, that's in separate mode or anything, or… and using the host metrics receiver is the way to collect host metrics, rather than having language-specific SDKs do that for various reasons.
Would people object to putting language in the README for host metrics on that?
Pointing to… I'm not sure what documentations show that as kind of a preference. There are some… blog posts out there that I've seen, but nothing, I think, from OpenTelemetry that really kicks that one in. I've just heard that in various conversations.
And then the third question is, would people object if we did the previous two of… adding host metrics to Auto Instrumentation's node, but having it off by default.
I have my own preferences here, but…
**Marc Pichler (Dynatrace)** 05:27 I'll give a short answer. I… I have no objections to all of these. I think all of these are sensible.
the… collector, for host metrics, I think that's… I have the feeling that that is the generally recommended way of going about things.
And it's also the way that… At Dynatrace, we recommend people use Or obtain host metrics is via the collector.
So… There's that. Also, the instrumentation interface not being used, I think, was… Somewhat done, because it was the first one… the first instrumentation that Collected metrics, and also the person that owned that component didn't want to use the instrumentation Interface for some reason.
I'm not sure… If the reason back then was because metrics weren't Ready yet, or if there was another reason for it.
But they were kind of opposed, I seem to remember.
to using that. If they're on board with it now, I don't see any reason why we wouldn't be able to switch that over. We can also just use the interface, and not… Pull in the abstract instrumentation there at all, because it's so lightweight.
What it does, I think, if we just… Implement the stuff there, enable and disable, we should be fine.
And spinning…
**Trent Mick** 07:17 Sorry, go ahead. Legenicus is listed as the maintainer of Phosometrics, so… I'm assuming he's not…
**Marc Pichler (Dynatrace)** 07:24 Maybe. Who you met.
**Trent Mick** 07:25 It says, opposed, initially.
**Marc Pichler (Dynatrace)** 07:28 then I might be mixing that up with something else. Might be the…
**Daniel Dyla (Dynatrace)** 07:37 I think it was, Obeckney, originally.
**Marc Pichler (Dynatrace)** 07:45 I seem to remember some instrumentation. Maybe I'm just mixing that up with something else. Then I guess we can disregard, I guess.
**Trent Mick** 07:57 Oh, Beckney was the original author.
Of the package, yeah.
Okay, sorry, and then I cut you off, you were still speaking.
**Marc Pichler (Dynatrace)** 08:08 Yeah, the last part was about the auto-instrumentations node. I think auth by default makes sense, given that Like, if we all agree that, the collector is the way to go, then I think we should have it off by default.
**Trent Mick** 08:28 Also, I've seen reports of… performance concerns with the host metrics. The package it's using under the hood, when it's… all the metrics are enabled, there can be some… performance gremlins.
I wasn't able to… so I got… I work an issue on that one. I wasn't able to reproduce it, though, so it could be tied to specific… Hardy machine situations, so…
**Marc Pichler (Dynatrace)** 08:55 Beautiful.
**Trent Mick** 08:55 would be scary to turn on by default everywhere, I think.
**Marc Pichler (Dynatrace)** 09:00 I don't exactly record how these work. Are they observable instruments, or are they just… Yeah, they're mostly observatory instruments here.
I suppose that might be happening when there's a collection cycle that's rather short, so if it collects the metrics quite often, then that could get expensive there.
But I think with the concerns that, there's… Some problems with performance, and also the concerns that the… collector would be the better way to go about it. I think it makes sense to have it off by default there.
**Trent Mick** 09:57 Okay, great.
**Marylia Gutierrez** 09:58 Yeah, so what… yeah, what I was thinking when I saw that, yeah, kind of, like, similar, so yeah, I don't see why not to put on the instrumentation, but this way I put a comment, like, I think it might probably be, like, off by default because of performance issues, transforming that into instrumentation.
I think makes sense, to the point that I actually did not realize it was not instrumentation, because in my head, it makes sense to beat one, so this is why all my comments were like, yeah, you just have to add this, because that is an instrumentation, so… hearing, like, from translator, there was not. I was like, oh, wait, and then I had to, like, backtrack and look again. So yeah, makes sense. For the collector part, yeah, I don't know too much about this, so I know that a lot of… we are getting a lot of requests in general, because talking about, like, the injector and stuff like that, I don't know if you necessarily use the collector, and a lot of people are using, like, just auto-instrumentation as is. So this is why I wanted to have that option for them, yeah, as long as they can use with the auto-instrumentation. I don't know how the collector fit on that part.
But if it is, like, recommendation, it's always good to have, like, documentation about it.
So, yeah, that is what I was thinking.
**Trent Mick** 11:16 Yeah, I don't think OTEL Project, as far as I know, has a position on that, but it's… Seems to be.
Like, if you want… if you're operating multiple languages services, as far as I know, some of the other languages don't have a host metrics instrumentation. It's because they're expecting people would use the collector for that, so yeah.
**Jamie Danielson** 11:35 There is… yeah, I was remembering this conversation coming up a while ago, like, there's this old issue in SEMConf that was, like, guidance needed, process versus system versus container versus Kate vs. front. The whole thing was exactly that, like, there's… different languages have host metrics of some kind, like.
NET, us, and Go. But generally, it was discussed having having that from, like, the collector level or, like, a single level versus each language having their own thing is generally ideal, and so I think that is… the recommendation… I was trying to find where, like, a recommendation actually lives, that's a really long issue.
But I think that is sort of the recommendation, is to… Have that off and rely on the collector for those metrics.
**Trent Mick** 12:24 Okay, cool.
**Marc Pichler (Dynatrace)** 12:27 I think one of the things that you run into with these host metrics It's also that, like, if you turn the instrumentation on.
and you're running in a container somewhere, or… I don't know.
Like, if you run it on not a host, necessarily, or, like, a bare metal machine, or a virtual machine, or anything.
Then the metrics might make less sense, because the, like, how much CPU you use, if you have a container with, like.
Half a core assigned or something, then, it looks weird.
Maybe.
**Jamie Danielson** 13:13 Maybe it's misleading.
**Marc Pichler (Dynatrace)** 13:20 I think that's also the reason why, The collector might be a better way to go about it.
**Trent Mick** 13:30 Great.
**Marc Pichler (Dynatrace)** 13:34 I wonder, should we maybe have some, or look into having some page on OpenTelemetry I.O. to recommend how to Set up.
Dead.
I… I just know that it's fairly simple to set up. We… at Dynatrace, just have, like, one example collector config that we recommend people use.
And… That is… fairly simple to configure, as always in the public… in our public talks, so if we could… move.
stuff like that over to, OpenTelemetry I.O. could also be helpful, maybe.
**Jamie Danielson** 14:17 We do have, like, there's, like, an example, like, for receivers, and the collector shows host metrics in there, but I don't know that it's very, opinionated, per se. Like, there could be… Something in there that says here's, like, a recommended… Way of doing this.
**Marylia Gutierrez** 14:38 Yeah, there's, like, two ways that we can go about it. One is, like, if this is a specific case for JavaScript that we want to show, like, if you're using JavaScript, this is… then you can go, like, to the JavaScript page and add, if it is, like, a short example, makes sense to put there. If it is something, like, bigger, we can also use blueprints.
Don't know if you guys are aware of the Blueprints. So, Blueprints is another project from Hotel that is… because a lot of people that want to use OTEL, they're like, I have this… set up, and I don't know how to start with hotel. So, we have this SIG that is about, like, creating, like, those blueprints, like, things that you should be setting up, this is, like, examples of configurations.
the… how to, like, connect your collector or whatever, things like that. So it's a very recent project, but if you have idea of, like, examples of things that people are asking, those are being added as blueprints, and they would be part of the .io.
Right now, they are only on the, like, GitHub, yeah. And then we're just gonna keep adding there.
Meetings happen every other Monday, in case anyone wants to join.
**Marc Pichler (Dynatrace)** 15:54 Puts on.
**Trent Mick** 15:55 So I… I think I could… I mean, I'll follow up on the host metric specific… the JS package thing, but I think to the README, I can… in the README, I could point to the… that receivers link that… that Jamie posted.
Which does show an example of using the host metrics receiver there, so…
**Jamie Danielson** 16:12 What is the name of the… SIG, Merlia, that you were talking about?
**Marylia Gutierrez** 16:17 So it's gonna be on the end user, so they do…
**Jamie Danielson** 16:20 Oh!
**Marylia Gutierrez** 16:21 Because they do one-week end user, one-week blueprints, because it's the same group of people.
**Jamie Danielson** 16:26 Okay, gotcha.
**Marylia Gutierrez** 16:29 So the end user happened on Thursdays, and then the blueprint happened on Mondays.
**Jamie Danielson** 16:35 Oh, I see it now, end users say go tell blueprints.
**Marylia Gutierrez** 16:38 Yes.
**Marc Pichler (Dynatrace)** 16:45 Yeah, I guess so we could link to that one, first.
And then if something more specific comes up that, just deals with, post metrics, then we could just change the link. I think that's it.
Good way to go about it.
Alright.
**Trent Mick** 17:15 So, to be clear, I would… I would probably propose having a new package called Instrumentation Host Metrics instead of keeping the same package name. I don't know if people would impose that. And then we'd end-of-life the Host Metrics package.
Because how it's used would change.
Next people are quoted. Okay, cool.
**Marc Pichler (Dynatrace)** 17:40 Alright.
Anything, Any questions or comments?
If not, then we can move on to the next one. This is about…
**Trent Mick** 18:01 Right, so SDK metrics are a thing in the spec, in development status, for the SDK to produce metrics on itself, so, there are a bunch of metrics there so that you can… monitor how the SDK is doing. For example, if it's dropping spans or whatever, and it's exporter, those kind of things. There are a couple PRs that have been merged for exporting some of those metrics, and there are 3 or 4 PRs that are currently open in review for doing that.
In review of the first one, there was this discussion… oh, no, sorry, this is… after the fact, the thing that's motivating this discussion. But, so in the current usage, so using the Node SDK class.
in the SDK node package.
there's an environment variable to opt in to getting these SDK metrics. The question is whether we want to do that.
Have an opt-in, or just have them on by default.
In what would Java do, they just have them on by default.
And, Anorag, who's the author of all these PRs, who had added the support in Java, I think he did… added the Java support. His answer was that people can use a view to turn off those metrics if they don't want to. So I guess we could change our docs showing this opt-in to, say, like.
you've now been opted in, and how to opt out, and give them a view example on how to turn them all off. It's pretty straightforward.
The reason this comes up now is because we're… doing the parallel work for the start node SDK, alternative way to start the SDK, which is part of the declarative config work.
And the question there is.
We don't do environment variables anymore, so there wouldn't be an easy opt-out, and there's no place currently in the declarative config schema to opt-in to something like that. This is a general concern that comes up from time to time, so there's that general question. But the easy way to move forward on this path would be to just turn on SDK metrics, if people are cool with that.
By default.
**Marylia Gutierrez** 20:10 Because my… my thinking here was the person has to pass that configuration. If they are not passing, it's not going to get initialized. If they are passing, it means they want it, so if they want it, we are putting… so that is kind of, like, what I… when I… I put it, like, I prefer the option to adjust accept, and don't have the extra step of opt-in. And if they still have the config, but they still don't want it, then they can, yeah, filter out. That was my… My idea.
**Jamie Danielson** 20:44 So, I think… I guess there's… right, there's a few pieces to it. I remember when Java changed to Opt… out, at some point, because suddenly I was getting, you know, a million metrics, JVM metrics, that I didn't expect, and I learned… I think it was maybe, like, a spec decision of turning all these things on by default once they were stable, like, traces, metrics, logs are special, I don't know.
And so I think, like, at some point, we probably were supposed to have it changed to be opt-out versus opt-in, like what Java did, for regular SDK. But then when it comes to declarative config.
everything declarative config is supposed to be explicitly opt-in, right? So, like, the whole.
**Trent Mick** 21:28 Interesting.
**Jamie Danielson** 21:29 what you get, you don't get anything without… Yeah, ish. There's… there's… nothing's… yeah. But I feel like this is one of the bigger ones that is intended to be… opt-in, right? Or is it because it's a meter provider, and it's fine because if there's no actual… Metrics being generated, then it's kind of a no-opt, aside from the setup.
**Marc Pichler (Dynatrace)** 21:53 So I think this is a bit confusing, because the… Back here is actually the… Though.
these are the metrics that, like, for example, the trace SDK would emit.
Based on its internal state.
And that doesn't have a setting.
in declarative config. So, you would still configure your… metrics.
your, your meter provider.
But you wouldn't get any… Self-monitoring metrics were dead.
And with the opt-in, you would get It's very difficult to describe without actually showing where the data goes to.
So…
**Trent Mick** 22:50 So the… okay, yeah, the… it is confusing. The… the combined ideas that aren't fully well-formed in OTEL for one declarative config, this idea of what you see is what you get, and also this kind of developing idea, but I'm not sure where it's going, so I don't follow that closely, of stable only by default.
And… I don't know, de facto stable things that have been in… development status for years kind of thing. It makes the whole thing kind of confusing. It's not… I don't think there's… I'm not aware of a clear path chart. If people know specifically on SDK metrics whether there's a problem there, I don't know. So, on the what you see is what you get. If you're doing declarative config, the idea… The argument in this debate in favor of turning on SDK metrics by default is that you have explicitly configured a tracer provider and explicitly configured a meter provider. Should that mean that your meter provider is gonna get metrics about how the tracer provider is functioning and how the meter provider is functioning, or not. Should that be a separate opt-in?
**Jamie Danielson** 24:04 That should be a separate opt-in.
**Trent Mick** 24:06 You think it should be? There is nothing to find in the… there's nowhere in the… declarative config schema to put a Boolean for that.
**Jamie Danielson** 24:17 Is that a missing thing from declarative config schema that should be considered for… being added. Like, I guess I have in my head the idea being that as we add or change any kind of configuration options anywhere, the idea is to have declarative config in mind alongside it. So, like… Avoiding adding one without the other.
And if there isn't currently… like, Java has a way to do all kinds of shenanigans with views and stuff.
Right, even if it's not specifically spec'd out yet in config, declarative config?
Is it a matter of… speccing that out. I haven't been looking at declarative config in a little while.
But is that mainly, like, you would be able to get rid of it with views?
Or opt.
**Trent Mick** 25:11 So if you turn it on by default, there's existing declarative config schema for Configuring a view that could filter those out.
There's no way to have a view, say.
Oh, hey, by the way, I explicitly want these ones, and then go kind of infer that from the… you can't have the tracer provider go look at the meter provider view config to look for a positive signal that, yes, I do want you to Start collecting metrics about dropped spans.
**Jamie Danielson** 25:44 Like, it seems to me like it's a question more for declarative config.
that we then follow. Kind of the idea of, like, spec needs to make a decision, and we can then implement it.
Like, I don't think it's a JavaScript-specific thing, is it?
I mean, for us right now it is, but if other languages had something similar.
**Trent Mick** 26:05 So, okay, one could totally go that route. We could say, okay, we gotta go back to the configuration spec, and we need a Boolean on the tracer provider config for enable STQ metrics or not.
from the tracer provider. Same on the meter provider, same on the logger provider, whether you want those things to generate metrics. And if so, then obviously meter… the meter provider that is configured in that same config is used as the Place to send those metrics.
**Jamie Danielson** 26:36 How does Collector do it?
**Trent Mick** 26:38 option.
**Jamie Danielson** 26:39 The collector has in the collector config a service a separate thing from your regular trace meter logger pipelines, you can emit your own telemetry about the collector. And I know the collector uses declarative config.
And so I'm wondering… how those things intertwine. Also, I think I interrupted you while you were about to give another.
**Trent Mick** 27:04 No, that's cool, I'll just keep talking, but… Yeah, I don't know on the collector thing, I don't know anything about it. Does it use… it uses a totally separate… No, I guess it has…
**Jamie Danielson** 27:15 He uses the gun.
**Trent Mick** 27:16 itself, so it uses the same declarative config schema.
**Jamie Danielson** 27:20 Yeah, it uses the declarative… the Go declarative config implementation.
And I know that Collector has its own separate thing for self-metrics and… stuff.
So I guess the question would be how…
**Trent Mick** 27:35 Wouldn't be…
**Jamie Danielson** 27:36 arc.
**Marc Pichler (Dynatrace)** 27:38 wouldn't it…
**Trent Mick** 27:39 take… Anyway, sorry, go ahead, if you actually know. I'm just guessing it's on by default, but I don't know that.
**Marc Pichler (Dynatrace)** 27:46 If I recall correctly, it's just a separate receiver.
so, the… I probably don't remember correctly, but… Yeah, we can… we can check another time, I guess.
**Jamie Danielson** 28:09 Yes.
**Trent Mick** 28:11 Okay.
**Jamie Danielson** 28:15 That's something…
**Trent Mick** 28:16 Okay, so lacking a way to do anything, the… so if… if we decide we want to be… not enabling this by T. So, I guess, sorry, to continue on the… we could do that as one side of the debate, and that we want Say we're arguing that we want to have an opt-in for this through declarative config.
Hmm, if… So, okay, two questions. First question, Jamie, if the SDK metric spec right now were stable.
would you… think we would want an opt-in still for the extra SDK metrics being collected?
**Jamie Danielson** 28:58 For… declarative config?
**Trent Mick** 29:02 Well, I mean, whether it's through declarative config or not is, I think, secondary, right? My issue right now is, like, we had an opt-in, but there's no way to specify the declarative config, so let's go back and talk about whether we want an opt-in or not. If the SDK metrics Semantic conventions were stable right now.
would we even have this debate? We would just say they're on by default. So when you're using an SDK, and if there's a meter provider, then you're gonna get metrics about SDK's own internal functioning.
**Jamie Danielson** 29:33 Unless you're using a declarative config? This is the part that I… sorry. This is the.
**Trent Mick** 29:39 Weather, generally.
**Jamie Danielson** 29:40 With or without declarative conflict.
**Trent Mick** 29:42 UC is what you get.
**Jamie Danielson** 29:43 Yeah, because my understanding is that is very specifically.
**Trent Mick** 29:48 Oops.
**Jamie Danielson** 29:49 like, that is intentional of… you have to have all the shenanigans in your YAML file, which is very much the opposite of what we'd been doing, like, SDK Node, right, is, like.
Or any other agent, or whatever other.
**Trent Mick** 30:04 It's all the providers.
Yeah, by default, yeah.
**Jamie Danielson** 30:07 Yeah, and config is very explicitly the opposite.
**Trent Mick** 30:13 And to me, it's, like, kind of explicitly the opposite. If I say, tracer provider, yes please.
I get all the defaults. There are a bunch of defaults that are applied, right? I do… yes, I have to opt in to a tracer provider by putting a tracer provider colon.
in my thing, but there's a… there's a… oh, and a… and an exporter. You have to specify a kind of exporter. That's the minimal thing, right? But after that, you get… you get defaults for what the batch size is, and what the timeout is, and other stuff. So, like, there are some implied things by turning this thing on. Whether that extends to SDK metrics is another thing, because it does imply more telemetry coming out.
So, I don't know.
**Jamie Danielson** 30:56 Yeah, because I know this had come up, again, I haven't been in it in a little bit, and Marie, I know you were very involved, I don't know if you're aware of this. One of the questions that had come up was… like, re… like, propagation, for example, like, all SDKs in OpenTelemetry included, like, W3C and trace, you know, trace.
**Trent Mick** 31:16 package.
**Jamie Danielson** 31:17 baggage, right? And that was not the case with configuration, because… again, you had to explicitly say it. And that… that to me is kind of the same… The same sort of concept as these specifics for, like.
SDK metrics and enabling some kind of recording mechanism. Like, having a batch size That's on by default if you've… gone as far as saying, here's the exporter that I want.
is one thing, but saying, yes, I want to have the default metrics stuff if there was a default something, but that doesn't mean emit more telemetry on my behalf unless I… tell you I want it.
I think I'm walking in a circle.
**Trent Mick** 32:06 No, you just made me realize I actually have to go turn on propagators in my declarative config.
**Jamie Danielson** 32:10 Yes, that's a thing.
**Trent Mick** 32:11 It strikes me as breathing.
**Jamie Danielson** 32:12 guns.
**Trent Mick** 32:13 insane, but I hate YAML, so…
**Jamie Danielson** 32:15 Foot gun.
**Trent Mick** 32:15 why not hit myself a little bit more? Wow. Okay.
**Jamie Danielson** 32:19 This escalated quickly.
**Trent Mick** 32:21 Yeah, sorry.
**Marylia Gutierrez** 32:24 Deep breath, deep breaths.
**Trent Mick** 32:29 Wha…
**Jamie Danielson** 32:30 Yeah, that's why we… and that's why it went back and forth, is like, well, we've always had these propagators by default, so maybe we should just keep them. But then it was like, well, how do you choose what you keep and what you don't? What you opt into and what you don't? By saying you have to opt into everything.
Then at least it's consistent.
**Trent Mick** 32:50 Well, can I throw another one at you, then?
**Jamie Danielson** 32:52 Yes.
**Trent Mick** 32:53 And this is just for fun of the debate, this is not a challenge at all. Log level in the… Declarative config has… its default behavior is defined as info is used.
Which is not the default behavior for SDK node right now. Our SDK node. Because ours is, like, do nothing, be totally silent, which is… Which isn't great, but… yeah. Yeah.
**Jamie Danielson** 33:17 You know, that's a thing that I definitely struggled with a lot when working on the declarative config stuff, is it… is very much the opposite of what most SDKs do by default.
Like, we're not the only ones. It very much is changing the default behavior compared to what we have in SDK Node.
For many things.
Which is where the, like, the blueprints or the idea of, here's your starter file, pretty much everyone should start with this at minimum. There's, like, the minimum recommended, which is, like, your, you know, tracer, meter, logger.
You know, providers, exporters, propagators.
Start there and then expand.
**Trent Mick** 34:05 Okay, is there an… I guess I can open an issue on OpenTelemetry Config.
configuration, sorry. Is that the best place to ask, or is there some SIG I should…
**Marylia Gutierrez** 34:22 sig… the config sig itself doesn't exist anymore. No, it's just part of, like, main… Like, any discussions you can bring to the main, like, specs, or things like that?
**Jamie Danielson** 34:33 Yeah, or if you put it in there, then, you know, there's a chance probably it gets forwarded to spec or whatever else. I think either of those places are probably safe, right? Like, someone will see it.
Probably.
like, maintainers of the repo, even if they don't have a SIG meeting, they're still… Yeah.
**Marylia Gutierrez** 34:51 Yeah, they are still… they are still active, so yeah, you can open an issue on the repo, you're just not gonna have a SIG to discuss, or you can, like, have… go to the semantic conventions or spec SIG, and just mention, like, I have this PR, people can take a look, things like that, but yeah.
**Trent Mick** 35:06 Okay.
**Marylia Gutierrez** 35:08 And for the DPR that I have open, so one thing that I can do is, like.
Remove that 1 and 2, like, the meter, like, that line itself?
**Trent Mick** 35:19 Yeah, yeah, if you don't pass through the meter provider, then we just don't get SDK metrics by that path, yeah.
**Marylia Gutierrez** 35:25 So I can, yeah, just for now, remove and put, like, we can have, like, an issue on the JavaScript repo as well, to say, like, we need to… figure out this, and I do that to do the same thing that I've been doing with the others, but, like, number of the issue and things like that.
**Jamie Danielson** 35:45 Yeah, I just shared this link that I think is… Relevant.
**Marc Pichler (Dynatrace)** 36:15 I think that is actually…
**Trent Mick** 36:19 That's a different thing.
**Marc Pichler (Dynatrace)** 36:21 -Oh.
Looks like… They're… they just need to… I have one way to define…
**Jamie Danielson** 36:39 This is, like, defining what attribute names are included or excluded when…
**Marc Pichler (Dynatrace)** 36:47 This is the accept and denialist behavior from the spec, I think.
this attribute keys…
**Trent Mick** 36:57 This is, at a minimum, an allow list of attribute keys.
Must be kept in all attributes. Others must be ignored.
**Marc Pichler (Dynatrace)** 37:13 I think this is, this is, only attribute keys.
Related.
**Jamie Danielson** 37:22 I guess it would be a similar thing, though, right? So instead of having just the allow list of attribute keys, it's like an allow list of…
**Marc Pichler (Dynatrace)** 37:30 metric keys.
Yeah.
But then again, you can also turn off a meter.
Completely, and if you have a, metrics SDK meter or Trace SDK meter, then you can just turn off all the metrics for that.
It is definitely possible.
I guess this warrants more discussion on an issue.
I also have… Opinion about these SDK metrics, but I'm gonna keep it to myself for a bit, and revise it on the issue.
**Trent Mick** 38:18 Okay.
**Marc Pichler (Dynatrace)** 38:18 No.
**Trent Mick** 38:19 Let me know, because I'm reviewing, like, those four PRs, if you have a…
**Jamie Danielson** 38:22 Mark's gonna log in as anonymous.
handle and put some words in there.
**Marc Pichler (Dynatrace)** 38:26 Not, not Mark Pisha. Yeah, I was gonna say, he's gonna…
**Marylia Gutierrez** 38:31 New user, definitely not Mark, that is that.
**Marc Pichler (Dynatrace)** 38:36 No, I was about to say, okay, I'm not keeping it to myself then. The… I think this is not… not different to an instrumentation, right? And I think it should be enabled via the instrumentation's config thing.
There should be, like, one well-known instrumentation key, or…
**Trent Mick** 38:59 SDK metrics?
**Marc Pichler (Dynatrace)** 39:02 Yeah, that's, like, SDK metrics, or, like, I don't know, I keep using the term self-monitoring, because that's kind of… I feel more descriptive.
There's, like, monitoring auto itself.
**Trent Mick** 39:18 Yep.
**Marc Pichler (Dynatrace)** 39:19 And if that is the same across all the languages, to turn that on, then you can just put instrumentation, I don't know, auto-self monitoring.
and turn that on, and you will know what you get, because all the metrics are defined in SEMConf, and you just turn that one instrumentation, even though it isn't on.
And you will get Oreo.
polyometrics there.
But you would think something…
**Trent Mick** 39:50 In instrumentation.general.something.
**Marc Pichler (Dynatrace)** 39:54 Yeah.
**Trent Mick** 39:55 Because they're already sitting there.
**Marc Pichler (Dynatrace)** 39:57 Yeah.
Yeah, exactly, like, in the reserve telemetry, or… I don't know, I'm not… Completely married to the name, but, there's… I think SDK metrics can be confusing in naming, because we have the metrics SDK and, the… it confuses me every time I see the link, as well, to the SEMConf stuff. When it says SDK metrics, I'm like, what is the metrics SDK doing in the SAMConf repo that… Doesn't make sense.
**Trent Mick** 40:37 We totally changed the word order of the two words, it's totally different.
Yeah.
**Marc Pichler (Dynatrace)** 40:49 I read…
**Trent Mick** 40:50 telemetry SDK metrics?
about SDK components. Yeah, okay.
**Marylia Gutierrez** 40:58 I was gonna start thinking something with, like, auto, because it's, like.
**Trent Mick** 41:03 Whoa.
**Marylia Gutierrez** 41:03 It's on its own, but then the auto is like, oh, so it's turned on by, like, automatically? Like, no, that's…
**Trent Mick** 41:12 Yeah, Otto is already… mushy.
**Marylia Gutierrez** 41:16 internals, I don't know.
nearer, because you're looking at yourself, I don't know.
**Marc Pichler (Dynatrace)** 41:28 Right, let's discuss… continue discussing on the issue, here, but… I think there's quite a few different options, and we need to figure out what everybody else is going to do.
**Trent Mick** 41:45 Yep, I can… follow up.
Probably with an issue in OpenSeometry Config, and then… maybe I'll swoop in.
Let's do… One of the other SIGs, the… the spec, or the SEMCOM SIG. Do you know what would be more appropriate?
Merillion? For discussing config. Like, it just stabilized, so good luck, but…
**Marylia Gutierrez** 42:10 Probably semantic conventions?
**Jamie Danielson** 42:14 at least comes up first, and then they can tell you, no, come back tomorrow.
**Marylia Gutierrez** 42:17 Yeah.
**Jamie Danielson** 42:18 back.
**Marylia Gutierrez** 42:23 And I can open the one on the JavaScript just to keep track, and so I can put the to-do on the PR itself as well.
**Trent Mick** 42:31 Great, thank you.
**Marc Pichler (Dynatrace)** 42:36 Alright.
**Marylia Gutierrez** 42:39 Next two are mine. Yeah, so the first one is just, like, a tiny… check on the limits for timeouts, already, like, addressed the feedback, but just waiting.
Approval to get merged.
**Marc Pichler (Dynatrace)** 42:58 I'm actually gonna add the browser labor to that.
I'll try to review this one, I swear.
**Marylia Gutierrez** 43:11 The next one… so, the next one, it is something on the… Postgres, package, which I am a co-owner, but… the changes that they are making, I actually don't know enough to review, so this is what I'm hoping. It keeps getting the unmaintained, because initially they made a change on MySQL, and then they remove it, so all the time I have to keep going and remove the MySQL and the not… the not-maintained, flag.
So yeah, they, they have something on SQL common that they added as well.
**Trent Mick** 43:47 You can add… you can add has sponsor if you're… And then it disables the logic for…
**Marylia Gutierrez** 43:53 Oh, okay.
**Trent Mick** 43:54 Doing anything with the unmaintained thing.
**Marten Hennoch** 43:56 I also have a question about it. So, I ran into some coverage issues when doing this.
it said that I've lost, like, a lot of test coverage, and then I looked into it, and it… because I added tests… I fixed it, I fixed it already, but it lost, like, I don't know, 13% or a lot. It seems like CEI only runs, like, run some… it doesn't run the integration tests with the environment, so it just runs the test all versions, so, like, half of the… Tests are not run.
NCA.
So that's why I was not hitting coverage, so I enabled this, like, for this PR, if you look at changes. Some… where's the GitHub workflow?
Yeah, yeah, so the… so I added the test services, which, like, enables, like, most of the tests. So my question is, why are we not running at least I think we're not running Like, a lot of the instrumentation… integration tests.
Because… And the CIA always runs the… Run test all versions. The CI doesn't fail because, like, all of the tests are left pending.
It's green, but it never runs.
**Trent Mick** 45:15 This is running… Pistol versions of the…
**Marten Hennoch** 45:21 So in the back… JSON, yeah, in the package JSON, we have those scripts that… Run with N, and run with… whatever.
**Trent Mick** 45:31 How is that test all versions… Wasn't that failing if test services env isn't loaded?
I actually don't understand how your change there makes a difference to what I understand that is meant to be.
**Marten Hennoch** 45:45 My understanding was that it runs with N, but… I don't think it does. Maybe it does, I didn't look, like, that much into it. But after adding the environment, it started passing, so…
**Trent Mick** 45:57 Desktop version.
**Marten Hennoch** 46:00 Yeah, so it…
**Trent Mick** 46:01 Oh, that… so that… okay, at the end of that, after we are highlighted, that thing, that testel version should maybe be test all versions colon with services in.
If you look down on line 27.
**Marten Hennoch** 46:16 Yeah, so maybe I should change it here.
**Trent Mick** 46:19 We… if you're willing to try that, that might be a better fix for it.
**Marten Hennoch** 46:24 Yeah, I had to… I was just wondering, like, why are we not running it in debugger?
Okay, I'll change your perspectives.
**Trent Mick** 46:31 Okay, if Tesla's… so the way it is… Without your change.
It runs test all versions, but… Oh, without the test services, and then the rule is the tests should… pass, but just skip. Okay, so it was just skipping all the tests, so that's a bug. Yeah, definitely try fixing that there.
**Marten Hennoch** 46:52 Fix it for everything.
Yeah, so I'll fix that. The change itself is pretty much… I have to make this for MySQL also, but for Oracle and Microsoft, I had spec.
But for this, I don't have spec. I have spec issue, but nobody is really looking at it.
Maybe I have to go to the spec seat, but I don't really want to go there.
So I'm just waiting aggressively at home till it checks to accept it.
**Jamie Danielson** 47:22 Did you try posting a note in CNCF Slack at all?
**Marten Hennoch** 47:26 No.
**Jamie Danielson** 47:27 That might be the… Easier stuff.
**Marten Hennoch** 47:29 I had someone at least commented, finally.
Pespexig is a place wherein dreams go to die, so I'm trying to avoid it.
**Trent Mick** 47:38 He said waiting aggressively at home?
**Jamie Danielson** 47:40 Barrier?
**Marten Hennoch** 47:41 Yeah, yeah. We have a… we have a…
**Trent Mick** 47:43 See that?
**Marten Hennoch** 47:44 We have a joke that Estonian salesmen are the worst, because they aggressively wait for clients at home.
Yeah, so… I have the same change for MySQL also.
But they haven't done it yet.
I'm thinking if we… if we will even accept it, if there's no spec.
Because… I linked, like, all of the discussions, like, there is no… this is not the best way to do it, but, like, the correct way would… involved, like, changing Postgres.
Itself, which will take years.
So this is, like, the past… way of doing it right now. Datadog does the same way.
For Java, at least. For Node, they actually don't. For Node, they use SQL Commenter, but…
**Trent Mick** 48:39 Yeah, I was gonna ask, is an SQL content? Yeah. Sorry, I haven't read this issue.
**Marten Hennoch** 48:43 Yeah, so you can take a look.
I will fix the… I'll try to fix the test issue.
But everything else is so.
**Trent Mick** 48:53 Okay, thank you.
**Marc Pichler (Dynatrace)** 48:57 So try to have a look at that one.
been… Diving into some… parts of the code that I… Haven't looked into for quite a while, so this will also… Be a good time to do that, unlimited.
Right.
and the next topic is Carlos, who's offline today.
He opened… one issue.
I'll actually comment.
Holded one, and… Then he also has another question here.
Api seems to expose both NOAA Blogger and… the constant, is this really needed? Probably not, so we should look into that one as well. I thought we did.
Pass on that already, and removed everything that was… that we were able to, but looks like there's still something left.
I'll just put a comment here.
Alright.
So that's just for API logs and stabilization stuff.
There are still, I think, a few PRs open for the log stabilization, so, if anybody has time.
Would appreciate a review to Milestone.
Is… Here, and the PRs are linked here, so.
**Trent Mick** 51:06 Did you… can I put you on the spot? You were gonna… you can reply later as notmark. The interface attributes, widening that, whether we consider that a breaking change?
**Marc Pichler (Dynatrace)** 51:17 I think it is breaking, and I think it.
It will badly break people, and I can… If you want, I can… I can give some code examples on what I think would break on Compile.
And comment that on the… on the, PR or on the issue.
Hmm.
**Trent Mick** 51:45 Okay.
I can't remember if it was an issue, or yeah, I had a PR.
Okay, not sure where the best place is.
**Marc Pichler (Dynatrace)** 51:54 I'm not happy that it's breaking. I'm actually very upset about it.
But, I think we need to be careful with this change, because it, kind of… like, these sorts of breaking changes can be very frustrating to folks, and I think in the past, whenever we've run into something like that, there was a huge influx of issues, of people that are running into these problems, demanding it be fixed.
And it could be difficult to do.
**Trent Mick** 52:37 Okay, I was debating with… Yeah, in a little bit, and I was coming out thinking that while it could be breaking the SDK component.
authors. It shouldn't be for API users, so I was… vacillating there, and was hoping we could move forward with that.
Because… Having two attributes type is just… Feels like crap.
I agree.
**Marc Pichler (Dynatrace)** 53:03 That's also why I'm upset. I would love to have just one attributes type, and also have the Be structured in a way that it can be expanded later on, so that we can widen the types somehow.
have been… Thinking of different ways how to do it to keep just one type, I don't think there's a good way without bumping to 2. Which…
**Trent Mick** 53:37 So… I would welcome your code example so we can get to specifics on that one. The… the question that I have then as a follow-up is if we are… if we decide and agree that we need to… attributes types in the API.
Does that mean we need parallel methods on spans for, like, set attribute?
There's… does there need to be a set attribute, too, that takes extended attribute?
**Marc Pichler (Dynatrace)** 54:06 I think we can still expand that one, because it's just breaking to… implementers, and that's… Allowed by the spec. It's not great, but, it's better than breaking users.
Directly?
A user will not run into that issue, because, dude.
From their point of view, you can just pass more to that function there, and they won't… Care much about that.
But the other way around, if they accept attributes, or the current attributes type somewhere in their own functions right now, because they have some utility library.
**Trent Mick** 54:47 But they shouldn't do that.
Anyway…
**Marc Pichler (Dynatrace)** 54:49 Oh, man.
**Trent Mick** 54:50 And then… but they shouldn't be breaking apart the thing. I mean, this is your example with the… the type, narrowing, right?
**Marc Pichler (Dynatrace)** 54:57 Yeah, like.
**Trent Mick** 54:58 To break compile of types, yeah.
Don't do that.
I… yeah.
Okay.
But, yeah, thanks, please, if you can put that. I know we discussed it privately before. Yeah.
**Marc Pichler (Dynatrace)** 55:11 I'll, take that example and put a few more, in there.
To kind of demonstrate what I'm talking about.
Alright.
Bountain… Talking about, more happy things, fulfill yeah.
**Marylia Gutierrez** 55:36 Yeah, what I share, was just… they just published the due diligence about 2 hours ago, so that was one step that was… Probably the… that'd take longer to actually get it. So now, at some… yeah.
is a long document, but… and there was one point that they say, like, yeah, this… basically, the assessment, yeah, has met all criteria for graduation. Now, there's a couple more steps that they actually need to vote, for this, and… But hopefully… so it's a… it's, I think, like, two weeks of private voting, and then one week of public voting, so there's just… few more steps, that was… that was the big one. So, just wanted to share some good news, and… For everybody in their work.
On something that was… in the end, was all of it that everybody's doing, is to help out graduation, so thank you all for all your work.
**Marc Pichler (Dynatrace)** 56:43 Thanks for, sharing that, and also thank you to everybody who Was working towards that.
Alright.
There's 3 minutes left, the last topic is a bit of a… larger one, so I would just skip that one, and move it to next week, if that's okay for everybody.
Do we have anything else that we want to talk about?
If not… Then… Thank you, Rivera. Thank you, everybody, for joining.
Thank you for saving me from, park triage by having lots of discussion today, and I will see you next week.
**Trent Mick** 57:49 Thanks, Julian. Thanks for having me.
**Marylia Gutierrez** 57:51 Right.
