SIG: Semantic Convention Tooling
Date: 2025-10-08
Duration: 46 minutes
Zoom Recording URL: https://zoom.us/rec/share/lh778SObCRoEtSV2jqbeqfQAmF0cMuvvt5TFbhW6WAKaMlmm_L-kCFNLJKTtUkKb.ukWQql4MgNKCZjOs
============================================================

## Zoom Recording Transcript

**Laurent Quérel** 01:30 Hey.
**Nathan Smith @ Elastic Observability** 01:37 Hello.
**Laurent Quérel** 01:39 Hello again.
**Nathan Smith @ Elastic Observability** 01:48 I'm just listening in today, but… Not many people yet.
**Laurent Quérel** 01:53 No, I just know that Jeremy will join us a little bit late.
And, looks like Ludmelier is, is on vacation.
I don't know for, Josh. I was in a…
hoping that Josh will be there today, because I didn't participate to the…
To the last, few meetings.
So I'm not necessarily the most aware of what is happening these days.
But, let's see… do you have any,
Question on your side? Specific questions?
**Nathan Smith @ Elastic Observability** 02:34 No, I'm just trying to keep up with the work, so… Just listening in for now.
**Laurent Quérel** 02:49 Okay, I'm just updating the… Right now, the… Google Documents.
We've had the list of attendees.
Azrush.
We conseer you.
Oh, Magic Shunker.
**Josh Suereth** 05:11 Hey, can you hear me?
**Laurent Quérel** 05:13 Yes.
**Josh Suereth** 05:15 Okay.
Yeah. My laptop will no longer let my microphone connect to Zoom. I don't know why.
Yep, okay.
Fun times.
**Laurent Quérel** 05:32 Yeah, I was seeing Natan… I was asking, basically, Nathan, if he had some specific questions, so the answer is no, and I just updated semantic convention tooling dock.
with, the traditional, information in the simul.
**Josh Suereth** 05:54 Yeah, that's cool. I didn't see a lot on the agenda. I have been a bit distracted with other
Yeah, we canceled because people were traveling last week. I think Lyudmila's on vacation. Given travel and given entities' work, I haven't had time to make progress on the, V2 schema stuff.
I think we had… but… but why don't we go through, kind of open pool requests and project board?
Cause I believe… We had a few things, so let's,
Let me pop open Weaver, alright.
Yeah, we have attribute groups in V2. This is approved, so I think this is actually ready to merge, but had open questions, is that right?
Oh, I didn't… I didn't approve this yet, but I think I was going to.
Did you have any concerns at all with this, Lawrence, or should we… should we merge?
**Laurent Quérel** 06:58 No, I think I already approved it.
Yes, I did.
**Josh Suereth** 07:02 Yeah.
Yeah, I forget what I wanted… there was something I wanted to check before I approved, but I think I'm good to go. This is in V2, we have attribute group with internal…
in public… Internal doesn't have common fields.
Oh, because it's internal. That makes sense. Okay. You didn't have any concerns with that?
**Laurent Quérel** 07:27 No.
**Josh Suereth** 07:29 Cool. Well, the main concern I had was about the…
**Laurent Quérel** 07:33 Forcing the entire project to, to, to remove an entire, lint.
But, I think that has been fixed.
**Josh Suereth** 07:41 Oh.
Yeah, she fixed it here.
**Laurent Quérel** 07:44 Yes, so that's… it's unfortunate, but I prefer this solution that is not ideal to the other one, so…
That's okay for me.
**Josh Suereth** 07:54 I'm gonna I'm gonna mark this as approved, and…
I think we can try to submit this, but I don't remember if it's submittable. Let's see.
Because I'd like to get this in… yeah, we have to resolve conflicts. Alright.
That we can do later. Was there any other pull requests that were sitting here?
This is August 7th, so I think we've already talked about bundles and offers and packages.
And namespaces. I'm… I'm debating…
Closing some of those for the V2 work.
**Laurent Quérel** 08:34 I don't remember where your intent was for this kind of, additional, ideas…
you were asking to wait for the finalization of the Schema V2, and then to introduce them, right?
**Josh Suereth** 08:50 Yeah, yeah, or introduce them as part of E2, but I'd rather wait for the finalization of E2, because I'm finding,
V2 would be easier if I didn't have to preserve V1 resolution. So, what I want to do is do the bare… do the bare minimum,
So we'll have a V2 input, and we'll have a V2 output, right?
And then we'll have a period of time where we convince people to move both their inputs and their outputs to be V2,
And then after that, I want to change the resolution structure to be only V2 to V2, because it'll actually… I think it'll clean up the code, honestly.
Particularly with lineage.
**Laurent Quérel** 09:33 Yeah.
**Josh Suereth** 09:34 And then once that… then once that's done, we can, we can move forward with, adding these things. So that's… yeah.
Okay, cool. Let's go to… R… Triage board here.
For… to consider for next release.
Oh, by the way, thank you for your fix on the, the template registry directory thing, that's nice.
**Laurent Quérel** 10:03 Yeah.
**Josh Suereth** 10:04 Execute.
This is the one I wanted to kinda…
think about here, this is about using strict mode for Jinja 2. This does break Semcov, and I think it actually…
**Laurent Quérel** 10:19 In practice, it's a little weird, right? Where if you try to ask something…
**Josh Suereth** 10:23 interest at bills.
**Laurent Quérel** 10:24 We'll.
**Josh Suereth** 10:25 Oh, I'm sorry
Okay, here. Enable strict mode for Jinja 2 behind a CLI option. I'm happy to introduce this, and it's something to consider. We just… we know it breaks SEMCOV, because we rely on
We rely on a non-existent field being treated as null or empty.
This would cause that to actually fail.
**Laurent Quérel** 10:51 Yeah, but if we are willing to… to make the…
a correction into the semantic merchant, I think it's a good idea.
**Josh Suereth** 11:03 Yeah, okay, so…
Is this something you might have time to do? I think I absolutely will not, because I'm working on the V2 stuff.
**Laurent Quérel** 11:14 I can try. So, it looks like the enabling the strict mode is probably just straightforward.
But what will matter, really, is the amount of correction that will result from that.
Either into the River Registry or into the Sanity Convention. So, I don't know what is the…
**Josh Suereth** 11:35 No, no, no.
**Laurent Quérel** 11:35 What size of this serve?
**Josh Suereth** 11:38 I think… I think what we should do for now, is we make a CLI option.
Or a config option that is strict mode, and the default is still false, and then we can make the default true later if we want.
**Laurent Quérel** 11:50 Oh, okay, okay, that's, basic. Yeah, I can do it.
**Josh Suereth** 11:54 Yeah, because it… and then in our docs, we can show how to use strict mode to look for errors with your templates, if you're not getting output.
**Laurent Quérel** 12:03 So that's the 931. Let me just, put that into the Google Doc.
**Josh Suereth** 12:11 Okay.
**Laurent Quérel** 12:12 I'm working on it. Noise…
**Josh Suereth** 12:15 Alright, I will… I'll add you to the assignee as well.
**Laurent Quérel** 12:19 Yeah.
**Josh Suereth** 12:19 Yeah, please.
That's one I wish I had time to get to, because I think it's relatively easy. This one… this one I think we actually need to do some design on, but this is basically if there's a documentation-based URL field in Manifest.
Then, what we want to do is, anytime we detect
in notes or something. Here, what is it? So…
We'd have to look at the semantic convinced it's Java, but anytime we have an absolute path, like this.
We would want to prefix it with the doc-based URL.
So, if we're… if we're getting a,
the… the note field, or the brief field, or the description field, or whatever, on… in our model, and someone puts a relative URL there.
We would want to find a way to add the doc-based URL from the manifest for that repository.
When we resolve.
so that nobody has to, like, fill out the full URL, and so if I'm doing code gen for Java, I get the same base URL as if I do CodeGen for Go. It's not, like, 100% configured and awkward, right?
I think this might be a bigger… a bigger chunk of work, though.
**Laurent Quérel** 13:38 And we want to do that on, every… Text production, From Ginger.
Or when there is a… maybe a parameter, again.
Oh, no, when we have the manifest file with this specific information, any production from DJ has to be post-processed with this,
Old.
Adding a base URL?
**Josh Suereth** 14:05 I'm trying to get you an example here. I think if we look at what they have, like, what this was commented on.
Come on, come, come, come on…
I don't know if we need to do it in Jinja. Like, the theory here was…
Weavers should do this in some way, so that not everybody has to do it.
**Laurent Quérel** 14:27 Do we expect that, we introduced some kind of function into Ginger.
So people can reserve their URL, and it's done automatically, but you have to use the function, or do we ex… do we expect
To detect, automatically, absolute pass.
Which could be problematic, because sometimes it's a pass, sometimes it's a URL.
Do we expect to post-process the output of Jinja and do this, type of collection.
**Josh Suereth** 15:00 Yeah, I… I'm not… I… I think the… the expectation here… the GitHub's not loading for me, hold on, let me… let me pull this up.
I think the expectation here is we'd actually, we'd do it When we resolve the model.
So we wouldn't do it in Jinja, we'd do it all the time.
**Laurent Quérel** 15:18 Oh, yeah, yeah, man.
**Josh Suereth** 15:20 repository.
Yeah, and that means, like, okay, I think database was one example, right? So if we look at, like, common.
And we look for a URL here. Maybe it's not uncommon.
**Laurent Quérel** 15:34 So it's part of the reservation process.
**Josh Suereth** 15:39 Yeah, so it'd be part of the resolution process, and that's why we would have it. So, like, here.
We know that this is a markdown link here, right?
**Laurent Quérel** 15:49 Yeah.
**Josh Suereth** 15:50 So, we would do it for links that we detect. So, if someone just throws a random URL in there, we can't do anything. But if it's a link, like this.
**Laurent Quérel** 15:59 Oh, okay.
**Josh Suereth** 15:59 And it's relative?
Yeah, if it's a link and it's relative, then we would add the base URL that's configured in the registry. So, like, all of these would be untouched.
But the markdown link… where was it?
This one here, for example, right?
We would look at the base URL configured in registry, in the registry YAML,
And then that base URL would get prepended to this link during resolution.
**Laurent Quérel** 16:33 Okay, I see two ways to do it, right now…
So, we already have a function that render, For example, in HTML.
A text like that.
And basically, this function is, if I remember well, parsing the Markdown file.
So we… we have a view on… at the… Markdown AST.
So we could detect links like that, and so… so it's not really,
inside the resolution process, but more when we are rendering text to HTML.
The other option is to do, like you said, during the resolution process, but that means that we will do two times, most of the time, the same work.
Which is not necessarily thin.
**Josh Suereth** 17:24 Yeah, so the thing about multi-registry here, though, Lauren, like, we… the reason I was thinking of putting it in the manifest is, like, if I'm using the semantic convention.
And I'm using my own registry at the same time.
the doc base URL needs to come from the manifest of semantic convention registry when it's a semantic convention link, and it needs to come from mine when it's my link.
**Laurent Quérel** 17:50 Damn.
**Josh Suereth** 17:51 And so, if we actually do it during resolution, or post-resolution is like a post-processing step, but prior… but the resolved application schema, or resolved telemetry schema, has just full URLs, always, because the.
**Laurent Quérel** 18:09 Yeah, we've…
**Josh Suereth** 18:10 You've done the stock base?
Yeah, yeah, so that… yeah. But it could be… it could be either way. So that's the straw man. I still, like, as we talked it out, I think this is a good bit of work, so I think I'm gonna… I don't think we assigned this to anyone just yet, but, does that sound reasonable to you as, like, a thing to do?
**Laurent Quérel** 18:28 Yes, I will put that on my side as a stretch goal.
Looks like…
**Josh Suereth** 18:36 Yeah, let me…
**Nathan Smith @ Elastic Observability** 18:36 And that comment above yours, Josh, is from me, and says…
I think it says about the same things you guys just said.
But I didn't really know… where in the codebase I would find,
to start looking at this, you know.
The, the, the… It was a little bit…
off-putting to me that, like, in this model YAML,
if I'm making a relative link there, I'm making an assumption that this…
in the same repository as this YAML, there is a docs directory where there is generated markdown
from the YAML, so it's kind of…
**Josh Suereth** 19:21 Yeah.
**Nathan Smith @ Elastic Observability** 19:22 Coupling the… the output to the model, which,
is probably fine, but, like, I mean, I don't know any other way to do it.
**Josh Suereth** 19:39 I… I think, like, you…
Yeah, your comment is 100% accurate in terms of, like, the frustration, right? Of, right now, our YAML model assumes that there's a docs directory locally, and that all of this will work, and all of our command line options assume that you can, like, do craziness with repending.
Having it be more rigid, where, like.
there will be a document-based URL field in the manifest.
where all your YAML files are, and then you can just… it's clear then, cool, whenever I put a URL that's relative, it's relative to that base URL.
I think that this just makes the story better, so…
Hopefully that helps, but yeah, your comment totally makes sense to me.
Doc space is already making assumptions to resolve the transformation that may or may not happen. Right.
Right.
**Nathan Smith @ Elastic Observability** 20:40 I mean, it does have… in the SEMCOM repo, it does, like…
Docs is committed, and it's there.
And that's probably going to be the way it works for… for every registry. So it's probably a…
Safely valid assumption, but it's still… it's still an assumption.
And I think the problem is when you're generating it into
a Javadoc comment, you know, then it must, you know, you can't… you don't have a relative.
place there, so we need to replace it with the full URL.
**Josh Suereth** 21:15 Yep, yep.
**Laurent Quérel** 21:18 Yeah, I… Oh, sorry, go ahead.
**Josh Suereth** 21:20 Go ahead.
**Laurent Quérel** 21:22 No, I wasn'.
**Josh Suereth** 21:23 No, you go, you go.
**Laurent Quérel** 21:24 Suggesting to, to… I didn't see, Swiss, your, your comment there.
If you want some help to add this modification into Weaver, I can help you to figure out where to put that and how to put it.
**Nathan Smith @ Elastic Observability** 21:45 Yeah, yeah. Yeah, if you can just give me, kind of.
a starting point, maybe… Yeah.
**Laurent Quérel** 21:51 Now that I know what we need to achieve.
So it's a validation… it's inside… at the end, in fact, of the validation process, and we want to analyze the brief, the notes, use the mark done processor that we already have, and introduce the
basically resolve the URL with the…
the manifest file, the specific field that we have, I see exactly what to do, so yes, I can…
Give you some guidance.
**Nathan Smith @ Elastic Observability** 22:25 Yeah, and you can just DM me on CNCF Slack, or put a comment on this issue, whatever. Okay.
**Laurent Quérel** 22:31 I read.
**Nathan Smith @ Elastic Observability** 22:35 Yeah, and thanks for the help on there, I…
was looking for a way to kind of introduce myself to the codebase and start, you know, contributing something small, so this might be… I started looking at it like, oh, this might be easy, and then… and then it looked a little bit more complicated.
So, I'm glad, glad to have you.
**Josh Suereth** 22:57 This, I would argue, is a medium-sized task, and it's a good introduction to the codebase, for sure, but you'll be, you'd be well on your way to working in Weaver if you accomplish this.
**Nathan Smith @ Elastic Observability** 23:09 Right. No, no promises.
**Josh Suereth** 23:14 Alright, cool. So, that was to consider for next release,
template extension weirdness. This is just a bug that we need to kind of…
diagnose what the heck is going on, but this is where sometimes YAML will put, like, string quotes in front of things, and sometimes it won't.
not clear.
what was going on there? .
**Laurent Quérel** 23:48 I don't know.
**Josh Suereth** 23:49 Yeah, man.
Anyway…
That's a to-do to figure that one out. And I think that's it for… to consider for next release. I wanted to do a quick check on if there's any… because I think we've been making some ease-of-use changes. I think the V2 is the biggest ease-of-use change.
Is there anything we think we should pull in from this list? I can go through them in the meeting, or if you guys are,
you know, remember anything you wanted to pull in. Is there any ease of use we should consider for next release?
**Laurent Quérel** 25:01 Nope.
**Josh Suereth** 25:03 The thing… the thing I… I don't think I'll have time to do, and I want to wait till the V2 schema's done, is the,
JSON's, like, automatically generating documentation from JSON schema, and automatically generating the JSON schema.
I'm really tired of doing that by hand now that we have two versions, and, like, looking at that. So,
Yeah, that I think, we should prioritize.
Cool.
Alright, so under no status here.
Let's see if there's anything new…
span links and YAML, that one…
I'll throw that in the V2's schema.
**Laurent Quérel** 25:42 Sorry to interrupt you, Josh. I have to leave in 3 minutes. I just want to know if there is any specific question for me, or comment.
**Josh Suereth** 25:57 I don't… I don't think so. I think you actually answered all the questions we had there. I was gonna… I was actually gonna end this early, because I think we… unless anyone else has a topic they want to add.
Like I said, I was on travel, and I've been focused on the entity's work, so I haven't had time to do much updates in Weaver. I'm hoping to get past that for next week, so I should have more results.
But yeah, I don't… I don't have anything, like, urgent beyond what we already talked about.
**Laurent Quérel** 26:32 Okay. How about you, Jeremy, or Nathan?
**Jeremy Blythe** 26:35 I guess the only thing is whether we want to do a release, so…
I think there are a few things… In the main branch.
Which, to do with life check.
So… We improved the messages, I debugged a few things.
I think we've improved a few bits and bobs there, it's just whether we feel… Should do a release.
**Josh Suereth** 27:01 We… we just… well, I'd like to merge, Lyudmila's private attribute group thing to continue the V2
Left-hand side schema thing, or like, you know, definition schema?
And then, yeah, I'm fine. I think we just cut a release two weeks ago, but I'm fine cutting… like, I'm fine cutting releases more often, as long as, you know.
work is getting in. So yeah, I… if you want to, would you want to shepherd, Ludmila's PR through and then cut a release?
**Jeremy Blythe** 27:33 Is that a V2 thing? Which, which, which PR are we talking about?
**Josh Suereth** 27:39 What's the, attribute groups PR?
**Jeremy Blythe** 27:43 Okay, I can take a look at that.
**Laurent Quérel** 27:46 Yeah, it looks like there is only, a merge issue.
Yeah, on the… Changelog, so it's, it's nothing.
**Josh Suereth** 27:55 Oh, okay. Yeah, it's… It just has to update the changelog, that's it, yep.
**Jeremy Blythe** 28:01 Yeah, I can take a look at that.
**Laurent Quérel** 28:03 I have to go. Thank you, guys.
**Jeremy Blythe** 28:05 True.
**Josh Suereth** 28:06 Alright, see ya!
Alright, so this one…
**Jeremy Blythe** 28:16 This came from the Slack.
**Josh Suereth** 28:19 Yeah, run, make table check, and it says Weaver Panics, but that… I think that was the whole… that was actually on purpose.
like… We, we were… this is expected behavior, if I remember right.
Check out a specific commit, this is so… okay.
**Jeremy Blythe** 28:40 is.
**Josh Suereth** 28:40 How's it?
**Jeremy Blythe** 28:42 Is a panic, like, a good thing?
**Josh Suereth** 28:46 No, so, so they had a pool request. Let me see if I can find this. I'll show you, I'll show you what it was, but, here.service… they had a pool request where, basically the panic was…
we were appropriately failing, but it wasn't… it wasn't… I don't think it was a real panic.
Hold on, so if you look here, here's the… the checks and the failures, right?
And what had happened was they had made a table change, that, when we did a…
check to make sure the tables were up to date. It wasn't, because they hadn't regenerated the tables, or the registry.
So they had to… this verify semantic invention tables was failing from Weaver, and it gave them an error message.
That they just ignored and said, oh, Weaver's panicking.
But we're literally returning a non-zero exit message because
there's an error, and we're writing the error, and I think… I don't think this is a bug. I think this is… this is expected behavior of what happens when you fail. If we go to.
**Jeremy Blythe** 30:06 It's not actually a panic.
**Josh Suereth** 30:10 I don't think it was a panic.
Hold on, how do I get show…org?
**Jeremy Blythe** 30:17 Wasn't that what… was that what they were talking about in the Slack conversation?
**Josh Suereth** 30:23 Yeah.
**Jeremy Blythe** 30:25 Didn't have been printed out as a…
It says thread name, source registry update markdown.
**Josh Suereth** 30:36 Those checks…
**Jeremy Blythe** 30:37 and everything.
**Josh Suereth** 30:42 Yeah, so you're saying it's actually a panic? Maybe, maybe it is panicking, and that's the problem.
**Jeremy Blythe** 30:48 Unless this…
**Josh Suereth** 30:48 And we need to turn it into an error.
**Jeremy Blythe** 30:53 Unless these are two independent… maybe these are two independent things. Hang on.
Yeah, the person who reported in Slack.
I don't believe is the author of the…
**Josh Suereth** 31:04 vote.
No, it's the same person. It's the same person.
**Jeremy Blythe** 31:07 Oh, it is.
**Josh Suereth** 31:08 It's Michelle.
Yeah.
**Jeremy Blythe** 31:11 Okay, so they have a screenshot in Slack of a panic.
**Josh Suereth** 31:17 Yeah, and above it is the error message.
So… Do you… do you have the screenshot? Let me… let me pull that up.
This is in Hotel Weaver, right?
**Jeremy Blythe** 31:29 Yeah.
**Josh Suereth** 31:29 Or was it in some counts? Oh, it's right here, yeah.
**Jeremy Blythe** 31:31 How am we going?
**Josh Suereth** 31:33 No, it's not a panic, it just says error, process completed with exit code 2.
Oh, it does say thread main panicked and update Markdown. Okay.
**Jeremy Blythe** 31:42 Nope.
Update markdown 1389.
**Josh Suereth** 31:46 So this is probably my fault, then. Let's take a look. So this should be… let me move this to consider for next release.
Okay.
**Jeremy Blythe** 31:56 Yeah, it's okay if it's an error, but, like, it shouldn't panic, right?
**Josh Suereth** 32:00 Yeah, this… Should just be an error.
Air return, not a panic. Okay.
So let's do that. Did I move it to ease of use by accident? I think I did.
**Jeremy Blythe** 32:16 I don't know, your… your screen doesn't seem to be… Keeping up with something.
**Josh Suereth** 32:21 Here.
Anakin Weaver, yeah, I missed it by one. Okay.
So, I think what this is, if we take a look in Weaver.
I bet it's something dead simple.
This is the table check, right? That's what… that's the thing that was being complained about? Registry…
**Jeremy Blythe** 32:48 Yeah.
**Josh Suereth** 32:49 It's update markdown, and it's the… yeah, so if we look here… Yeah, we're asserting.
**Jeremy Blythe** 33:00 So that will panic if that's not true.
**Josh Suereth** 33:03 Is that right?
**Jeremy Blythe** 33:04 No, you weren't a test.
**Josh Suereth** 33:05 Oh, that's a fifth Okay, okay.
**Jeremy Blythe** 33:07 Line 138, look, it has error, panic.
That's… Yeah.
**Josh Suereth** 33:13 Okay, so we just need to change that to literally… literally return… return… return extra code of error. That's it. Okay, cool. Alright, that's an easy fix.
**Jeremy Blythe** 33:25 Okay, yeah.
**Josh Suereth** 33:26 Alright.
**Jeremy Blythe** 33:27 Where's that?
**Josh Suereth** 33:28 Hilarious.
Yeah, I… That's my bad, man. I think I made that panic and didn't even think about it. Alright.
Okay.
Alright, let me… let me…
line of code. We just need this to return your exit code instead of panicking.
I think, I think, also, it needs to… well… Alright.
We'll mark that as good first.
Issue type, because that's literally the one line change.
**Jeremy Blythe** 34:10 That's funny.
**Josh Suereth** 34:12 Ugh, okay, cool.
Alright.
That's all I have, then. I think, I think that was the… the newest… let's take a look here. Was this one new? Resolve output should be deterministic.
Output of resolve should be deterministic, so one can check resolve schema diff, sort by output group IDs. Oh, okay.
Yeah, should we be… should we… we be sorting things?
I think… I think this is the use of HashMap versus the use of B-TreeMap.
**Jeremy Blythe** 34:52 Probably.
It is more pleasant if it's… If it's ordered right.
**Josh Suereth** 35:00 Yeah.
Yeah. We… we probably want to do this, right?
**Jeremy Blythe** 35:09 Yeah.
**Josh Suereth** 35:11 Do you think that this should be considered ease of use, or do you think this is something else?
**Jeremy Blythe** 35:16 Probably ease of use.
**Josh Suereth** 35:20 Let me pop it into there.
Okay, that one I don't think is too bad.
Weaver cannot load registry directory beginning with dot.
Oh, my.
This is absolutely a bug.
I'm gonna put this into consider for next release. That seems like a thing that we need to eventually get staffed and look at.
Yeah, my guess is we're being too aggressive with our regexC, lobby.
Handling.
Upgrade scheme. This one… this one, I wasn't sure…
Wasn't sure how much work this is, or what we want to do here. The,
This is about using the 2020 version of the schema.
**Jeremy Blythe** 36:35 Oh, and .
**Josh Suereth** 36:36 For a JSON schema, yeah.
**Jeremy Blythe** 36:39 Maybe that's a thing to do when we get to that after the V2.
**Josh Suereth** 36:43 Yeah, the thing I'm not sure of is, though, I think this is still in draft, right?
**Jeremy Blythe** 36:49 What is it?
**Josh Suereth** 36:51 Let's gonna increase to this, which V1 was using, the idea set on… yeah.
We're on draft 7 instead of Draft 2020.
I don't know what that means.
Okay, anyway, we can look into it.
That seems minor.
Yeah, I might label this as ease of use.
Because I think it's about, integrations with other tooling.
Where's… oh, ease of use isn't there. Ease of use is in the project, okay.
I'll pop it into ease of use here.
And then, simple example repository. This is a good issue that I think…
We talked a bit about things… yeah, this is an old one.
**Jeremy Blythe** 37:50 Okay,
I think we've got a few of them, right? We've got yours, we've got… we've got one that I did…
Then I'll link to Readme.
**Josh Suereth** 38:03 Yeah, I think… I might… Step-by-step instructions, basic demo…
I think we're missing some of the things here, though.
**Jeremy Blythe** 38:15 That person is registered on setting up and using Weaver.
Basic demonstrating how to create a custom registry with attributes. Example of how to generate.
**Josh Suereth** 38:23 Yo…
**Jeremy Blythe** 38:23 My Weaver example does all of those.
**Josh Suereth** 38:27 What I kind of want to do, Jeremy, is maybe we can move your Weaver example into an OpenTelemetry location.
**Jeremy Blythe** 38:36 Oh, yeah.
**Josh Suereth** 38:36 called Weaver, Example.
**Jeremy Blythe** 38:37 What we talked about?
**Josh Suereth** 38:38 Do you want to.
**Jeremy Blythe** 38:39 There should be another reefer?
**Josh Suereth** 38:41 Yeah, I feel like we can make it be another repo, and it's fine. Like, we could go one of two routes, and we could have it embedded in Weaver, but I…
I feel like that sometimes is awkward, like, having it be a separate project that's standalone, that you can just consume and use. We have… we have other examples where some example projects are repositories. I think if we look…
I don't want to do this on camera, but if I look in OpenTelemetry, I'll find one and send you an example. So…
Yeah, OpenTelemetry has 97 repositories, for example.
And, yeah, there's an OpenTelemetry Java example. Yeah, like here.
But this is just a bunch of examples for Java.
**Jeremy Blythe** 39:24 Yeah.
**Josh Suereth** 39:26 So, I feel like we could do the same, and, like, if you wanted to, you could initiate a donation proposal to CNCF, or to OpenTelemetry, of like, I want to donate this example repo.
It's basically, you know, for Weaver, it's like the Java one. I would sponsor that, and then we can just, like, create a repo, like.
literally create a repo that is just a fork of yours, or merge your repo into the OpenTelemetry org, and make sure all the Code of Conduct stuff is added and all that kind of crap.
But I'd rather just use yours directly and give it a… give it a first-class name, you know what I mean?
**Jeremy Blythe** 40:05 Well, that's only what… what I'm thinking of doing is, like, I'm doing a bunch of stuff for this CNCF talk.
In the conference at the beginning of November.
**Josh Suereth** 40:15 Yes.
**Jeremy Blythe** 40:16 And so I'm adding a whole bunch of stuff to do with live check.
which I'm doing in…
it's… we're actually using it in a real project at my company, and so I'm going to be showing that in the talk. But what I want to do is extract from that, like, a bunch of stuff that we've done, and put it into that Weaver example, so I was planning to do that. So maybe once I've got that in there, that can tie into all of this.
And then that would be a good contribution at that point.
**Josh Suereth** 40:43 Yeah, that sounds good. So, you're gonna keep working on it locally for your talk, and then post your talk, we can contribute it into the OpenTelemetry project and keep it up to date that way.
**Jeremy Blythe** 40:53 I…
**Josh Suereth** 40:54 I like it.
**Jeremy Blythe** 40:55 Maybe… maybe just before… See you on the timing. Like, that's what I've been working on.
Well, so these donation requests can take a long time, so don't, don't…
**Josh Suereth** 41:09 I mean, they don't have to, but, like, don't expect it to be done for your talk.
**Jeremy Blythe** 41:13 Okay.
Maybe I should look at it fairly soon, then. Donation… What is it? Donation request.
I'll have to move that up.
**Josh Suereth** 41:22 Yeah, there's a donation request where you can say, hey, I want to donate this.
**Jeremy Blythe** 41:25 Okay.
**Josh Suereth** 41:27 And you can… you can, like, add me on the thing and say, like, we talked about it in the SIG, about how we need a… we want an example repo. Yours is the canonical repo we want to use anyway, so let's just have it in OpenTelemetry so it's the official one.
**Jeremy Blythe** 41:42 The only thing I want to make sure we do is, I find that
Examples are great, until the example becomes, like, this, like, giant thing.
And then the example is something really difficult to follow. Like, there's a thing called the OpenTelemetry Demo.
Which is the repo, which is, like, this giant thing that's Kubernetes and everything.
I look at that and go, I don't want to settle that up.
So, I think it's important to make sure that you've got, you know.
**Josh Suereth** 42:11 Cool.
**Jeremy Blythe** 42:11 Like, really simple things that don't, like.
**Josh Suereth** 42:15 Yeah.
**Jeremy Blythe** 42:16 You know, you're not met with a wall of text before you can get started.
**Josh Suereth** 42:20 Well, you've seen the job example one. I like how this is done. So everything's in one thing, so there's a ton of crap here, right?
**Jeremy Blythe** 42:27 Hmm.
**Josh Suereth** 42:27 And… and you can be like, oh, this is overwhelming, but what's nice is it says, hey, you have to use this Java, you can build everything at once if you want, but you're interested in SDK auto-configuration. You click on it.
And it's just the auto-config directory is a standalone example. It has a REME that describes what it is, how to use it, that sort of thing. So, like, you… what you built today, we could give it a name and a label of, like, here's how… here's an example of, you know, end-to-end,
Company-specific registry, right?
**Jeremy Blythe** 43:02 Yep.
**Josh Suereth** 43:03 We could have… and then we could have a different directory that is basic… that is, like, you know, pure semantic conventions, or another one that is, you know, metrics only, or Prometheus, or whatever, you know?
**Jeremy Blythe** 43:14 Well, that's why I was thinking… So that was… About this live.
**Josh Suereth** 43:17 Yeah, go ahead.
**Jeremy Blythe** 43:17 The live check stuff is getting really more detailed into, like.
you know, custom REGO policies and things, and I kind of don't want that in the beginner example.
**Josh Suereth** 43:29 Right, right, which we could… we could literally have, like, an example that just says, like, custom, custom, Rego policy, and we have another example that is, like, custom rego live check.
**Jeremy Blythe** 43:40 Yep.
**Josh Suereth** 43:42 So…
**Jeremy Blythe** 43:42 Okay, I'll look at this… maybe we'll model it on this one, if we like this one. Draw, for example.
**Josh Suereth** 43:49 I do. Yeah, yeah. This… this one, I'm a fan of this. We can talk to… you could… you could talk to Trask or, the Laureate or the JavaSig to basically say, hey, how do you feel about this? Is this working well for you? You know, that sort of thing. But I… I personally like this, and I think there's,
You know, it sets a standard for us to model, so…
**Jeremy Blythe** 44:11 Okay.
**Josh Suereth** 44:12 Alright, I'll look at that.
**Jeremy Blythe** 44:14 Alright, with that…
**Josh Suereth** 44:15 I don't have any…
**Jeremy Blythe** 44:16 Love Miller's PR as well.
**Josh Suereth** 44:19 Yes.
**Jeremy Blythe** 44:20 Okay.
**Josh Suereth** 44:24 I think… I think we're good, then, for now. There's a bunch of other things for us to go through, but we have, like, all the…
This is an example of something you were just looking at, you know, anyway.
I think we have a lot to get through, but in terms of what I wanted to get through today, I think we're good.
**Jeremy Blythe** 44:43 Yeah, I feel like we need to get this V2 thing done.
Yeah. There's a lot of these other things, it feels like, well, I don't necessarily want to put the effort into this when it's all going to change again anyway.
So a lot of, like, things like the documentation improvements and stuff like that, I feel like…
Let's war, you know, they're kind of on hold.
**Josh Suereth** 45:06 Yeah, I do… I also think,
half of the things in this backlog will fix with V2. Like, V2 will actually take care of them.
**Jeremy Blythe** 45:18 No.
**Josh Suereth** 45:18 To the point where, like, the motivating reason we wanted some of this craziness, we won't need.
**Jeremy Blythe** 45:23 Some of it…
**Josh Suereth** 45:25 We'll still have to have… we'll still have to have.
Okay, alright, I'm gonna call it there, unless anyone else has something they want to talk about.
**Jeremy Blythe** 45:34 Nope.
**Josh Suereth** 45:36 Cool. Alright.
**Jeremy Blythe** 45:38 See y'all next week. Cheers, bye.
**Josh Suereth** 45:41 Yep.
