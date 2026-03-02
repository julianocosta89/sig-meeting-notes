SIG: Collector SIG
Date: 2025-07-02
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 01:07 Hey!
**Evan Bradley** 01:12 Hey, there!
Should we get started?
**Dmitrii Anoshin** 04:16 Sure. How's that?
Hi, everyone!
**Pablo Baeyens** 04:32 Drop your first.st
**Jade Guiton** 04:39 So
my point here for today is to announce a slight amendment to the pipeline component telemetry. Rfc.
the idea is that if you're not aware that Rfc defines
2 things. 1st of all, in what way we
set attributes on the internal telemetry of collector components
in order to be able to identify them.
and second, it defines ways in which we want to instrument the collector pipelines to generate internal telemetry automatically.
And the amendment here is about reflecting some of the changes to the implementation we've already made.
So, for example, we are the the pipeline instrumentation. Sorry.
the components identifying attributes that we're automatically inject injecting into the collector's internal telemetry were switched from data point attributes to instrumentation scoop attributes
that that's a decision that's been made some time ago, and it wasn't reflected in the Rfc, so my pr updates, that but the more significant change is about something which hasn't been implemented yet. Which is tracking the outcome
of
the outcome of calls throughout the pipeline. So when a component calls another downstream component to pass some data that call can return an error or not. And right now we set an outcome attribute to either success or failure, based on that
what the Rfc. Prescribes is to have a 3rd value for the outcome, which is refused
to indicate that the error that was returned did not originate from
that next component. It's it actually originates from further down the pipeline. And we're just bubbling it up.
So the it's a very slight change. But the idea was that
currently the Rfc. As written, specifies that outcome equals refused should apply to both the component in which the error originated.
Oh, sorry outcome equals failure should apply to both the component in which the error originated
and the component just upstream of it. Basically, the attribute will be set on both sides of the interface
to which the data was passed, which I find kind of confusing, and I think users might find confusing as well if they see outcome equals failure on a component that did not, in fact, fail.
So the slight change is to change that case. 2 outcome equals refused.
It's pretty technical, but if you're interested in
if you think this might be a mistake, or if you're interested, please check out the Pr
it's already been approved in multiple times. But this is because it's a change to an Rfc. There will be a waiting period for people to comment.
Yeah, I think that's all about that.
I hope my explanation was clear. But it's a bit of a technical change.
**jmacdonald** 08:22 I just want to say that that makes a lot of sense to me. And the other way, the way it was written doesn't make a lot of sense to me. So thank you.
**Evan Bradley** 08:39 Is there some rewording we should do inside of the Rfc. To make that a little bit clearer.
**Jade Guiton** 08:47 Make what a bit clearer I I tried to in my Pr. I tried to reword some things to make it as clear as possible, but
It might still be confusing.
so please take a look at the wording in the Pr. I guess, and make suggestions.
**Pablo Baeyens** 09:17 I added the final comment period label, and I'll put a comment saying that we can merge these.
I guess. July 9.th Probably we can give one more day. Given independence. Days in between on a lot of you are in the Us.
**Jade Guiton** 09:38 I'll also post a link to the
Rfc. In the Dev Slack Channel as as intended by the founders.
Maybe we can move on to the next point
just by polling.
**Pablo Baeyens** 10:19 So let's go to the next one, and
we can come back. If if he's able to join, I will ping him and.
**Sam DeHaan** 10:32 See if he can join. He works at Grafana with me.
**Pablo Baeyens** 10:36 Okay, yeah, he said he was. He had some sort of conflict with an article in a slack thread. So.
and since I am talking. I guess I will cover Biha's
Rfc, so this is another Rfc
is is related to a previews
feature flag that he has worked on regarding how to merge configurations while
appending things on slices instead of overriding them.
Because that makes it easier to yeah. Split your configuration into multiple files, and you have a list of receivers, for example, and you add them there.
So this tries to figure out how to configure the merging behavior. And
yeah, there's some discussion here about how to do it, whether we use
See a life logs, whatever we use, demo tags, or
and what kind of of flex. Do we want to support?
And yeah, I don't know. I think that's mostly it. I guess.
**jmacdonald** 12:06 I read your feedback, Pablo, on the on the Pr. And you mentioned something about Yaml custom tags or vias, did I clicked the link, and couldn't find the word custom anywhere in the document. Did you want to tell us what that is?
**Pablo Baeyens** 12:19 So the yaml spec allows you to define arbitrary tags. I don't know if custom tags is the name.
but the same way you can have, like
2 exclamation marks, and then Str to make something via a string.
You can have your own defined types. Let me see if I can find a link
that I can share.
If you look at. Yeah, example 2.24 us, a shape.
**jmacdonald** 12:55 So.
**Pablo Baeyens** 12:55 Full line.
so it would be something like that. I don't know if this is a good idea or not, or how easily supported it is, but I think it's worth exploring, because it's like the standard Yaml way of
specifying types. And if we have, like a mergeable array type or something like that. Then maybe we can. We can make it work that way.
Evan.
**Evan Bradley** 13:26 Oh, so this is a separate point. I mean, we can discuss. I think the tags are good, although we'd want to make sure that you can override that in certain cases. I mean, I could see that, for example, for
the transform processor, I could see us having statements be append by default. Possibly I don't want to commit to that. But you know, of course, there's also cases where people layer their configs in such ways they might want to override it.
Now, I wanted to talk about how we basically point B here. But I don't want to interrupt Josh. If you have anything else to say on that.
**jmacdonald** 14:01 Oh, oh, no, I I mean this. This is tricky, because Yaml is such a complicated specification, like, I think that's the the 1st reaction that I have.
and I, I can imagine some other solutions. You know. I think you're you're imagining, like we have control over the types of the go objects, and we have control over the unmarshalling procedures.
Why would we use query arguments or query parameters, as as was proposed as opposed to just like listing file names in fields.
and like, you know, you could embed a like, expand me yaml, file type and and give a file name and put it in line wherever it appears. I've seen that done. It's complicated, but everything is complicated here with configuration, and I'm not sure this is better. I'm just curious if anyone seen other patterns.
**Evan Bradley** 14:55 So, if I understand you right, the the reason that we're using the query parameters is just to configure the keys that you allowed to merge. Not necessarily which files you're going to merge.
**jmacdonald** 15:06 Okay.
**Evan Bradley** 15:08 The goal is that you might not necessarily I mean, I guess part of the the reason we're being so cautious about this. You might not want to merge everything. You might want to only merge certain keys, and then everything else gets overridden. Which is, you know, the default behavior. So. But we wanna make it so that you can, you know, specify just the ones you want, or, you know, just put a big asterisk there, and you know it does everything.
**jmacdonald** 15:30 Okay.
**Dmitrii Anoshin** 15:31 And also, how do how you merge? That's important, whether you prepare independent, whether you allow unique values or not.
That's also something that we want to make configurable.
**Evan Bradley** 15:52 Okay, I think I can. Or Josh, are you good.
**jmacdonald** 15:56 Yeah, I'm I'm great. Thank you.
**Evan Bradley** 15:57 Okay, cool. So I wanted to talk about the the query parameters thing, because I've been thinking about that for a while.
and this is a good opportunity to talk about it. Do we? So, Dimitri? You suggested that query parameters are all right, but I know we had discussed previously. I think Pablo is there as well. That. We were thinking about putting this all in a
I don't know if it'd be a separate config file the same config file as the collector config and configuring it that way.
Did you have any more recent thoughts on that.
**Dmitrii Anoshin** 16:27 Yes, I believe that that's the way to go, because for some config providers it can be like the Con configuration interface for some config provider might be too complex to put them in query params. And I believe we need a way to like separate them somewhere else in separate section being config providers something like that. So once, if we have that, and we duplicate and remove query params
in in favor of that approach, then we good? We can. We can keep a query params specifically for the immersion. Let's say
everything that is not applied to the config provider specifically. But how we treat like those arguments in general for the collector.
If if that's if that's what we can agree, that's good way to go. At least, if we agree that we will have that capability going forward, that then we can resolve this, and we will not have any conflicts.
because, like sharing
query params, for even if if it's unlikely to have conflict sharing them for 2 different purposes, that doesn't seem right to me at this point.
**Evan Bradley** 17:52 I think ultimately we'd probably want to consider how we could put these configurations options in a file as well. But I mean, as long as it's bind a feature gate. I think.
I'd be fine with query parameters for now, and we can reevaluate later.
**Dmitrii Anoshin** 18:07 Yeah, sounds good.
**jmacdonald** 18:17 Shall I take the next item?
I have a few in flight pieces of work related to the collector, and I thought, just fish for interested parties. I'm mostly looking for reviewers and people with opinions on these topics, so I'll run through them very quickly. The Batch processor has been neglected for a long time, and there's talk of replacing it with exporter helper feature now that it's basically finished, not feature for feature could finished, but finished
in a in a stable basic way. So I think that's a good idea to stop recommending the batch processor. We've talked about this. I opened the issue on the documentation site because a lot of it's in the opentelemetryio Repository.
Okay? So next one, I've been working with Bogdan and a couple of people on rate. Limiter Apis. It's not what I want to talk about, but there's a pattern that's emerged, and I realize it had been talked about a lot, but never documented. So this second Pr is about a functional composition pattern.
If this interests you. Bogdan has left some comments, and it left me with lots of questions, and I want to discuss them in there. The question is, how extensively do we apply functional option patterns on top of the existing pattern that I've already documented.
There was some a couple of issues here about printing configuration, and I got involved in that this past week. There! There's an open feature gate protected command called print initial config, and I was trying to use it. It didn't do exactly what I wanted, and I've proposed. Now that we extend the print command with feature support. I'd like to be able to show the redacted but complete with default, configuration I'd also like to be able to show yet a Json configuration, you know, as a opposed to a Yaml configuration.
I was debugging a pretty kind of tricky bug this week as I upgraded one of my my collectors and noticed a problem in the
go viper map structure V, 2 implementation of of the Mitchell H map map structure. I have a Pr open. If you could approve it, it'd be helpful to get us to a place where, when you embed a struct which I have a habit of doing and go, you get a really unhelpful error message especially gets bad when you combine it with squash tags. It's anyway, you can see the issue.
I think I saw David Ashpole was in the room. I want to talk briefly about this one letter E, it's called Runtime Metrics instrumentation. It's not about the collector itself. It's about the go SDK, I've I wrote this instrumentation a few years ago at my last last employer, and never had the like urge to put it in the contribute repository. But now I do
we've been talking in this meeting, and others about being able to inject sdks. Why do people want to inject inject sdks? The one that we know about is to be able to add features. That hotel doesn't have like
context based attributes. And that's a whole separate topic for the Spec. Sig. But in this case the issue is about runtime metrics for go. The the Go team came out with a metrics interface for for probing the Runtime. It's really useful information, and the question is, exactly, how should it get conveyed into open telemetry? I don't think open telemetry should write these specifications. It's a go team specification, and I'm trying to just pass it through to open telemetry. It just needs a little bit of attention.
but I would strongly recommending anyone who runs a collector. This is instrumentation that we need exactly the way it's written here. I'm strong, strong opinion on that. Lastly, or a couple more. The tail sampling processor is something that I've picked up in the sampling Sig.
I'm not giving it a ton of personal attention, but we are as a group trying to crowdsource some attention on this to get it to upgrade to the the latest otap which gives us sampling probabilities. This makes it so. You can make metrics from your sample spans. It's pretty cool. And we're trying to add this in the tail sampling processor. Eventually, we're going to need code reviewers, and I'm probably going to step up as a code owner there as well.
Last thing is, if you care about rate limiting Apis. This has been ongoing for quite a while. I don't want to talk about it here, but there is a Pr. And I left linked to the latest comment. That's pretty insightful and interesting from Andrew Wilkins. He can't make this meeting, but he is the one I want to remind you that has the elastic
component called rate limiter processor. We're trying to make a rate limiter processor into extension, limiter, processor and rate limiter. And that's why he has such insightful remarks. So anyone else who would like to help us sort out some questions about rate limiters. Please join the conversation, and that's all I have. Thank you.
Evan, your hand is up.
**Evan Bradley** 22:40 Yeah, this is kind of a dumb bike shed question. But on Point B here for functional composition. 1st of all, thank you for documenting this, I think that's important, but my question is is, why functional composition? When I look that up, it's like a G of F of X kind of thing, and that doesn't immediately come to mind. When I look at this pattern.
**jmacdonald** 22:59 Thank you. Actually, this is a great way to frame to have this conversation. I didn't know what to call it. I was calling it Bogan style for a while, and I asked him about it, and he kind of denied that there was a style. He said, look at Nethtp has a thing called Handler Funk. And I'm like, that's exactly a counter example. I want to name this style, and I think if there are better ideas, let's hear them?
I asked an AI Chatbot, and this is the best I could find. David.
**David Ashpole** 23:30 Yes, I wanted to. Just I don't know if this is necessarily the right place to have this conversation, but at least like
get on the same page about runtime metrics. So I when
so the new version of runtime metrics. I don't know if you're aware that there's now like 2 versions of runtime metrics.
So there was the old one which had.
I'll say, names that were somewhat inspired by the Prometheus set.
We actually went to the Go team and asked them to help us craft a set of metrics
that would be useful to a broad a broader group, because
the the kitchen sink version of runtime metrics where you get everything like a lot of those metrics are meant for, like the Go developers themselves.
And Prometheus has a set, but it's largely based on how go was designed in like
2015, and they found that there are a few of them in particular that are very misleading, and so part of the objective there is to limit
the production of some of the metrics that were misleading.
and the other goal was to try and provide like a
picture of metrics that would be easily consumable by people not as familiar with the runtime, and
like kind of guide them to the ones that are actually important.
So there's.
**jmacdonald** 25:03 So I'm referring to a package named Runtime Metrics, which came out in like, Go 118. Is that not what you're referring to?
**David Ashpole** 25:09 That. So there is a package.
**jmacdonald** 25:13 Before that there was read Gc. Stats or read Men stats, and that was the old terrible stuff. Nobody. It was super confusing.
And then they came out with runtime metrics.
**David Ashpole** 25:24 Which which are better, I.
**jmacdonald** 25:27 Are better.
And the the Pr. That that I'm let me pull it up. Since we've got this far in the conversation.
and I'll the the. There's 1 very important metric here that I want, and I would actually give the rest of them up. We have views for this reason, like you should be able to configure a view that just gives you the runtime metric you want.
the one that's really important is go CPU time, and I've taken the ghost, the the runtime metrics, conventions which have slashes in them and turned them into like hotel style. And I prefix process, runtime go. But, like the the important point here is that CPU time comes out of the runtime structured as metrics that are counters, and if I turn them into a single open telemetry counter with attribute dimensions, and if they are 3 dimensional.
you can get a very good picture of like, where is my time being spent. I've got user time. I've got idle time. I've got Gc. Stats. I've got. Gc, assist, and Gc, assist is when things have fallen apart. It's good to know when you're falling into Gc. Assist, and so like. These were very, very helpful to me, and I want them exactly the way they come out of the go runtime. So this is why this is not an open telemetry specification. It's not a convention that comes from open telemetry. It's literally just passing through what comes out of the Go team's mouth
as metrics.
**David Ashpole** 26:45 But you're you're like restructuring them right? You're changing some stuff to labels here.
**jmacdonald** 26:49 Yeah. So I turn it into open telemetry style. And and the way I do that is by finding their conventions. So let me. So let's see, did I put a link into the actual here, this one.
Come on. Want to take you here that didn't work.
So here we are, and these are the ones I'm talking about. So CPU classes, Gc. Mark, assist
CPU classes. Gc. Mark dedicated the pattern. Here is, it starts with CPU classes, and then there are 3 dimensions.
and then there is a colon, and then some units, and I have hard coded in my Pr. Let me show you
that.
this is the thing that I change every time a go comes out with a new release. So
the classes counter. I've identified conventions within the Runtime metrics. They have not explicitly stated these conventions, but they are patterns that are very strong and exist. I think they understand their own patterns. So classes counter Gcpu classes. I put a star to say that anything else is a dimension.
and it will just come out as the dimensions that are implied by the Runtime metrics. We don't say what the instrument is, and then, you know, the units become units. So the classes counter is one pattern. There are 2 of those ones for Gc. And ones for CPU classes. Then there's the classes up down counter, which is the memory usage statistics, and they have a bunch of classes as well. It's not as many dimensions as Gc. Or CPU. Time, but it's very functional and very useful.
I've had to ignore the histograms, and that's a little bit of a blemish here. But it's an open telemetry problem, not a go go runtime metrics problem. We don't have an asynchronous histogram instrument. I can't do anything with these really without investing a ton of time in the spec. So.
**David Ashpole** 28:52 The new. The new instrumentation uses the metric producer interface to provide this.
**jmacdonald** 28:58 So is it? But it's but it's an interface to the same
same data, I assume. Okay, why don't you follow up with this lead on my my Pr. Because I don't care how the information gets to me. I want exactly this information.
**David Ashpole** 29:13 Okay, I
yeah. I guess I mostly want to make sure, like, I understand what you're doing. I think Tyler had a very similar.
either prototype or package a while ago. I just want to make sure you're aware of, like the progress we've made as well over the past 2 years, and like.
**jmacdonald** 29:31 Okay. So a lot of effort
is, I'm trying to avoid go SDK and its ecosystem. And I'm not on the go team. I just want these metrics in the collector, and I'm putting it in this meeting because they're not in the collector, and there's no runtime instrumentation in the Go contrib package yet. Help me have that, and I'll be happy.
**David Ashpole** 29:49 What do you mean? There's no runtime instrument.
**jmacdonald** 29:51 I I can't get the same equivalent of Go CPU time from any instrumentation package that I know of that's automatically installed in the collector. I need to know exactly this dimensional breakdown, which is what the Go team gives me. The fact that there's a 1st dimension is whether you're doing Gc. Or scavenger, idle or user. The second dimension is whether you're doing mark or pause, or assist, or background. The 3rd dimension is whether you're doing assist, dedicated or idle.
And that graph forms an area graph. And I can see what my Runtime is doing. That's what I want the collector to have.
That's all I care about.
**David Ashpole** 30:24 Okay.
**jmacdonald** 30:24 And I don't know how to do that with go SDK.
**David Ashpole** 30:29 It.
Okay? I I mean, I certainly think we could do that with a go. SDK.
**jmacdonald** 30:33 Okay, let's get some instrumentation in the control repository that we can put in the collector is what I'm really getting at here. Thank you.
**David Ashpole** 30:41 Okay.
**jmacdonald** 30:42 Thank you.
**David Ashpole** 30:45 I'll plug my own the the Runtime metrics as well, and say we should put them in the collector.
**jmacdonald** 30:53 I didn't quite understand David.
**David Ashpole** 30:58 So they're we just turned them on by default in the last release.
meaning we switch over to the new Runtime metrics in Contrib.
I think this new version is something that the collector should consider should strongly consider consuming.
**jmacdonald** 31:18 The existing Runtime Metrics package is being upgraded.
**David Ashpole** 31:21 Yes. So we we just switched a feature flag to switch the new ones on
and we're getting user feedback. But I think it's something the collector should consider adopting.
**jmacdonald** 31:33 Okay. I was out of touch.
Thank you. Your needs as well.
Cheers.
Next topic.
**Mikołaj Świątek** 31:45 Alright. So that's me. I'm bringing up. I want to bring up a an issue that was already discussed, I believe, 2 weeks ago, but with a slightly different crowd. And and there's been some development on it. It's about
being able to report sub component statuses.
So the idea. The reason this is bringing this is being brought up at all is that there's certain situations where the current status reporting just doesn't allow us to report statuses for things which exist the main reason this came up was actually the receiver. Creator. If you spawn a receiver inside the receiver, Creator, there is no way to report the status of that receiver. It's completely invisible.
And in the process we also realized that there are some other components where this might be useful, which don't, strictly speaking.
spawn a component, but which spawn individual independent units of work, which you also might want to see the status of individually. An obvious example of this is the host metrics receiver. It's often happens in the Host metrics receiver, that you have a bunch of metrics has, which are all fine. And then one of them, which is having some kind of problem
due to permissions. Typically. But there's, I think there's actually a surprising amount of components where that is. That is also the case. Even fire log receiver is like this. Right now, if we if we get into a situation where?
We were happily, happily collecting logs from some collection of files. But there's 1 file that we can't read, due to permission errors. There's like no good way to actually surface that to the user other than via logs and logs are easy to miss and ignore
in this respect. And I'm basically bringing it up to to get more attention on it. I think right now, there's like a question of
which way, like whether the onus of assembling something like an event that covers sub components should be on the component itself, or whether it should be on the on the receiver
of the events. Because right now, what happens is that the component just emits a status and it's done. It doesn't care about anything anymore. And then, for example, the health check the 2 extension aggregates the statuses into some other structure that can then be consumed. Whereas here there's a question of let's say, if
where, if if we're the host metric.
should the host metrics receiver just pass in the status reporter into the individual metric sets, and they just emit what they should emit. And again, it's the job of
the consumer of events to aggregate those together and and present them so that they are effectively part of a single of a single status, or whether it's up to the host. Metrics receiver itself to aggregate events from its individual metric sets and then emit one big thing. I believe it was, it was judged who proposed that in the past, because
in contrib for the health check the 2 extension. There's already an aggregated status that can contain a map
of substatuses, and we could use that.
But if we use that, then we're saying that components have to handle this themselves.
Which I am. This is something I don't. I don't personally like about that
about the proposal, because
status reporting is under adopted as is, and making it more difficult to adopt, is, is, in my opinion, not a good thing. But I also know that Pablo Pablo suggested that what we should actually do is just.
if I understood you correctly, Pablo, that we should just allow arbitrary data to be attached to a status event, and and just, you know.
**Pablo Baeyens** 35:51 Yeah, and have some sort of convention to represent the specific thing that you want it to represent here. Yeah.
**Mikołaj Świątek** 35:59 I kind of like that. Because
right now, the the status reporting is quite limited and rigid and if you want to pass anything. That is that the events truck doesn't let you, and it doesn't let you pass much. Then you're basically stuck. You have to park a whole bunch of things if you want to even play around with it. But if we allow like.
if we let, if if we let users attach arbitrary data to it. Then it's easy to experiment with things, and and then come up and say, Hey, you know we've experimented, and and this is the convention we came up with, can we enshrine it in core?
So I like. So I like that about this proposal.
**Pablo Baeyens** 36:42 Yeah, we already
want to have events in general in open telemetry, and that would make us closer to that. So
I mean, no, I mean, not in the collector, but in general, like we want to represent events as logs and logs have arbitrary attributes.
**Mikołaj Świątek** 37:01 Yep,
alright, if there's no if there's no questions, or or or other questions or comments here. Now, you know, please, if you have an interest comment. Comment on that issue
going twice, going twice. Yeah, David, David, please go ahead.
**David Boney** 37:26 Okay. Hi, I want to introduce myself. My name is David Boney. I'm new to this group. I'm either retired data scientist or unemployed data scientist depending on. If my resume can ever get through the Hr. AI. And get a person to look at it.
But I am a student at University of Houston, working on an Mba. So the hat that I'm wearing in this group is student from University of Houston. I'm not affiliated with any company. My interest is developing streaming analytics that could be included in a processor in long term. I'd like to form a sig on this, but I'm going to need a couple of more people to get to that point.
Adam Gardner, from Dynatrace is volunteering. He's a cloud native
computing foundation ambassador, but he's not actually a core go programmer on their collector for dynatrace. But you know, if anybody wants to volunteer, you know, hit me up on the slack channel, my goal. Right now, I'm very new to all this, and I'm definitely not an architect, but is by the end of summer to basically build the simplest
analytics processor and get it submitted as a contributor processor to do a moving average over the data. And you know, once the architecture part gets framed out, then, you know, longer term goals is to add other types of analytics. You know, variance
move towards Change point detector. I think that's something that could be really useful or drift concept, drift detection, which ask you if the probability distributions of the underlying data and the sort of long term goal to look at is.
how can these techniques be used to reduce the amount of data being sent from the collector when the system is running normal? I've had multiple people tell me that you can be deluged with the amount of telemetry data you're getting. And obviously, if you're debugging something, that's 1 thing. But if it's just running
normal. What are ways to reduce that? Reduce your operating cost of using telemetry? So that's sort of the long term goal. But it'll take a while to get there like, I said hopefully. By the end of summer I can get something up and running, and I just want to introduce myself. Hit me up on slack. If you have any interest, I want to build something that the community can use. I'm not.
you know, associated with a particular company, so I don't have an agenda in that direction. I do want to make an open source contribution. I previously worked on an open source project at Meta, so I have a contribution in that arena, and you know I just think that's good professionally to have
that as part of your portfolio.
So I just want to thank you all for your time.
**jmacdonald** 40:28 Thanks, David. Nice to meet you. I'll hit you up in slack, having a couple couple of ideas for you.
**David Boney** 40:34 Sounds, great.
**Sam DeHaan** 40:48 Paul, and I see you. You joined us, and you moved your conversation further in the agenda down. So I think you can go ahead, and next.
**Paulin Todev** 40:56 Okay, cool squad.
I'm trying to do it more total as well. There's this task to schematize the
configuration for each component, which is really interesting. It could allow us to
how to generate documentation and maybe some tooling to
standardized the documentation for each component. For example. So it looks the same. You have a table with the arguments, what type each argument has.
and so on.
So this is a project that predates the Pr that they linked 2 in the notes.
There was some discussions. A previous person did a lot of work on it. And then I basically picked up that work
that he did where he left off. And
yeah, there was some design decisions. A lot of people were involved, and it seems like a lot of people are on board
with this kind of project, but I'm a little bit worried that it can also restrict
the kind of configuration that people can make for their component
like. For example. Now, sometimes you see components with a custom Moon Marshall function, and I'm a little bit worried that this kind of thing won't be so easy, because
if if this chemotization is becomes a reality, would have.
we wouldn't have a config.gov file for every component which we can
manually edit. You'd have to edit
schema inside the metadata dot Yaml file.
and then another tool is going to generate the configgo.
And yeah, you lose some flexibility there you gain standardization, but you lose some flexibility.
and I'm not sure if that loss of flexibility is something that people would be okay with, you know, kind of. As for
so I totaled raise this to the broader group just to ask if
someone has serious concerns, because it's quite a big project and would take a long time. So it will be a real boomer if we make a lot of progress, and then it's canned.
**Evan Bradley** 43:34 Hey, Paul? And so 1st thank you for for looking into this and being willing to take it on. I do agree with you in general about the some of the maybe limiting factors of of adding a schema.
I
I think I'll put my hat in the ring. I would.
and I know it's a little unconventional, but I think it would be definitely possible to use. Go as the way you define the schema, and I think that that would enable us to possibly have some kind of trapdoors, if you will, for our escape. Hatch, I think, is the better term for it, for opening up possibilities for adding in some custom functionality.
I think the as far as
like the next step for achieving this work, my request would be for you to, since you like. As you said, it's a it's gonna be a big project. My request would be for you to open up an Rfc, and we can discuss the
we can. We can discuss basically the the general approach and kind of look at how we want to achieve this, and if there's broad agreement, then then move forward from there.
and if you want any assistance on kind of what we're looking for in an Rfc. I can point you to some resources, but you can see 2 of the the 1st agenda items in today's meeting notes are are Rfcs, and those might be a good starting point.
**Paulin Todev** 45:00 Thank you. Yeah, that sounds good. There was a Google Doc which was created by the original person who opened a Pr, the one that I sort of inherited.
so I can use that as maybe a base for Drc. Thinking I'll take a look.
**Evan Bradley** 45:23 Anybody else. I have the the last agenda item, any comments?
Okay. Christos, this is mostly for you. I'm glad you're here. So sorry. I know there's a there's a lot of dynatrace people kind of piling on you in that issue that I've linked.
But I so I read through it. You answered most of the questions I had I was just looking for. I've gotten questions from my team on on how we want to push forward here. I guess it sounds like you're good with basically adding a feature gate for transitioning to the new Semconf.
we can. And I think you could probably switch from the old one to the new one, or just double emit when the the feature gates enabled, and then iteratively add the the new metrics. To that.
The question I had is, what was your concern around Mdatagen?
**Christos Markou** 46:23 Yeah. So I think this conversation affects both kubernetes, metrics, and kubernetes amount convention, general and system semantic conventions as well, I think probably system semantic conventions will be in this phase of
yeah, we will 1st be in this position to 1st change, to change the host metrics receiver to adapt to the stable sematic conventions once we have them. So this affects to special interest groups, let's say to to working groups, the the thing with within these 2 groups we haven't thought yet.
how this will actually happen inside the collector. We have outlined the solution, using the feature gates one to to enable legacy or disable legacy accordingly, and the same for the stable semith conventions. But we yeah, I think my my assumption was so far, at least from our discussions that
we would like to do this altogether in a bunch. But I I kind of understand the concern that this will be a huge Pr, we haven't discussed this yet. Actually the the the concern about enter the Gen. Is that at some point we would need to have
both metrics right? Both a legacy set of metrics and the stable set of metrics. We would need to ensure. We had some discussions how intelligent should work to cover both.
I don't have the details right now. I can barely you know, recall the conversations there. But definitely, this is something that we need to to discuss within the collector sheet. But we haven't been there yet. That's the situation. I don't know if that answers the question. But at least that's all the information that I have right now.
**Evan Bradley** 48:31 No, I I appreciate that. I guess my my follow up to that would be, is there anything that you could use help on or
is there any place that I could follow? It sounds maybe like there really isn't a tracking issue for this overall change.
**Christos Markou** 48:47 Yeah, yeah, that's true. I can. First, st I can raise it with. The system. Samantha Convention Dimitri is there as well Brighton, too. Both David Aspel and myself. We're on the Kate Sig. So yeah, probably we can track this down, probably create an issue and start this kind of conversations.
But yeah, makes sense to start them early. So as we can identify any any
any topics that we haven't thought of yet.
**Evan Bradley** 49:22 Okay, cool? I guess. Yeah, I'll I'll try and or I'll wait for for the output of those discussions. And then I'll try to follow that, or, if you, if you remember, to feel free to send me the tracking issue, and if there's anything that you need from my side to kind of help. Move this forward. I can. I can offer input where it would help.
**Christos Markou** 49:43 Yeah, right? System has a meeting. Tomorrow I will take the action item to raise it there, and I will post back on the other issue that we start the conversation. So yeah.
cool. Okay.
**Evan Bradley** 49:57 Really appreciate the info. Thank you.
**Christos Markou** 49:59 Thanks.
**Ron Korland** 50:06 Hi,
My name is Ron Collin. I'm working on a company that call so Miss AI. We help to companies with the area of like Phoenix, but on top of a data dog and splank
and one of the things on one of the companies that we have built internally is called exporter, is exported, that our customers several customers use for give the option to expose internal metrics
for a cada scatter. So like example, if you have a cluster that is, have a many auto collector, all of them send their internal metrics like the Htp. Request. Duration is sent to one main collector with via grpc.
And use this exporter. So the Cada Hpa. Can, with custom metrics on top of it, create a Prometheus query with a threshold with target and scale up and scale down our auto collector deployment
this is one of the feature. This is one of the exporter that I open a pull request for the contribut, and I'm looking for someone that maybe can help me to as a sponsorship to this pull request to push it to a country, because I found also to link. I link it to the Pr, that also 2 issues, one in Canada and one in
hotel. That is a request
this exporter. So after that we decide to take this code from an internal report to to try to push it to contribute report as a official exporter.
If any anyone have a question or something they can. I'm in the slack channel
of hotel, and if ever anyone that have a question of why is needed? And what is the use cases, or
what what is missing, or or any idea to help me to push, to, to contribute. That will be great.
Thank you.
**Evan Bradley** 52:45 Sam, I believe you have the next agenda item.
**Sam DeHaan** 52:48 Sure. Yeah. Mine should be quick. Just wanted to to throw out that. I put together a pull request based on some investigation that was happening around the SQL. Query receiver
internally uses the scraper helper package. But
basically, the way that package runs, everything in series meant that things like having a database connection. Pool were pretty meaningless because it's just running each query in series. So
somewhat small pull request for a scraper controller. If anyone's interested in giving it a look to allow
parallel use. I know there's some been some conversation about expanding the scraper helper, scraper receiver patterns to to
a wide variety of scraper based or scraping based receivers. So if anyone's interested, please take a look.
**Evan Bradley** 53:58 All right. Any anybody else. Have anything, any questions, any other last minute agenda items going once, going twice.
Alright. Thanks. Everybody. See you next week.
