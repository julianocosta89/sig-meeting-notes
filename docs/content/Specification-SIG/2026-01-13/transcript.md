SIG: Specification SIG
Date: 2026-01-13
Duration: 118 minutes
============================================================

## Zoom Recording Transcript

Trask Stalnaker 00:03:14 Who's our merry narrator for the day?
Reiley 00:03:20 I think Bogdan.
Ted Young 00:03:24 I'm a little under the weather, so I don't want to do it.
Trask Stalnaker 00:03:28 Oh, it's a… it's a TC rotation responsibility.
Ted Young 00:03:32 Oh, even better.
Carlos Alberto Cortez 00:03:35 Yeah, I suggest we wait for both the number of minutes.
David Ashpole (dashpole) 00:03:45 Ogden asks if it's possible to switch for a different week.
He's recovering from a cold.
I can run, if nobody else wants to.
Carlos Alberto Cortez 00:04:03 That would be great.
David Ashpole (dashpole) 00:04:05 But… Let's see, Ludmila, tell us about, per-message span events.
Is Luke Mill on the call?
Carlos Alberto Cortez 00:04:23 Not yet.
David Ashpole (dashpole) 00:04:28 Alright, why don't… why don't, carlos, why don't we skip to your… your agenda item, then?
Carlos Alberto Cortez 00:04:33 Perfect, yes, let's do that. So basically, this is something I was discussing, a little bit with the JavaScript team.
Basically, this is about how to manage, how to handle auto resource attributes, environment variable.
There's a link there.
Actually, let me share my screen for a second.
But basically, the situation there is that it's… Barely specified.
And, one of the things is that it seems that different things… different Sikhs are doing different things.
So this is the one.
I will open it just to show you how it looks now.
So, basically, this is saying that the handling of this environment variable is done after… it's modeled after the W3C baggage.
Format.
And, all… for example, it mentions only that all attribute values must be considered strings and characters outside the baggage octet, which is basically ASCII.
range must be person-encoded. So, JavaScript is doing something there, like some handling, but then there were some discussions about making it better, and the thing is that, and I would like to talk to, maintainers on whether you feel strongly one way or another. So the first thing is that It doesn't mention what to do if you have invalid you know, sorry, I was supposed to write invalid.
invalid entries, you know? Like, what do you do? Do you draw up the rest? Like, for example, you're specifying 3 attributes?
And one of the, attribute values, has embodied characters, did you drop them? Did you… did you… drop everything, what do you do? So that's not specified. The second thing is that it mentions that values outside the octet the baggage octet value should be person encoded, but it doesn't mention… it doesn't mention who would do that. Like, would that be the user? Would the SDK try to do that for the user? And finally, handling of white space, you know?
Which is defined as part of Bagash.
But, it seems that some Sikhs are actually… Taking the white… any white space between values as, you know, as valid white space, part of the keys, or values, you know.
So, yeah, I would like to get some opinions on maintainers of this one.
Mostly as I said before, because it's underspecified, in my opinion.
Jack Berg 00:07:16 Hi Carlos. I'm writing some notes down here. I'm… I got the Java code pulled up just to kind of look at what we do. So, On some of these questions, so what happens if there's an invalid entry?
What we… we wrapped the entire… Reading of, this… environment variable, hotel resource attributes, in a single try-catch. And so, if there's a percent encoding error or typo in the the environment variable value that triggers an exception, then we fail everything, and we just short-circuit all of configuration.
So, like, we kind of do do fail fast. That's, like, kind of the philosophy in the Java auto-configuration module, so… That's sort of consistent. The next question, who should percent encode the values? We assume the user's gonna do that.
Handling of white space…
Carlos Alberto Cortez 00:08:19 That's… Look at some test cases for that one.
Trask Stalnaker 00:08:22 Yeah, I think that's the main, issue here, to my understanding, and I think in Java, Jack, I actually looked at this, I think we do allow white space, we don't fail.
On white space…
Jack Berg 00:08:38 So, can you give me an example of the white space, then? Like, are you talking about… so, like, the… it's a comma-separated list of key-value pairs, and the key-value pairs are separated by an equal sign? And so, like, are you talking about whitespace, like, you know, around the equal signs, or around the commas?
Trask Stalnaker 00:08:58 I think, yes, but also, like, white space in the value.
Right, so there's one question of what we should do with, like, around trimming, things, white spaces on the outside, but then there's also, I mean, white spaces could be inside the value. And I think Java accepts that.
Jack Berg 00:09:29 inside the value, that would be… because we use this URL decoder, which I think is part of the… standard library, so I think whatever we do is based on what that does.
Trask Stalnaker 00:09:43 Yeah.
Jack Berg 00:09:45 I think we do strip white space around the commas and the equal signs, though. So, that part is clear.
Trask Stalnaker 00:09:59 I mean, Carlos, I had asked that this had come up, I know the folks who had raised this in the JavaScript repo, I had asked them to open a ticket.
And to list the behavior of the different SDKs.
Because, I mean, it… it is… I don't think you're gonna get answers on this call of, like, nobody's gonna know off the top of their head how this is… is kind of, nitty.
Yeah. Issues.
Carlos Alberto Cortez 00:10:28 And so I can… I can do that. Sorry, go ahead.
Jack Berg 00:10:31 Yeah, and I guess, like, yeah, I agree with that, and it would be good to actually write out a list of test cases, like, because then people can just translate them to their language, and, you know, directly show the output, rather than having to, like, sort of guess on what the questions are.
Carlos Alberto Cortez 00:10:50 Yep.
I guess that the question is, well, I will do that as a follow-up, but I guess that the question is.
whether… let's say that different Sikhs have different behaviors. What would you… what… what should we do then, you know?
Say it's an implementation-specific thing, should we try to make them uniform?
What could be the suggestion here, you know?
Trask Stalnaker 00:11:13 I personally don't see a problem with spaces being in there. I mean, we just have to define, I think, the trimming, you know, like, the keys and values should be trimmed, but spaces inside of the values should be preserved.
It doesn't seem like that causes any harm, if, you know, as opposed to requiring users to percent in code spaces.
I was a little surprised when I saw that the… The environment variable format was based on the baggage specification. I didn't really see the connection between resource… environment variable and… baggage specification, I suspect maybe that was just, like, a convenience thing of, hey, here's some… Key value in coding.
That's already specified that we could leverage.
Carlos Alberto Cortez 00:12:14 Yeah, I think that was the case.
Trask Stalnaker 00:12:18 But as far as how to… oh, go ahead.
Jack Berg 00:12:20 I was gonna say that, a different way that we could take this is to say that, like, you know, the specification, make it, like, relatively, strict with what is with what is acceptable, and then state that, like, you know, other things, like whitespace and non-percent encoding, it's unspecified. So, like, basically, if you're doing those things, you're playing with fire.
And, you know, basically optimize the spec for the common case and provide incentives for users to do the right thing, rather than trying to make it as permissive as possible.
And the incentive here is by saying that behavior outside of this, like, this well-known path is unspecified, so it may work and it may not work.
Carlos Alberto Cortez 00:13:09 Yeah, that could be a good trade-off, I think.
Trask Stalnaker 00:13:14 But let's see what all the… let's get an issue tracking what the behavior is in all the SDKs, because I think that will help guide us.
Carlos Alberto Cortez 00:13:24 Yeah. It's fine.
Trask Stalnaker 00:13:25 that all, you know, almost all the SDKs are doing one thing already, then that will, you know, help.
Us.
Carlos Alberto Cortez 00:13:34 Perfect, yeah, I will do that, but yeah, I think that was an initial feedback that I appreciate, so I will come back next week, probably. Most likely.
Thank you. That's all on my sights… for now.
David Ashpole (dashpole) 00:13:57 Great, thank you. Sorry.
Forgot. Ted.
What's going on with Hotel Unplugged?
Ted Young 00:14:04 Yeah, we're… we're coming up on it, a couple of weeks out, three weeks out, so if people haven't heard, Hotel Unplugged is an unconference. We feel like we haven't had enough… in-person meetings, and certainly don't have enough events in Europe. We can sort of hang out with each other at Hotel Community Day, and KubeCon NA, but we don't have an Hotel Community Day, and we don't have a project meeting or anything like that, where we can just get around and talk to end users and talk to each other.
So as part of Fostum, first weekend of February, we're gonna throw Hotel Unplugged, which is an unconference. So, that'll be Monday, February 2nd. It'll be in Brussels, which is, like, a quick train ride from a lot of places in Western Europe.
So if you can be there, it would be really helpful. It would also be really helpful to just spread this around, LinkedIn and the OTEL community.
Just, just spreading a link, just, you know, take 2 minutes, take the link, and say, hey, if you're in EU, think about coming to this.
We look like maybe about, 70, 80, people will be attending at this point, but we'd love to get more.
So, that's all I got.
David Ashpole (dashpole) 00:15:26 Cool, thanks.
Jack?
Jack Berg 00:15:29 Hi, I'm acting as a messenger for the config sig.
Back in July, I opened up this PR to stabilize declarative config.
and the spec, and then… or back in June, I think. And, there's some feedback, and also I went on parental leave, and so couldn't get that over the hump.
We've, taken the opportunity to have a little bit more time to go and tighten things up a lot. We've added a lot more tooling and validation and kind of coherence and consistency.
to the declarative config data model, so it's a lot tighter than it would have been had we stabilized in June or July. And we've incorporated a bunch of feedback.
Into the spec, and we're ready to take another crack at this.
Soon. So, you know, the status over on the config data model side is that we cut, our RC3, our third release candidate.
Back in mid-December. And, we're waiting for just one more language to update their prototype to be RC3, and then I'll update the spec stabilization PR to be ready for review. So, my ask of folks on this call is if you have any feedback or any blockers, please voice them.
it's not great to kind of wait to the last minute to know that there's a big sort of problem that needs a lot of rethinking. So, yeah, If you have concerns, please let me know so I can address them sooner rather than later.
Ted Young 00:17:13 Jack, one quick question. Are there, are there, like, demo environments, in languages that are, like, fully up-to-date with the latest version, and, like, demo configs and things people could play with to get a sense? Like, something to make it easier to get end users to look at this thing?
Jack Berg 00:17:32 So the… in the Java SIG, we point a lot of people to this thing. We have a Java… a dedicated Java examples repo, and we steer a bunch of users' opening issues to our example that uses the Java agent with declarative config, because it unlocks things that are not possible to configure without jumping through a bunch of hoops.
So, yeah, I can include a link to that. That's for the Java case, and then, you know, other languages, I don't know their kind of example story as much as the, you know, my own backyard with Java.
I would say another thing that we're working on is creating, Jay DeLuca, he's on this call. So, we're working on generating, sort of, more comprehensive docs for declarative config, and syncing them with OpenTelemetry.io.
You know, right now, one of the main artifacts of declarative config is our schema that describes all the types and their properties and their semantics. And, you know, the schema is expressed in JSON schema, which is, like, it's really cumbersome to go navigate, like, a 700 or 1,000-line JSON schema file to understand the things that you care about. And so, we generated a human consumable artifact.
to navigate the schema and understand all the different things at play, and it has a bunch of things like, you know, interlinking between the types to show usages, and snippets to show little examples of all the different parts of the schema, and cool features like that. So, we're gonna get that promoted to Opentelemetry.io.
Ted Young 00:19:16 That's great.
I would say that's the only thing I'm noticing looking at the… because I've been interested in this, and then when I go look at the actual languages that are implementing it, it doesn't… doesn't quite seem like anything's, like, fully… Fully up to speed.
And I know… JavaScript, like, it's just a little bit blocked right now, because they're working on other things. Like, I know Marilia was trying to get it over there. So that would be my only piece of feedback, is it seems like you're trying to get the thing marks stable on a release candidate that doesn't have prototypes.
Jack Berg 00:19:50 No, there are a lot of prototypes, and I think it's, like, kind of… it's kind of overwhelming how many prototypes there are, because just off the top of my head, there's Java, Go, PHP, Erlang, some Python, some .NET, some JavaScript.
there's a lot of prototypes… C++ is a very important one as well. Like, there's a lot of prototypes that are at various stages, and one of the things we're tracking in this, and we're gonna get synced to Opentelemetry.io, is An implementation status document that allows you to understand the implementation status of all the different languages and all the different types at a glance.
And so, Jay has built some really cool tooling around that, and we're working with the communication SIG to get that up, so, like, if you're a polyglot environment, and you're thinking about using declarative config, you can understand whether the implementations that you care about are at a point where you can use them.
Ted Young 00:20:47 At a glance, like, very easily.
I'm just responding to the language implementation chart that you guys have.
And there's, like, a lot of implementations, but, except for maybe… maybe Java… maybe C++, maybe Erlang? I don't know that any of them.
Jack Berg 00:21:08 Go is a really important one, because they're… they're really aligned.
Ted Young 00:21:11 They're reporting it being at version 0.3. That's all I'm noticing. It's like, you've got a lot of prototypes, but you want to stabilize this latest version, and I… Maybe this chart just needs to get updated, and some of those, really cool things you're talking about need to get surfaced a little bit more.
Jack Berg 00:21:30 Two of the prototypes are at the… are at the edge.
are all the way up to date, and we're waiting for status updates on the other ones. There's some issues with the… the Go implementation is the one we, I think, care about most, because it's integrated with the collector.
And the collector, you know, is leaning on this heavily for internal telemetry, for configuring internal telemetry. And the issue with the… with the collector is that, you know, they want the Prometheus part of the declarative config data model to be stable.
And we're blocked on that from the Prometheus exporter specification being stable, right? So, like, that's… that's sort of, like, following the breadcrumbs back to why Go isn't at the head.
Ted Young 00:22:18 Okay. Yeah. Anyways, not trying to give you guys a hard time, I think I'm just trying to express this feels like a big project that has, like, a lot of effort being put in it and a lot of interest, but it's sort of like our typical OpenTelemetry submarine, where it's like.
you know, I'm pretty heavily involved in O-Tel, and when I… but I'm not involved in the config SIG, and when I talk to you guys, it sounds like there's, like, a lot of stuff coming, and, like, almost there, and it's, like, really exciting. But then I want to, like, evaluate it.
Jack Berg 00:22:50 I also… I want to remind folks that, like, the… what counts as a prototype for the purposes of stability is a PR.
Ted Young 00:22:57 Yep.
Jack Berg 00:22:58 We've litigated this in the past, so it doesn't have to be merged code, and so if the PRs have you know, are at the edge, the RC3, and if the maintainers reviewing those PRs are comfortable with it, then that's okay. So, like, even if the Go implementation isn't merged, and it's not integrated into the collector, it can still count as a valid PR.
Or a valid prototype for the purposes of stability.
Ted Young 00:23:24 I think I am just, trying to encourage, like, you guys have a lot of stuff, and I think my feedback is just, it's less visible outside of the SIG than it is inside the SIG.
And since we're trying to stabilize, I guess I'm just trying to encourage you all to surface these things. And it sounds like you guys are already doing a lot of this stuff, so sorry if that just sounds pedantic.
But that's my experience trying to evaluate it from the outside.
Jack Berg 00:23:54 Yeah, and there's a bit of a chicken and the egg issue, like, so, we're fighting against that as well, but I think the big thing we're doing that has not landed yet, but surfaces this more to the outside world, is the integration with OpenTelemetry.io. So that just, like, surfaces that to the users in a real way.
Ted Young 00:24:10 That will be very helpful. Thank you.
Jack Berg 00:24:15 I'll cede the floor.
David Ashpole (dashpole) 00:24:18 Awesome. Thanks, Jack.
So I have the next topic. I just wanted to follow up on the discussion last week on the opt-in advisory parameter.
One of the pieces of feedback was that people were interested in exploring metric levels.
And that concept deeper.
So… I… I tried to come up with a way For a metric levels concept to exist.
At the same time as This kind of opt-in parameter.
In a way that made sense.
And… This is what I came up with.
Which would be using views to produce metric levels.
Doing things like… Enabling or disabling attributes using cheaper aggregations.
Smaller exemplar reservoirs.
And then for more detailed view-based levels, you could have More metrics turned on, more attributes turned on, more expensive aggregations. It's mostly just a sketch.
But… Mostly, I'm hoping to avoid having to expose levels directly to Instrumentation authors, because it's always kind of a tricky.
Thing to get right, whether something is info or detailed or… You know, whatever.
I did also look into the history a bit of how metric levels ended up in the OpenTelemetry collector. And it turns out it's pretty ancient.
And the initial PR actually used metric levels to control which attributes were present on a metric, and not which metrics were actually present.
It was done back in the Open Census days.
So… Yeah.
I'm happy to… Answer potential questions, but my goal is mainly to unblock the work on the opt-in parameter, or the opt-in advisory parameter.
Liudmila Molkova 00:26:24 Yeah, David, it makes sense. Thanks a lot for the, educating, at least me on the levels in Collector.
We do have metric or attribute requirement levels. There are… three of them. The opt-in, recommended, required, and maybe at some point, we probably should merge attribute and metric requirement levels, but leaving it aside, we do have some levels, and your opt-in level that you're introducing is synonymous to this one. The instrumentation authors know about these metric levels.
And, the idea of recommended, that they are opt-outable, right? So, they're required to always be present, you can disable recommended and still get some value, and you can enable opt-in if you're brave.
So, would we… if we introduce the Boolean opt-in enabled flag, we would need to do the same for recommended.
David Ashpole (dashpole) 00:27:33 Good. That's… that's helpful. And then, presumably, You could have one additional level, if you were using views.
That turned on all the recommended ones.
Or that turned off… turned off all the recommended ones and only kept the required ones. So that would enable you to have, like, one more level of detail if you wanted to turn everything On or off.
I see a thumbs up from Josh.
Okay, I think… I guess, is there any other feedback or ideas? Otherwise, I think I can try and update the proposal to support.
opt-in or recommended. We don't really have a mechanism yet, To use Recommended?
So I'll have to think more about How that would interact with views.
Jack Berg 00:28:26 So… So, just… I need to read this PR, and I'm sorry that I'm not caught up to speed on this. There's a lot of things in flight. So, a summary of this is roughly that there's a new advisory parameter, so a new portion of the API, that would specify different, what are we calling these things? The requirement levels, or.
David Ashpole (dashpole) 00:28:47 There's a… The way the PR is written today is that there is a new advisory parameter, opt-in, which just is a way for the instrumentation author to say, this should be turned on by default, or turned off by default, right? So, opt-in equals true.
Turns it off by default.
And then the user today would have to go in And in the view, set enabled to true.
We initially were gonna use… The default aggregation.
Jack Berg 00:29:16 Yeah.
David Ashpole (dashpole) 00:29:17 But during the discussion, we figured out that actually a lot of use cases today, someone might use the default aggregation as a fallback. Like, I want to enable exponential histograms.
And then for everything else, just use the default aggregation.
And so, for people who are using default aggregation as Keep everything the same.
They would end up… Blasting on all their default disabled metrics.
So, we… we would add to view an enabled field. So, if you wanted to enable everything that was previously disabled, you'd just set it to true. Otherwise, leaving it unset just keeps the default behavior.
If that makes sense.
Jack Berg 00:30:03 Yeah.
is… there's some overlap in terms of, like, you know, enabling or disabling an instrument via the view, and with this new enabled flag, and then also with, like, the drop aggregation? Like, two ways to do the same thing, but maybe there's not a way to get out of that.
David Ashpole (dashpole) 00:30:20 Derek.
There isn't a great way, and in some ways, I actually think it's an improvement in ergonomics.
Like, yes, the drop aggregation makes less sense, as a thing.
Jack Berg 00:30:37 I just wonder if, like, is the drop aggregation used anywhere else? Like.
you know, we kind of have this mentality in OpenTelemetry sometimes of, like, hey, we don't want to have two ways to do the same thing. And so, like.
Is there a route to deprecating the drop aggregation if we have this, like, more clear mechanism for just, like, explicitly saying that a metric is disabled?
And I don't think it necessarily is part, like, blocking your PR, but, like, maybe it's part of the conversation.
David Ashpole (dashpole) 00:31:07 I think it's part of the conversation, but I would probably… I'd have to think about it more to make sure, but I don't know of any other use cases. Like, drop aggregation is not part of default aggregation in any way.
It's just available to users to set, and only on views.
Jack Berg 00:31:22 No, the other place it shows up is on metric readers as well, because metric readers can specify an aggregation as a function of type.
So, like, those are the two places the drop aggregation shows up as part of the interface.
David Ashpole (dashpole) 00:31:34 I, like, couldn't replicate it then, unless… Yeah.
Jack Berg 00:31:40 Anyways, yeah, thanks for the summary.
David Ashpole (dashpole) 00:31:45 Trask.
Trask Stalnaker 00:31:47 I just… I wanted to circle back to what Vanilla was saying, and I didn't quite follow the connection to the recommended Requirement level.
Was that, was that discussion just about this possible future level, Advice… Or is that… an alternative to, David's current opt-in metric advisory parameter.
Liudmila Molkova 00:32:23 I…
David Ashpole (dashpole) 00:32:23 be an alternative, I think. Or, like, a… more general version of it. I still have to think, like, things get a little funky with Yeah, I would have to think about it more, because… it doesn't… it doesn't have meaning on its own without some sort of SDK config, right? Like… the fact that I marked something as recommended.
Presumably will have the same implication that it does today.
Of just a metric being enabled, but presumably there's some mechanism that can Like, we have to introduce config or a knob somewhere that allows you to Check to see if something is recommended, and then, like, decide to keep it based on that, or decide… Right.
Trask Stalnaker 00:33:12 What's the use case?
For… for that?
David Ashpole (dashpole) 00:33:18 So… like, when I was writing the, like, hypothetical metric levels, design, right?
one thing that I came across that's a bit of a limitation is that there's no good mechanism to, like, as a general statement, reduce the number of metrics that the SDK emits, right? So.
the only way to go and say, I have 100 metrics, I'd like to keep 50 of them, is to go turn them on or off.
Individually?
And so.
if… and I don't personally have any, like, user evidence of needing this, but, like, I could imagine… actually, the collector does this, so maybe there's at least some precedent where if you… Just run the collector, you'll get… You know, some set of metrics, and then if you set it to basic.
You'll drop some of the more expensive metrics, and keep just, like, requests and errors, or something like that.
Trask Stalnaker 00:34:24 Okay, thanks, because I hadn't really seen the, what I've seen from Java, users is they want… It's just about opting in to specific metrics that are opt-in, so, like, this seems like the… your current PR feels to me like the simplest Or, you know, solution to that use case, so I think it would… I just want to make sure that the more general thing is grounded in user… Demand.
David Ashpole (dashpole) 00:35:01 Yeah, I… I was hoping… With the metric levels.
That are based on views, that just making the aggregations cheaper, and maybe reducing cardinality on attributes or something would be enough.
to get, like… so this is the opposite direction, it's like… I turned on my Java agent, and it gives me too much stuff.
Is there a way for me to ask for less?
Jack Berg 00:35:26 That… I mean, there's knobs for that right now.
David Ashpole (dashpole) 00:35:31 Just using views, or…
Jack Berg 00:35:34 It depends on what you're trying to do, but yeah, you can, the knobs that come to mind is, like, you know, if exemplars are your problem, you can turn off exemplars. If, the histograms are too, too fine-grained, you can adjust the histogram buckets at the reader level.
Or adjust them to exponential. And if your individual metrics are too noisy, you can disable them at the view level altogether, or you can adjust their cardinality via attribute keys at the view level.
David Ashpole (dashpole) 00:36:03 So those are the knobs.
Jack Berg 00:36:05 That you have.
Liudmila Molkova 00:36:07 Yeah, so in the perfect… yeah.
In a perfect world, we could have, some sort of a profile. It's a very theoretical feature that nothing exists, right? So, very, essential, very, verbose, and something in the middle. I think this is what we are trying to achieve with the requirement levels.
Trask Stalnaker 00:36:30 What… the piece of that that I struggle with, though, is are… is there really a one-size-fits-all profile? Like, normally, what I've seen is people want to turn off, like, specific metrics that aren't useful for them. I… as a… maintainer, I think I would have a hard time drawing that line of… In the middle, like, the opt-in ones are clear to me, like, and that one feels like a good story.
But I don't know how to define that middle layer.
Liudmila Molkova 00:37:06 So what we do today with you in semantic conventions, we try to define this for attributes. We actually, I… while we were talking, I've checked whether we leverage the requirement levels in metrics, whether we have a clear distinction between the required and recommended to answer a question if it's grounded in the user demand, and it seems we don't. It seems we use required versus recommended randomly across different metrics, and they don't carry the actual meaning. And… that's maybe the feedback back to the metric requirement levels, that we don't care. We should probably just say, okay.
there are, I don't know, recommended or required an opt-in.
David Ashpole (dashpole) 00:37:55 Yeah, I think… It does feel like there's a mismatch, at least, between the current proposal and, like, the way that we write our semantic conventions, so… It's maybe worth exploring. I do… I feel like opt-in is much more useful, at least today, than the other levels.
Liudmila Molkova 00:38:18 I would not, be against just… building the story for opt-in. It seems for the years we had, we didn't need the recommended for metrics anyway.
Jack Berg 00:38:38 It just… I'm trying to decide whether or not to say this or not. I'm gonna say it just because… you might end up doing extra work if I don't. So, like, remember exemplar filters? How we were deciding whether or not they had, a rule?
And views, whether they should have a knob on views, and we said no. They shouldn't, because, like, most of the time, what you want to do is you want to configure, like, an SDK-level profile, for example, ours, that say whether they're on, off, or trace-based.
And so the only knob that you have is at the SDK meter provider level.
And so, like, the reason to have a knob at the view level is for granularity, but it's really bad ergonomics. I've talked about this before, but views have, like, a terrible merge semantic.
And so, like, if you have views that could collide with each other, it can quickly get out of hand and produce, like, sort of unexpected, unintuitive outcomes.
And so, like, the reasons to have a knob at the view level is for granularity, but the reasons not to have a config at the view level is usability. Views have bad UX compared to having knobs at SDK meter provider level.
And so, I'm wondering if we should follow a similar train of thought as what we did with the exemplar filter, and start with a knob that is up at the SDK meter provider level, that's like this profile.
level configuration knob, rather than a fine-grained configuration knob, and expand down to views if we need it. Like, basically, we have to take a bet on what will help more users, whether more users want a fine-grade knob, or more users want a profile-level knob.
I don't… my intuition says a profile level knob is easier UX and is more, is more useful to more people.
Trask Stalnaker 00:40:27 Does meter provider level mean scope level?
Jack Berg 00:40:31 It… I… that… that could… that's another Right? You could do… you could do meter provider, scope level, or view level, and those are kind of, like, getting more granular as you go.
Trask Stalnaker 00:40:41 Meter Provider Global?
level.
Jack Berg 00:40:44 It's… that's global level. Yeah, that's across all scopes.
Trask Stalnaker 00:40:47 from… just from the Java users I've seen, I don't think that would be useful for them, because that would opt them into all opt-in metrics, which they don't generally want, but I could see possibly the scope level would solve their issues, and that's what we generally do, like, for… for example, for our experimental Telemetry, we just have, like, a scope-level config setting that says, give me all the experimental telemetry, we don't itemize dot.
Jack Berg 00:41:34 This is going to be a recurring debate with every new config knob that we add. Should it be the global level, the scope level.
Or, in the case of metrics, all the way down at the instrument level.
David Ashpole (dashpole) 00:41:47 I… I do feel like the idea of a view preset Like, building… building a global feature.
That depends on views has a lot of merit, because… Then maybe we can have the best of both.
And I think if we did that, we would also address the mergeability of, like, these Global, kind of, default views, and… the, like, particular… Modification of some metrics.
But I haven't… I wrote something like that down in the view-based metric levels.
issue, but, I don't think it's fully fleshed out yet.
Alright, thanks for the discussion. Please… If you have thoughts, write them down on the issue, or on the PR, and we can… Work through them.
Josh, you're next.
Josh Suereth 00:42:54 Alright, so, just a few entity SIG-related updates and things to talk through.
The first is a big one, which is, a definition for the data model for entity events. So this is trying to define, the state of entities in your system and their relationships with each other.
Go ahead, Tigran.
Tigran Najaryan 00:43:19 No, sorry, go ahead, finish your thought. I had a question about the PR.
Josh Suereth 00:43:23 Okay, yeah, so, effectively, for those of you unfamiliar, we already have a collector component in the, Kate's Object Receiver, I think it is? Not the event receiver, the object receiver, that, like, will report, like, what available… Kate's objects you have. So, this would be deployments, pods, nodes, that sort of thing.
as part of the entity SIG, we want to be able to define the relationships between things. So, for example, you could report yourself and say, hey, I'm a service, and I am part of this pod, but someone else can describe that the pod is part of a deployment via relationship. So, this is meant to be a proposal on the data model.
for, entity, events, states, and relationships. So there, there's an entity event, this was in the original, proposal from Tigrin, and this was expanded on by Dimitri. So.
Please take a look. We just had our first discussion of it in the last SIG, but I think this one's pretty important that we kind of all pay attention to and watch. Go ahead, Tigran.
Tigran Najaryan 00:44:28 The question I have is, do we think that NC events will also become a native signal in the future, and so that this is a possible representation using log record?
Or this is the only way to represent entity events, and we don't plan anything in the future.
Josh Suereth 00:44:47 So, so right now, it is a data model. That data model can be expressed as log records, or could be expressed as its own signal. We have not made that decision yet.
Just focus on what the contents need to be of a message, and what the interaction with that message should be from systems.
Tigran Najaryan 00:45:04 Okay, but you're leaving that door open, from what I understand, that the possibility is there. What I would advise in that case to do is to split this document into two parts, one being A logical data model, which describes the concepts and what we want to represent, the two types of the events, like the state and the delete.
And then the second one, how do you represent that logical data model using log records? That then leaves the option for describing, then, how do you represent the exact same logical data model using native protobuf definition. I think that would be the right delineation.
Josh Suereth 00:45:46 You should make that comment on the PR. From my understanding, the examples that show log records are not meant to be definitive, they're meant to be examples. So this should only be… this PR should only be the logical data model and how to interact with it.
And then it gives you examples that are practical, given, like, how the collector works today, but that's not meant to be, like, you know, that's not the important part of the example. The example's just a… you know, how you interact with it. The important part are things, like, from the OTEP, which is, you know, you send a status update every once in a while with all data, and then you have an additional delete method, it's talking about how to keep things in sync. Like, that's what we're focused on right now in the data model.
Tigran Najaryan 00:46:26 Okay, I agree with what you say, but when I read the PR, that's not what I… what I get from the PR, because the very first sentence says, entity events provide a way to communicate entity information as structured log events. That's where it starts, immediately, right? Yeah. I would advise that to be somewhere later, here's a way to represent entity events as structured logs.
Josh Suereth 00:46:51 Yep, feel free, again, if you see that in the PR, comments on it, the focus of this is, let's get the data model correct for reporting. We're using logs today to do all the prototyping, but, like, the data model should be independent of the vehicle.
Tigran Najaryan 00:47:06 Okay, okay, sounds good. I'll… I'll take… I'm reviewing the PR right now, I'll do that.
Josh Suereth 00:47:12 Cool.
Awesome.
So, we can go into details there, but I think that it's better for folks just to read up on that. The second thing is the entity merge algorithm. We got a bunch of reviews before, made a couple updates, just want to remind people of this PR. This is the merge algorithm for how to create a resource in an SDK, or in a collector, when you have an existing resource that may have entities in it, and then you have just a collection of entities. So we're trying to update that merge algorithm to be a bit more rich, based on feedback we have.
And how to handle failure scenarios. There's one update I need to make to it from the entity SIG, but for the most part, I think the algorithm, we want to make sure it's readable, well-specified. We have several implementations of it in different SDK, prototypes.
And I'd like to start bringing this to SDKs soon, as, like, official, you know, experimental, in-progress stuff. So, yeah, if we could get that reviewed and make sure that all of the concerns folks have are outlined. I think almost every comment should be addressed, and there's one last one I'm gonna do shortly.
Okay, the last one is… this is an OTEP that we'd like to… From an entity SIG perspective, we'd like to kind of get approval in this direction, and then kind of table the OTEP for now, because we think we're going to have to focus on stability efforts, and we're trying to limit, what we're doing with entities, but this is about allowing an SDK to report data against multiple resources.
It proposes a notion where you can take a provider.
like a meter provider, a tracer provider, and you can say, I want to create a new version of this.
That will report data against this set of entities.
And then it will use that merge algorithm I just mentioned to create a new resource, and then it will report data against those new sets of entities. It would share the existing pipeline that you already have set up for exporting data, and so these pipelines would get updated to allow multiple resources to be reported from an SDK. We don't think the collector needs anything to support this, because the collector already supports handling multiple resources.
that's what that OTEP is about. We want to kind of get alignment on that vision of, like, does this make sense as the right way to do multiple resources and things? And we might table actually driving this through SDKs and bring this back up after some of the other higher priority work has completed.
But I just, like, because it's close, because a lot of people reviewed it, and we had a lot of good comments, I want to try to get to this to the point that we agree on the direction, and then table it. Is that fair?
Okay.
If anyone has thoughts or questions on those, we can talk about them now. Otherwise, please, please, please review. Thanks.
Liudmila Molkova 00:50:24 Okay, I think this is my topic. So we are moving forward with RPC deprecation.
And one of the things we don't, really want to target is… representing… messages in the stream as a part of our PC stabilization effort.
So… We would have some basic observability into the streaming, but not the messages.
Currently, we define her message as pan events.
And the SPAN events deprecation, in doubt, and upcoming deprecation in the SPAC, this is not a viable approach in the future.
So what we are proposing is to deprecate these events without a replacement, so instrumentations that emit them would, keep emitting them as long as they support the whatever old version of semantic conventions.
With, new version semantic conventions opt-in, or with major version BAM, they will do… they will stop emitting those.
The usefulness of these events is also somewhat questionable, but essentially, we can always add them once we get feedback.
from the people who actually need them. So my ask here is, if you know that they are useful.
Or if you have some thoughts on how they can be useful, please post your comments on the issue, or speak up now.
Thank you.
David Ashpole (dashpole) 00:52:10 Thanks.
Any other topics?
Carlos Alberto Cortez 00:52:14 Tev, I think that you wanted to talk about potential of the roadmaps last week, but… I think there won't be time for that, maybe.
Jack Berg 00:52:30 8 minutes is not nothing.
Carlos Alberto Cortez 00:52:34 Yeah, I don't know, or better said, maybe it won't be enough.
David Ashpole (dashpole) 00:52:43 I would… I would probably argue for tabling that for a different week.
And maybe getting it earlier on the agenda, if we want to tackle that.
Did you say Ted was gonna lead that?
Carlos Alberto Cortez 00:52:54 Yeah, I remember a point, last week that, Ted, you mentioned that Do you want to discuss that this week?
Ted Young 00:53:02 Sorry, discuss what? I'm still sick, so I'm half paying attention.
Carlos Alberto Cortez 00:53:07 Oh, sorry, the other roadmaps, you know, the Charter for SIGS.
Ted Young 00:53:11 Yeah, yeah, I feel like we want to, in general, figure out for OpenTelemetry as part of graduation. We know that we have work that we want to do across the different SIGs. We know that up till now, OpenTelemetry has some… had something of a roadmap with tracing metrics and logs, and we're kind of concerned that coming to the completion with logs, getting stable, having, like, no roadmap now, and just kind of hacking on the spec doesn't feel like enough. Like, there should be a little bit of structure.
But… On the GC, you know, we're still not entirely sure how that should work, and we want feedback from SDK maintainers, about how they would like that to work.
On the one hand, you know, we… it's great when we focus our efforts and try to get things sort of done with a lot of concentrated attention, and then move on to the next thing. But we also don't want to get in a habit of telling people, no, they can't work on the thing that's exciting to them.
So, I don't have any details, but if this is something that maintainers have feels about, please let me know.
Because we just want to, in general, get a discussion going about how we can do project management that gets the community more involved, people having a better sense of what they're going to get out of OpenTelemetry in the future, but doesn't feel like we're… we're really, like, locking things down from some, like, top-down approach.
So… That's the hope, but I don't have a concrete, like, proposal to give to anyone right now.
Does anyone have any thoughts and feels on that right now? We've got 6 minutes.
4 minutes.
Jack Berg 00:55:08 I feel like, In terms of levers that we have, we've talked a number of times about creating tooling to create issues and sub-issues when something gets merged to a spec. So, issues tracking, like, hey, we introduced this new feature at the spec, and sub-issues for each of the language implementations.
If you had that automation, you could build Tooling on top of that to see, at a glance, how things were progressing.
And, like, you know, that would give you the, I think, visibility to understand maybe where things were lagging behind.
That need to be emphasized?
Or, like, maybe where you're at a point to stabilize something because it, you know, it's got enough, you know, implementations, prototype implementations, and I think that would go a long way to supporting this type of prioritization. We're kind of in the dark right now with, like, where all the different SDKs are along their maturity path for all the different features.
And these things seem intertwined to me. That's my bit of feedback.
Ted Young 00:56:22 Totally agree.
Something we have right now, kind of loosely, is sort of a GC liaison.
program, but that's really basic right now. The whole point of it was really just to say, hey, rather than, like, forcing maintainers to, like, bring something up, like, let's just make sure we're at least checking in with maintainers at some cadence, so there's some opportunity. If there was something brewing, they could be like, hey, I need help with X or Y. Like, let's make sure we check in.
But it's not, like, something that's, like, a big, hey, let's discuss the roadmap of this SIG, and, like, where are you guys at with implementing, you know, OpenTelemetry, this or that? What do you want to work on this quarter? What do you think's realistic?
Because the reality is, like, all these SIGs are in different spots. For example, the Kotlin SIG started recently, where they're trying to implement stuff in Kotlin. Like, where they're gonna be is, like, totally different from where Python is gonna be.
So, there's, like, some SIGs where we could say, like, everyone try to go implement config right now, but there's also some SIGs where having, like, you know, they're just in, like, a totally other spot.
So… that was one bit of feedback we got from Daniel Dyla, which was, like, just having, like, a set of topics that we're all north-starring towards doesn't… totally work for everybody, that only works for some SIGs that have been around for a really long time.
Jack Berg 00:57:51 But at least the signal could be there. Right now, we don't even have, like, a good mechanism for getting the signal out to SIGs, because not everybody convenes in any location. There's no one meeting that every maintainer or even a majority of maintainers attend, right? So, like, this tooling that we were discussing, like.
If you had issues and sub-issues for each feature in the specification and their implementation status, and all the different languages, you could use that also as a mechanism to communicate signal out to these things, because you could annotate those sub-issues with labels that indicated their priority level. And, you know.
if the GC annotates issues as, like, a higher priority, that is going to come up in these SIG meetings. Like, the so-and-so SIG, you know, people will be like, hey, look, the GC opened this issue against our repo, and they say it's important to us. That's going to impact what they do.
Ted Young 00:58:44 I think that it's interesting, we were trying to model this. We've been, you know, not secretly, but we've been trying to model this stuff using GitHub projects. And we're running into this wall, which is, like, if it's any info that's just in, like, the project data model, you just don't see it.
it's not in people's faces enough, and so it's like, we're just doing it for ourselves, and then it's not very helpful. But actually, they've… some recent improvements, like sub-issues and stuff like that.
It's not like you get a fancy UI like a Kanban board or something, but maybe that really was all we were missing.
If you can make sub-issues across different repos in the same project, it might just be easier to kind of create more of these lists, like what you're doing with config or something else, where we… it's just easier for people to follow the breadcrumbs from a major initiative to what the heck People are actually doing on that initiative.
Yep.
Cool. Well, food for thought, but if anyone has seen, stuff from other big open source projects that they like, in terms of this kind of stuff, you know, definitely bring it up.
We want to get it sold.
I think that's all we got time for, though.
David Ashpole (dashpole) 01:00:05 Yep, we're out of time. Alright, thanks everyone.
Jack Berg 01:00:08 Gotcha.
Reiley 01:00:09 Thank you.
Trask Stalnaker 01:00:10 Bye.
