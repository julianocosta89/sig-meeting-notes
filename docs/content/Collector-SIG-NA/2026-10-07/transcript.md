SIG: Collector SIG (NA)
Date: 2026-10-07
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 00:55 Hello.
**Evan Bradley** 00:57 Hello.
**Alex Boten** 02:26 Looks like we have a pretty full agenda. Do we wanna start with the first item there? 15 minutes to go through the high priority.
Issues. Looks like there's also a comment from Tyler in there. And Pablo, you have the first item.
**Pablo Baeyens** 02:40 Yeah, and there's 2 more items later than I think we can move to this section, since they are on the high priority list. Let me do that.
Yeah, so my topic is just that, we have an RFC for getting a core distro to be won by KubeCon Europe 2027. I have a bunch of comments that I have to reply to or address, but in general, this is just.
PSA, so that people review it if they have feedback about it.
There was a bit of discussion about this on the System Semantic Convention SIG. I will post a summary of that discussion.
On the RFC, but yeah, in general, just… Please review it if you have.
Any… Big buck.
And… I think I can answer Tyler's question.
Also, but I'll… I'll let Tyler speak first.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 03:40 Yeah, okay, so I was looking at the transform processor, trying to get it ready for 1.0.
And as part of that review, I noticed that we support In our… config a public field called, like, Profile Statements or something like that.
And it represents where you would write an OTTL statement to transform a profile.
We're gonna move Trace's… metrics and logs to stable, and we want to tag the component 1.0, but we want to keep profiles in development, because it's still in development, still in development in OTTL as well. In OTTL, for the public API, we could move profiles into their own module. I think it's an OTTL context X profile. That's its own module. It won't get tagged 1.0.
But for a processor or any component that we tag 1.0, because the config is part of that guaranteed API, because that config has to expose things for non-stable signals.
We're ultimately going to end up with a config struct that's tagged 1.0 that contains fields that support development signals.
And if that development signals, what if I wanted, like, in the future, if it's… if OTEL decides to change the name from profiles to profiles with two S's or something, you know, I've got to go change my config, I've just made a breaking change.
to a field in a 1.0 struct.
So, like, is that okay? Am I allowed to do that?
**Pablo Baeyens** 05:21 So the wording we have on the component stability is, once a component is marked as 1.x, signal-specific configuration options must not be removed or changed in a way that breaks our API compatibility promise, even if the signal is not stable.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 05:39 Okay.
**Pablo Baeyens** 05:40 I think… I mean, I don't know exactly what the configuration option allows, but if… If using it is… effectively impossible unless you're using the profiles feature gate. I would say the only guarantee we're making here is that the The name of that configuration option does not change, and that whatever is… validates Today, Continues being valid later?
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 06:20 Okay. I'm not actually really that concerned about it for the transform processor, because… It's going to be named profile statements, just like it is for traces, logs, and metrics.
But I guess… That, and maybe a less mature component, or in other situations that aren't profile-related.
I think there would probably be situations where I would.
There's not a good way to add support Let's say we're… let's say a component is 1.0 already. Let's say Transform Processor didn't have Profile support yet.
Or let's say K8 Attributes needs to add support for profiles, I don't know if it does today or not.
In order to add support and start developing.
support for profiles. The second we put that field on the config struct.
it's stable.
Is that… is that just the reality we have to live in? We gotta get that name?
Gotta get that name right, first try.
**Pablo Baeyens** 07:25 I don't think you need to get the name right. It's just that you cannot remove it later. If you get the name wrong, then you need to keep the old name forever in some way.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 07:34 Yes, and then just make a new one and deprecate the old one and say, hey, switch to this, or we support both, I guess, essentially.
**Pablo Baeyens** 07:40 Yeah, something like that, yeah.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 07:42 Okay.
Alright, that answers my question.
**Alex Boten** 07:46 Yeah, so one thing we might be able to take inspiration from is the configuration SIG. So, the configuration schema supports developmental… or features that are experimental or under development by appending the, like, development suffix.
to the name of the configuration item. There is an open issue currently discussing whether or not that's the right approach moving forward.
But for now, it kind of feels like, you know, at least we have some guidance on how we could support this in a way that's compliant with the rest of the project. So if we wanted to go in that direction, we could say this… we're following the same model, and we can update the phrasing in the Collector to follow suit as well.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 08:31 So, like, I could have in the transform processor, the field could be named profile statements development, for example, and that would be the public field. And then at some point when we feel really good about that and we're ready to move it to beta or whatever, I could add a profile statements field.
Both would be used, probably validate that only one is used, and then, like.
Deprecate the old one. Are you doing the same trick for the… like, map structure?
Like, the actual field in the YAML, like, are you… Are you throwing the word development into the field in the YAML as well? Okay.
**Alex Boten** 09:04 That's right. The field in the Yaml contains the like slash development pre suffix.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 09:10 Okay.
**Alex Boten** 09:10 Which is actually preventing us from using it within the Collector because of reasons.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 09:14 But… Evan, do you feel the need to do that for profiles, or do do you feel I feel pretty confident we wouldn't actually end up changing that name, but it it's good to I think it would be good to have a strategy like that documented for components to use.
**Evan Bradley** 09:27 Yeah, I agree. I mean, profiles, like you said, the signal name isn't gonna change, so… I think we're good. I don't see that config key changing at all. Less than a 1% chance.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 09:39 Okay.
Cool.
**Pablo Baeyens** 09:42 We expect this in general to be, like, an unusual situation.
A lot of our… the components are going to be… like, agnostic to the signal or the configuration? That would be my bet.
But.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 09:56 That's fair, yeah.
gary scott: There is. Yeah, for the configuration. The behavior could be different. But That can all… that's easier to gate, because we have feature gates.
**Pablo Baeyens** 10:07 Yep.
Okay, I put two more topics from, like, high priority stability. There's one that I'm guessing is from JMAPD?
If he's around? The one about the VATI migration? Was that you?
**Joshua MacDonald (Microsoft)** 10:29 I am. Can you hear me? Where are you?
**Pablo Baeyens** 10:31 Yes.
**Joshua MacDonald (Microsoft)** 10:33 Yes. Well, I was just putting PSA there for my batching migration, and I thought I was at the end of the notes, so I wasn't ready. But here we are.
**Pablo Baeyens** 10:42 We can do it later. Sorry, I move it. No problem.
**Joshua MacDonald (Microsoft)** 10:45 So, the batching migration has been documented, it's… for months, it's… it's underway, and I have, several PRs this last few weeks that have been in flight. Two of them are still open, but I think ready to merge, and then one has merged. It's the MDataGen support. So, what we're gonna see is, after this well, a blog post, which I'm going to try and show you next week. If you come to the specification SIG, I'll have it by then. We're going to talk about the OTEL Collector V1 and Spec SIG next week, and I'm going to try and talk about batching a bit there as well.
So, I'll have that blog post written and, or drafted at least.
The open PRs are… are no big deal. The one that emerged about MDataGen is something that we'll see in the, sort of coming months. So what… what will happen is that we're going to try and change from an opt-in to an opt-out over the next phase. So, currently, you will not have to do anything.
The MDataGen support is now there, though, so what you can do is begin to document the overrides. If you really want to not take the default options for QBatch, you will have to do an override by the end of Phase 2.
It's also basically giving us an opportunity to evaluate all the old defaults that were set, who knows when, you know, some of them were set so long ago that the batch processor, the queue batch processor didn't exist at that time. So… In the next few months, there will be, some 25 or so exporters in Contrib have overrides, and the question is how many of them need them, and how many don't, and this is what the tool is going to help us with. I will be taking care of most of this, I just wanted to give the PSA. Thank you.
Any questions.
Cross your fingers, it won't be very disruptive, but this will… in the end of Phase 2, we will get to the place where batching is on by default for most of the exporters, unless there's a good reason not to.
And that's the that's the whole objective here to retire the batch processor as well.
I think that concludes my my section. Thank you.
**Antoine Toulme (Splunk Inc.)** 13:02 Thanks, Josh. I think I got the next one. So… There's been a discussion we've been having on Config HTTP, or Config GRPC as well, and others.
We would like to customize the behavior of those extensions, of those libraries to take on an extension to do additional things.
The problem is that the way we do this, usually, is that we add fields.
To those libraries, those fields expose the functionality.
And in this particular case, this field is just a component ID that points to an extension.
I find that a bit difficult because we're trying to stabilize those libraries. We would very much like to reduce the mess, if possible.
In terms of discoverability, it's great to have it on the library itself.
But given that this function itself is deemed experimental or advanced.
I don't really feel the big need to make that available directly on Destruct.
So, in general, also, I find that we could hide a lot of mess in the internals of those libraries if we were able to have a way to make this configuration happen in the extension itself.
So, in discussing with Pablo two days ago.
We had a… I had an epiphany where I said, well, maybe… The extension should decide which particular exporter is going to apply itself to.
So, I'm asking if we would be open to having an inversion of control to how we define these relationships right now. Right now, the way it works is that the component starts, looks for the extension that is being asked to review.
You know, binds to that extension, and then goes from there. We would like to probably do it in reverse, where the component starts.
Looks for any extension of a particular type, and finds that at least one extension is registered to be applying to itself.
Based on some… Either exact match, or… well, we can start with exact match for now.
If there's more than one, then it, you know, complains and panics and fails, and… burst in flames. But if there's just one, then it knows what to do with it. If there's zero, it just continues to do what it's been doing before.
This allows you to have all the Additional mess in the extension configuration itself.
What do you all think?
**Pablo Baeyens** 15:36 One thing I thought yesterday was that one limitation Here is that it's hard to express the… Interaction between multiple extensions, if… say the… you need to apply them in a particular order. I think it was something like Middle Wars. Like, you need to define in what order you need to apply them, and it's hard to do that on the extension.
But for use cases that are not that, I think… it could be a good way of trying out experiments without having to modify config Http or configure Grpc.
Public API, but yeah, I'm curious about what other people think.
**Joshua MacDonald (Microsoft)** 16:24 Did we… have we… have we clearly stated the problem with doing it the way… the normal way, I guess the word normal meaning, that just put a new… config… extension field in the config HTTP. That's… I guess that was the plan of record.
And in my understanding, the goal of using a struct for config instead of an interface is that it allows us to add fields.
Yes. And so I guess I don't see why we wouldn't take that approach. Maybe you just said it and I missed it, but I'm just trying to understand.
**Antoine Toulme (Splunk Inc.)** 17:01 Well, I think, I'm trying to limit a little bit how much.
how much I'm impacting the library, if I can.
I'm trying to be nice. We… the current PR to add the dialer to Config HTTP and Config DRPC, is approved by you and others, and I think it needs a maintainer to review and merge. So that's an option, right? There was a final… There was one more comment from Alex that the name was actually probably going to clash a little bit with some other concepts, so renamed it to something else.
So, it's definitely, it's definitely fine to look at it this way. We have to do the same thing for Listener next.
I just think, like, we're not done. There's going to be another one, and another one.
So…
**Joshua MacDonald (Microsoft)** 17:58 I guess what I'm reacting to is that another one and another one is, like, maybe it's supposed to be the way it's supposed to be. Like, you can add struct fields.
If you're careful.
**Antoine Toulme (Splunk Inc.)** 18:09 Different.
**Joshua MacDonald (Microsoft)** 18:10 Anyway, I just… I don't see a problem, but maybe others do.
**Antoine Toulme (Splunk Inc.)** 18:13 I think that's a fun stance to take. I'm also just saying, like, in general, like, we have… So, look at it the other way, which is that I don't want to have so many things exposed in Config HTTP, because this is so custom, in a sense, that I don't know that people will be using that all that much.
Is there a better composable way, also, to have configuration?
That is maybe less discoverable, but also allows us to do more stuff, right? That is less in the way of where we are trying to be.
So to to I don't know. It's a it's a design.
It's a design decision.
Pablo, you got your hand up.
**Pablo Baeyens** 18:58 Yeah, I guess the context from my side, why I think this is interesting is, we want to mark configurative PS 1.0, we want to also allow experiments. It's hard to add fields in an experimental way, so this is a way out of it, and…
**Antoine Toulme (Splunk Inc.)** 19:16 Yep.
**Pablo Baeyens** 19:17 I don't know. I think that's the shortest way I can put it.
**Alex Boten** 19:21 Yeah, I mean, that's kind of.
**Pablo Baeyens** 19:22 I'm interested in Alex's opinion.
**Alex Boten** 19:24 I was gonna say this ties exactly into what Tyler was just talking about, where we don't have a good way of, you know, supporting experimental features in fields and config today without, you know, supporting them indefinitely.
And so, you know, when we're talking about adding the dialer, for example, you know, sure, we might nail it on the first try, but, you know, even looking at the dialer we have today, like the… The… I could've… I could have merged… I could have merged the PR with the dialer as the original specification that you had opened, Antoine, but then that would have conflicted with the other dialer option that we already had on the server side. Which, you know, we could… we could have merged it, we could have released it, and now we have this… like, two ways of configuring dialers that are completely different in… depending on if you're configuring a client or a server. So, like, errors can… happen as we move the project forward, and it, you know, it's large in scope, so I guess the… the fear of adding something to the struct or to config is that we don't have a way of easily, like, removing it in the future if we find that it was not appropriate, or it doesn't work the way it was intended, or whatever. So, I think the sooner we identify a way for us to get out of that, the better.
**Antoine Toulme (Splunk Inc.)** 20:42 Yeah, that's where I stand too.
Go ahead.
**Jade Guiton (Datadog)** 20:46 I was gonna say, how bad would it be to just… make fields… Deprecated, and then new op.
And then in the next major version, properly remove them.
**Antoine Toulme (Splunk Inc.)** 21:01 I mean, it's… once we release 1.0, I think we can have a… discussion about how fast we want to go to 2.0.
**Jade Guiton (Datadog)** 21:13 I mean, that is, like, the point of a major version is removing struct fields, among other things, right?
**Antoine Toulme (Splunk Inc.)** 21:20 That's fair.
But if I find you a clever way to avoid that discussion in the first place, I'm probably saving you a few hours of your life where you talk about conflicts trucks.
So… You know, to do it.
**Jade Guiton (Datadog)** 21:37 I mean, if it's an equivalent… an equivalently simple solution, then yeah.
**Antoine Toulme (Splunk Inc.)** 21:41 It's… the only thing I'm sacrificing here is, like, discoverability of this thing becomes really difficult. Like, if you don't know that this thing is possible, good luck finding that. But the way we're going to expose this is through an extension that's going to come with a lot of opinions baked in.
And it's going to be like, hey, if you want WireGuard, you need to tell us where you want it, and, you know, list the components you want to apply it to.
And that might actually be a bit more.
Interesting, because it would be applying itself to different components in your pipeline, such as receivers and exporters, in which case.
We can gloss over how this actually is getting injected in Config HTTP, Config gRPC and whatnot.
So it's actually, from a point of experience.
I would need to look at the different ways of doing this, but if we were to do it the way we do it today, every component needs to pepper itself and say, oh, I have this extension on myself.
And we actually, by inverting control, you can say I have a wire guard endpoint is going to be for all of those components. And that is much easier to read, isn't it?
That's the… it's… it's difficult. I… I don't sit… I have a perfect solution, but I'm… I think this might be a discussion worth having.
**Jade Guiton (Datadog)** 23:03 Fair enough.
**Antoine Toulme (Splunk Inc.)** 23:08 Okay.
I will take this cue as let's go and build it and see what people think.
**Joshua MacDonald (Microsoft)** 23:15 Can I just reiterate one thing, which I'm thinking, just following the quote that Pablo placed in the chat, like.
I agree with that… the requirement there, and my… my excitement about extensions interfaces, which caused me to, like, write that document a while back.
is that… this contract between config extension, which is very opaque, just an identifier, like, that's not gonna break. Like, so putting the extension reference, or config, you know, component ID, into your… stable configuration.
Is… Unlikely to break anything.
itself.
as long as we agree there should be an extension of this nature, that then you can go have an unstable API for your extension, and keep iterating on that.
Is the way I understood.
Well, you need to stabilize the extension interface.
So…
**Pablo Baeyens** 24:22 think.
**Joshua MacDonald (Microsoft)** 24:22 I rest my point. The point is you have to commit to something somewhere. And we'd made this mistake with config HTTP, as I recall. We stabilized it a little early and then had a bug fix, because it had lacked the context argument.
Okay, I take it back. This is hard.
**Pablo Baeyens** 24:41 I think if you have a POC with an alternative way of doing it, that would be well received. But yeah, I guess we should move on to the next topic.
Six for over 15 minutes. So, Alex?
**Alex Boten** 24:55 Yeah, this hopefully will be a quick enough conversation. So there's an open issue 16075, which talks about how when we bumped a version of the OTEL config package, we increased the size of the Collector by about 4 megs for the binary itself.
This is due to some resource detection, the resource detectors that were included in the AtalConfig package. And, the question that came up in that issue is, you know, how can, as an end user, I reduce the size of the binary?
The proposal that I put forward for the OTel config package is to use GoBuild flags after discussing it with some folks on Monday.
And, I've made the same… proposal for the contrib repo for every one of the resource detectors, and yeah, I think that's going to be a good way to move forward with it. I'm also currently prototyping what it would look like to add configuration into OCB so that people can disable, you know, or opt-in or opt-out of resource detectors, as they need based on their environment. And, like, in Contrib, I was able to reduce the size of Diotel Collector by about 60 megs when I disabled all the resource detectors. So, yeah, I guess if you have any thoughts or opinions.
Feel free to raise them here, or on the issue.
**Rita Lopes (Gigapipe)** 26:41 Well, I guess I'm next. I don't know if someone wants to comment on what Alex said, or if I can go ahead.
**Alex Boten** 26:48 Yep, go ahead, Rita.
**Rita Lopes (Gigapipe)** 26:50 Okay, so I'm Rita, and I'm here today to discuss a donation of a component, which is the GigaPipe Exporter.
Basically, this component is to allow any telemetry data from OTLP to be inserted into Gigapipe, which is a backend of observability compatible, fully compatible with OTEL and Grafana.
And, we need this component because we use ClickHouse as our database, but we have our own specific schema, so without it, the data cannot be read by Gigabyte, on Grafana itself.
So, basically, I found a sponsor, which is Paulo, Paulo Giesch from Five9.
And the two of us, we are listed as code owners, but first question is, I am not sure if I can be a code owner, since this is my first contribution to the repo.
And if I can be… if I need a third person, because I read on the rules that ideally we would be three.
And, what should I do as a next step on the repo, if anything? Because I assume that I need to condensate it into… A different type of fan.
files I made to produce the documentation. So, I'll just ask some guidance, assuming that the labels on the issue are correct, because it says already accepted components, which I believe I will add a label as sponsor.
**Alex Boten** 28:34 Sorry, maybe it was just on my end, but I… I couldn't fully hear what you were, saying towards the end there, but I think… I think the next step is to, open the… PRs, which I don't know if you already have opened. And then, I think if… if you can… open a couple of PRs, then, you know, go to the community repo and ask to become a member of the OTEL org, then you can get a couple of sponsors there, and then, you can become a code owner of the component as well.
**Rita Lopes (Gigapipe)** 29:23 I should be able to get this. Is this recorded?
**Alex Boten** 29:32 Yep.
**Rita Lopes (Gigapipe)** 29:35 Okay, okay.
Thank you.
**Alex Boten** 29:41 Yeah, no problem.
Emilia?
**Emilia Ferreyra (New Relic, Inc.)** 29:52 Hello? Can you all hear me? Okay.
**Alex Boten** 29:56 Yep.
**Emilia Ferreyra (New Relic, Inc.)** 29:57 Alright, sounds good.
I see that there's an action item from Thomas and Mike that… I don't know if that's more urgent before I… like, pretty much the short of what I would like to say is just, like, I have Created a feature request for another way to do the processor config validation, and I wanted to go into why I felt like we needed yet another way to have a tool that does all the, like, config validations and how I came up with the solution, but.
If there is… if we are short on time, I like.
Y'all can do the action item first.
**Pablo Baeyens** 30:49 I think you can go ahead, we can… Sure.
**Emilia Ferreyra (New Relic, Inc.)** 30:52 you Alright, so… Hi again, I am Amelia from New Relic.
I posted an issue last week about this topic that I wanted to talk to y'all about today, and share a proof of concept that I've made.
In short, I've made a CLI that takes in a config and a payload. Runs a dry run validation of the config, and then runs a dynamic run, showing the actual diff on the payload as a result of the given config.
I came to this solution for various reasons while I was drafting up an OTEL configuration to mimic some of the functionality of our New Relic language agents.
I actually wrote a blog post about it a few months back, if y'all are interested in reading more about it, but what's relevant here is that to do so, I had to trawl the OTEL docs for processor components in Autel, pick some candidate processors, and play with their configs until I got the results I wanted.
Existing tools like OTELBIN only offer static validation. It doesn't validate auto, and it doesn't show you what the config actually does to the data.
Auto Playground, on the other hand, was invaluable in my research due to its ability to take the transform and filter processor config in a payload. And then output how that config changed the payload.
However, while I was looking at the transform and filter processors as potential candidates for the config I was writing, I was also considering the attributes processor, which contains no auto, and therefore was not included in the auto playground. Instead, I cloned down the auto playground code and added functionality for the attributes processor so that I could play with the config and payload for that component in the same way I had the others.
While it makes sense that the Auto Playground was scoped to just, like, auto-related processor components, I felt like what Auto Playground did had a usefulness that could apply to most, if not all, OTEL processors.
On top of that, while Auto Playground significantly lowers the barrier of entry to write auto-based configs, I feel that we can make OTEL config writing even more accessible by integrating LLMs.
With my proof of concept, which I call Model Duck.
Users can prompt Claude or the LLM of your choice to draft an OTEL processor config and use the CLI to validate it and confirm that it does what was intended, all without having to read a browser, stand up a pipeline, or require network access somewhere.
Also, with the CLI format, ModelDoc can be placed in CI workflows as a configuration verification step.
The POC has four main sub commands.
validate, run, test, and examples, which I can tell you about, but I can also… Demo, if I can share the screen?
**Antoine Toulme (Splunk Inc.)** 34:18 Go for it.
**Emilia Ferreyra (New Relic, Inc.)** 34:18 Okay.
Alright, let me do that.
here.
Start here.
So… Validate, over here, takes in a… File path for the config, and then the specific component that you want to test out, and if it's a valid config, it will tell you as much.
If it's an invalid config, then it will tell you why it was invalid. So here are a few examples, like missing semicolon, not semicolon, close parentheses, an unsupported function. Over here, it's just, like, an unsupported input.
or like just an incorrect struct, incorrectly structured config run.
Does.
Similar what the Auto Playground does, and it takes in a config file.
a payload file and the component that you want to test out, and if the config did nothing to your payload, it will say as much. And if it did change, then it will show you the diff.
Test does pretty much what Run does, but it's a bit more CI-friendly.
And, It just takes the additional input of an expected file to compare the resulting payload against, and if it's the same, then it's a match. If it's not the same, then it'll show you the diff.
And to make this a little bit more entry-level to people, there is an examples. Command where… If you just say model duck examples, then you have, a list of all the supported, component and signal pairs, which you can filter down by either component or signal.
But if you provide a component and a signal, then it will give you the promised example. So, over here, we provided the transform and the signal metrics.
And then you can see that it gave you a related config.
A payload for you to tinker with, and then it will run the validate and run for you.
So, over here is the rest of the payload. This is an example payload for a, like.
Theoretical cashier app, but… Over here, the validate is run, the config is validate, invalid, and then it does the dynamic run, which then shows you the diff that the config did. And then it's just, like, a little invitation to go into the code and tinker with the payload, and… the config. So… Yeah, that's what I got. Any questions?
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 37:30 Hi, Amelia, thanks for sharing. That was pretty… that was really cool. Pretty, pretty interesting stuff. A couple questions. The first one was, I was looking through the issue, and I just want to clarify.
Because I got confused the first time I read it. This is not a request to make a new processor that can do this, right? This is simply a CLI tool that you've written. This is not a collector component, right?
**Emilia Ferreyra (New Relic, Inc.)** 37:50 No, it's not a Collector Component.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 37:51 Okay.
**Emilia Ferreyra (New Relic, Inc.)** 37:51 It's like a proof of concept that I created for that would, that it's trying to address an issue that I did and like came upon when I was trying to figure out Audible for the first time.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 38:04 Sweet. And then, the next question is.
with your issue, is… is… is this, like, an informative situation, or are you hoping to, like, donate This tool to collect or contrib, like, as a new command or something.
**Emilia Ferreyra (New Relic, Inc.)** 38:20 It can be. I wanted to, like, present this as a proof of concept and, know, like, invite a conversation about how this, like, may be a thing that… Y'all would be interested in accepting, or, like… Showing… That this problem exists and how… start a discussion about how you would rather it be fixed.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 38:46 Okay, yeah. I mean, helping people learn how to configure a collector is a never-ending chore, so definitely looking for opportunities there. During your investigation, by any chance did you… See the, like… Open Telemetry Collector's validate command.
**Emilia Ferreyra (New Relic, Inc.)** 39:05 are.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 39:06 binary.
**Emilia Ferreyra (New Relic, Inc.)** 39:08 I did, I did.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 39:09 Okay. I'm curious if, like, there was… obviously, you built stuff that's way past the validate command.
**Emilia Ferreyra (New Relic, Inc.)** 39:17 Yeah, I think that the validate command in my CLI pretty much just uses the validate command.
From the Collector.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 39:25 I… I would need to spend some more time thinking about it, if we would want to support another binary and, like, manage another release and, like, separate it, or if this would… if these are additional features that could be built into a collector. One benefit of such a feature existing within a collector is that the collector knows the components that it has compiled.
And therefore, it can be… Gregory A. really specific with what it says will and will not work, whereas, like, a more generic tool is… is still going to run into a problem of, like.
if you go… if you do a bunch of config and work through trying to figure out how you're going to use the transform processor, and then you go throw it into a collector that doesn't include the transform processor, like ADOT.
Gregory A. Then you're gonna get like an A, an error experience that you didn't before. But if you could have, if you can use the Collector that you're going to deploy to do all of the testing and validation, and you get more confirmation that Gregory A. your config really will work because it has the components. It has the knowledge about the components that would work.
Gregory A. So that that's my 1st thought is like this would be really cool as a feature in the Collector itself, like in the in the binary flags instead of Gregory A. instead of a separate cli.
**Emilia Ferreyra (New Relic, Inc.)** 40:45 Okay, yeah, that sounds great.
I can do more research into that.
Oh.
**Evan Bradley** 40:52 another… Oh, sorry.
**Emilia Ferreyra (New Relic, Inc.)** 40:54 go ahead.
**Evan Bradley** 40:55 This is more for Tyler. Tyler, I know we, print the transform context as part of debug logs. Do you think we would be able to, like, use those as, like, an event sourcing thing and use those to construct a diff if you send data through a collector?
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 41:10 I think you could. They are an exact diff. Like, it's all structured, and it's the exact before and after.
So you could do… you could do anything with those, really.
I mean, you'd have to parse them, but…
**Evan Bradley** 41:25 Well, they're Jason, I think, so it should be fairly easy.
But, Amelia, if you're not familiar, if you turn the collectors, if you turn its SDK, the logging component, to print out, I think it's… is it verbose logs, or is it detailed?
But if you increase the verbosity of the logs, the transform processor will print out, befores and afters of the transform context.
Which is basically the payload, so it'll… it'll print out the state… or the data that you have, you run the statement, and then it prints out the afterward. And it's used for kind of scenarios like this. I don't know if that's helpful or not, but just kind of an FYI.
**Emilia Ferreyra (New Relic, Inc.)** 42:07 Yeah, for sure. I'll definitely be taking y'all's advice into account after this.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 42:19 So if you have… if you came across any cool examples while you were building the CLI, Especially if those examples aren't already on like the transform processor, readme or in the OpenTelemetry doc site.
People are always asking us for more examples. So.
having having more like real life examples that you've that you found through your research would be great.
**Emilia Ferreyra (New Relic, Inc.)** 42:43 Examples of just, like, config and payload, or, like… Specifically…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 42:47 So specifically OTTL in this case, since it seems like that was one of the things that you were focusing on.
**Emilia Ferreyra (New Relic, Inc.)** 42:53 Yeah, definitely, it's just, like, you read the README in the docs, and there's just, like, then you have questions where you're, like, I wonder what would happen if it did this. Do you mean that? Where it's just, like, more examples of, like.
Here's another corner case of how to use auto that you might have been wondering about.
Okay.
Are there any other comments, questions?
Cool. Well, thank you.
good to speak here for the 1st time.
Yeah, I guess the next person can go now.
**Thomas Baldwin** 43:43 Hi, everyone. My name's Thomas. I am an engineer, with Bloomberg, and I'm with my coworker, Mike, and… I apologize if I used the action needed, label, if that was the incorrect one, I just figured, that made sense.
as we just wanted some guidance on a PR we have. And I'm happy to explain the backstory of this PR as well, if anyone needs, but… We have this PR, we've already received approval from the code owner, and I believe we've addressed all the feedback to the best our ability of what we think is there. I guess we're just wondering, what would the next steps be? Should we… ping individual maintainers? Should I post in the Slack channel?
I figured also coming here and just, you know, talking through the PR and what it does may also be helpful.
To give some context, this is a PR that adds an interface to the basic auth extension to allow users of the Basic Auth extension to add a referencing, secret provider to it, and The idea behind it is, I recognize there's already secrets providers, but the idea behind it is that using, this.
the exporter, whatever's using the basic auth extension, can get another secret, and it doesn't need to rotate it. And this just establishes the interface. We have work that we would like to do as a follow-up that would actually go ahead and implement this, but we figured It may be a good idea to break it into pieces.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 45:22 Pinging, pinging code owners in the OpenTelemetry… the OTEL Collector Dev channel is okay, probably.
If you throw a link into the…
**Pablo Baeyens** 45:33 I think we…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 45:33 I'll add the… Waiting.
**Pablo Baeyens** 45:36 We already have the approval from the…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 45:38 Oh, then I'll…
**Pablo Baeyens** 45:39 You're looking at a man.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 45:40 container label and our maintainer will go review it hopefully.
**Thomas Baldwin** 45:46 Sounds good.
And then, in general, like, going forward.
in the OTEL Collector Dev Slack channel, is that a recommended approach to post there? I saw people post there, but also don't want to be too annoying about it.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 45:59 The struggle with a large project like Contrib.
**Thomas Baldwin** 46:04 I recognize it.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 46:04 bandwidth is that, like, sometimes there are things that are lower priorities for approvers and maintainers that take longer to get through, simply because, like, they're not advancing the SIG's primary goals, such as, like, 1.0 stuff. But, I'll add a… I'll add a waiting for maintainers label. Those normally get checked as part of the release process.
**Thomas Baldwin** 46:30 Okay, thank you so much.
That's it for me.
**Sam DeHaan** 46:41 Alright, looks like I've got the last thing on the written agenda anyway. So… In Grafana and Ally, we have a support bundle that's super useful for seeing kind of a point-in-time representation of an issue.
Obviously, there's various other similar implementations, Datadog's Flare, a few other things we ran into while researching, but we wanted to have something kind of native upstream. We were looking to do just.
built-in extension that we had over in Grafana Repository, but figured we'd start a conversation upstream first, and people seem more interested in maybe just adding this to the only real existing debugging extension at the moment, which is ZPages. So if you have any opinions on either whether or not it belongs there, or the implementation plans, or anything like that, would love to see some more feedback. But otherwise, yeah, looking to… looking to contribute something that's valuable to.
to everybody for that kind of point in time, what's going on in a collector issue debugging situation.
Not really any specific conversation that needs to be on this meeting, but more just getting more eyes on it.
**Alex Boten** 48:02 I'll… I'll just add a comment in here. I think, you and I, Sam, talked about this some… a few weeks ago, and I'm… I fully support it. I will go review the issue here, and add some comments. But I think it'd be great to… make incremental improvements to the ZEP pages extension, because it's… It's been, maybe lacking some attention or love, so… Alright, I guess if there's no other comments, Does anyone have any other topics they want to bring?
Or if not, we can get 12 minutes back.
All right.
Thanks, everyone.
**Pablo Baeyens** 49:21 Thank you.
