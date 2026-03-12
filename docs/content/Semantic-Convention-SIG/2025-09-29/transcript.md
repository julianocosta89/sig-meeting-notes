SIG: Semantic Convention SIG
Date: 2025-09-29
Duration: 53 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 02:16 Hey, folks.
Give a… Minute or two more for… Hopefully, people to show up.
**Liudmila Molkova** 02:40 Hello. Hi, everybody.
**Trask Stalnaker** 02:45 Hey… I can drive today.
**Liudmila Molkova** 02:54 Oh, thank you.
**Trask Stalnaker** 03:27 Let's go to the triage board to begin with.
Alright, we've got something ready to be merged.
Oh, status metrics, yes, yes.
Any… open… Okay, so… I… Yes, I will leave that tab open in case Josh makes it.
Let's see… block… I… Is there a… ordering… Do we just pick random ones to look at?
**Liudmila Molkova** 04:33 I think the ordering is the… the… Last block that appears at the bottom.
the time?
**Trask Stalnaker** 04:42 Okay.
So, we've got…
**Liudmila Molkova** 04:55 There, there are quite a few, things that… Don't follow our practices.
And I've left a review, and I don't think there was an update on this.
**Trask Stalnaker** 05:10 Okay.
And this is… oh, this is Gen AI, okay.
**James Thompson** 05:16 There has… has been some cleanup on it, alright? So it has been improved to remove a lot of the… some of the feedback being taken on, but the metrics and that haven't been updated.
Right, so the attribute names have been updated, the redundant file's been deleted, so there has been some progress on it.
**Liudmila Molkova** 05:34 Okay.
**Trask Stalnaker** 05:36 increase… Let's see… General signal docs. What do we have here?
**James Thompson** 05:51 So, the changes have been done there. So, when you go to the signal page, for example, logs and that, you still have all the attributes there, so that hasn't changed, but when you go to the events page, you now see the relevant attributes for the general events.
Right, so you…
**Liudmila Molkova** 06:11 Ha!
Do we have to duplicate?
all the common attributes in each signal? Why?
**James Thompson** 06:19 Because some of them don't apply in all cases. So, for example, they don't apply to metrics.
Right.
**Liudmila Molkova** 06:33 I think we… We have the idea that every attribute is opt-in on any signal.
a general idea. And if somebody wants to populate hard cardinality attribute on metric, it might not be high cardinality for them.
**Trask Stalnaker** 06:52 Like, yeah, I could definitely see some people, like, thread name or end user.
ID, you know, putting onto their metrics.
Does this tie into… I thought that, Maybe as part of the SEMCONV2 work, but the attribute groups… Having attribute groups, which would be a new concept for, like, thread… Code, and that would fall under there.
**James Thompson** 07:30 That's one way to express them.
**Trask Stalnaker** 07:34 I think probably, we should hold off on… This until that gets sorted.
I don't think there's any, like, urgency in… I think moving things once will probably be easier, just because it's a lot to… Review, and then we end up with the duplication Potentially.
Let's see, I can leave a comment… Let's see, next, introduce deployment target.
**James Thompson** 08:56 That's for DCICD, SIG.
Because deployment's covered by them, and it's based off what they're already modelling, right? It's CD events, anyway.
**Trask Stalnaker** 09:07 Gotcha.
So, this… okay, it's there… Lynn Milla, should we move it to awaiting Code Owner's approval?
**Liudmila Molkova** 09:22 As part of it.
**Trask Stalnaker** 09:23 FCICD…
**Liudmila Molkova** 09:26 I'm curious, what is the status of the CICD group? Is the Phase 2 starting?
**Christophe Kamphaus** 09:32 We are still reviewing the Phase 2 proposal.
**Liudmila Molkova** 09:39 So it would probably take a while.
**Christophe Kamphaus** 09:42 Probably, yes.
**Liudmila Molkova** 09:47 So I think maybe we should either draft it, or maybe close it until then, so we don't… Spend time over and over again traging the same issue.
**Trask Stalnaker** 10:03 Yeah… Alright, let's do… I think we had a pretty light agenda, so we could potentially… Let's do one more here.
Enum briefs for system.
**James Thompson** 10:56 So they've actually been gone and made more informative.
**Liudmila Molkova** 11:02 I'm kind of curious, like, where is it coming from? So you've started with, just using a different casing. So your motivation was to change the casing.
Now that we've said that casing is not good enough, you're adding more verbose things. What is the motivation? What drives this PR?
**James Thompson** 11:25 That's so…
**Liudmila Molkova** 11:26 Why do you care?
**James Thompson** 11:28 Alright, so from a readability perspective, right, I originally went with casing because I thought that'd be easy to get through, right, because it wasn't actually adding additional changing wording, so it would be easy to pass through. The intention was always wanting more informative descriptions, right?
**Liudmila Molkova** 11:50 Oh, wait, why?
It is, is this… Description of the attribute, plus the existing description.
Like, how… how free?
**Trask Stalnaker** 12:04 is…
**Liudmila Molkova** 12:05 worse than free virtual memory. It's… it's still obvious.
**Daniel Dyla (Dynatrace)** 12:12 I don't think it's always obvious to everyone. What's the point of having a description field if it's the exact same as the ID?
**James Thompson** 12:21 And, I mean… So, there's a lot of them actually being made.
Taking paragraph… a sentence or two from the definitions, right?
Right?
But if it just says used, Alright.
**Liudmila Molkova** 12:43 So, my point is that when you write, disk conventions, you don't just duplicate what's in the ID, yes, there is no point, exactly this, but then, somebody who writes the conventions provide, enough information. It's not a mechanical thing that you, just… Write it down, duplicating things, or you, use AI to generate it. It's more like somebody who actually wants to provide useful information adds this information.
Going through all the briefs in all enums, and mechanically adding descriptions.
Does not seem like a useful thing to do as a project across semantic conventions.
**James Thompson** 13:36 So, for me, it was about improving the readability of the document when you're looking at it, because when I'm looking at it and noticing inconsistency formatting, right.
Those small things It could quickly become irritating.
Alright.
**Daniel Dyla (Dynatrace)** 13:54 So, I'm.
**Trask Stalnaker** 13:55 I agree.
Yeah, go ahead, Daniel.
**Daniel Dyla (Dynatrace)** 13:58 Go ahead, Trask, you were talking first.
**Trask Stalnaker** 14:01 I mean, I don't mind having Briefs… I mean, I think this is a… potentially a good example. I don't even think this is correct. I think this is free physical memory, probably? I don't know, we've got, fairly odd parents, on the call here to tell us for sure.
**Fairly OddParents (ca-wat-brt3)** 14:28 I'm pretty sure these values are based on actual things, actual, like, values from ProcMemInfo, so I think… it's whatever the man page says for those… for those values. I think they may be translated to lowercase without the mem, but, like, the words are from… the MemInfoMan page.
**Trask Stalnaker** 14:49 I think this is physical memory.
**Fairly OddParents (ca-wat-brt3)** 14:53 From Procm Info, it would be… Might be virtual. I have to look again. Might be virtual.
**Trask Stalnaker** 15:06 Certainly I could use a note, at least, on this.
**Fairly OddParents (ca-wat-brt3)** 15:14 Yeah, if… these briefs, we could add… like… Information of these briefs… right now, they aren't adding much information.
Free… saying free virtual memory isn't much more information than nothing.
We could… Put in the briefs how they map to things from meminfo and Linux are the same thing in Windows, but then, like, is that… is Brief the right place for that, or is Note a better place for that, because we're talking about platform-specific, differences.
I don't know.
**Daniel Dyla (Dynatrace)** 15:53 I would think Note would be a better place for that type of, like, more detailed, mapping, but brief is where, like, just the question that we just came up with, is it virtual or physical? I think that that would be a decent place to have, like, where you don't have to… you're just looking for quickly, what is this?
**Fairly OddParents (ca-wat-brt3)** 16:14 But in that case, shouldn't that be in, like, the brief of the metric, of the attribute, like, or, like, the description of the attribute itself, rather than in the description of every single value in the enum?
**James Thompson** 16:24 That's like…
**Trask Stalnaker** 16:25 If one of them applies to virtual, all of them apply to virtual. Oh, I'm sorry, I missed… I missed that these are…
**Fairly OddParents (ca-wat-brt3)** 16:34 These are enum… yeah, these are enum members.
**Trask Stalnaker** 16:36 just… Date…
**James Thompson** 16:39 Yeah, but then you have the scenario of when you're actually reading the document, right, the attribute can quite often be quite a fair distance away from it, so you're looking at the It split the information up.
Whereas having the used virtual memory on the definition of the enum has it right there and there for you.
Right.
**Trask Stalnaker** 17:04 So, James, the… my only… my main concern with this is that there's 10 of these, like, as you can see, this is more complicated than I think you initially, like, thought it would be, right? And… reviewing them is gonna take time and effort from people who are, you know, both experts in that and non-experts like myself to Google stuff, and… Feel comfortable approving but there… you have, I think, like, 10 of these PRs open right now?
My… my suggestion would be to pick, you know, let's just do one See how that goes, see if we can get agreement.
I don't mind looking at one, but when I see 10 of them open, I'm… I just… I'm like, I don't… like, that's gonna be way too much time to look to… Go through in detail.
**Fairly OddParents (ca-wat-brt3)** 18:13 The intention is… I think physical, by the way, so the initial brief that was there already was probably wrong.
I'll take an action item to get that sorted.
**Trask Stalnaker** 18:31 Yeah, so, I mean, I don't… like, I think it's a… I actually think that, potentially, that there could be some benefit from going through this exercise, but it is a… Time-consuming exercise, and we want to draw the right balance of… Not… You know, like, do we… Duplicate things. In some cases, how, you know, do we want to do something like this, where it doesn't provide value?
Do we want to generate stuff? I think there's been a lot of, kind of, open questions across these PRs that we haven't… Addressed, and when there's a lot of them open, it… It's confusing to me, and where to… How to help move them… move it forward.
Alright, well, we should move on, to… general topics, Lyudmila.
**Liudmila Molkova** 19:51 Yeah. So, can you open this comment, please?
**Trask Stalnaker** 19:57 Yeah.
**Liudmila Molkova** 20:03 And maybe if you scroll up a little bit… Yeah, so if you look into our OpenTelemetry IO, looks for semantic conventions… oh yeah, thank you.
there are… Two, or maybe three main sections.
Yeah, so there is registry, which is… we want to deprioritize, right? But that's not the part of this discussion. Maybe we can do it together. And there is general.
Which is a weird combination of, like, policies and lists of attributes.
So, we have some naming guidance, but we also have some, general attributes here, I think, which nobody likes.
Yeah, this one. This is, like, the list of attributes that are generally applicable.
Then, beyond general, we have, how to write conventions.
Big group.
And also… The… another one, the third one.
Duh.
The non-normat… yeah, right.
And then the non-normative section.
So… Neither of those are semantic conventions? Well, maybe the general attributes are.
But these three groups, they stand out. They are not part of semantic conventions per se.
So, patrice, who works on OpenTelemetry I.O, suggested, Something maybe we can discuss, that we have, Different structure under docs.
And we would have, SPAC or SEMConf for SEMConf?
And we have some, additional folders for, like, supplementary things and how-to guides and whatnot.
So, I wanted to come up with some specific proposal based on this, but they didn't have a chance.
I wonder how people here feel about it, and if you have any thoughts on organization.
**Trask Stalnaker** 22:41 Definitely like the idea of moving semantic conventions to a top level.
**Liudmila Molkova** 23:02 Another thing we can do, we can also put registry somewhere where it's, well, hidden.
**Michele Mancioppi** 23:11 some, some feedback on the registry. Actually.
I use it a lot in my daily work.
Occasionally, there are… there are potential users that come up and say, yeah.
why don't you support error equals true? I look at them and say, because that's open tracing, not open telemetry semantic conventions.
And then I show them the registry. Say, hey, you see here, there is error of the type, there is error of the message, there is no error equals.
I, I think it's a pretty good asset.
So, I would love it if it stayed in reach.
**Liudmila Molkova** 23:51 Oh, yeah. Yeah, thanks.
**Michele Mancioppi** 23:52 To be top of mind, but on reach, yes.
**Trask Stalnaker** 23:56 So our goal for… the reason why we were, Thinking of… Not making it quite as visible, but not missing, is that we… actually, we want people to come through the, the semantic conventions themselves. Like, we don't want people to view this as, like, a grab bag of… attributes, but more, like, consistent semantic conventions for CICD come into here and see how you're supposed to build spans, and what attributes should be on those spans.
As opposed to… right now, we worry that People… the first place they go.
will be here, and they're like, oh, look at all these attributes I can use, and… Missed the cohesion.
**Michele Mancioppi** 24:52 Oh, by the way, there is occasionally confusion around… I mean, there are several registries.
In OpenTelemetry, one is for attributes and entities, and then there is the one about tools, and when you talk about when… even inside dashboard, we talk about, oh, the open territory immediately comes. Wait, which one again?
**Trask Stalnaker** 25:11 This one.
**Michele Mancioppi** 25:12 Yeah.
I've not seen… Muggles?
come up with that question. But, inside the service comes up.
**Trask Stalnaker** 25:34 Yeah.
Do you know if we… use this term anywhere for the semantic convention registry?
Or if…
**Michele Mancioppi** 25:47 It's literally how it's called in the navigation bar. It's the registry.
**Trask Stalnaker** 25:52 But it's underneath the semantic invention node…
**Michele Mancioppi** 25:57 Yeah, that's… Do you expect people to concatenate the,
**Trask Stalnaker** 26:02 Haha.
**Michele Mancioppi** 26:02 Red crumping their heads.
**Trask Stalnaker** 26:06 Fair.
**Michele Mancioppi** 26:09 Besides, also something else that causes a bit of attrition is having the aversion.
And, in navigation bar, it immediately begs the question of, wait a second, there are others?
And, there, I assume, is because The SIG wants to make people aware that semantic conventions evolve over time.
But then maybe having a factory kind of the change notes to be more visible.
Would make a better job of, having this kind of moving target of the current semantic version.
I do not see practitioners.
Follow that very closely.
And this is why, in Dash0, we automatically migrate it for them.
**Liudmila Molkova** 27:03 So you would like to see, version more visible, part of the.
**Michele Mancioppi** 27:09 No, less feasible. Semantic conventions are what you should be doing.
They're a slight moving target, but, I mean, the SIG is doing a good job of keeping stable semantic conventions stable.
So, I do not feel the need of saying, okay, is it 1.37.0.
Like, HTP is a fatal written in stone, you know.
I could leave, for example, with removing the version from here, and then having… Somewhere in the navigation, an updated feed of what changed since.
Which is pretty much what is happening with the schema migrations, right?
**Liudmila Molkova** 27:50 Well, yeah, to some extent.
**Daniel Dyla (Dynatrace)** 27:54 I do find…
**Trask Stalnaker** 27:55 the version in here a little odd, in the table of contents. I could… Like, see it here.
But over here, like, we don't do that for, you know.
Anywhere else, like, we don't have, you know, Java.
DK… One point.
**Michele Mancioppi** 28:15 This is where my project, whatever put is the version as one of those tags.
You know, like, when you go, like, GitHub builds, and then latest version something, and just put on the tag on the main page. Like, the current normative version is version blah, you click on it, you go to… To… to the details of that, or maybe the delta from the previous one.
Hi, Clara, let me see if I find something that will convey the idea that I'm trying to express.
Yeah.
If I may share very quickly…
**Trask Stalnaker** 28:54 Sure.
**Michele Mancioppi** 28:55 Something like this.
One of these types, and this tells me which one is the latest.
**Trask Stalnaker** 29:13 Where are you… are you suggesting to put that in the website somewhere, or on the.
**Michele Mancioppi** 29:18 On, like, when you click on semantic conventions, then on top of it you see the latest version is.
**Trask Stalnaker** 29:24 Yeah, a bat, like a badge, like that, yeah.
**Michele Mancioppi** 29:32 The same would apply, technically, for the openermic Collector and a bunch of other stuff, too.
I mean, after all, versions of the specifications are effectively GitHub artifacts.
**Daniel Dyla (Dynatrace)** 29:47 One thing I've always… and this kind of reminds me of, one thing I've always appreciated about the Node.js docs is that like, each… each API that's documented, right by the header, it says what version it was introduced or stabilized, and if you click on that, it goes back to, like, that changelog.
I have always appreciated that, and if we can… Because, you know, HTTP, for example, been stable for a long time. Exactly how long? Not easy to answer that question without digging through some history.
It would be nice… to just have right on the HTTP semconconf, like, stable sense… One dot, whatever.
**Trask Stalnaker** 30:35 You're thinking more in the, Oh, I guess we do. Yeah, it's the same thing on the website, yeah.
HTTP…
**Michele Mancioppi** 30:44 And in this optic, also attributes that are deprecated, A deprecated sense?
**Daniel Dyla (Dynatrace)** 30:51 Yeah, exactly.
**Michele Mancioppi** 30:51 Put them at the end of the page.
**Daniel Dyla (Dynatrace)** 30:54 Right, so where it says stable there, if it said, like, stable since 1.24, that's probably not the correct version, but I think you understand my meaning.
**Michele Mancioppi** 31:04 And that would look very cool, like a badge.
**Trask Stalnaker** 31:13 Yeah, we could potentially stack. I like the, the width of these tables is hard to manage, But that could be stacked.
**Michele Mancioppi** 31:23 But here, about this, a fine point of design of this information. No, please, do not move away from the table. I wanted to make…
**Trask Stalnaker** 31:31 Sure, sure. Let me take a note, though, before I forget.
Okay.
**Michele Mancioppi** 31:45 this table.
Is intended for, Two slightly different personas.
One is, the intelligentsia?
It needs to have a lot of details for things.
But for end users, the main question is, what is there? And second, can I rely on it?
the… can I rely on it for pretty much all end users, ends up in, stability? Like, do I expect it to change?
And the second one is, do I expect you to find it implemented?
In the SDKs. So, for example, if you were to move the badge with stable very close to the attribute, since the attributes are pretty self-descriptive.
That would be the second most interesting piece of information.
Funnily enough, when I look at this table, as a user, I would say, I want to know which attribute it is.
Is it stable or not?
Is it required or not?
And then the rest is less useful going forward. Most attributes are string, but now the type is the second.
And you effectively always see it by scanning.
So I could see changing the order of these columns to be focused on people looking at this and say, should I implement that?
**Trask Stalnaker** 33:12 So you're saying, to you the ordering is attribute name, stability, requirement level?
**Michele Mancioppi** 33:18 Yep.
Because if it is required, but it's not stable, I ain't implementing that.
But if this table ain' required, oh, now you have my attention.
**Trask Stalnaker** 33:39 Cool. Was that, too much feedback?
Lyudmila.
**Michele Mancioppi** 33:44 I'm sorry.
**Liudmila Molkova** 33:45 No, that's great! Really appreciate it.
I like the idea of reordering columns in this table.
**Trask Stalnaker** 33:58 I kinda like the… idea of… Potentially just putting the badge in here.
Cause it could wrap.
**Michele Mancioppi** 34:07 So long as it's easy to copy and paste, as long as it remains easy to copy and paste, like, for example, you put the copy button so that people do not get wedged by mistake when they drag the mouse over the column.
Then the badge in there is a criteria.
**Trask Stalnaker** 34:20 Hmm.
**Liudmila Molkova** 34:21 So, copy and paste attribute name?
**Michele Mancioppi** 34:24 Yeah, they had to rename, yeah. Because, for example, what a bunch of people will do is actually to copy that and put it in their manual instrumentation.
**Liudmila Molkova** 34:32 Mmm.
**Michele Mancioppi** 34:33 And if you add things in the same table, then… for example, here, you see it, like, those two papers on top of each other, right?
**Trask Stalnaker** 34:42 Which.
**Michele Mancioppi** 34:42 Drag again your mouse, selector again an area.
You had a tooltip coming up.
**Trask Stalnaker** 34:49 Oh,
**Michele Mancioppi** 34:50 There you go, the fourth icon from the top.
If you make it easier to copy, you can pile more stuff inside the cell.
**Trask Stalnaker** 35:03 I'd have to test it with the… I mean, with a badge here.
I would suspect it wouldn't be hard to drag just up to the badge.
We could try it, yeah.
**Liudmila Molkova** 35:14 Especially if badge is on the next line.
**Daniel Dyla (Dynatrace)** 35:18 Yeah, if you just always have a line break, you solve that.
**Liudmila Molkova** 35:22 And there could be more than one page, right?
Blake.
Stability, maybe, seems very…
**Michele Mancioppi** 35:29 or Development Sins, those two can be paired.
Right?
**Daniel Dyla (Dynatrace)** 35:38 Yeah, you can have one badge, because the badge is… the one you showed before that had Apache 2, it's like a two-part badge. The first part could be the stability level, and then the second part is just a date.
**Michele Mancioppi** 35:49 Yeah.
Yep.
**Christophe Kamphaus** 36:01 Should people be copy-pasting the attributes?
Wouldn't we rather have auto-generated constants?
**Michele Mancioppi** 36:10 There is actually, libraries in pretty much every SDK, but people don't know that.
So, in most languages, you need to import the right package.
And then, you need to find this, the autocompletion, and it's not always in the most intuitive thing, or you may be having an older version of the SDK with attributes that are missing.
And then it's a bit of a harrowing experience.
**Daniel Dyla (Dynatrace)** 36:35 They're also, in some cases, even, like, discouraged for, like, particularly, development attributes, where some SDKs are saying, like, don't use the constants that we provide, you should be copying and pasting this into your own things so that you know when things change, or so that you avoid, like, in some cases, the diamond dependency issue and stuff like that. Copy-pasting is definitely something that is encouraged in a lot of places.
Whether or not we want that long-term is a different question, but it's the case right now.
**Christophe Kamphaus** 37:14 Yep, makes sense.
**Michele Mancioppi** 37:21 And besides, I mean… A bunch of instrumentations will soon be written by AI.
I think AI is just people to copy and paste, copy and paste without any thought about sustainability of the code going forward.
**Trask Stalnaker** 37:38 Cool, Ludmila, anything else you wanted to… Discuss…
**Liudmila Molkova** 37:44 Now let's stop there. I think I've got the answer that there is general, support for some organization there. I will go ahead and create some issues to track table reorganization.
And if anybody is interested in picking any of this up, go ahead.
**Trask Stalnaker** 38:06 Cool. I like… I mean, I… overall, I like, Patrice's… Terms.
Alright, Michelle, you got the next…
**Michele Mancioppi** 38:20 Yes, I, I came forward to this fellow council, To ask for guidance.
On how to fix a significant bug in the peer namespace.
So, from… the olden days of PR.service.
Nobody thought of saying, hey, what about service.namespace?
How do we represent that in a peer dependency?
And, of course, the, like, if you go on files changed.
The, intuitive way would be to say, hey, peer.service is not an attribute key, it's a namespace. And then we put under it peer.name and peer.namespace.
And then… I, went and looked at the code, And there are exporters.
that rely on peer.service for stuff, like the Zipkin one.
**Trask Stalnaker** 39:13 Zipkin.
**Michele Mancioppi** 39:15 Yeah, and then I got cold feet.
So I'm asking, should we rather instead have other peer.service underscore namespace, and symmetry be damned?
**Trask Stalnaker** 39:31 So, I'm trying to think if this could fit, this is a big… change, right? Impact-wise.
**Michele Mancioppi** 39:40 It doesn't have to be.
**Trask Stalnaker** 39:44 Well, the peer namespace… anything… I think anything touching peer namespace is potentially… a big change, just because, I mean, we need to think through that. It's… It's unfortunately not a stable Namespace, but at the same time, it's widely used.
Therefore, any touching it I feel is… Needs to come with… A good amount of thought.
What I would…
**Michele Mancioppi** 40:19 Have an even more unholy suggestion.
So, one option, the one about the very idealistic one that I sketched in the PR, Yeah, I see it now, but it's not gonna work.
It's… The world would break.
There is an option of adding another key.
Or… We could open up a bit what the valid values are.
Because service.namespace is a very optional.
Attribute in the identity of a service.
Like, everybody, or most everybody, uses service name.
But very few actually use service.namespace.
So, what if… we allowed… Interpolated string of service namespace slash service name as a valid value for peer.service.
And then we don't need to change the key.
We just put a bit more effort in the backends to support it.
**Trask Stalnaker** 41:23 I… don't mean to kind of cut off discussion of the details here, but at the same time… This is the kind of, like, bigger change that we would generally want to be driven through a SEMCONG SIG.
And we do have one just kicking off, I think this week. Which… we could try to… I mean, you could try to get this SIG to sort of take that on.
I mean, it would be wonderful to get the peer namespace… the peer namespace sorted and stabilized.
But I… I think it's… You know, it's, it is a big deal.
I hear you. Any decision?
**Michele Mancioppi** 42:25 Where do I find this sig?
**Trask Stalnaker** 42:27 It is… Meeting… .
**Michele Mancioppi** 42:37 Could you, could you copy for me the, the chat?
**Trask Stalnaker** 42:42 Yeah.
So Thursday at… 8 AM Pacific time, so same time as this meeting on Thursday.
And there is a… I saw a Slack channel just got created, I will drop a link to that.
It's not on the calendar yet, but, we will get it on the calendar before.
**Michele Mancioppi** 43:33 When you look at the scope.
I can imagine me going there and say, hey, how about we touch Pierre namespace, and then… Everybody melts in a puff of smoke.
**Trask Stalnaker** 43:48 That is…
**Michele Mancioppi** 43:49 I can try.
**Trask Stalnaker** 43:50 That… that is a definite possibility.
**Michele Mancioppi** 43:53 I can try.
**Liudmila Molkova** 43:56 So from… from… pure technical perspective, we should rename peer service to peer service name, and the only reason not to do this would be that the world would melt.
**Michele Mancioppi** 44:09 It's a pretty compelling reason.
**Liudmila Molkova** 44:11 To be honest.
We've melted the world before, so I have mixed feelings about this.
**Michele Mancioppi** 44:18 It's a feeling that was relayed to me by a few people by whom I run the PR, and yeah.
I see it. That's why I thought, hey, maybe we don't change the attribute, and we just make the key.
a bit more complicated. And if you have been perfectly happy with the current peer.service and service.name, then nothing breaks for you.
**Liudmila Molkova** 44:41 Actually, maybe I'm wrong, but, the peer service is something that inherently opt-in Yeah. You cannot populate it without some opt-in.
**Michele Mancioppi** 44:53 Cut.
**Liudmila Molkova** 44:53 And the amount of world melting maybe overrated, And this opt-in mechanism could include the opt-in version. Like, what we do with HTTP stability and other stability projects, where we make the New version opt-in.
Right?
**Michele Mancioppi** 45:18 Yeah, there is one factor that, I mean, I hear you, and… Make sense, what you're saying?
You know what is the number one tool with whom people have used peer-to-service?
That's light step.
Last step… Is going to meet its maker.
And there is going to be a bunch of people migrating from, LightStep to other OpenTelementary tools.
That, may have strong feelings.
About touching what, for them, has worked for a bit.
So, for example, an automatic migration from service.name… from peer.service to peer service.name would mean perfect sense to me in a world where we have automatic schema migration.
But then I found out that people use it in routing and a bunch of other things, and gave me pause.
**Trask Stalnaker** 46:16 To Lydmilla's point, I don't think it's any more world-melting than what we did to HTTP semantic conventions.
**Michele Mancioppi** 46:23 Probably not.
**Trask Stalnaker** 46:24 What we did to database cement to conventions.
**Liudmila Molkova** 46:27 Or deployment.
**Trask Stalnaker** 46:30 Yeah, that one…
**Michele Mancioppi** 46:31 I found that one.
**Trask Stalnaker** 46:33 Yeah, I don't mind world melting if we are going to stable.
So, like, I can get behind… this… If we go… if we, like, have… if we feel conf… if we're going to stability, and, you know, we go through that process, because stable is… stable is… how I justify those world-breaking.
**Michele Mancioppi** 46:59 And, I mean, I, double in and out of… sakes. I have a curiosity.
How come nobody has stabilized Pierre yet?
**Liudmila Molkova** 47:15 Because we need you to do it.
**Michele Mancioppi** 47:18 People who actually use it.
Terrible answer.
**Trask Stalnaker** 47:22 There's a lot of things that are surprisingly not stable. Thread namespace is not stable.
Code name.
**Michele Mancioppi** 47:31 My question was more like, was there… Significant interest group against.
touch imperial service, because I went through the issues in semantic conventions, and occasionally there have been attempts.
They just… beached.
As far as I can tell.
So I was wondering if there was something, That I did not see on the matter.
**Liudmila Molkova** 47:55 No, it's the lack of energy more than any resistance.
**Michele Mancioppi** 48:00 Okay.
**Liudmila Molkova** 48:01 Not lack of energy, but no, not enough resources, let's put it this way.
**Michele Mancioppi** 48:06 Also, maybe not such a compelling event, like Lightstep.
Shutting down.
Okay, got it.
**Liudmila Molkova** 48:17 I have a question to Trask. Trask, do you think that the… the… To me, if we stabilize service name, it's actually… a good time to also stabilize the peer service name. Oh, sorry, the service name is stable. The, like, how much… interest do you think the new SEC around service and deployment would have in the peer namespace?
**Trask Stalnaker** 48:44 I mean, it's definitely a good group of people to… Potentially have that discussion with?
Cause, I think, you know, we have to consider… we'll be considering the cross-section with entities and… I… don't initially think that's related to peer service, but I'm not… I mean, there's… At least on the SDK side.
But certainly, on the back-end correlation side, there's… I mean, you could.
**Michele Mancioppi** 49:26 I will attend it.
**Trask Stalnaker** 49:29 Yeah, and if we don't find a home for it there.
I mean, if you are motivated, you can definitely propose a, you know… well, so what we did with with code attributes. We stabilize code attributes In the last year, and we didn't form an actual SIG to do it.
But we did have a group of maybe, like, 3 people who were sort of… driving that.
So… I could see something similar working for… this.
**Michele Mancioppi** 50:14 Okay.
I'll try the… the sun comes circular, why is I'll write up a project?
**Trask Stalnaker** 50:23 back. Yeah, okay.
Sounds good.
Yeah, I mean, we're… we love… Getting things to stable is just a matter of… Energy has lived less.
**Michele Mancioppi** 50:35 This one is actually particularly important, because… the, There is great use for this kind of stuff, especially in the spansometric kind of story.
That's actually super useful.
**Trask Stalnaker** 50:50 Yeah, because you can't calculate it on the back end for your… yeah.
**Michele Mancioppi** 50:55 Even if, technically, maybe you could, for example, if the backend is doing the aggregation for you, but to my recollection, there is nothing. For example, in the HTTP semantic conventions, or the RPC semantic conventions, I mean, the metric ones, that would allow you to represent the other side.
How's the dimension of your metric?
And the closest thing… Spear of the service.
**Trask Stalnaker** 51:19 Yeah, I think a big reason why, like, you ask why there hasn't been It hasn't happened yet. I think a big part of that is the opt-in nature of it.
And how it requires configur… like, there's nothing automatic.
for it.
**Michele Mancioppi** 51:37 Well, one, it's not difficult to make it automatic, I mean, the same way that we do… the collector doesn't do it yet.
But, for example, something like, when you look at most service maps out there.
They are powered by effectively taking spans and extracting point-to-point connections between services.
So the collector may not do it, but backends definitely do.
And today, there is no way for most customers to be able to submit metrics to people data service map.
Because it's missing the point-to-point aspect.
**Trask Stalnaker** 52:12 Yeah.
Have you looked at, Carlos… had sent an OTEP at one point for… trying, I think, for doing, like, a reverse… Baggage propagation back from the service to send, basically, the service name back.
To the caller, so that…
**Michele Mancioppi** 52:33 But that will never work on anything that is not asynchronous. I mean, you can kiss it goodbye on messaging.
Right off the bat. That's… I don't believe that… I mean, I remember that OTEP, and I was like, meh… It works only in HTTP, RPC, and a bunch of other stuff.
Ultimately, been able to effectively buffer spans, and then when the other side comes in, and meet the metric at the point for the connection, it's not rocket science in the back end, especially not the SaaS one.
**Trask Stalnaker** 53:02 Yeah.
Okay. Alright.
**Michele Mancioppi** 53:08 Well, thanks for the pointers, and wish me.
**Trask Stalnaker** 53:10 Yeah.
Yeah.
**Liudmila Molkova** 53:13 Good luck! Thank you for coming and bringing it.
**Michele Mancioppi** 53:18 I'll need luck. Thank you.
Bye, folks.
**Trask Stalnaker** 53:22 Alright, yeah, I think we hit the end of our agenda.
So, thank you all, and see you next time.
**Christophe Kamphaus** 53:33 See you.
**Liudmila Molkova** 53:33 Thank you.
