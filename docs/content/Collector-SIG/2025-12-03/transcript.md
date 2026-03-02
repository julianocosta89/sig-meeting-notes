SIG: Collector SIG
Date: 2025-12-03
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**Andrzej Stencel** 04:24 So we should go to the…
**Jade Guiton** 04:32 I have a hard time hearing you.
**Pablo Baeyens** 04:43 It's difficult to hear you, Andre.
Yes, we can…
start, but Andre, I… I'm not sure what you said, so, like, if you want to… to talk again, this.
**Andrzej Stencel** 05:38 I'm sorry, I think my headset was messed up, and I just started hearing you.
In a second ago.
**Pablo Baeyens** 05:48 Yeah, I guess we can… start with… the board,
Shad, do you want me to… to do it, or…
**Jade Guiton** 06:02 Sure, either way.
Okay.
**Pablo Baeyens** 06:09 Yeah, so… I guess under discussion… I… maybe I put…
the one about semantic conventions, we talk about that In other contexts, like,
This issue is about host metric receiver, but there's also… The Kubernetes,
Semantic conventions, and we had some discussion about the
gRPC semantic conventions used by config gRPC?
I think it makes sense to have a… unified… Decision about all of this.
I was… thinking maybe a short RFC would be a good way of…
Of having this written down somewhere.
I honestly don't have a…
very strong opinion here, but I guess… The…
Main thing we have discussed here, and…
Chris, just correct me if I'm misremembering, but, would be to have…
Two feature gates, one for, disabling…
The old semantic conventions, one for enabling the new ones.
And so… We would,
Eventually migrate people to the new ones, but they can emit the old and the new at the same time.
I… I don't know if I got that right, Christos, if you want to… Correct me.
**Christos Markou** 08:03 Yeah, I think that's correct, and we actually…
have derived this from the strategy that the instrumentation, the SDKs were following, when migrating things like HTTP, SMAT convention, other related areas. I think there is a wider discussion around SMAT conventions in general.
And if we should be blocked or not by these while trying to stabilize components. So, I agree that maybe an RFC
Touching all these different topics would be ideal, because so far the several different subtopics have been discussed in different issues.
But for this specific one, I think, yes, that's the recommended… that's the approach that we had in mind so far. My only concern about this is that, there was this question if we should have a single feature gate pair.
Or if we should allow having, let's say, multiple feature gates show us to start,
show us to start the migration earlier, instead of waiting for the whole namespace of gates, let's say, or system or process to become stable in some other conventions before being ready to, like, make the actual migration, the component.
The argument against this is that it makes things harder for users to maintain multiple feature gates, and maybe the user experience won't be great there, because people might only want, like, a single feature gate pair, so as to migrate from the old mapping to the new mapping.
But realistically, my concern is that,
let's say the stable feature gate. It might be, like, a bucket that we will start adding, stable semant conventions there, and it's not really specific when we should, like, stop adding metrics or whatever, or semant conventions there, and actually
say that, okay, that's a feature gate pair now, we stop adding new things, and we should, like, mature, progress the feature gate pair, make it from alpha to bet, and then promote it to stable, and eventually remove it. Because I'm afraid that we might end up with a situation that we will
have the feature gates there for, I don't know, multiple years, keep adding extra things, and…
Then, after a while, what if we want to actually do an extra migration, because we're having a new, let's say, group of metrics, we want to stabilize them, we stabilize them in some art convention, we want to migrate them back to the components.
I assume we cannot actually use the same feature gates, right? We would need something different.
So this is my concern, mainly, but if people agree on having a single pair, I would at least try to make it per component, so as to unblock the work there, and at least be able to finalize the work
in cage attributes processor, for example, and then handle other receivers, cage receivers,
Specifically, in other words, more later. Yeah.
**Pablo Baeyens** 11:23 Yeah, I guess…
I think it doesn't make sense to have a single feature gate, it could make sense to have, like, this.
Meta gate that allows you to enable or disable other, ones.
But… but yeah, I agree with you that it's unclear when that… would be… marked stable.
Well, or, like, faced away.
I… So, go ahead.
**Jade Guiton** 12:00 Yeah, I was going to say I support the idea of multiple feature gates. What I was thinking is that…
instead of having a pair of feature gates, one for enabling, one for disabling, if we're going to be going with the same model as the… as, like, the HTTP and RPC semantic conventions.
maybe it makes more sense to stick to the method that they're using, which is to say, have a single environment variable that switches between, I want the old convention, I want both conventions, I want the new conventions.
Like, the last time this was discussed, there was the idea that Using the existing feature gate.
feature of the collector would make things more consistent, but on the other hand, it… it… there's the question of how this is going to interact with the environment variable-based
gating.
So maybe it would make sense to… Standardize on that instead.
I don't know what you think.
**Christos Markou** 13:08 Have we used this pattern so far in the collector? I mean, the environment…
**Jade Guiton** 13:13 implicitly used it, I would say, since we have
We are using package, that produce HTTP and RPC,
telemetry, and that use this environment variable, under the hood. I don't think we've ever advertised it, but…
I think we technically already have stuff in the collector that uses these environment variables.
**Pablo Baeyens** 13:44 My concern with that is that it… Like… If you're not…
say you have a team that maintains the collector deployments, and then there's another team that handles instrumentation, or something like that. If you're not aware of the instrumentation side of things, the thing that you know for migrating on the collector is feature gates. You don't necessarily know about environment variables, and .
**Jade Guiton** 14:12 Yeah, I guess that's… Yeah, it's a good point that the…
the thing I've been talking about here is the collector's internal telemetry, whereas I assume here we're more talking about matrix produced by receivers. I guess that, yeah, you could make a case that it's different enough.
**Pablo Baeyens** 14:35 Okay, I'll…
I don't know if I'll have time to publish a full leafletter I've seen, but at least I'll…
Write something down, un… At least share it with…
the people that I've been discussing here to get early feedback, and then… Publish it.
maybe when I'm back from vacation, but we'll see. If I have time.
Okay, and then there's a few PRs… 4D…
Kubernetes attributes, and for the Prometheus receiver, that's the project link, I…
Don't know that it makes sense to discuss any of them in particular, unless somebody wants to, but,
They need, they need some love.
on some reviews.
And… unless somebody else has… Any other topic on stability?
We can move on to the next topic.
**Andrzej Stencel** 15:57 Yeah, I do have one. So, about the filet receiver, I'm looking at this.
I was out for the last couple weeks, so I'm just looking at this.
There's this issue to promote it to stable, and I think there are no sub-issues for this, right? So this is still in progress. We need to define what we want for the file receiver to be stabilized, what we need to do before that, right?
I think I saw something about Braden volunteering to work on this.
I can reach out to him.
**Pablo Baeyens** 16:30 Yeah, so we talked, last week about,
Having somebody for each component that would
add issues to the, to the project board, like, add… list the issues that would be needed for stability. So yeah, I guess you can reach out… reach out to Raiden.
**Andrzej Stencel** 16:52 Yeah, sure. Okay, thanks.
**Christos Markou** 16:54 I… yeah, maybe, Pablo, you can, like, correct me here. I followed the pattern that I saw for the Prometheus
stabilization issue. I saw there Artur created some sub-issues based on the requirements, like testing, configuration, documentation, so on. So I followed the same pattern and created sub-issues for this, and also adding additional ones for the KH processor.
**Pablo Baeyens** 17:21 Heidi, the same as you.
**Christos Markou** 17:23 Okay.
**Pablo Baeyens** 17:24 Yeah, I did the same as before, the resource detection processor.
**Christos Markou** 17:27 Okay, cool. Maybe we can follow this pattern, for the components.
**Andrzej Stencel** 17:35 Yeah, sure, thanks, I'll do the same for the follow-up receiver.
**Pablo Baeyens** 17:49 Cool. Let's move to, the next topic, then.
She's from, hank, I don't know if I'm pronouncing your name correctly, sorry.
**Pankaj Kumar** 18:05 Yes.
So, this is an issue, right, for a…
This issue contains, basically, a design.
For the introducing the auto-discovery of the domain controllers.
In the Windows 7 log receiver.
Right, and I just wanted the input from the code owners of this component.
But I guess code owners are not present, so…
If, like, other members can also have a look.
Hey, guys.
Code owners are required, right, to make change in this component.
**Andrzej Stencel** 18:46 Yeah, I think you would need Paolo Gianotti to take a look at this, right? He's been involved heavily in anything Windows. The other code owner
It doesn't look like they've been active for the last 2 years, at least.
They used to work with ObserveIQ, but they've switched jobs since, and maybe we should just…
I'm gonna let them go. Politely.
Well, yeah, Paula, you should chase Paulo, and he should be good as long, yeah, as long as he feels fine for that, sure.
**Pankaj Kumar** 19:19 I discovered Peru, he said he will join this thing, but I will discuss offline.
In Slack.
**Pablo Baeyens** 19:28 Yeah, it's a bit early for…
For Paolo, and Paolo's time zone, so… maybe…
on one of the other meetings, you would be able to catch him, but right now, I think it's 5AM for him, so…
Torrely.
**Pankaj Kumar** 19:47 Okay.
**Andrzej Stencel** 19:48 Yeah, but chasing him on Slack is probably very good as well. You need to be persistent, I suppose.
**Pankaj Kumar** 19:57 Hmm, right?
**Laurent Dufresne** 20:03 Okay, so I guess, next topic is mine. So, yeah, I'm very new to the whole process, so that's why I joined, so feel free to interrupt if, or…
Yeah, if I go in the wrong way. But yeah, I guess I want to bring some eyes to this issue. So, this comes from basically an issue that we observe where
we had out-of-memory crashes, in production, when there was, like, too large an OTLP message, and so the idea was, like, to figure out a way to, yeah, to deal with that, and so this issue
Sort of, adapt the…
PData code generator to be able to deserialize the protobuf message, not as once, or, like, not unmarshall the whole OTLP metric messages, but, sort of do it a bit more in a stream way, or lazy deserializing.
So I'm not only… like, I created this issue with a lot of detail, like, there's an implementation that exists, so, like, could definitely also go with the PR, but I wanted to, I guess, let
the chance to discuss, because obviously it changed a bit, the way things are done, so I sort of assumed that maybe… or I actually asked and Jade reply in Slack, that maybe it's best to create an issue, to allow for discussion for that? Yeah, so…
not exactly sure where to go from here, but I wanted to, yeah, advertise, I guess, about this issue and get some feedback, about
The way to go about it.
**Jade Guiton** 21:33 Yeah, so… I believe there's been…
I don't know how far he looked into it, but I think Bogdan looked into lazy deserialization at some point, right?
And he's one of the… listed as one of the owners for Pdata, so, I think…
If you can find a way to… to contact… Bogdano Dimitri.
It might be good to discuss it with them.
Because it's possible there's already some… some stuff…
in the works for lazy deserialization.
But I don't really know how far along it is.
**Laurent Dufresne** 22:16 Okay, sounds good. Like, would the most appropriate way, especially, I think Bogdan is working for the CNCF, or his members, so I guess probably on the Slack of the CNCF would be ideal, at least for Bogdan, I'm not…
**Jade Guiton** 22:30 Yeah, so I think on Slack would probably be… Be the best option.
**Laurent Dufresne** 22:35 Okay, great. Thanks a lot.
**Douglas Camata** 22:44 Okay, I guess it's me next. So, I am here again, asking for some, some eyes on these two issues. I'm sorry if it looks repetitive for some that also joined US Call, but there is a slightly different audience here.
So I'm bringing these… these two again, and
Mostly, I want some… some opinions, I want to see if people agree with my proposal, or, with my proposals, or if there is anything that we should, change there to get to… to an agreement.
Yeah, even on whether we want to implement those things, and if yes, A bit how?
And yeah, I have a strong interest in moving these
forward with the implementation as soon as possible, right, if we come to an agreement that we want to have these things first, and relative good alignment on how to implement them.
So… so please, if you have some time, have a look, let me know if you think it's a good idea, or if you think it's a bad idea, or if you have a good hint on…
Good… on a good path to implement some of these things.
for example, the, reporting the configuration file without the defaults included via OPA… OPAMP Might require some…
a smart implementation to avoid breaking the…
the notify config interface. The other issue that is related to the supervisor, maybe…
Maybe there are some details hidden there as well, so… just looking for some… Opinions, and
alignment, so that I can proceed with implementation.
And and one other thing I wanted to mention is that I… I talk a lot in the… in this SIQ call about OPMP, because the OPMP call
is a bit late for me. I am in, in,
in the EU time zone, as I suppose a lot of the people here
So 8… it runs at 8pm my time, so that's why I bring a lot of these topics here instead of off there.
**Jade Guiton** 25:25 Yes, I've been meaning to jump… to join the OptMSIC meetings as well, and it is a little bit…
difficult, so… I don't know.
If I fly.
**Douglas Camata** 25:35 I plan to… to message… Sorry, I plan to message Tegram to ask if,
If we could bring it
a few hours earlier, maybe 2 hours earlier, so that it matches the time of the US collector call.
But if it runs on… if it could run on a different day, maybe it would allow more people from European time zones to… to… to also join. But it could also affect…
people from… time zones more around Asia as well, so I don't know.
But I plan to start a conversation.
**Antoine Toulme** 26:16 You can take a look at the calendar of the OpenTometry figs, and you'll see that it's pretty difficult to find an open slot at this point.
So.
**Douglas Camata** 26:26 It's a must be.
**Andrzej Stencel** 26:28 What is the up-and-stig? Oh, sorry.
**Antoine Toulme** 26:33 Just… sorry, let's machine my point. This is not a Tiguan question, this is a communication question. You can ask this as an issue on the community repository.
And I think, you know, Tigrant does not get to decide when things happen for this SIG. This is a consensus issue, so you have to kind of make that public, and Tigrant can probably help you with the process if you reach out to him, but open an issue under the committee project piece. Thanks.
**Douglas Camata** 26:59 Yeah, sounds good.
**Evan Bradley** 27:02 So, I attend… Oh, okay, so I attend the OpAM SIG fairly frequently. I don't think that,
what do you call it? I don't think that worrying about, those in Asia is too much of a concern at this moment. Of course, that could change later.
I would say that, to Antoine's point, open a community issue, but also, put that in the hotel op-amp
Slack channel. I think that there would be probably broad agreement that we could move it forward. I think we always want more people in that call, so anything that we can do to accommodate more folks would be welcome.
Jad, you can go ahead.
**Douglas Camata** 27:42 It's…
**Jade Guiton** 27:44 Yeah, I didn't have much else to add. Maybe I was thinking…
Since it's 2… every two weeks, maybe there's an open slot on the week it's not usually on?
But maybe doing it every week would be too often, I don't, I don't really know.
**Evan Bradley** 28:04 I think every week might be a little frequent, but, you know, it's worth discussing, at a minimum.
So, for the… Douglas, for your issues specifically, reporting the file content, we do have a feature gate to disable
masking secrets, I think that could…
kind of help here a little bit, but as for per-file config, that would need some pretty extensive changes in core. I don't see a way to…
Easily do that without, getting pretty creative, with, you know, reading the collector's command line arguments and manually reading the files or something like that.
**Douglas Camata** 28:48 I have an idea that I wrote in, in the issue. I don't know, maybe there is something else hidden there that makes it not possible, but I… I thought we could, put it in the… in the conf, struct that is passed in the notify config
function call.
Because I… that… that,
That struct is populated when the config is being processed by conf, by our library.
So I thought we could somehow leave the…
the raw files there, because, and… and also, I would… I would say secrets could stay masked, but…
What annoys me in the… what makes the effective configuration not useful for me and makes me want those raw config files is that the effective configuration has all of the defaults, right, that are added by the collector.
And, and all of the components, right, that own their own configuration. And, those defaults that…
that annoy me, and I would like to just see the file without any defaults, and without having to somehow hack my way through
Remove… figuring out all of the defaults, and remove them from the effective config to get to the…
to what would be the contents of the file. But secrets, I don't… I would prefer that they stay unmasked, even.
**Jade Guiton** 30:26 Yeah, I think…
**Evan Bradley** 30:27 Go on. Go ahead.
Oh, okay, I was gonna say that, the… as for the defaults, anything where it's a zero value, in the go struct, we can put the, and I've done this for a couple, but I'm sure I've missed a few.
We can put the omit empty, or I don't remember if they renamed that tag, but basically you can have it not omitted. The reason that we include defaults where it's not the zero value, so let's say this is, like, a timeout of…
you know, 30 seconds or something like that, is so that you understand, like, why the collector is behaving like it's behaving. But I do understand the, the desire to get, you know.
Closer to what was actually input into the collector.
**Douglas Camata** 31:10 Yeah, those defaults… those defaults that are not zero values are also important, because right at the end.
You might want to know the exact configuration after everything, because you need that to understand the behavior.
And even if there is a default there that is not a zero value, like, maybe a timeout is 30 seconds, with just the effective configuration.
You cannot know if that was part of the input, someone wrote that in the config, right? Or if that is a default value.
So, so yeah, like, zero values are a bit easier, but there's a lot of… there are a lot of defaults that are not zeros, and then you… you cannot know if that was part of the config.
file or not.
But, but yeah, there, maybe, maybe there are some tricky things. We can talk in the, in the issues as well.
Or in other channels, if you all agree.
**Jade Guiton** 32:14 Yeah, I'm definitely supportive of the idea of exposing the actual configuration files to OptMP, especially because the protocol already has provisions for returning multiple files.
Especially because the mapping between… from the text config files to the effective config to the marshalled config that gets exposed through op-amp is non-trivial. So I'm definitely in support of it. I think the bigger problem is…
exposing it through, Conf or through the Notify Config interface, that's definitely doable.
The hard part is actually keeping track of all the…
the files through the confab and marshalling process. There's just a lot of work, essentially, to be done on the core collector for this to happen first.
So, yeah, it's definitely doable, just, a lot of work, and I think that's why there's…
No one jumping at the bit to implement it right away.
maybe, like, I don't know, if we can propose a… more concrete.
implementation in Core, maybe it would help move things forward?
I don't know.
**Douglas Camata** 33:33 Yeah, yeah, that is… that is one of the things that I wrote in the issue, is that I'm aware it could mean a lot of changes in core.
But, first, I want to see, right, if we all agree that we want to have this feature, then I can probably work on a more concrete implementation plan, and share it there, and of course, if other people
Have better ideas on how to implement it, then we can discuss and find a way.
Yes, Pablo?
**Pablo Baeyens** 34:05 Maybe you can… I think having an implementation plan would be useful here, and maybe…
Thinking if there are steps within the implementation plan that are…
useful by themselves. Like, even if we don't get to the end goal, the ideal state where you have what you want, maybe there are intermediate steps that are… that are useful.
And that, we could… we could just work on… until that step, and, see…
See how it works. I guess, to add also to Jad's point, there's a few…
cases where I don't know what would be the best way to represent things, so…
I mean, mostly edge cases, but things like,
If you're merging multiple configuration sources, if you have, say, a sensitive field that is constructed from multiple
environment variables, something like that.
I don't know how to best model those, and
I… don't know if we want to do the reduction of sensitive fields, for example, how we would
do that reliably, or at least it seems hard. I'm sure we can do it, but it seems hard.
**Jade Guiton** 35:24 I think, like, since the goal here is to just get…
the raw data before it's been processed. At least, that would be my understanding of the goal, you know, because otherwise, if you want something that's pre-processed, you already have the effective config.
If you want the raw data, I think it would be maybe possible to just expose just the file names.
potentially multiple of them, and just emit those to op-amp.
I don't think, like, we want to emit a merge config, because you might have issues with the merging, for example, that you want to debug.
**Douglas Camata** 36:00 That's true.
**Pablo Baeyens** 36:01 Sure, but I…
I guess… well, yeah, if you don't want to… if you don't care about the sensitive fields, then maybe it's easier, but if you care about the sensitive fields, sort of tracking back to the configuration sources which one of them should be reducted and which one should not, is a harder problem than it seems.
**Douglas Camata** 36:24 Oh, yeah, yeah.
**Jade Guiton** 36:26 I don't… I'm not sure if it's really…
possible in general to do redaction while allowing access to the raw files.
So, like, if there's a… maybe we'd need to expose this capability as something that's optional and has to be enabled
Explicitly with the understanding that this will send potentially sensitive information.
But…
**Douglas Camata** 36:53 sounds like a reasonable approach, yeah, and just to clarify a bit, something that I will also put in the issue, I was think… I was… my intention is to rep… or was, at least, but I think it still is, to report
each file, right? We have their config map structure, where we can put each file in its own entry, and, ideally.
As raw as possible, so no injection of environment variables, so maybe there would be less potential for secrets to pop up, but of course they could be hard-coded, and then they would pop up, so…
This conversation about reduction is potentially important as well. I will add there to the issue.
**Evan Bradley** 37:47 So, just an addendum, we could do something where we track, which fields the users manually set, and then see at the end which ones were created by default that don't match a zero value, but, that would be, on top of a problem that already requires quite a bit of work, a ton of work.
But just throwing that out there. However, the… I was gonna talk about your second issue as well. The fallback config I generally agree with. I thought we actually had something that already did that, but I would need to double check.
It's been a while.
But I think if we don't have that, that, adding a fallback config that is only run if we are not able to make a…
connection to the op-amp server, or there's some other issue, would be good.
**sylvaingerme** 38:45 Specific.
Excuse me.
Super cool.
**Douglas Camata** 38:49 Yay.
Thanks, thanks. I don't think we have, something yet. From… from what I… from the quick look I had in the issue, today, if,
Write a new supervisor start without any previous state.
**sylvaingerme** 39:04 situation.
**Douglas Camata** 39:04 At least in this case, I know that if it cannot talk to the OPMP backend, it will not even start a collector.
**sylvaingerme** 39:12 Wonder existing languages.
**Douglas Camata** 39:14 I'm not sure about the case in which there is already a state in disk, and
And it loses connection, but that's something to test.
**sylvaingerme** 39:29 Fantastic.
topic.
**Evan Bradley** 39:33 I think that if we already have it, I'm not sure off the top of my head either, which we should.
**sylvaingerme** 39:40 It's cute.
**Evan Bradley** 39:40 document that, but I don't know if there… I think if there is existing state, it will start the collector with that state until it, gets a connection from the server, in which case, I think we should,
We should leverage that functionality to say, even if you don't have… if you don't… if you have state, you can use it. If you don't have state, then there's a fallback for that as well.
**Douglas Camata** 40:06 Yeah. And, and, do you…
**sylvaingerme** 40:08 Do you agree with my idea that.
**Douglas Camata** 40:12 this fallback config would be completely discarded after connection to the OPMP backend is achieved successfully.
**Evan Bradley** 40:22 Yeah, absolutely. I think that whatever the server says is what goes, right?
**Douglas Camata** 40:29 Yeah, we already have other ways of, of mixing configs if you want, but, this… this is… should be very separate.
**Evan Bradley** 40:42 Yeah, yeah, agreed. And thanks for driving both of these forward.
**Douglas Camata** 40:52 Okay, awesome. Thanks, thanks everyone for your input. I will do some… some improvements there to the… to the issues where it's needed, and
If nobody else has any comments to make, I think we can move to the next.
**PL Pavol Loffay** 41:13 Hi everyone, I'm next on the list. I would like to discuss the collector config schema. I was working on the MCP server.
Which, should help users to… to configure the collector. And, I was looking if there is a way how to get
the…
the entire config schema for each component, and I couldn't find a good API in the collector, and I wonder if there is any… there are a couple of issues open in the collector and collector contrib, and I was wondering if there is any… any progress on improving the config schema.
**Pablo Baeyens** 41:59 So I'm going to… We have another issue on the…
Zoom chat, because I did the work of listing all of the attempts that We've had a…
well, generating documentation of component configuration, but surely we've always tried to do that through our schema, and
There has been… 1, 2, 3, 4, 5…
Five different attempts at starting this.
But, yeah, to answer your question, we don't have a schema, would be great to have it, would be great to have it per component. It…
Seems like it's a hard problem, given the amount of attempts we've had at it.
I would love to have it, because it would allow us to have better
Automatically generated documentation, but we don't have, schema right now.
**PL Pavol Loffay** 42:54 Yeah, so maybe I can add what I actually end up doing. So…
I was able to generate schema with the help of the collector builder, so I defined it… I essentially copied the… the contrib…
manifest for the collector builder, and then I imported the components
And then I generated the schema from the source code.
And I wonder if this could be…
If we could extend the collector builder in a way that it would generate the schema for the
You know, components that are defined in the manifest, and then…
This could be used for documentation, but as well could be…
somehow import it to Component and served at runtime.
**Jade Guiton** 43:54 Curious how you're…
**Pablo Baeyens** 43:56 Okay.
**Jade Guiton** 43:57 Go ahead.
**Pablo Baeyens** 43:59 I was gonna say, like, as a general thing, we definitely want this. I…
I haven't looked at your specific implementation, so I don't know how it works, or what…
would need to be done to all upstream it.
Go ahead.
**Jade Guiton** 44:15 Yeah, I was thinking, I'm curious to know how you're generating a schema based on the code. That's for each component, yes?
**PL Pavol Loffay** 44:25 Yeah, yeah, you can see there is a link, you can jump into the repo.
**Jade Guiton** 44:30 Hmm. I see.
**PL Pavol Loffay** 44:32 I just want to make sure there is no, like…
ongoing efforts to improve it. I can maybe… crafts…
not sure if new issue, or somewhere on the existing issue, like, document how I did it, and how this could be…
Done in the… In the collector builder.
Or as a collector component. I think first we should start with the builder, because that's…
the most important piece that I need to make this work.
So, yeah, let me know if I should open a new issue or document it on one of these existing ones.
**Pablo Baeyens** 45:22 Looking at it, I'm curious about… So, for example, I see…
**sylvaingerme** 45:27 What's…
**Pablo Baeyens** 45:28 configure bake is not explicitly handled, which I guess should be easy to fix.
Do you handle config optional in any special way?
**PL Pavol Loffay** 45:44 Maybe. I worked on it a month ago. I don't remember all the details, to be honest, but .
**Pablo Baeyens** 45:49 Fair enough, fair enough.
**PL Pavol Loffay** 45:55 But it was, like, for… I remember that, like, for the HT… for the OTLP receiver and exporter, I think I was able to, like, get all the fields, even from the…
Like, dude.
the server TLS config.
**Jade Guiton** 46:23 Yeah, we're related to…
**Pablo Baeyens** 46:26 Go ahead. Go ahead.
I was gonna say, my preferred way of doing this would be… If we can…
Use the tool that you built to progressively replace the…
configuration struct on different components by JSON schema, and then generate the configuration struct from there. I don't know how easy that would be. If that's too hard, I'm also, like.
fine with a previous step of, like, just… we generate the schema from the existing code. I think that's also…
valuable.
**PL Pavol Loffay** 47:08 Okay, awesome, so I'll…
I will continue in one of these issues and maybe open, like, a proof-of-concept PR that will maybe showcase better what needs to be done.
**Pablo Baeyens** 47:19 Yeah, maybe something like the OCLP receiver could be a good, more complex example.
And, Jat, sorry, you were saying something, and I… Started speaking as well.
**Jade Guiton** 47:37 Yeah, it's just related to what you were saying about config optional and config opaque.
I'm… A little bit worried about how…
this would work with custom and martial functions, because there's quite a lot. Most of them provide defaults, which I guess doesn't really change the schema, but…
While I think we could definitely generate a best effort.
schema? I'm not sure how easily we could replace the config structs with something generated from the schemas.
because of… Like, the potentially arbitrary…
Unmarshalling code that components may have.
And we could handle everything on a case-by-case basis, but…
**Evan Bradley** 48:32 I agree that that's a blocker for any components that do that. That's part of why I've been pushing to try to minimize those functions as much as possible.
**Jade Guiton** 48:44 Yeah, I think ideally, ideally we want to move away from that.
It's just… it's a lot of work. There's a lot of components that still use on Marshall, and a lot of them use them in different ways.
**Evan Bradley** 48:57 Oh yeah, no.
**Jade Guiton** 48:58 I, I, I…
**Evan Bradley** 48:58 It's gonna be a long road.
**Jade Guiton** 49:00 Yeah, I'm relying on the… on the ultimate goal.
And, I mean, at that point, we'll probably have much easier ways of generating a schema.
**Evan Bradley** 49:16 So, I will throw in, my initial preference for, like, where to have component authors write the schema would still be in GoCo, just because you can annotate it with struct tags, and we have fairly good reflection capabilities that I think will…
make it a little bit more, just easy to work with than JSON schema, not to mention the fact that, in my opinion, if we were to go with JSON schema as the source of truth, we'd probably need to…
essentially, you know, wrap around it, like, some kind of nice metadata.yaml abstraction or something. But I think for the sake of the most flexibility, using Go code as the source of truth is,
maybe… it feels a little weird, because it's not, like, a declarative file format, but I think that's what's going to provide us with the most flexibility.
**Pablo Baeyens** 50:10 That's fair, and I mean, even if we want to do JSON schema to Go code at some point, I guess starting with Go code as the source of truth.
Given that that is the reality today, it's a… would be the startup.
As well. So, yeah, we can…
maybe just start with a tool that produces JSON schemas from GoCode.
**Evan Bradley** 50:35 That's also a good point. I'd be… I'd be in favor of exploring other options after we've, gotten our feet wet a little bit.
**PL Pavol Loffay** 50:52 Okay, thank you, folks.
**Israel Blancas** 51:01 I think I am Nitz.
So yeah, I would like Jazz to have some eyes for this PR.
It's APR for the reduction processor to improve those features that were recently added to do some DV and URL sanitization.
It's improved that, you know, when you have everything enabled, for instance, right now there is a bug that is…
breaking the functionality, but also, for instance, you have URL sanitization, DV sanitization, right? About, it seems like
you use the URL syncision thing with
database queries and things like that, right? So please, when you have some… some time, if you want… if you can, take a look.
Oh… And yeah, it's just to get some feedback on this.
**Evan Bradley** 52:35 I think that's it.
**Pablo Baeyens** 52:40 Yep, I was gonna say, it's on my list as well, it's just…
**Israel Blancas** 52:44 Yeah, yeah.
**Pablo Baeyens** 52:44 I have a before I go on vacation, but…
**Israel Blancas** 52:47 I know, I know, I know, don't worry, but, you know, it's like, not just asking for code owners, right, but if somebody else can take a look, right? Because I know it's a big PR, but also the things that they tried to cover many cases and everything, right? Because we were…
Kind of relying on the underlying…
Library is right for doing the same, but it's true that depending on what you enable or In…
what attributes and things that you are using in your response and things like that, right, can have a different output, right? A different outcome. So I added…
bunch of things, right? So I know this is a bunch of codes, so if we can have more eyes than just the code owners, it would be… it would be great.
Thanks.
**Pablo Baeyens** 53:44 Cool. Yeah, I think Evan was saying there… there are no more topics?
So… Thank you, everybody.
**Evan Bradley** 53:54 See you, everyone.
**Christos Markou** 53:55 Everyone.
**Douglas Camata** 53:57 Bye-bye.
