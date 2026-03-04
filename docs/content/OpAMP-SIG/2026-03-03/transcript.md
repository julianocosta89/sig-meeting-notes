SIG: OpAMP SIG
Date: 2026-03-03
Duration: 52 minutes
Zoom Recording URL: https://zoom.us/rec/share/qU0XNfvwr_uwmVJ7JQrCnccUnB_8LgpM_OgZ5-sakkLlziEvPkP8o4U3lTtbeHD6.8g_yQaLooNaSA2ZG
============================================================

## Zoom Recording Transcript

**Tigran Najaryan** 00:08 Hi, Martin.
**Michel Laterman** 00:10 Loween.
**Tigran Najaryan** 02:05 We have two topics, and
Jade has the first one, maybe let's wait.
One more minute.
Hi, Jade, your topic is the first one. Do you want to go ahead with that?
**Jade Guiton** 02:41 Yeah, sorry, I took some time to find the new link.
Yes, so…
I was looking into correlating the op-amp payloads with the internal telemetry, so specifically metrics that the hotel collector emits.
And, canonically, the way this is supposed to work according to the spec is that
In… under the agent description message, you have identifying attributes, which are supposed to be…
The same as the resource attributes on the OTLP telemetry emitted by the agent.
And while looking through that, I saw that the LPAMP extension does not always respect that. There are some cases where the reported value of service.instance.id does not actually match
The value used in the internal telemetry.
And specifically, the… that's the scenario where this happens is, when a user uses the
instance UID config key in the op amp extension.
And the reason why that's related is that, IP Extension always reports It's, instance UID,
The one from the outbound protocol, as the service.instance.id.
So if they ever defer, because of that config key,
It's going to end up reporting, identifying attributes that, do not allow correlating with the internal metrics.
And so, yeah, I have a draft PR, which currently does not… at least last time I checked, it did not pass the tests.
But, you know, proof of concept, at least.
That would… Just always, always set that reported attributes to the…
the value from the resource attributes, and I wanted to get some feedback on whether that makes sense, whether instead maybe the specs should be changed, and there should be some other way of correlating things.
And maybe also start a conversation on the other identifying attributes, which… I think always match… the collectors…
When the collector has them set,
But it will not always match, if the collector has those attributes disabled.
Which, if you're too exhaustive about how you're filtering for metrics, it might still break the correlation.
So… Yeah, I'm not sure if I made myself clear, but, thoughts? Feedback?
**Tigran Najaryan** 05:41 So, just to be clear, with this change.
If instance UID is explicitly set in the configuration, then
Then, the value of the reported service
instance.id in agent description will be different from that.
And will be the same as the service.instance.id of the metrics that that collector reports about itself. So those… the service.instance.id will be the same in
Both places, in both the metrics.
and in the opum agent description, but it will be different from the instance UID value.
If it's… if that is specified in the config.
**Jade Guiton** 06:27 Yes, that is, that is the idea.
My understanding is that the spec allows for this, at least.
**Tigran Najaryan** 06:36 It does.
**Jade Guiton** 06:36 elsewhere.
**Tigran Najaryan** 06:37 I just took a look, yes. It says that… the spec says that what was that?
It says that it may be set equal, yes, to the instance UID, but it doesn't say it must or should be set.
which I think… I think it's fine.
I wonder if there is.
A possibility of a problem with that, and whether we should rethink that.
**Jade Guiton** 07:08 Yeah, and one thing…
One thing is that even at the moment, there is a case in which they will defer, which is if the server uses the new instance UID message to impose a new instance UID,
That does not update the agent description at the moment.
So, it would create a discrepancy even in that case.
**Tigran Najaryan** 07:34 I can't… I don't remember any functionality that depends on these two things being equal. Instance UID and service.instance.id. Anywhere. From what I recall, it should be okay, I don't remember.
Any… anything in the spec, in the OPAMP spec, or anywhere else that… Would make this a problem.
**Jade Guiton** 07:58 Yeah, I think I found one instance in the supervisor where this is tested for, but it's a relatively easy change to check against the message instance UID instead.
But yeah, it's reassuring if you can think of…
Other situations where that would be expected.
**Tigran Najaryan** 08:17 Yeah.
But, again, just to be clear, the intent was exactly that.
Yeah, that's a… The agent description, or the identifying attribute, the agent description, the attributes in the agent description.
We'll match the attributes in the… in the agent's telemetry, so that you can correlate.
Between those two things. So… I think the PR does the right thing.
It's just that we need to maybe look at all the places where
That difference may be causing problems, because of incorrect assumptions, And… and fix those.
But otherwise, I think it is the right approach.
I think it would make sense to…
**Jade Guiton** 09:04 To put this change behind a feature gate if we think there might be places where this assumption is made?
**Tigran Najaryan** 09:14 Possibly. I'm not sure. Evan, what do you think?
Do you see that as a…
**Evan Bradley** 09:19 I think we should be good, because this is mostly gonna be used with the supervisor, which is gonna set these things pretty rigorously. I think that's why it hasn't really been an issue up until now.
And I don't know that we've looked at the case where there's a user manually configuring the extension.
I'm not aware of any cases. I think it's mostly either used by…
What do you call it? It's mostly either used by the supervisor or the bridge.
**Jade Guiton** 09:46 Hmm.
**Evan Bradley** 09:51 And it's automatic. I was… I was gonna actually argue for just taking the…
removing the UID option from the extension, just taking it from the service instance ID, resource attribute.
I guess the case for that is, yeah, if you deliberately, like, unset that or something, I guess you would need…
**Jade Guiton** 10:13 Yeah, the problem would be if you do the opposite, and if you instead set a specific service instance ID in the collector that isn't, like, a UUID or something like that.
So, we used to be able to…
**Evan Bradley** 10:27 Right, we used to be able to do ULIDs, but then we moved to UID7.
So there, there is something, like, if you…
I think at this point, it's been long enough that I don't think anybody's depending on their instance running a particular ULID.
I would almost say that you shouldn't. If the service ID is detected in the collector's resource attributes.
I'm almost even tempted to say feature gate, and when it's enabled, you throw an error if the instance UID is set, and that option's only if…
For whatever reason, you remove that attribute from the collector's SDK.
**Jade Guiton** 11:06 Hmm.
**Tigran Najaryan** 11:09 What happens if the specified service instance ID is not a valid UUID?
I think that's the… that's the situation where we have a problem there.
So, if it's… oh, I see what you're saying. If that's not a valid UUID…
**Evan Bradley** 11:24 and it's not a valid ULIT, then… you're right.
Yeah.
then we would need to generate something, or the user would have to… I mean, I think that falls into being unset, I would say. If it's not a valid instance UID, then you have to specify one, or one's… we could just say you… the collector will generate one.
**Tigran Najaryan** 11:43 Yeah.
**Jade Guiton** 11:44 I think one thing that could be done, because I think right now, what happens is that if the instance UID is not set, it will look at service.instance.id from the collector, that if that fails to pass as a UID, it just crashes immediately already. That is the current behavior.
So, I think we could reasonably do something like…
If the two values don't match, We error out.
Like, if both are set, if the instance UID config is set.
But it doesn't match the service.amstens.
ID?
**Evan Bradley** 12:20 And service instant ID isn't… What is… Andy, does the SEMCOM say it has to be UID, or…
No, it just says it is unique, okay.
**Andy Keller** 12:33 Yeah…
**Tigran Najaryan** 12:33 It's recommended.
**Andy Keller** 12:35 Brilliant.
**Evan Bradley** 12:35 Monday.
**Andy Keller** 12:36 for…
**Tigran Najaryan** 12:37 Yeah, but it's just a recommendation, it's not, yeah, it's not required to be a UID. It's most likely going to be a UID, right? That's… that's what most likely what is going to happen. So the… the question then is.
For the edge cases, when it's not, what do we do, essentially? Do we generate one, or do we refuse to run, or whatever is it that we do?
**Jade Guiton** 13:03 Right enough.
**Tigran Najaryan** 13:04 I've heard…
**Jade Guiton** 13:04 I hear that.
**Tigran Najaryan** 13:07 I like your proposal, Evan, that we… if it's set, if it's valid, it makes sense to me to use just that.
**Jade Guiton** 13:21 Alright.
I guess I'll try to do something like that. We can discuss it on the PR more specifically, what to do in the Edge case.
I think.
Yeah, the other thing I wanted to talk about is that, from the current code, for service.name and service…
That version, that's taken from the resource attributes, except if they're not present, in which case it uses the…
Distribution name and distribution version.
Which, on its own, makes sense, it's very useful information to have.
But what I'm wondering is.
If we guarantee that the identifying attributes are supposed to be on the telemetry,
would that also count as predicting the correlation? Should we put it under non-identifying attributes instead?
That way, you can always say, if you want the metrics, just find the metrics that have all the identifying attributes.
And you're guaranteed to find something, and you're guaranteed to find the right thing.
But we can also expose things like the collector distribution
Name and version, which is a useful piece of information on its own.
Even in cases where the corresponding attribute has been disabled at the collector level.
Would that make sense?
We probably need, like, a new convention.
I don't know if we need to…
Collector distribution attribute, or something like that, but…
**Tigran Najaryan** 15:01 So…
Sorry, can you say that again? What is it that you're suggesting? Where do we… do you want us to put the…
Yeah, that's.
**Jade Guiton** 15:10 Yes.
So, if a user disables service.name.
Or disable service.version in the collector resource attributes.
the op-amp extension… Still sets those attributes in, under identifying attributes.
And it takes the values for the distribution name and distribution version.
Which, arguably, breaks the correlation with internal metrics.
Would it make sense in that scenario to still expose that information because it's useful?
But to expose it under non-identifying attributes, for instance.
**Tigran Najaryan** 15:57 Yeah, it's a good question.
**Jade Guiton** 15:59 I guess it's a bit of an edge case as well that, hasn't really been encountered.
**Evan Bradley** 16:06 I don't see any issue with it. I mean, we have that data.
I don't think it hurts to add it.
I mean, the only thing I would worry about is maybe cardinality with metrics.
But…
**Jade Guiton** 16:23 It would increase the cardinality not to set those values?
**Evan Bradley** 16:28 It would increase it to set them, right?
**Jade Guiton** 16:33 I mean, we're not emitting any metrics here, right? Like, we're just…
**Evan Bradley** 16:37 Oh, you're saying just for the op-amp connection?
**Jade Guiton** 16:40 Yeah, yeah, the, the…
**Evan Bradley** 16:41 Oh, okay, okay. Yeah, I don't… I don't see any harm in that.
**Jade Guiton** 16:46 I guess… Well, I guess the spec does only say should be specified, so I guess it's…
Okay not to set some of these attributes if we don't have a right… a good value for them.
**Evan Bradley** 16:58 No, we usually… so, usually the suggestion here is to set things like this, because then you could say, I want all of my collectors that are on, you know.
this old version, you know, for this distribution, I need to…
select on these and do some kind of upgrade mechanism or something. I don't know, but…
As a way to quarry for that group of agents, I think that makes sense.
**Jade Guiton** 17:24 Right, the problem is, like, if you've disabled those attributes in your collector resource, does that mean that inherently the collector does… no longer has
Aversion.
Or…
**Evan Bradley** 17:36 No, I think… I think anything in the build info's fair game.
**Jade Guiton** 17:40 Hmm.
**Evan Bradley** 17:41 Because I don't know that we can necessarily…
**Jade Guiton** 17:46 Yeah, I guess the fundamental problem is that there's data we want to be able to filter by, and separately, there's data we want to be able to correlate to internal metrics.
And because users can mangle and make the collector resource attributes as bad as… and useless as they want.
There's kind of this tension with trying to, keep the set of identifying attributes useful.
**Evan Bradley** 18:15 Wait, so just to back up, you're saying… you're saying to…
include these as separate attributes even on top of the ones that the user has already set in their resource attributes on the SDK.
**Jade Guiton** 18:26 No, I mean, that could be a nice thing, to be honest.
like,
Yeah, that could be useful, for detecting, like, collective distributions, regardless of how you've named your service.
But what I was saying is, if the user disables service.name and service.version in the collector attributes.
Should we still set them in the RPM payload? You're saying it makes sense to still set them because you can filter
collectors when you're doing remote config and all that.
**Evan Bradley** 19:00 Right. No.
**Jade Guiton** 19:02 No longer matches the resource attributes.
**Evan Bradley** 19:05 Right, no, I'm sorry, I was thinking just from a general standpoint. No, I would say we should still set them, because we don't know, what the collector's SDK is. Like, I don't think we can make assumptions about…
How it works, or… I mean, we obviously know how the upstream one works, but,
you know, if you set one of those telemetry factories in the builder, and it exposes things differently, or the SDK is initialized in some weird way, I don't want to make…
Assumptions, just because that… just because they're not there…
There was some intent behind it.
If that makes sense.
Like, I think we just have to… we have to work with the data that we're given, and so if they're not there, then we just… we assume they're just not available for whatever reason, and we set them according to the fallback.
**Jade Guiton** 19:54 Hmm.
Do you think it would make sense to put them as non-identifying attributes in that case, or would that still be a problem for…
**Evan Bradley** 20:08 I need to double check. Are they… they're listed as identifying attributes right now? I would think that the service instance ID is sufficient to be identifying.
**Jade Guiton** 20:16 Yeah, identifying attributes includes service name, service version, and service instance ID.
Also, in principle, service.namespace, but we don't actually set that in the extension.
**Andy Keller** 20:28 Yeah, that's in the… that same link that I… I added the semantic commissions that say,
Name and namespace, should… should… Make it globally unique.
that the instance UID… the instance ID isn't necessarily enough to be globally unique.
**Evan Bradley** 20:48 Wait, I'm sorry, one more time.
**Jade Guiton** 20:49 Service.instance ID doesn't have to be globally unique, it just has to be unique per service name, is that what that…
**Andy Keller** 20:56 That's the… that's the way the semantic conventions read, yes?
That the… the triplet of namespace, name, and instance ID Must be globally unique.
I think in practice, the instance ID is generally globally unique, but it's… Not… not…
That's not in the semantic conventions.
**Jade Guiton** 21:20 I guess that explains why.
**Tigran Najaryan** 21:21 danger of it, right? If it happens to be non-unique, we're going to end up in a…
In a collision situation. At best, the server will detect and ask the agent.
**Andy Keller** 21:33 Well, I think… Yeah, and we always… we still have that fallback that the instance UID can be different.
than the service ID. I think it makes sense to… to… sorry, the service instance ID. I think it makes sense to…
default the service instance ID to…
Sorry, let me get that correct.
to default the instance UID to the service instance ID,
In the extension when possible, but… to allow OpAMP to override the instance UID.
2… make it unique.
**Tigran Najaryan** 22:18 So I guess I… I'm not entirely sure what do we gain by…
by doing that, by trying to use the service instance ID as the instance UID.
The spec doesn't require the two things to be the same.
They can be different. By generating it.
**Andy Keller** 22:36 Yeah, and they're both gonna be available in fields in the message, so…
**Tigran Najaryan** 22:42 in trying to use that value, which can be set by the user in a config file, is, I guess, asking for trouble there, for having duplicates. Whereas if we generate it, we practically guarantee it to be unique.
So… maybe we shouldn't, I would say? I don't know why we even expose it as a config option.
What is the use case for that?
For the instance UID, I made.
**Jade Guiton** 23:13 I assume it's the supervisor, mostly.
**Andy Keller** 23:17 When is…
**Evan Bradley** 23:18 You'd get it during the bootstrapping process.
**Andy Keller** 23:21 Yeah, I don't remember, Evan, the… the… low, but…
Often it's helpful if that ID stays stable, so is it… is it regenerated?
Each time, or is it written somewhere?
**Evan Bradley** 23:35 It should be persisted.
Yeah, it should… it's regenerated on a new… if there's no persistent state, but if there is persistence state, it should be read from that file.
That's my memory of how that works.
**Andy Keller** 23:48 That's for the supervisor, right, but not the extent.
**Evan Bradley** 23:50 For the supervisor. No, the extension doesn't have any kind of persistence,
The UID, I think, is just taken from the service instance ID most of the time.
You can manually set it, but…
We could just change it so that it's auto-generated on its own.
**Andy Keller** 24:11 I guess I wouldn't want it to be auto-generated each time.
**Tigran Najaryan** 24:15 Yes.
**Andy Keller** 24:16 And then have every restart of the collector generate a new ID.
**Evan Bradley** 24:19 Okay.
**Andy Keller** 24:20 Really? Not really all.
**Tigran Najaryan** 24:25 So we have to weigh… we have to have a way for the supervisor to tell the extension what UID to use. That's why we have it there.
**Andy Keller** 24:36 Yeah.
**Tigran Najaryan** 24:37 So, I think I'm leaning towards…
not trying to couple the service instance ID and the UID, keep it separate. If they are different, then that's fine, they are different.
And…
And yes, continue accepting the UID as a config option, because we need that for the supervisor to supply it.
And that's it. They are just two separate things. And yes, use the service instance ID value from the resource.
So that the correlation works correctly between the metrics and opal.
I mean, that's what we should go for.
Don't… don't try to cross…
report the values from the UID to service instance ID, or the other way around.
We don't.
We don't need to do that, I think.
**Jade Guiton** 25:37 Right.
**Tigran Najaryan** 25:38 If the UID is in a config, you use it. If it's not there, you generate one.
And the supervisor will persist the time and reuse it.
Across the Rhines.
**Jade Guiton** 25:52 Alright.
**Tigran Najaryan** 25:53 So I think…
**Jade Guiton** 25:54 I've talked a lot about this topic, so I think for the service name and service…
version thing, I'll probably create an issue, and we can talk about it more there for that specific edge case.
But I guess I'll move along with my PR in that case, and we can move on to the next…
Next topic…
**Andy Keller** 26:13 Sounds.
**Tigran Najaryan** 26:13 Okay, yeah, sounds good.
Okay, the next one is the… the roadmap discussion.
Let me maybe share my screen.
Where is that? Here.
So, we had a discussion, maintainer's discussion, About the roadmap.
And the Evan and I.
And, we wanted to understand, okay, so what do we want to be included in the roadmap? We had a bunch of
small items here and there, but what is the, essentially, the theme of the roadmap? What is it that we want to achieve? And we came up with the following.
There's essentially… three areas of work. One is the supervisor.
The other is the… the OPAMP specification itself, and the, the implementation in Go, the OPAMP Go. And for the… for the supervisor, we, we…
We believe that the goal should be, essentially, To release a production-grade
Version 1-2, which is essentially what you would call a minimally viable product.
And then in that, you have…
three, I guess, pockets of work. One is the implementation of those MVP features.
And we'll have to decide what exactly.
what exactly is included in the… in the MVP.
We have a bunch of.
features, candidate features we have in that roadmap document we will need to discuss and decide. The second would be to make sure that the implementation is of production grade, so that we have the tests
whatever. Essentially, we do the hardening work, right? So we make sure it's a production grid. And then we make an actual release of the
the supervisor.
bundled together with a collector, in the form of an operating system packages. It could be Debian, RPM, or whatever we decide to make a release.
So those, essentially, three things That will need to happen for us to make a… make a release, 1.0.
That's for the supervisor, for the…
for the spec and Go implementation. For the spec, essentially, work on marking it stable.
And again, releasing 1.0, and there is, there's a bunch of features at different levels of stability in the spec today.
Many are marked.
Beta right now, and so the next level of stability will be stable.
So, work on that, making sure that we move I would imagine.
Most or all things that are better today, too stable, look at the rest.
Things that are in development.
Maybe also want to mark those stable.
And once we made up our mind on what needs to be stable, we'll make a release.
Then, for OPAM Go, the goal would be to implement that stack completely, and again, make a 1.0 release. I think most of the features are actually implemented by Opam Go today, but we…
probably misspun, I would say. It's a couple…
But, yeah, it's fairly, I guess, well covered, but…
But there's probably some limitations, so that would be for the… for the goal.
This is, like, the high level
Thinking that we have about what should be in our roadmap.
everything that we have in that document, we have a list of things to do. Essentially, we would need to go over that list, and
either a fine… The item to one of this high level.
Line items, or if it doesn't fit, then we explicitly say that
If it's against what we want to do here, it's going to be then out.
Or if it's…
It's not against, but it's not particularly contributing to the goal, then we'll probably say that maybe it's a maybe item that we can work on sometime later.
So this is our thinking.
If anybody has any comments, happy to hear.
**Andy Keller** 30:46 We're gonna… I was thinking maybe we could clarify this right here, just say implement the stable features of the spec completely?
**Tigran Najaryan** 30:56 Yes, sounds good to me.
I mean, there's nothing preventing us from implementing non-stable ones, but the.
**Andy Keller** 31:05 Of course.
**Tigran Najaryan** 31:06 stable ones to include in 1.0. Yes, makes sense.
So, if anybody has any thoughts, any comments, feedback is welcome, and then…
The next step after this would be to go over that document and The exercise of
What things should be included and not included based on this goal setting.
**Aunsh Chaudhari** 31:37 And so, one quick call-out, are we also looking at
the Kubernetes operator bridge implementations as a follow-up from this, as part of the roadmap?
**Tigran Najaryan** 31:47 I mean, that's a good call-out. We haven't discussed it, guys, so we… we should probably… yeah, it's a… so, yeah, we… that's a good question. We haven't thought about it. We'll need to look into that else as well.
**Aunsh Chaudhari** 32:00 Yeah, because Jacob was actually going to also add a couple of features to that document. We've added a few of them for the bridge, which we'd want to add in, but I think that's one thing that definitely users will find value also, if we have a well-defined roadmap for that.
**Tigran Najaryan** 32:17 Okay, yeah. I added a note here, we'll need to look into that, I agree.
**Aunsh Chaudhari** 32:27 In the same way, even for the extension itself, if there are certain capabilities within the collector extension, is that basically an evolution of what we're thinking of on the spec and Go goals itself, or should we
Probably, the way I was thinking of it, we should also track the extension separately, right? If there are certain capabilities, we want that to also cater to, in compliance with respect.
**Andy Keller** 32:53 The supervisor requires it for the… so for the supervisor to be stable, it really requires a stable extension, so I think we should just add another bullet here for it.
**Tigran Najaryan** 33:02 Yeah, yeah. My thinking was exactly that, Andy, that the extension… we'll work on the extension to the extent that is required for the supervisor goals, essentially.
**Andy Keller** 33:11 Okay.
That makes sense.
**Tigran Najaryan** 33:14 If… but that's… but actually, Ansh, you have a good point there. Is there any separate goal for the extension outside of the requirements that the supervisor places?
I don't think we have discussed that.
Probably, it's worth also looking into that, if we believe that the extension
if we want to have an extension with, I guess, a no-pump managed collector that is just using the extension without the supervisor. Our thinking so far was that
The supervisor is our primary goal right now.
I would like to see maybe some more feedback, and maybe from the community, and from people who are using the collector with the extension, without supervisor, for us to understand whether it's,
It's important for us to make that a goal, so that the extension on its own needs…
needs to be something that we release and say that this is a bundle with the collector without a supervisor, and here's how you use it. So far, we felt that the supervisor is the one that we want to use as part of the roadmap.
**Aunsh Chaudhari** 34:36 Makes sense, yeah. I know there's a topic later on that I've added, which is in context to some discussions that were had across the collector and OPAMSIG for adding remote configuration support to the extension. You know, there were some concerns
From a user's point of view, that…
You have the supervisor running separately, which can add to
just friction in terms of onboarding, you know, the feedback we get around open telemetry components, so if it's possible for us to add certain capabilities to the extension where it's able to operate standalone, right? So, that was one of the reasons I called out the extension, but yeah, happy to gather more feedback around that.
**Tigran Najaryan** 35:15 Yeah. Let's do this. So I added a note here again. Let's do this. When we go over that list of
the roadmap document that you've written down. Let's take a look at what do we have there that is about the extension, but which is not necessarily part of what would be the supervisor goal.
And we can make a decision on that.
**Aunsh Chaudhari** 35:39 Okay.
**Tigran Najaryan** 35:44 Other thoughts? Anyone else?
Okay, so let's do this then. We'll copy-paste the gold into the document that you created, so that we understand what is it that we're doing. Maybe also rename the doc, it says Supervisor Roadmap, I think this is the entire
OPAMP roadmap, essentially, the supervisor being part of it.
Although maybe the biggest part, I guess.
And then we do that exercise I was talking about, right? We go one by one for each item and decide whether it contributes to a particular goal that we accept it, or if it doesn't, then that gets punted down the road or rejected.
**Aunsh Chaudhari** 36:36 Sounds good. And we'll talk about these two things also.
**Tigran Najaryan** 36:48 Okay.
What's the next item?
**Blake Rouse** 36:53 Yeah, that was nuts.
**Tigran Najaryan** 36:54 Blake, you're here? Yeah, go ahead.
**Blake Rouse** 36:55 Yeah, I just wanted to call this out. We had talked… I had joined, the SIG, I think, last time, and talked about
Partial reload support. I did get the RFC written, and it is there, so I just wanted to bring it up in the meeting for those that might have missed it. If you haven't missed it, great. But please take a look. If there's any interest to you all, or anyone on this call, it brings any value, your comments, suggestions.
It'd be greatly welcome, so… That's it, I don't have anything else to add.
**Tigran Najaryan** 37:26 The partial reload is…
So that when you… when the configuration changes, you only reload the components which are… which have changes in the configuration, or the components which are…
downstream of the… of that component in the pipeline, I guess, right? Because you have to… the restart is required, yeah. Okay.
Okay.
I mean, it makes sense to me. We've always wanted to have something like that. It's a matter of, I guess.
Who is able to do the implementation?
But as a concept, it would make sense to me.
**Blake Rouse** 38:01 Yep.
Yeah, so just, you know, I think… I don't know ex…
from the RFC standpoint, just having more people say, yes, we want this, I think it's just good. So, if you could put that on there, that you're interested in this, and it provides value, and how it provides value, I think would be really good. So…
**Andy Keller** 38:21 Thanks, Blake.
Thanks for bringing this to my attention, I'll take a look at it.
I was on PTO last week, and I'm just seeing it for the first time now.
**Tigran Najaryan** 38:37 Okay, and the next one, I know, is actually about one of the topics you brought up, right? Till pump extension. You might talk about it.
**Aunsh Chaudhari** 38:46 Yeah, yeah. I think, as we referenced earlier, I was just looking at some of our discussions in the past across different work streams, including The Collector, where
We… I don't know that, for example, some users would prefer to
Actually have, the extension itself being able to perform some of these capabilities, like remote configuration.
Versus the supervisor that's actually running, separately, right, in terms of the steps that they need to set up, even if we try to bundle this as part of the collector to an extent.
So I was trying to just follow along, understand…
Whether we have a clear thinking around,
what would be the best approach to take if we were to bring that capability to the extension itself, right? If we were to perform remote configuration.
using files, or I know there's a discussion around policies and how the op-amp provider being proposed would actually bring in some of these configurations, but just wanted to open it up since that discussion, maybe end of December or so, if there's any thinking around how we could
Add support to the extension to do so.
**Bejal Lewis** 40:01 I'm no expert on this, by the way, but I just linked to an issue that Evan outlined, which was…
Talking about how we could make a confap provider.
That could help us, which is pretty interesting.
**Tigran Najaryan** 40:19 That's… that's one of the ways, and I think, Andy, you also previously described another way of doing it, right? You… you were restarting the collector process, I think.
**Andy Keller** 40:30 Yeah, we have a different entry point in our collector. It's open source if anyone wants to look at our distro and,
Take some inspiration from it, We… we basically bootstrap
In front of the collector service, and start the collector service, and when we get a configuration change.
we shut down the collector service and start the collector service. So it's the service itself within…
Within the same process, you know, it's not… it's not starting a new process.
But I… that… that may… I have been meaning to spend some more time on looking at what it would take to…
donate that upstream. I think it probably involves changing the collector itself.
And, you know, not just a contrib component or something like that.
And I don't know how
you know, certainly in this discussion, in Slack, there was a lot of interest in that. I don't know broadly, in the community, how much interest there is.
But if somebody's eager to take a look at it, like I said, I can post a link to it real quick.
**Tigran Najaryan** 41:45 Yeah. At the same time, I guess, if… so we just talked about what the goal of the roadmap is going to be. This… this is not very well aligned with what we wanted to do. This is essentially trying to
Recreate the functionality that we already Have, with the supervisor.
But without a supervisor, so… sort of…
it's not like it's against the goals of a pump, but it's extra work that is
In some ways, a duplication of efforts here.
**Andy Keller** 42:19 It is, it's… it's different, for sure, and and I think, you know, it's… it is a little bit of an either-or situation.
And there may be some…
some users who prefer one approach over the other, and so they could… they could coexist, but it certainly, you know, is going to require resources to do either of them, and so doing both of them is,
It's more work.
**Tigran Najaryan** 42:47 So, I guess my position on this would be that I'm not against it.
But unless there is a significant number of people who are willing to
to make this happen, to work on it, I don't think we should make this a burdening for maintainers or existing contributors. That's my opinion, because it, again, is sort of… it competes with the solution that we already haven't committed to working on, which is the supervisor.
**Bejal Lewis** 43:18 I have a question about that. I'm a fairly new contributor, so I'm not really sure what the process looks like, but I have a lot of interest in this.
And I know it's a very big project.
And what's the usual way that you would go something… that you would go about this? Would it be discussions in the SIG, or…
proposals that people can go over, just because if it feels like it's not aligned with the goals, but there's still interest, I'm wondering how the discussion can progress in the meantime, even if it's ultimately rejected.
**Tigran Najaryan** 43:53 Yeah, this is the quick discussion we're having here, that's… Not necessarily enough to
Changed my mind, in particular, as a maintainer.
I would want to see, let's say there's an issue open in GitHub, I would want to see
Upvotes, people saying they want it, the significant community feedback and requests from people that this is an important thing for them.
And then that probably would make me change my mind, right, as a maintainer, and I would say, okay, let's do it. Let's add it to our roadmap. So far.
I'm not seeing it, but again, I'm open to reconsidering it.
**Bejal Lewis** 44:31 That makes sense.
Thank you.
**Aunsh Chaudhari** 44:38 Okay, so I think, yeah, we'll, maybe, Angel, you and I can just sort of compile some feedback, or also reach out to folks and see if there's interest out here, and then follow up on that. I did want to…
understand, in this case, Andy, with the implementation, with, buying planes collector, do you also handle lifecycle management operations similarly, based on this approach itself, which means not just configuration, but
The way you start and restart the collector, it also applies for upgrades, because the supervisor is also the thinking of it being separate from the collector, it also being able to perform those operations, ideally, but looks like you're also doing this
For the other operations within the.
**Andy Keller** 45:20 We also support upgrades, there's a separate,
kind of small binary called the updater that we distribute, and the way it works is,
The updater kind of takes over.
replaces the binary. If the new binary doesn't start, the updater will restore the old one. It waits for it to report itself as healthy, and…
So, it does support upgrades.
Okay.
it's fairly full-featured. I… you know, we're really happy with it, and have been using it in production from…
several years, I don't know, 3 or 4.
at the same time, we're also heavily invested in the supervisor as an approach, and I think the…
Our primary interest in the supervisor isn't about the functionality, because we already have the functionality in our distro, it's about bringing other distros into
Op-amp enabled.
environments. So, if, if we have a customer building their own distro, which we have many that do, and… and,
You know, they… they… the… the…
the way they get op-amp is via the supervisor, so…
So it's the way you support any arbitrary build of the collector, and not just our distro that happens to build in OpAmp.
So…
**Aunsh Chaudhari** 46:49 Agreed.
**Andy Keller** 46:49 Just in terms of history, you know, when we did this implementation in our collector, there just wasn't anything upstream. There wasn't an extension, there wasn't a supervisor, there was…
And we were really early on the project and wanted to have our collector support op-amp, and so we… we took this approach.
And,
There were a bunch of issues that we had to resolve around restarting the service, because there were singletons that were created, there were ports that were opened, and it wasn't necessarily a clean shutdown that would allow a restart, but we basically addressed those over the last…
Several years, and haven't had issues, so…
And there's also the, you know, there's now the SIGHUP
approach is in that discussion in Slack of reloading configuration. There's…
**Tigran Najaryan** 47:45 And, you know, so…
**Andy Keller** 47:48 There is some… Interest in dynamic reloading and, you know, hot reloading, and… and that is related
obviously to OpAmp, because that's going to provide the configuration, so if we've got a…
A collector that can do a hot reload.
And we have OpAmp that can communicate configuration.
You know, can't we combine these things and allow,
the standalone collector to reload when it receives a message, so… I think…
there's a lot of different ways to solve this problem. We've got a lot of momentum a lot of…
Progress on the supervisor and extension approach.
But I… at the same time, I think…
The kind of beauty of open source is that we can… we can…
Do lots of, you know, as far as there's… as long as there's interest in doing these things, then there's,
you know, people willing to contribute the effort, we can… we can do all of them. We can have lots of different ways to do this.
So…
**Tigran Najaryan** 48:52 Yes.
I think that makes sense. But again, to reiterate, I think it's… it's important for us to… we invested a lot in the supervisor. I think it's important for us to get it done.
**Andy Keller** 49:05 I agree. We don't want… we don't want 5 partial solutions.
**Tigran Najaryan** 49:09 Yes.
**Andy Keller** 49:09 Yeah. What?
**Tigran Najaryan** 49:10 When it's done, and there is still a need for a different solution, then we can look at those alternate solutions, but…
Yeah, I think that's what we should continue.
**Andy Keller** 49:23 Agreed with you.
**Tigran Najaryan** 49:23 There.
**Blake Rouse** 49:25 Just to provide some context from the… from an elastic side on how we run the collector, we run it also as a sub-process, like the supervisor.
And we look at it as a standpoint of not mixing the control plane and the data plane.
We don't want a bad configuration or something to bring down the whole process, and then we have no way of recovering. So using a supervisor is really the best way to do this, so this is…
I would say the better architecture is to use the supervisor in this regard. That way, if something does go wrong, you have a way of recovering. Whereas if you're
process with the collector, and you get a config that causes a crash.
You now have to recover from that scenario, and that's not an easy scenario to recover from.
So, I think from the standpoint of going down the supervisor path, This is a much cleaner.
**Andy Keller** 50:19 Certainly, you know, part of the design principle of the supervisor.
**Aunsh Chaudhari** 50:24 separation of concerns, yeah. Yeah.
**Andy Keller** 50:26 Yeah, I will say the way we handle it, if there's a panic, there's nothing we can do about that. Hopefully, we don't have configs that cause panics and cause the process to crash.
But,
you know, we can determine if there's a configuration error on startup, and we will restore the old configuration, and that's all possible in process.
But again, if you, if you literally panic and crash.
Then it's gone, and it's not gonna… it's not gonna reach out again, and it's not gonna get a new configuration.
**Aunsh Chaudhari** 51:00 Yeah, you're gonna lose out on the management… management connection, yeah, yeah.
**Andy Keller** 51:03 Yeah.
**Aunsh Chaudhari** 51:09 Yeah, makes sense. I think there are trade-offs for sure, I think, in terms of the onboarding versus, the…
**Andy Keller** 51:15 She mustn't think so.
**Aunsh Chaudhari** 51:16 That's always the case. So, yeah.
Sounds good.
Thank you.
**Andy Keller** 51:26 Yeah, I guess it would take more than a panic, but something… something very violent that would bring the collector down.
Could be a problem.
**Tigran Najaryan** 51:37 I think we're done with the agenda in the doc. Anything else, anyone?
Alright, thank you all.
Bye.
**Aunsh Chaudhari** 51:57 Thank you.
