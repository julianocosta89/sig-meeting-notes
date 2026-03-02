SIG: Specification SIG
Date: 2025-08-12
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**Armin (Dynatrace)** 03:48 Alright, looks like we only have two items on the agenda today, and I don't see the first.
owner here in the meeting, so maybe, Robert, you could…
Go ahead in a minute or two.
**Owen Williams (he/she)** 04:11 I also… Artur and I also know what the first item is about.
**Armin (Dynatrace)** 04:16 Oh, that's great. Alright.
Either that, go ahead, kick it off.
**Owen Williams (he/she)** 04:21 Yeah, so what we're running into is a conflict in stability guarantees between different parts of, OTEL.
And so… … Yeah, the first bullet talks about how the… …
we want to change a piece of configuration in the hotel configuration, repo, and that's in a block that's experimental. The Prometheus exporter is experimental, so that should be able to be changed.
However, then downstream, you get to OTEL Collector, and you're not supposed to, just suddenly change, things like that, so breaking changes aren't allowed.
So, the question is, how do we… how do we resolve those two things?
Basically, we want to, create a new, configuration option and deprecate another configuration option.
**Trask Stalnaker** 05:34 For those of us who aren't familiar, how are you using… is declarative config in the collector, specifically around the…
… the… the FDK… configuration, as opposed to, like, pipelines, or it's the whole thing?
**Arthur Silva Sens** 06:01 I think Robert will probably have a better answer, but I can try. … the collector.
uses, they'll tell Go SDK, the reader, the config breeder.
To… expose….
**Trask Stalnaker** 06:17 several parts.
**Arthur Silva Sens** 06:19 Including the Prometheus exporter.
So there is the whole pipeline thing, which is exporters, receivers, processors.
This is separately… this is separate from the configuration part that is implemented by the Go SDK.
**Trask Stalnaker** 06:40 Thanks.
**Arthur Silva Sens** 06:47 Robert has a raised hand.
**Robert Pająk** 06:50 Yeah, I just want to double check. So, is the concern mainly about the stability of the primitives exporter, or are there other, stability, like, kind of blockers and concerns?
**Arthur Silva Sens** 07:02 Like, the… The collector configuration is declared stable.
**Owen Williams (he/she)** 07:07 So….
**Arthur Silva Sens** 07:08 I know that the Prometus exporter and the Go SDK is not.
But how it is used in the collector?
It's….
**Owen Williams (he/she)** 07:17 So the main… yeah, the main thing is we… we're trying to deprecate one of the options, which is being superseded by a different one. So, specifically the without units, …
option. So, we'd like to get rid of that because it'll be obsolete, and the question is, what is the… you know, if you remove that, then suddenly people are passing an option that's no longer there. Do we just have to keep the old option around forever, or is there a way to phase it out?
Over a number of releases, like, is there a process for that?
**Robert Pająk** 07:50 And you're asking for… not for the collector, but for the declarative config, right?
Specifically.
**Owen Williams (he/she)** 07:56 Specifically, yeah, the declarative config to make… we want to make the change there so that all the SDKs are unified, but then the collector is downstream of that. And so then the collector would be out of sync with the declarative config.
**Robert Pająk** 08:14 I can say how I understand it, as a… someone who is, like.
in a similar… has a similar view, because I'm not also not a configuration… not part of configuration seek, but as far as I understand, like, as a specification sponsor, the declarative config, for sh… wouldn't go stable.
before the premier TOS exporter configuration is not stabilized.
And I know that you are also working very hard on making it stable, so also you're making changes which you are basically going to this direction.
Regarding future changes.
I do not, of declarative config, I knew how we will just phase, you know, phase out if we want to evolve in future. I think we just need to, you know.
probably it will be similar to the normal, you know, APIs. Probably will need to obsolete things and, you know, keep back course compatibility once it's V1, V1.
create a new configuration for, you know, something which is not backward compatible, but probably it's something that should be avoided as much as possible. I think that maybe Tyler can also add something to it.
Maybe someone else, maybe Josh, I don't know. That's all from my side.
**Josh Suereth** 09:31 I'll just talk about a way to think about backwards compatibility and stability, is, we consider a lot of the specification work more kind of like HTTP header specification work. That's one of the areas we took with semantic conventions. Basically, once you add it.
It's out of the gate, people are using it. And the… if you want to actually get rid of something, the thing that matters is not what… necessarily what you've told users, but how much usage it actually has.
So, like, it's more important to get people to use the new thing to the point where nobody's actually using the old thing, and then you could get rid of it. Likely, though, we won't. We'll just leave it there, leave it obsoleted, people won't engage with it, all the documentation stuff will advertise the new thing, and you'll leverage the new thing.
But, like, for stability reasons and for getting people to actually depend on us and continue to rely and depend on OpenTelemetry, you know, a lot of what we do has to stay stable and has to remain for a while.
so we have a very long kind of time horizon there. So think more like HTTB headers that you would depend on and rely on, versus, like, this is a, you know, Go library API, right?
**Arthur Silva Sens** 10:46 Yeah, I think… I think we can work with that. I can leave the existing configuration to say, hey, this is duplicated, you should probably use the new one.
I think that's totally fine for us.
**Owen Williams (he/she)** 10:58 Yeah, and luckily.
**Arthur Silva Sens** 10:59 rolling.
**Owen Williams (he/she)** 10:59 Luckily, the logic around… you know, the worst case scenario is somebody specifies both, and then, like, which one takes precedence, and I think they can fairly safely override each other, so that if you have a conflict, it's just whichever one is second wins, and, like…
I don't know…
I'm not sure if we even bother to document that, but I think it's sort of an intuitive, behavior in that case. But it's not a… it's not a super… you're not gonna end up with a totally broken scenario if you're doing both.
**Arthur Silva Sens** 11:32 Sounds good to me.
**Owen Williams (he/she)** 11:35 So is there… is there a way in the declarative config to say, deprecated, or is that just… or do you just put that in a comment nearby?
**Tyler Yahn** 11:50 Yeah, right now, it's just a comment.
**Arthur Silva Sens** 11:54 That's a bit.
**Josh Suereth** 12:00 Is there… is there a plan to formalize that, Tyler?
**Tyler Yahn** 12:06 … No, there isn't a plan to answer directly. ….
**Josh Suereth** 12:11 Well, okay, should they….
**Tyler Yahn** 12:12 The whole idea….
**Josh Suereth** 12:13 Yeah.
**Tyler Yahn** 12:14 The whole idea was that this is in a development.
Section of the configuration, which is already intended to be, like.
Replaced with a stable one, eventually?
… So…
Yeah, I think it's more of what that looks like in the long term, is kind of the question.
I think to, …
Arthur and Owen's point, though, that, like, if this is already getting used by, like, the collector in a stable way, but it's not itself stable.
like, … Yeah, I don't know, I…
I don't know what to say too much about that. I think it's just something that has to be thought about a little bit better here.
**Arthur Silva Sens** 12:55 We can bring this to the collector SIG, how to deal about experimental parts.
**Tyler Yahn** 13:02 Yeah, I would be interested to know what their input on this is, for sure. That would be, helpful.
**Reiley Yang** 13:12 Owen, you mentioned, like, there's a potential way to follow the ordering, so I'm curious, like, is there any prior art that people rely on the ordering in the configuration? I personally find this a bit concerning.
**Arthur Silva Sens** 13:30 Yeah, I… Owen, to be honest, I think he… Owen got a little bit confused with the Go SDK, that in the Go code, you can….
**Owen Williams (he/she)** 13:37 out.
**Arthur Silva Sens** 13:38 choose the order, but in the config, the YAML file, the order is not that direct.
We'll probably need to just say, like, the new one overrides the old one, and not care about the other.
**Reiley Yang** 13:51 Yeah, please. I feel like people who use both the new one and the older one, the new one should have the power, and we shouldn't rely on any ordering.
Thank you.
**Arthur Silva Sens** 14:01 Yeah.
I think we can move to the next topic.
**Owen Williams (he/she)** 14:24 Yep, yep, I think that's all we need.
Thank you.
**Armin (Dynatrace)** 14:28 Thank you, alright, then Robert, go ahead, please.
**Robert Pająk** 14:32 Show my screen.
So, I gave 3 minutes, in case there'll be any questions. So, there are 2 PRs which are probably good to merge.
One is the proto, this kind, which was discussed also recently. It's here, it's up, I think, almost a month, …
This one.
And during the lock seat, we also discussed that probably it will be sorry.
My Zoom, yeah, can you see the screen? Because Zoom is… Almost crushing for me.
**Armin (Dynatrace)** 15:05 Yep, all fun.
**Robert Pająk** 15:07 That's nice. And also, I created a separate one, which is here, which is in specification, just to formalize that, extend the attributes is no longer breaking change. Basically, just remove this section that we will… that…
extending the set of attributes is a breaking transformers. It's about removing this section and stating,
that we see in the changelog, that we see that extending the standard attributes value types is no longer a breaking change, which was previously approved via the OTAP.
But just to make it explicit also in the specification.
And that's basically it. Are there any questions?
Go on, Josh.
**Josh Suereth** 15:54 So, yeah, the apologies on the proto, I think that probably can merge. I think that just got… I was, paying more attention to the profiling PRs. But the… the… the changelog, I feel like you should call a lot of attention to that.
Like, put… put… give that a breaking tag of the notion of what's breaking is changing.
or something, so, like, like, I just…
If it's just there as a line item, I think people are gonna….
**Robert Pająk** 16:23 I see.
**Josh Suereth** 16:24 Yeah, so let's….
**Robert Pająk** 16:26 You suggest giving a break-in tag, just in case in the changelog, and I also call it out in the Slack channel, Autel Maintainers.
**Josh Suereth** 16:35 I'm thinking about people who aren't as engaged in the ecosystem. What's their channel for understanding spec changes? It's this change list. It doesn't have to be a breaking notion, it just has to be a giant call-out of, hey, by the way.
We considered this a braking change at one point, it no longer is, and so if you were using that interim time where we didn't consider this, or where we did consider a braking change.
You know, the….
**Robert Pająk** 17:01 Okay.
**Josh Suereth** 17:02 Yeah, like, if you would have….
**Robert Pająk** 17:03 If you have any ideas, if you have any ideas, then please propose changes. I will also try to figure out some proposals.
**Josh Suereth** 17:10 I mean, I would… I would have just put, like, a big light bulb or a big, like, stop sign or something, emoji. I don't know exactly what I would do there, but just something to make it more than a single bullet point, that's all, yeah.
**Robert Pająk** 17:22 Thanks.
**Trask Stalnaker** 17:24 And so, Josh, this is in addition to when we
Given that we're not actually changing anything now, we're just relaxing the conditions so that we can change it later.
**Josh Suereth** 17:34 And we would call it out a second time.
What?
Well, we don't consider it a braking chain, so later it won't have the braking tag.
Right? This is saying we changed what the definition of braking is, so I feel like that has to be well communicated, because the next changelog won't say it's braking.
**Trask Stalnaker** 17:54 Right.
Okay.
**Carlos Alberto Cortez** 17:59 By the way, similarly, I wonder, you know, you are in the specification PR, you are removing, some text section. I wonder whether it could be an overkill to put a note like.
This is how it was. I'm saying this because I think that probably some people may say, hey, I used to remember that there was a section here and it disappeared.
So, I don't know, maybe it's an overkill. We could talk about that offline, just a small suggestion.
In all cases, it could probably be done as a follow-up, if truly needed.
**Robert Pająk** 18:47 Yes, thank you.
I think we can go to…
Other agenda topics, if there are any, which are not
Which are not explicitly in the… In the agenda?
**Armin (Dynatrace)** 19:08 Any other topics?
**Robert Pająk** 19:14 I think the only thing maybe worth going out is that,
the CFP for KubeCon Europe is opened.
So, it will be good to have some proposals from our community.
**Antoine Toulme** 19:34 Did we announce the, holiday for KubeCon NA yet?
Has that been done?
So it's the….
**Trask Stalnaker** 19:54 What do you mean, Antoine?
**Antoine Toulme** 19:57 I'm asking, so, we don't have the schedule yet for holiday at KubeCon North America.
Right? I haven't seen that being posted yet.
**Trask Stalnaker** 20:08 Holiday, like….
**Armin (Dynatrace)** 20:09 Co-located event.
**Antoine Toulme** 20:11 Yes.
I have not seen that being…
Yeah, I just… I went to the page, still not there.
**Tyler Yahn** 20:20 So I… Anton, I don't think that the talks have been accepted for that day yet. So, I don't think they can post the schedule for that day.
**Antoine Toulme** 20:28 Yep.
Do you know when that will be?
**Tyler Yahn** 20:32 No, I don't.
**Antoine Toulme** 20:34 You're good.
**Armin (Dynatrace)** 20:35 It says, schedule announcement tomorrow.
Just in time.
I'll post the link just for reference.
**Antoine Toulme** 20:46 Thank you.
**Bob Strecansky** 20:48 Do we know if we get discounted or free tickets to this event as maintainers of telemetry?
**Tyler Yahn** 20:59 I think you can apply for, like, assistance.
**Bob Strecansky** 21:03 Oh, okay.
**Tyler Yahn** 21:04 No, I don't know. No, it's not based on your role here.
**Bob Strecansky** 21:08 Alright, cool. Also, I am from Atlanta, so if anybody has questions about anything, please feel free to reach out, I'm happy to give guidance.
**Antoine Toulme** 21:17 There is something for you, there is a maintainer summit, which is the day before KipCon.
Which I think you can attend for free.
**Bob Strecansky** 21:26 Dip.
**Antoine Toulme** 21:27 … oh, someone helped me here, I got the wrong lead.
Winter Summit, Kube Kong… 25.
Hell yeah. Here you go.
I'll post it in the chat.
**Bob Strecansky** 21:54 Thanks.
**Antoine Toulme** 21:57 So, I believe you can attend for free.
And it's… it's different from, …
We're not going to talk about open telemetry, we talk about meta things, like how do you deal with a big open source projects, how do you work with your community, how do you have governance.
And I believe…
I believe that we can have a session during the day where we can have just the maintainers of OpenTelemetry, kind of come together, have discussions about maintenance.
I don't know that we're doing anything for that yet, I can't remember off the top of my head. Last year.
Well, in February, in London, Austin… Austin took care of organizing that.
It was worthwhile.
So….
**Bob Strecansky** 22:42 That's on a… that's on a Sunday? Er, I'm sorry, I'm looking at the wrong month.
**Antoine Toulme** 22:46 What's on the Monday vacation?
**Bob Strecansky** 22:47 blender.
**Antoine Toulme** 22:49 Yeah, Monday, maintenance summit, Tuesday, holiday, and then keep going.
**Bob Strecansky** 22:55 Yeah, it always silly me when they put a conference on a holiday, but, well….
**Antoine Toulme** 23:06 Do what you love.
**Bob Strecansky** 23:07 That's right.
**Armin (Dynatrace)** 23:16 Right, then it looks like that's it. Do we have any other topics?
If not, let's call it for today. Thanks.
**GZ Gregor Zeitlinger** 23:25 Sorry, I joined late because I was in a different meeting, and actually, I put my item on here.
And I'm just trying to understand this thing about declarative configuration and not being able to remove things.
So I'm just reading, the notes.
If I get it right, Josh, you said, that you can't remove stuff, is it? Right?
**Josh Suereth** 23:56 So, yeah, what I phrased was, the way we think about removing things is based on usage. So, if there's a lot of people using it, don't remove it, and we treat things more like HTTP headers, where even if it's removed, we still will keep it documented.
and not use that name again for any other purpose, because of past dependencies. Like, we…
we can document that the thing is deprecated and gone and not used anymore, we can have the new thing, but we treat this more like HTTP headers versus, like, a Go API with how things work. Does that make sense? I'm making it briefer, so apologies, I can expand a little bit.
**GZ Gregor Zeitlinger** 24:38 Yeah, yeah, yeah.
I'm late, that's… so it's okay, I'm… I still have to figure out how this fits for our use case.
**Robert Pająk** 24:50 I suggest watching the recording later.
**GZ Gregor Zeitlinger** 24:53 Oh yeah, that's a good idea, yeah. I didn't think about that, thanks.
**Robert Pająk** 24:56 Welcome.
**Josh Suereth** 24:59 And if you want to talk through your use case or whatever, happy to follow up, like, here or in chat.
**GZ Gregor Zeitlinger** 25:06 Yeah, okay, let's do that. Thanks.
**Armin (Dynatrace)** 25:12 Alright, then. Okay, thanks, everyone.
And let's call it here. See you next week. Bye-bye.
**Carlos Alberto Cortez** 25:18 view.
