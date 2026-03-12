SIG: eBPF instrumentation
Date: 2026-02-25
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Rafael Roquetto 00:00:45 Hey, guys.
Stephen Lang 00:00:50 Whoa.
Giuseppe Ognibene | Coralogix 00:01:20 I didn't want…
Mike Dame 00:01:26 Name?
Tyler 00:02:39 Hey, how y'all doing?
Nimrod Avni 00:02:43 Good.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:02:44 Hey.
Tyler 00:02:46 Hey.
Okay. Well, welcome, everyone. We could probably get started here in just a second. If you haven't yet, please go ahead and add your name to the attendees list, and if you have, agenda items you want to talk about, please go ahead and add them there as well. And, yeah, well, let's jump in here in just a second.
Awesome. Okay, so to start us off.
I wanted to talk about some V2 configuration and adding the OB to the collector contribib.
distribution, but, maybe we can start off, actually, with this release image stuff. So, I was just looking at this as I saw the meeting notes here, so why don't we… Go ahead and jump in.
here. So, Mattia, you're noticing that the CI release job is broken for the V05 image, wasn't published.
And then, Steven, you're talking about the signature verification's broken.
just before this meeting, I was looking at the CI that did the release, there's, yeah, so I think it got published, I don't think it got tagged as the V05. I can see that the job was successful, and that the SHA is there.
It's just missing the V0 tag. V050 tag is, I think, the issue here.
I'm not exactly sure why that's the case. I was looking at it really quick before the meeting. This workflow here is the one that is calling it. It's calling it with the input tag. This is the… the other… file, that is… that is the… publish the Docker Hub main.
It does look like it's taking the tag.
Not exactly sure why… This is failing.
Stephen Lang 00:05:19 These workflows have changed.
Since… this as well, so QEMUs are no longer used.
But the inputs and outputs should be the same, they haven't been changed.
But it used to take.
Like, 40 minutes to do the multi-arch build, now it takes about 4 minutes.
That's not going to really affect what the issue was here, unless it was to do with something, with it taking so long.
But yeah, just so you know that this… file looks different in main.
Mattia Meleleo 00:05:55 Was this workflow triggered by the push to the main branch, or… The… the tag creation.
Tyler 00:06:04 No, so… In theory, it's created by the tag creation, but it's not on this particular one. This one was, created by… A manual trigger? Because our release process is broken for the exact one.
So it had to get re-triggered Yeah, so this is, I think, the one… that was triggered by the tag itself. This is the one that was… Hmm.
Interesting.
This is the one that I manually triggered. The build artifacts release failed. This was because you can't change the… the GitHod, essentially, that you're building again, so all the fixes to fix this weren't included, but the build push steps did successfully get pushed, and that's what we were just.
Mattia Meleleo 00:07:05 Okay, so the image was pushed, but the… just the tag is missing, or…
Tyler 00:07:10 Yeah, correct, yeah.
Nimrod Avni 00:07:12 It relies on the… on, like, the release… the name of the release, because this job triggered on, like, main branch instead of the release tag, and then, like, it didn't tag it, or something?
Tyler 00:07:25 Yeah, that's a good question. That's what I was trying to figure out here. I don't know why that would be the case.
Given it is using this ref for input tags, And then… Yeah, yeah, I'm trying to figure out why, because, like, given that input ref is here, use here… I guess I don't see the input rough being used here, I see this metadata outputs tag.
Mattia Meleleo 00:08:01 So, when you trigger a workflow manually, do you have to put these inputs, like, manually, or do they get inferred somehow?
Tyler 00:08:11 No, yeah, see, yeah, we can go through that.
Probably good to know that. So, yeah, it is…
Mattia Meleleo 00:08:22 based on the branch, that you're trying to go against, and then you add in the tag specifically here. And this tag gets validated down the road, so, you know, this is, yeah, this is essentially what was done right here.
Tyler 00:08:34 Okay. Yeah, and I mean… I do wonder if, like, you did something like this, like Nimrod's saying, though, if that would change that.
I mean, it obviously wouldn't change the build artifacts, But I do wonder if it would change the… what's getting inferred here in this release, or this, build step for the outputs.
Stephen Lang 00:09:00 I think it wouldn't. I think that's just selecting, like, the YAML source file for the workflow, as opposed to the input tag.
Tyler 00:09:13 Yeah, so the thing is, is though, like, so this… this is the thing that sets it, right? This is looking for the output of… tags here, although I'm not… like, this is, like, the weird thing, because I'm not actually seeing… tags being set here, I just see the… Oh, I guess metadata, actually.
Stephen Lang 00:09:33 Yeah.
Tyler 00:09:33 Figuring this out, yeah.
Stephen Lang 00:09:34 Yeah, look at the action. No, so I mean, if you did run it off the 050, you would also still have to put in the text box V050 as well.
Tyler 00:09:44 Yeah, 100%. Yeah, that's definitely the case. Yeah, I do wonder… I wonder where it gets these tags from.
Hmm.
Stephen Lang 00:10:06 vis-a-vis inputs, does it have a list of outputs?
Tyler 00:10:10 Ehhhhh Maybe…
Stephen Lang 00:10:21 It was a Jason?
Sorry, at the end of that list, I think there was a JSON output objects.
Tyler 00:10:26 Oh, there we go, thank you.
Stephen Lang 00:10:38 Adjacent output is a JSON object composed of general tags and labels.
Tyler 00:10:45 Yeah.
Stephen Lang 00:10:49 Oh, is this… so this is showing you an example of consuming the output, doesn't actually show you the output?
Tyler 00:10:54 Right, yeah.
I don't know if there's a way… this might be something that we can update, though.
Here we go, I guess. Tag returns the tag name.
Trigger the workflow… Okay.
I guess this might be… what it is, is that it was empty, because it literally…
Mario Macias 00:11:33 Yeah, probably in the GitHub history, we can… in the Git history, we can see if something has changed, or something has been removed.
So this is missing.
Tyler 00:11:47 I don't think that it's… I don't think that's necessarily the case. I think the problem here is that, like, so we're using this… this step here is supposed to extract this tag volume that's used later on, right?
And this is being called from the release. The release is being called off of the main branch. And so, if we're being called off the main branch.
it's… it's gonna look something like this, right? Like, these are gonna be the ref… I'm guessing, that it's using. It doesn't actually use the input ref, it uses, like, the GitHub, like, action ref, so this won't actually be set.
to a tag is the problem. So, there's no way to actually, like, tell this metadata action here to say, on the output, also, like, you know, includes the tag, I guess is what I'm thinking.
And so when it comes down here and it looks for the tag, like, this is just gonna be empty, so it's just gonna use the SHA as the problem.
I guess the question is, is, like, if I re-ran this workflow, Using this tag right here, if that would cause a problem.
I actually don't know if it would.
Because it will go down this whole pipeline, it'll fail this thing again. I'm wondering if this is gonna solve our problem. And then it would rerun this, but it would rerun it and tag it with the correct thing, so it would try to re-push the exact same Docker image with the same SHA, And, the only difference at this time would be that it would also push the new tag.
Stephen Lang 00:13:14 But why would it work a second time if it didn't work the first time?
Tyler 00:13:18 Because I would run it with this, input from the tag, not from the, the main branch.
So, in the GitHub, the metadata action, right? Like, the ref… not the input ref, but the actual GitHub, ref that's being used, right? So the GitHub ref name would be populated at that point, and it would not be, you know, this… refs heads master, it would be refs tags V0.5.0.
Stephen Lang 00:13:50 Okay.
Tyler 00:13:51 And because of that, then this field would get populated. Because this field would get populated, this would then also have the tags set at that point, is what I'm saying.
Stephen Lang 00:14:00 Let's see. Okay.
Mario Macias 00:14:04 I don't know if this is taken from the Baylor release workflow, but yeah, in the Baylor release workflow, it assumes it's run against attack.
when you do the release, for example, and the tag is automatically created. So maybe you're right. If you try to run it with a tag directly, you will… You will… you will get this populated.
Antonio Jimenez 00:14:29 Tyler, what about if we run it from scratch without TAC?
Tyler 00:14:34 Without what?
Antonio Jimenez 00:14:36 With attack, like, the 050.
But not rerunning the failing one, but rerunning from scratch, I mean, from the beginning.
Tyler 00:14:43 Yeah, that's… that was what my suggestion here is, yeah. Okay. And so do something essentially like this. So to kick this off, it's going to… it's still gonna fail this build release artifact step, which is, like, fine.
Actually, because it's not going to do another draft, because we've already made the release. But it should rerun this as well, with all the same info, and the only difference this time is it should have another tag.
I don't think there's gonna be any conflict, But I also do know that we could talk to, like, hotel maintainers, and they can just explicitly go in and add a tag.
To solve this. I don't know… that might be the safer option. I'm not exactly sure if this would, like, try to redo things.
I don't know why it would be a different Shaw if it tried to build it a second time differently, but, I'm happy to… Ask what you all think is the next best approach here.
Pellared 00:15:37 If it was not published, before, then even if you create a different shot, I don't think it's.
Tyler 00:15:44 No, it was. It was published. So, yeah, that's the whole thing, is like, it was published, it was just published without the bag.
05, Tega.
Pellared 00:15:56 Okay.
Tyler 00:15:59 So, like, if you go do this, This, this should, this should exist, right?
Sorry, that's not… I read Docker.
Alright, well, apparently this isn't right.
I don't know why this checks on length is… That's because I forgot the E.
Pellared 00:16:27 Just to double-check, even if you create a new SHA, it will also publish a new SHA Right?
But it won't be mailed, it won't be on mail.
Tyler 00:16:39 It's fine if it's not on main, right? Because that's actually not… it's not on main, like, this is a different tag.
Yeah, the only… I guess… I guess, Robert, you're right, like, if it does have a different SHA, then it has a different SHA, and since we don't already have a V050, that won't cause any conflict from somebody, right? Like, because they can't be downloading it anyways.
Yeah, alright, well, I'm happy to hit this… start this… And then if this fails, I guess we could always just go back and tag it.
So, I'm guessing, from folks, that sounds like a reasonable approach?
Mattia Meleleo 00:17:12 Yep.
Tyler 00:17:14 Okay, cool.
Let's let that, stu in the background, then.
Cool. Alright, then… Steven, also the image signature verification, is also broken.
Stephen Lang 00:17:28 Yeah, so I had a little look at this. I thought it was an eventual consistency issue, so I added a, like, retry with 10 seconds in between each try, and… it still didn't work. So I asked Lord about this, and it seems that there's only the cash repo.
image repo is failing. Like, the, the main… OB or UBPF instrument repo is… is fine.
But the cash one, for some reason, doesn't work.
And, Claude suggested this might be a configuration on the repo itself.
Which… I'm pretty sure I don't have access to.
So I might need a bit of… Bit of help with, with this one.
But as it explains, like, there's just… I think the, the image… Is, yeah, I don't know, I got a bit stuck on this one.
Tyler 00:18:27 Hmm… Yeah, I think this might be something to just open a community issue on. Like, we don't have, like, maintainers don't have access to the, the Docker Hub account. It's a TC thing? I know Trask has it. So… Yeah, they can help you from that one, if you need to set something differently, I think is the idea.
Stephen Lang 00:18:51 Okay. Yeah.
Pellared 00:18:54 I can also, I can also say, I haven't, sorry that I have missed, this PR and comments.
But I can see… I can say that… I saw that the last time I was checking the cosign verify, it also worked for this For this Kubernetes cache as well, so it looks like it's totally not deterministic, which is painful.
Stephen Lang 00:19:17 Okay.
Pellared 00:19:18 But, yeah… I can try to, yes, we can sync later, if you want.
Stephen Lang 00:19:23 Yeah, that'd be great, thanks.
Pellared 00:19:25 Thanks.
Tyler 00:19:28 That's… Huh. It's non-deterministic, huh?
Pellared 00:19:33 I think… if I remember when, like, I think it was last week, when I was checking.
Before I went to the PTO, it was not working. When I returned and I checked with all of the images, I remembered that for cache, it was working as well, and I think in the PR, I even made a comment with the result for the verification.
And I also remembered that… We also checked that even the cosign Docker image, the official one, we also failed to verify this one. Do you remember that when we were checking this, or…
Stephen Lang 00:20:07 Yeah, I remember that. That only worked when we downloaded the signatures locally, but yeah, maybe we can catch up on this later.
Pellared 00:20:15 Yep.
Tyler 00:20:17 Okay.
Yeah, alright, yeah, keep us posted. Open the community issue if you need some help on the actual upstream issue, Steven, and then, yeah, we'll keep it in mind.
I am realizing, as I was thinking about this, this release is going to fail, yeah. And that's… for reasons that it's going to fail to validate the tag, yeah.
So this isn't gonna work, yeah, because when I try to run this against the V050 tag, that means it didn't have any of the fixes for the workflow, so this isn't even gonna get kicked off. So, yeah, I also will take as an action item to go ahead and tag the existing image that is already there, by asking some of the Docker Hub maintainers, yeah.
For what it's worth, I don't think… yeah, go ahead.
Stephen Lang 00:21:24 I was going to suggest you could rerun the original release that did fail, the step that was supposed to do the tag.
Which presumably would fail if you just rerun it anyway.
But my suggestion would be to rerun it with the debug logging enabled, and you should be able to see the inputs and outputs from the actions, at least.
Tyler 00:21:46 Yeah, so you're saying this guy here that actually ran it is to rerun this one here?
Stephen Lang 00:21:56 Right, yeah, because this is the one that… Failed the tagging. Yeah.
Tyler 00:22:00 Yeah, and so you're… you're saying just try to rerun this, and then it would be able to…
Stephen Lang 00:22:06 There should be an option, I can't see on the Zoom share, but there should be an option to rerun with debug logs.
Specifically, and that enables, GitHub to print out the inputs and outputs of each step.
Tyler 00:22:20 So we could maybe use that to help debug why.
Stephen Lang 00:22:24 The tag wasn't picked up by the… By the action.
Tyler 00:22:29 I see…
Stephen Lang 00:22:31 enable debacle.
Tyler 00:22:33 Yeah, okay. Alright.
Yeah, this can verify that.
Yeah, I do think that this is the problem that we'll have, is that we need to change this to be, the steps metadata output tag, or, Or the input ref, I think is also the thing that we needed to change here, but… Well, okay, we'll take a look at that.
Okay.
Alright, moving on. So, next up, I wanted to talk about, the configuration. So, we've been talking about this as, like, a V1 setup. We wanted to do a… Deep dive into the configuration and look at it, I think, holistically asking, you know, does this need to change going forward before we stabilize?
So, I was doing that, and I went through the whole configuration. I think the configuration is… is great, it provides all of the access that it needs, it's just that it is a collection of… I think an accretion of all of the things that, like, have been added as features, and it's something that I think we could probably do a little bit better at.
So, I've gone through and I've taken a first stab at it. I know Nimrod's taken a look at this already, and I wanted to maybe just start off by talking about, like, methodology here. So, like, the idea here is that, like, I really wanted to make sure that this is… A configuration defined for the users, like, the end users?
something that, like, it's consistent and it's easy for them to, like, you know, get onboarded is the goal. You know, we do a pretty good job already of having a very good defaults, so if you don't really even have to touch the configuration is the idea.
And once you, you know, want to jump in and start actually manipulating things, I wanted to make sure that, like, we actually are addressing those. So I went through, first off, asking about, like, you know, user journeys of, like, what… what our users are actually going to be using this configuration for, and, like, what's the common use of OB itself? I think that, you know, some of the main things is just, like, they wanted to start instrumenting all their services running on some sort of platform.
They want useful defaults, they want enabled network observability in addition to application observability.
the goal here is, I think these are kind of, like, the main ones that people want, and I don't think they should be able to… they don't… shouldn't have to touch a configuration for this, which… I think we're already solving today. I don't think you have to touch a configuration to get this, to get this level of, you know, function out of Obi. I think that the next things, though, are, like, people wanted to come in and they want to target their instrumentation. They want to say, like, hey, I don't want everything, or I want a particular thing, I want to scope this in a particular way.
I want to combine targets, I want to, you know, I want to do something that was going to scope and select targets, is kind of the idea.
I also have, you know, on one of these top things, exporting, I want to be able to send OTLP to some backends, maybe Prometheus, I want to use the collector, for pipelines, so how do I configure all of this stuff? This is things, you know, obviously, again, like, things you can do today, but just, these are, like.
Maybe it's not the easiest thing to do today.
enriching, I want to be able to, like, you know, take that data that I am sending it, add in useful things from Kubernetes, other wonderful things that we're also adding from, you know, maybe cloud vendors or something like that. Limit cardinality is another great thing.
Push specific or annotate things with different attributes.
Moving down, I think that, like, also they want to make sure, like, you know, once you're… once you get it started, once you start seeing the value of OB, like, running safe in production, so they want to be able to have, like, clear understanding of, like, what Obi's doing, clear controls onto, like, the… the operations of what OB is actually, you know, functioning, and being able to debug, I think is kind of the game, the important thing.
Validate and migrate is also, like, kind of the last thing, so, yeah, finding actionable errors when things do go wrong, being able to debug is, I think, kind of a key thing here.
So, I don't think there's, like I said, anything stopping users from doing a lot of these things today. The problem is, is that… In some of these things, it's… it's… it's… spread out. You aren't going to go to a particular portion of the configuration to achieve these things. In some cases, you have to go to multiple portions of the configuration.
to achieve these things, and even worse, in some places, there are places where you will configure it in one place, and another place will also get configured, and it can affect that other place, so… Ideally, those would become consolidated, they'd become single points of targets, for users, and so they have, like, one, you know, one concern, one place, so I've kind of come up with some design principles for this next iteration.
You know, focusing on the user journeys is kind of a big thing. This one concern, one place is kind of an important thing.
Another thing that I really wanted to, you know, we've always talked about is this compatibility with OpenTelemetry declarative configuration. So this is something that, you know, from the community's perspective, this is a very valuable thing. I want users to be able to say, like, I have a declarative configuration, I want to ship this everywhere.
OB should try to, you know, honor this. There is overlap with what already exists there, but there's also more configuration that OB needs, so I see the OB configuration as an extension of the OpenTelem declared configuration, which… We'll talk about.
Yeah, and then there's a lot of other, I think, design things here. Protocol-level ownership, meaning that, like, I really wanted to make this easy to set things up for, you know, particular instrumentation, particular selection.
Deterministic precedents, there shouldn't be any confusion.
around what's happening underneath the surface. If you configure something, it should be in a, you know, an ordered structure. That ordered structure then should then be reflected in how the code is set up. It shouldn't be the other way around.
No redundancy, not in naming, not in multiple knobs to turn… to, to the same thing. Versioning, should be important, because we want to be able to move forward, we want to be able to determine our versioning of configuration. This is something we're missing right now. I think this is a very important thing going forward to make sure we have, so we can tell the difference between, like, a V2 and a V3.
Backwards compatibility, then, is something that we can try to, achieve. This is actually pretty useful, you know, especially if we're Moving forward with new features and that kind of thing, having backwards compatibility is helpful to get a migration path, and then, obviously, making sure that this is a useful, path forward.
So, that's kind of, like, the groundwork. I think maybe the next step is just to jump in here and look at, like, an example configuration.
So, this is taken from… what our defaults currently are today. That is just, this dumped, you know, this is essentially, a very simple script of just loading the defaults and then dumping them. And so, what this is… doing is it's taking all of these values and it's mapping them over here. In fact, it even includes a verification script, so this verify checks parity, so it does check to make sure that, like, anything that was defined in this default config is still defined somewhere, in some way, in this other default config. But, yeah, just to walk through, I just want to give, like, an overview. So, this is all OpenTelemetry declarative configuration at this top level. So, this file format, resource, propagator, choice provider, meter provider, all are things that are defined at the declarative configuration is the idea. Everything below here is OB-specific. This extension doesn't technically exist in the declarative configuration, but it should at some point, but we can talk about that in a little bit.
So, everything below here is a restructure of the OB configuration outside of configuring pipelines. So, one of the main things to take away here is that all of the, you know, defining the trace pipeline, defining the meter pipeline, would then be moved outside into, you know, standard OpenTelemetry declarative configuration.
If we are able to move to using, you know, upstream SDKs and APIs, which is something we could talk about as well, we could just start using upstream tooling as well, from the Optel Conf package and our contribib package to set up a lot of these pipelines for us, so this becomes a big win. Another thing is, is that, Since we have the collector-receiver now, we can have partitioning around where this, like, the run modes here.
And if you're running this as a standalone binary, obviously you want to set all this stuff up, but if you're running this in the collector, you don't want to set any of that stuff up. That stuff is literally the definitions of the pipeline in the collector.
So what we can do is actually accept only this section of the configuration, which is really nice because it cleanly separates the concerns across the configuration. Nothing in here is defining pipelines, by… by design.
Yeah, so obviously, to start, we have a version, we have a selection. This selection is the… targeting of the particular processes, workloads that exist. This is unified. This is something that is not, like, instrumentation-specific. This is something that is not particular technology-specific. This is saying, like, OB is going to target these particular services. Obviously there's, you know, policies. This talks about, like, you know, how you want to do the matching, what this… what this ordering should be, how quickly you should be doing that, and then the rules themselves.
This is what our default rules already are, this is what the default rules turn into, are essentially saying, like, you know, match everything, but then from, therefore, we can exclude, these particular processes, we can exclude these particular Kubernetes namespaces, we can exclude these particular services that are already instrumented with OTLP.
on this port using, you know, this protocol. We can also exclude these other paths, for this Linux system's, executable paths. So essentially, this becomes, like, a targeting system.
And then from there, you have instrumentation definition, so for all the services that you do have, if they have these particular protocols enabled, then, you know, this is where you would turn them on and turn them off. This is for… You know, you can do additional filtering if you don't want these to target all of your, you know, selected services.
But essentially, this is where all of the configuration comes in. This is… should look familiar.
the enabled gets broken out into having both traces and metrics. I thought that was pretty useful if you wanted, you know, before, it used to be was, like, you would find the metric, pipeline, and then you would define an instrumentation. This is the other way around, where the instrumentation says, like, yes, produce traces for me, or yes, produce metrics, or either or for those.
Http obviously has a lot of configuration, there's heuristics here, there's, you know, pattern matching for routes, that kind of stuff, so there's a lot of really good stuff. gRPC, very similar, SQL, Redis, I'm not gonna go through too much of this, Kafka, Mongo, Couchbase, DNS, GPU.
Down here, this is, an iteration. Nimrod, we talked yesterday, or Nimrod provided some really valuable feedback, on this. One of the things is, like, in particular languages, or runtimes is what they're being called here.
You need to be able to say, like, you know, how you want to instrument them. This is, you know, using particular probes. The Node.js is using some sort of additional agent, similar for Java. Whether you want to enable that or disable that, I think is, you know, important for users to have a knob to control that, so that's… defined here. Obviously, you can do more filtering as well if you didn't want to target everything, that actually exists.
This is the network section defining network controls for telemetry flow. I'm gonna go through these a little bit faster, because, yeah, I'm guessing people are zoning out at this point. Enrichment, this is where we would talk about annotating telemetry with particular things. The idea is you would have enrichers, so things like Kubernetes, things like DNS, things like cloud providers, would be fine here.
And then if you wanted to, you know, enrich your service name, you can map that here. If you want to enrich with attributes, map that here.
Correlations, this is where I moved the log trace annotation, Nibrod as well. Thanks for the, response on that. I think this is a great idea. There's also the idea, eventually, of correlating with, profiles, so, you know, this is also included as maybe an extension in the future. Not obviously doesn't exist today, but this is where that, like, trace information gets correlated.
across, or outside of OB. Doesn't really match the instrumentation, definition, because it's not really instrumenting anything, it's providing information across things that are existing outside of it.
Then finally, this operations section, so this is like that, like, how do you actually tune the details of what OB is doing internally? So, things like limits, things like, defining, you know, how this telemetry reporting is actually being Performed the processes themselves.
How, you know, telemetry's being captured, logging profiling, this is another one.
which maybe needs to get broke out. I'm not exactly sure about this one, but we could talk about that. But yeah, that's a big overview. I also have a migration plan included in here, which I'm not gonna go into. There's, you know, please, we can take a look at that in a second, but I just wanted to kind of, like, pause here, and, you know, that was a lot, so maybe… Maybe see if people have any thoughts on this.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:35:26 I just want to say praise. This is amazing. Like, I was seeing all the options, and everything that you've done, and how it makes sense now, I don't know, like… It's amazing.
Tyler 00:35:38 Yeah. Well, that's great feedback.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:35:40 makes so much more sense. Now, I'm looking at this, and how the protocols are broken down, do this for this protocol, do that.
Yeah, I'm sold.
Let's do this. I'm gonna review it carefully today, but yeah.
Tyler 00:35:53 Yeah, I… well, cool, that's actually my ask, is like, I tried my best to provide parity, I tried my best to make things make sense. I obviously made a bunch of mistakes, Nimrod's already found, so… yeah, if you could… if you could put some detailed thought into this, maybe just do another review of this. Yeah, I think that'd be great. I think, if that's the case, like, we can… we can also move it on. Like, my goal… In this migration is to… kind of agree on this next direction here for the configuration, and then, you know, phase… the next phase would be lock the V1, so we aren't going to be, you know, changing things too much. So, yeah, I think… I think, yeah, just getting a good review here would be great, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:36:32 Alright, yeah.
Wow, that's… it makes more… so much sense. I like the attempt to sort of break down by themes, okay? You want to achieve the baseline, and then you go into the decorations, then you enable debugging, and all the options are sorted based on the use, rather than thrown in randomly in various categories the way we saw fit in fast.
Yeah, scope.
Tyler 00:36:54 Yeah, yeah. Yeah, and I tried to keep the design principles there, like, it sounds a little bit, like, pedantic, maybe even a little pretentious, but the idea is that, like.
going forward, as we're adding to the configuration, we should be able to try to use these design principles to decide where things go, to help guide ideas as we go and develop it. But yeah, obviously they're probably not perfect either. They could probably get Improved as we figure things out, but yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:37:21 Yeah, normally. I mean, that's expected.
Tyler 00:37:25 Yeah, yeah.
One of the major things that did stand out is… you know, in your reviewing this, I guess maybe people aren't as familiar with the declarative config, like, I have everything in OB under this thing called extensions.
In the declarative config, that doesn't exist in the declarative config. It does… it's allowed in the declarative config. There's actually validation steps that make sure this conforms with the schema, JSON schema from declarative config.
that schema allows additional properties, right? So there's nothing wrong with what we're doing here. In fact, actually, this could work, and we could go in this direction, and it probably should. It's just that, like, declarative Convig also has a section called Distributions, and it has this section called Instrumentation, or Instrumentation Experimental.
It's, very confusing.
there are open issues. Robert's also talked about this as well for, like, the .NET, instrumentation, auto-instrumentation, they have this exact same problem, like, this doesn't really fit here, There's also overlap, the instrumentation stuff has, like, this thing for HTTP instrumentation, which kind of overlaps with us, but it also doesn't. Like, we have way more knobs on what we… we have features here, we… you know, so there's, like… There's a… there's a mismatch here. I think going forwards, we should keep this structure the way it is. Extensions is what I'm calling it now. If we wanted to migrate going forward, you know, to another place in the declared config, we can do that, given we have this versioning capability. So… Yeah, I think that, like, we could just start here and move forward. If we have feedback from the declarative config group, like, we can also, you know, take that under advisement, but I don't see this happening within a week either, so, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:39:00 Well, cool. Yeah, it's good.
Tyler 00:39:03 Cool.
Awesome. Any other… Thoughts on this? Nimrod, I know you've looked at this a little bit more as well.
Nimrod Avni 00:39:12 Yeah, I'll have another, run of review, but that's great. I'm not super familiar with the… declarative config, I need to do more reading about that as well, but it looks way more, like, organized than things we have now, so that's… that's pretty great.
Tyler 00:39:29 Cool, alright, yeah, that was kind of, like, my main goal, is just that, like, organization, I think, is more important. The overall, like, details of how this gets out is, I think, a little bit harder, but yeah, from the user's perspective, I really wanted them to go, like, hey, I, like, I need this one thing, like, how do I do this? Like, it'd be nice if they just could easily find it, I guess, the goal.
Okay, cool. Then… Moving on to the next agenda item is also mine. It is, talking about the collector contribib.
donation. So, yeah, I opened this issue after last week. We were talking about committing, binary objects to the… to the repository, and, you know, the takeaway from there was just, like, well, does the collector contrib really… Are they willing to accept additional, ways to actually make this happen? And I think that they are. I'm not exactly sure they know what they've signed up for yet, to be… to be… to be honest.
But, I, like, I got positive feedback. I opened this issue, I put in a bunch of options. The ideas here are, like.
We can go through different ways to build this. The one way that I think that is really ideal is to, you know, build this into the distribution, don't build it directly into the hotel collector contribib, mainly just because then we're going to be duplicating our collector package. Our collector package is what needs to exist in the collector contribib as a… Receiver component there, which is, like.
fine, we could, you know, even wrap it, but it's, like, it's just, like, a very thin wrapper here. Where it all gets actually built, though, is not in the collector contribut, it's in a completely different repo. That completely different repo is this, collector releases, repository, if you're not confused yet.
You are… you were made for this project.
So, yeah, here, essentially, I've done that as a proof of concept. I'm still working on it, I don't think that the CI is actually passing yet. But the idea here is, in the build process, it prepares Obi for us. What that does is it… It does not check it out in, like, a Git history. It downloads the particular files, from that particular Tag of whatever we're trying to download.
And in that download, it then goes in and explicitly expands and builds out all of the needed binary files.
It turns it into a particular, you know, module, which it can then do these replace statements on, and then build this into the collector, just the same way that we were doing for the proof of concept in our, example for the, you know, local example, how we're using the collector builder here, so… Yeah, like, it's pretty straightforward. Obviously, there's, like, a gross, like, bash script that sits alongside this that gets plumbed in, but… Yeah, so far, like, I haven't seen, like, any people in the collector world saying, absolutely not, like, we're not gonna go this way, so… I don't know how fast this is going to happen, but I just kind of want to give you an update that this is happening. There is movement on the collector side to try to support this, so, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:42:29 I had a question here, something that completely slipped my mind, But, related to this, I mean, we've now built the Java agent, and it sits as a standalone in the binary directory.
What are we gonna do about that one?
Because that one is another artifact that's beyond just the…
Tyler 00:42:52 So I have… Oh, interesting.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:42:53 Yeah, so that… the option we used before, and I think it was part of the repo somewhere at some point, is that we actually… this agent doesn't change that much.
So we commit it, and then it's a resource.
Within the goal.
Like we do for the Node.js now.
although JS is a much smaller file, but this will be, like, we build the jar, and then we commit it, and then it becomes, like, a… A goal director that you just load on.
Tyler 00:43:23 Well, I mean, I think it… mmm… We're gonna have to do something like that, right? Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:43:28 There's no way, yeah.
Tyler 00:43:30 Yeah, like… Yeah, like, I don't see how we could do this Because otherwise, it's… I mean, we can download it here in the Go releases, but, like.
That's fine, and then it gets… built into this Go binary, but, like, the Java agent no longer is in that binary, and so that binary is the thing that's getting shipped, right? Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:43:51 Yeah.
Tyler 00:43:53 Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:43:55 Yeah.
Tyler 00:43:55 I mean, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:43:57 This is how it used to be. We had this, when I tried to initially package the Autel Java agent, the full thing.
Tyler 00:44:04 This is how we did it.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:44:08 But… That's fine. That's fine. We just need to change the build process and make one additional step, and if you're changing the Java code, you build and committed.
Tyler 00:44:18 Okay.
So we're gonna commit… we have to commit the jar file, is the problem here, though, okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:44:24 Well, yeah, I don't know what else to do.
Tyler 00:44:27 Yeah, how big is the jar? Yeah, go ahead, sorry.
Rafael Roquetto 00:44:30 I was just gonna say, remind me again, why do… why can we not embed the JAR file?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:44:34 Weekend, that's what I'm saying, yeah.
I didn't, no. I mean, it's, 5 megs?
Tyler 00:44:48 Oh, okay.
Wow. Hey, it's Java.
And by Rafa, you mean, you mean embed, you mean, like, using the embed package, right? To embed it, and then… And then, yeah, okay, yeah, that seems… So, like, does that work, Nicola? I'm guessing that's… is that what we do? Yeah, it does. Okay. Yeah, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:45:04 Yeah, it does work. We used to have the OTL Java agent a long ago, and this one is much smaller. Actually.
Tyler 00:45:10 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:45:11 Let me see if this is actually still that much.
Yeah, okay.
I just want to see if I… I built it on February 9th, so it should be pretty recent, so… yeah.
Yeah, it's unfortunate, but I don't see a way around this. I mean… We're embedding in the collector.
Rafael Roquetto 00:45:37 And I feel like embedding the binary also makes it easier for the user, like, you just give it a single binary that contains it all. If that's a problem, for whatever reason, we can… we could… Maybe that's not even a good idea, but we could have… two artifacts, like one OB, vanilla OB with a Java agent, or with agents that comes with all this embedded stuff.
Like, because then it becomes just a part of the open binary build, and we don't have to commit.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:46:08 I mean, the OB binary for me here… I don't know if I'd build a debug build or a production build, but it's 108 megs, so… This is gonna be 5 megs and talk.
Tyler 00:46:21 Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:46:22 It's not that.
I wonder what the collector contrib already is. I'm guessing it's probably a few hundred megs already, yeah.
Exactly.
Tyler 00:46:29 Yeah.
Okay.
Yeah, I mean, that seems reasonable to me. I do know that we have, like, additional flags to pass in the job agent. I'm guessing we'll just get rid of that if we start embedding it, right? Yeah, okay, yeah, that sounds…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:46:41 That's right.
Tyler 00:46:42 I kind of like that anyways, it takes away a lot of the… Complexity, yeah. Yeah, exactly, yeah. Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:46:50 Nice. Alright.
Tyler 00:46:51 Okay, cool. Yeah, then, I will… I'll add a comment to that issue that we're gonna try to look into that, and then, yeah, Nicola, I'll look forward to… to reviewing the PRs for that, if that sounds good.
Nimrod Avni 00:47:01 Okay, I have another minor question, because I think, Mattia, you told me, I think, that what you've been working on with, like, the trace profile correlation in the future, that the profiler might need to… kind of vendor Obi, Obi's definitions of, like, all the shared maps and stuff like that, and for that, we'll also need to, like, generate the.
Mattia Meleleo 00:47:23 Great effect.
Nimrod Avni 00:47:24 Basically.
Mattia Meleleo 00:47:24 I don't think we need that anymore, because we… once we agree on the shared map spec, they can just load it from… They can just redefine the spec and load it from the pin version.
Okay, cool. So, we don't need them anymore.
Nimrod Avni 00:47:42 Nice. So, I guess not.
Tyler 00:47:47 Cool.
Yeah.
Yeah, I'm looking… Florian, I'm looking at your comments about the binary blobs in the Git repo.
Using the go embed… I'm guessing this is… this is the EVPF blobs you're talking about? Like…
Florian Lehner 00:48:08 Yes. No, wait. Yes.
Tyler 00:48:10 Oh, okay.
Yeah, we talked about this last time as well, and yeah, it's, I think that Obi and, like, the auto-insertation for Go itself is also kind of in a unique situation.
Where, like, we've been contemplating this for a long time. This issue was open last week, but there's this issue that's, you know, many, many moons ago.
Created, and the idea here is that, like.
Yeah, most eBPF projects actually do exactly what you talk about in, like, just committing these files.
the… Problem is, is that, like, we have, like, a big numbers issue, for OB, because we have more of these files, and then we have a lot of dependencies, so any sort of, like, header changes, changes to all these files, any sort of… you know, update of new probes adds these files, maybe not nearly as bad as, I, you know, I originally thought. It definitely is a little bit more constrained, but the idea is that, like.
Within a year, we're gonna have a Git history, you know, on the order of a gig, and that's, you know, assuming no growth in any of these files and an average change across this. So this is something we've looked at.
This is the reason we didn't do this. It is a little bit of a unique project in that, like, this project is more organically growing a lot of different probes, and a lot of those binaries are interdependent, is kind of the issue. So, just kind of a heads up on why we're looking at going in this alternate direction, if that makes sense.
Florian Lehner 00:49:39 Yeah, yeah, sure, I wasn't able to try last time, that's why I just turned it.
Tyler 00:49:44 Yeah, and I'm not, sorry, I'm not, like, telling you, I guess I'm not telling you no, I'm telling you, this is our thought, if you have ideas on this… Yeah, please, please go ahead and comment on the issue. Like, I mean, yeah, like, we've been looking for solutions for this for a long time. Like, that issue's also a really great one, because it talks not only about, like.
committing… we talk about Git LFS, we talk about running our own module proxy server, we talk about, like, a bunch of different things to try to solve this, so, like, if you have other ideas, like, yeah, please take a look, I guess this kind of thing.
Cool.
We are running close up on time, so I do want to keep moving. Rafael, you wanted to talk about a quick update for the .NET TP injector work? Yeah. Yeah.
Rafael Roquetto 00:50:27 I'll make it very short. So, the idea of the refactoring was to be able to inject face parent headers.
on ingress.
and then letting .NET, forward, you know, propagate that… those headers. So, I had a… well, I have a prototype that kind of works, but… I've found out that the helper that I'm using, to inject this header sometimes stole the kernel TCP ingress queue.
There are a few kernel bugs, there are… yeah, it's… basically, it's complicated, so I'm… I'm… there is 90% a chance, at least that this is not gonna fly. I'm just, crossing all my, all my T's and dotting all my I's, but If that doesn't really work, then I'm gonna have to… see if there is anything else to be done. Seems like a dead end for now. And, I will upstream parts of what I've done, either way, like the ability of loading, having multiple C files, multiple translation units on a single tracer.
I found that useful, some other stuff, but yeah, I don't know what's gonna come out of that, so… I'll keep those guys posted. Just want to give an update.
Tyler 00:51:50 So, Rafael, this is for backwards compatibility support in .NET, or is this just for the modern .NET support?
Rafael Roquetto 00:51:57 modern .NET support, yeah, trace context propagation in .NET.
Tyler 00:52:03 Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:52:05 Yeah, I wanted to mention about that. So.NET will work now, unless it's the first application.
On the list of implications that we chained.
So, it's a current limitation, because they propagate the context, but they… and they will generate one for us. If there wasn't an incoming one, they will just put their trace parent on an outgoing request by default.
But… If we wanted to, if it was the first application in a chain of things, then… there's nobody to seed that initial trace parent, and OB cannot… if we cannot seed it.
Then, we'll make up our own, and then… You know, on the output, there will be something else that the client has, and those are broken traces.
Essentially. Because .NET will put something in there, which is… Can't tell which was the incoming request. And the way they handle internally the thread pools is just very complicated.
net does have a… a tracing interface that you can kind of, like, just like Java, you're gonna ask it to send you these details.
But it's… my impression is that it's async. I don't know… I don't know if we can rely on it. So it would be nice if they would tell us, but I think it's too late for us to generate the event.
So, something to look into, maybe another avenue of doing the same thing.
Yeah.
I don't know, maybe… maybe if that interface is on, we can just keep it warm, and then we can put a probe?
At the time that is generating the event.
So then, we'll get it.
And that will be synced for us.
So… That's worthwhile considering. Because they will ship amazing, but we… we just can't open up a dummy listener, so they'll have to go through the tracing.
And then… We, we tap into the tracing infrastructure.
Tyler 00:54:12 This seems reasonable. Seems possible. Rafael, does that track?
Rafael Roquetto 00:54:18 Yeah, yeah, that makes sense to me, yes. Okay.
We need to do some more R&D on that, but .
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:54:27 Yeah.
Rafael Roquetto 00:54:28 That would be the next logical step.
Tyler 00:54:31 Yeah, absolutely, yeah, we definitely need to… Shore it up, make it not just a… English sentence, but…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:54:37 Code, but yeah. Yeah.
Tyler 00:54:40 Okay. Well, cool, yeah, we'll keep it tuned. Thanks, Raphael, for the update. Yeah, we'll keep us posted on that one.
Nicola, next, you wanted to talk about the GenAI spec protocol. I can start sharing my screen again.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:54:53 Yeah, I just wanted to answer Matthias' question on… on… on the IP options? I think we should.
That's my take. We should take him out.
the only reason we have them in is potentially because… I think TC will work, even if our… other TP injector doesn't, but now that we have the TCP options, Yeah, I don't see why we should keep that IP options on, take away the tests as well. We have it in git history if we ever need to resurrect it, but it doesn't work anyways, right? Finally, the code, I thought we should keep it on.
Just to be able to kind of catch the sockets that are already established, but we found out it doesn't work. I think Rafael has an idea that maybe It's, it's a bug in our way that we populate that table, so… But if it's not for that reason, then we should probably take it out.
Rafael Roquetto 00:55:50 We got…
Mattia Meleleo 00:55:50 Thanks.
Rafael Roquetto 00:55:51 the, yeah, I… because I've been working on that, I think I saw… that we were using… the key we were using is the connection, info, but, I think it's unsorted, so… or sorted, so you only pick up one… one end of the connection. In this case, we want to really… we're overriding the connection. I changed that to use, like, a socket cookie. I'll see if we can… it can use, like, it can upstream that part as well.
And that might work, but… I agree that maybe regardless of that, are they…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:56:26 We can just keep that part. We don't have to do the IP options propagation, right?
Rafael Roquetto 00:56:31 So, yeah.
Yeah.
Cool.
Tyler 00:56:37 Okay, great.
Yeah, awesome, yeah. Keep going on that one. That's the end of the written agenda. We've got a few minutes left. If people have other topics or quick, shoutouts they wanted to make.
Any questions as well?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:56:53 I mean, I don't know if you want me… I just wanted to say a few words about the GenAI stuff. So, I don't know if you guys noticed this, but at least we've seen a bunch of people now, all of a sudden, this has proliferated, and caught on, like, fire, that people are adding Gen AI workloads related to anything touching OpenAI and traffic, and their applications.
And they expect that, there's gonna be a little bit more context than an HTTP request.
So when I find the stuff, like their tokens and everything, like, because tokens drive their costs, and they want to know how much tokens they've spent, and who's been sending those tokens, and which applications spend money, and so on.
And… there's no good support across the board on open telemetry for this, so I think this is a kind of an interesting use case for OB. We can quickly do this, then we provide a backbone for collecting this kind of stuff.
My understanding is Python has something, the Python SDK, but it only works with one API of OpenAI or something, not all of them, I don't know, so…
Endre Sara 00:57:54 I… I've been sitting in on the GenAI Sanity Conventions meetings, which is a lot of fun, but it… evolves, is a nice way to say it, very quickly. I tested it, especially in Python with OpenAI, Gemini, LightLLM, and, Yeah, maybe that's it. And maybe one more thing. There is a whole bunch of things about, chat, completions. Yeah.
And within the same SIG, there is also a lot of discussion about MCP, which is another animal. It's bundled into the same SIG, but I spent last week troubleshooting both my GenAI LLM chat completion and my MCP introductions, they were broken independently, and I, like, I wish I had some tracing.
So I rebuilt the actual agent with tracing, at least for GenAI stuff, but it would be great if, you know, it could be auto-instrumented.
Even if it's Python. And then I'm writing the same thing in Go, and I'm… I actually have an example, I think I showed you this, on Java, to do some OpenAI chat completion, image generation. It's a wide, wide waste. I will be so excited to work with you, Nicole, on this.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:08 Okay, cool, yeah.
Yeah, it's just gonna be… it's gonna be quite interesting, because I… I mean, internally, I'll tell you, Refana, we program all of this in Go, so the Python SDK, whatever support it has, it's not actually useful. And people will pick, like, Node.js. If their backend is written in Node.js, they'll just start calling the API Node.js, right?
And I won't write a Python application just to do this, so…
Endre Sara 00:59:34 Crazy Java people, but yes.
Mike Dame 00:59:37 I just… as a chance to plug it again, I've mentioned it to a couple people before, the LLMD, Observability SIG is always looking for, helpers, too, so I've been kind of involved with that, but any hotel experts, especially, you know, they're looking for it's more on the architecture side of deploying LLMs, but they have a lot of the same problems, and they're looking to, you know… the project is like a control plane for running LLMs on Kubernetes, so… I'll share a link to that community, and Would love to have some more people involved there that can help them figure out tracing.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:00:14 Cool.
Tyler 01:00:16 Yeah, awesome. This is great. Yeah. I'm excited to see this going forward.
Okay, we are right at time.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:00:22 talk, KubeCon Talk.
Tyler 01:00:23 Yeah, that's exactly what I'm thinking, too. Yeah.
Endre Sara 01:00:25 Yep.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:00:26 Okay.
Tyler 01:00:27 I, good talking with everyone. I will see you all in a week's time, or asynchronously. Until then, yeah, talk to you later. Bye.
