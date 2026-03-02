SIG: Semantic Convention SIG
Date: 2025-10-13
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 02:01 It looks like Josh won't be able to make it.
He seems to have caught the cold.
**Michele Mancioppi** 02:09 Oh.
I was hoping to see the second round of The discussion about… Embedding.
Manage spaces.
**Trask** 02:29 Hey folks, I haven't quite made it to my desk, if no one else can…
share and drive the meeting I can in… 2 minutes.
**Armin (Dynatrace)** 02:47 I'll quickly prepare the agenda in the meantime.
Mikhaleb, are you referring to some topic that should have been on the agenda already?
**Michele Mancioppi** 03:18 Next week, there was a discussion, led by, Josh.
about something that I brought in the time before.
**Armin (Dynatrace)** 03:29 Yo.
respect that one.
**Michele Mancioppi** 03:31 Yep.
I watched the recording, my feeling was that it was not conclusive as a discussion, and
I did not have a solid understanding of What would happen next?
**Armin (Dynatrace)** 03:56 I guess if you want to continue the discussion with Josh, you'll probably have to wait for next week, then.
**Michele Mancioppi** 04:03 No.
I don't know if it's only a discussion with Josh, because it sounds like the way the discussion went about embending game spaces
Is that it is a much bigger thing.
**Trask Stalnaker** 05:17 Alright… oh, that's the wrong camera, that's not useful at all.
Sorry, folks, just barely getting to my desk this morning.
Alright, let me pull up the meeting… Notice.
Yeah, Michelle, I… I watched the meeting, from last week, because I was interested in the peer service discussion.
I…
Don't think it… I don't… my personal opinion, and yes, it would be great to have Josh here, I don't think it should… I don't think anything should be blocked on the embedding concept.
Because that is something we can overlay later.
We can… Embed, we can take… we can explicitly embed things today.
And… Evolve to automate that.
You know, more formally later.
But…
That is my personal opinion. Sorry, I know we're bouncing you back and forth between Josh wasn't here the two weeks before, and then you're getting different opinions.
**Michele Mancioppi** 07:05 I miss one, one meeting and all the fun has already taken place.
**Trask Stalnaker** 07:10 The… Also, I understand Josh's concern in general with peer service.
But I know from Java instrumentation… Java instrumentation users that That is something that they…
That is used out in the world?
So, I don't know what… Maybe it should be…
called something different, but I feel like that concept does…
Is important to a certain subset of users.
And so, it makes sense.
To me, but I'm not sure if we'll have anything to discuss.
This week, without Josh.
**Michele Mancioppi** 08:00 Alright, then, I'll see you next week, folks.
**Trask Stalnaker** 08:04 Sorry about that.
**Michele Mancioppi** 08:06 Oh, good. Bye.
**Trask Stalnaker** 08:23 Alright, let's start with the board.
Ready to be merged.
Oh, I'm not sharing.
I'm sorry.
Clearly not awake yet.
Bye.
No, that… Doesn't look like I shared the right thing at all.
So, I know Josh has… Marked it… Ready… Royal… There was some…
questions here, so I think I'm not going to merge this.
Nice off.
Need more approvals… blocked.
I guess it's until, we roll out Yao's new triage.
workflows, it's really hard to tell. These are probably the same things that I've been blocked.
For a while… Needs more approvals…
Oh, this is Yao's… Workflows…
Okay.
I… We'll try to get to review that tomorrow. I'm going to be out.
Hmm… second half of today… Yeah, let's just go to topics, if there's anything that we…
Can discuss today.
There's no name on this…
**James Thompson** 11:52 That was me.
**Trask Stalnaker** 12:01 Oh, yikes, 222 files. Reordering columns, I see what you're… Yes, it's just a lot of automated…
**James Thompson** 12:09 Yep.
**Trask Stalnaker** 12:11 Can… let's see, okay, so if I filter by YAML, that would be the way to review this.
**James Thompson** 12:20 There was no changes to the YAML.
**Trask Stalnaker** 12:23 Oh, the… ginja. Got it.
Okay, maybe it's easiest to look at an example of the difference.
**James Thompson** 12:54 Yeah, and also in the conversation… in the summary, I listed out all the changes.
**Trask Stalnaker** 13:00 Great.
Okay, I still think, probably… Looking at…
**James Thompson** 13:31 So, look at something like CICD metrics, for example.
**Trask Stalnaker** 13:35 Okay.
I'm on GitHub.
What's that? Oh, that's a user error, okay.
So… I'm going to view this file…
Okay, so we've got…
**James Thompson** 14:18 Right there, that summarizes the changes, you can see.
**Trask Stalnaker** 14:33 So… The difference here… I see. We've got attributes here, okay.
We've got stability… Move to the front.
Description, examples, description… okay, description has been renamed to Summary.
**James Thompson** 15:08 Yep, because when we look at it, it's actually the brief.
**Trask Stalnaker** 15:25 Requirement level, okay, facility requirement level… Value… Type… summary… Example values.
Okay.
Seems… Very… Reasonable to me… Nice.
Alright, just summarize for… Other folks, possibly…
Okay, what else should, any other changes?
**James Thompson** 17:59 That was it.
**Trask Stalnaker** 18:01 Okay, so only on the… Oh, this is a general attribute.
This, so this would be on not just metrics, but spans, anywhere there, attributes. Correct. Okay.
**James Thompson** 18:13 Yep.
**Trask Stalnaker** 18:27 Cool.
**James Thompson** 18:30 Yeah, obviously I'll rebase it.
later on, once it's… Yeah. Because otherwise, it's going to be constantly being rebased, merged, like…
**Trask Stalnaker** 18:41 Yeah, with 222 files, yes, yes.
Yeah, it doesn't need to be rebased to review it.
**James Thompson** 18:50 Yep.
**Trask Stalnaker** 18:52 Okay, let's see which flows into this one.
**James Thompson** 18:59 Yep.
**Trask Stalnaker** 18:59 Thanks.
So… This spring… okay, let's look at an example here.
**James Thompson** 19:15 Nope.
Even if you just look at the… yes, so…
Just open one of the files.
It's purely been a ginger change.
Alright, so you have your standard attribute tables, which haven't been touched.
But when you look at the deprecated tables, they've been… The layout's been tweaked.
Right?
**Trask Stalnaker** 19:53 So what happened? Oh, I see, got it. So this was… .
**James Thompson** 19:58 So, if you look at the… probably the Android file's the best file to look at.
**Trask Stalnaker** 20:07 Android, you said?
**James Thompson** 20:10 Yep.
Yep, so you've opened that file.
Just preview that file.
**Trask Stalnaker** 20:23 So does… so it's now, the collapsing is new?
**James Thompson** 20:28 Alright, yeah, so there's now a deprecated attributes group. So, in the previous PR, you have the attributes group.
Alright, you've got the attributes table.
Right? Now you'd have a deprecated attributes table below that.
**Trask Stalnaker** 20:45 Okay…
**James Thompson** 20:46 And the deprecate attributes has less columns, because they're not relevant.
**Trask Stalnaker** 20:51 Right, sure.
So… We had a… what I'm trying to understand is, there was some kind of deprecated… Attributes listing already.
**James Thompson** 21:07 Yeah, so previously what there was…
was there's a totally separate Markdown file Right.
for that active group I've deprecated.
Here, I actually just look at the status and group it based on the status.
Alright, and… so, if they're in separate files, then that's still fine.
or if it's in the same file and you're just updating the status, it's fine as well. It's…
Grouped out to deprecated.
**Trask Stalnaker** 21:43 Sorry, I'm a little slow this morning. So… This is before we had…
We had deprecated split out already.
**James Thompson** 21:54 Yeah, alright, because that's in a separate Markdown file.
Right? But it uses the same layout as a non-deprecated…
Sorry, it's in a separate YAML file.
**Trask Stalnaker** 22:08 Okay, and how do we even spec… like, is this auto-generated? Yes. Is this auto-generated?
Okay, and this is looking… at the…
So the ginja… are there ginja changes here? Yep.
**James Thompson** 22:26 Yep, so effectively, it… when it renders that table of attributes, it first splits it. Is it deprecated, or is it not deprecated?
It renders the… Deprecated first, and then it renders the… it renders the non-deprecated first.
And then it renders the deprecated with a slightly different layout to the table structure.
**Trask Stalnaker** 22:50 Oh, I see what you've done. Okay, so you've… this would… if… this would end up being the way it's… like, this is for now just a sample for one of them, but all of them would be…
We would remove the red, just the deprecated, the separate deprecated YAML.
**James Thompson** 23:08 Yep, we could go through and remove that, and just put deprecate on it.
And that way, we get the automatic grouping and all that as well.
**Trask Stalnaker** 23:17 Okay.
Got.
**James Thompson** 23:21 And also, when the deprecreator rendered, it has slightly different columns.
**Trask Stalnaker** 23:30 Right, right.
I mean, we could do the different rendering without…
**James Thompson** 23:40 Correct. Combined. And that's already there as well. The different renderings there already as well?
**Trask Stalnaker** 23:46 Okay.
separate.
I just want to call this one out,
Okay, I understand.
Yeah.
**James Thompson** 24:36 So the big thing for me was changing the rendering of the deprecated attributes.
**Trask Stalnaker** 24:43 Okay, I would suggest doing that separately, then, because I think the, combining the two YAMLs into one YAML is going to be, more controversial.
**James Thompson** 24:58 Change.
**Trask Stalnaker** 25:01 But I think that, you know, rendering them Better.
It makes…
**James Thompson** 25:08 And what I realized just before was that the link wasn't there for the deprecated ones, so I'll put that back. I don't know how that got lost.
But, so, when you see the deprecated, where it says use X attribute instead, that can actually link to the new attribute.
**Trask Stalnaker** 25:27 Hot.
Cool. Yeah, yeah.
**James Thompson** 25:29 Right, because we're now actually using that rename to property to get that name of the property, so we know it's an attribute name.
**Trask Stalnaker** 25:38 Yeah.
I'm not sure what I feel about the collapsing. This is new, right? In your…
**James Thompson** 25:44 I've put it as a collapsible because the feedback previously was, we don't want people to be looking at the deprecated all the time.
Right? We want the… So it doesn't add to the clutter of the page?
Right? But if you want to be able to see the past attributes, you can expand it out.
**Trask Stalnaker** 26:03 Yeah, so, to me, that, when we were discussing that.
I thought we were talking about, the… pages,
The semantic convention pages, not the non-registry pages.
**James Thompson** 26:23 At the moment, it's consistent across both.
**Trask Stalnaker** 26:26 Oh, do we… what do we do for defecated?
**James Thompson** 26:31 Apparently, we're removing… we just dropped the attributes off them, totally. See?
Which…
**Trask Stalnaker** 26:37 Yeah, which is what I… I mean, like, I think that was the more or less consensus on that we liked these pages not to be cluttered by deprecated things.
But I think with the registry, it's okay to clutter it with the deprecated things.
**James Thompson** 26:56 Yeah, yes, so I can automatically have the registry as automatically expanded already.
But that's… That's easy to do.
**Trask Stalnaker** 27:06 Okay.
**James Thompson** 27:07 Alright?
Right, because also… but if you were to render a deprecate attribute on a signal, it could automatically be collapsed.
That solution already works.
**Trask Stalnaker** 27:23 Alright, anything else folks wanted to chat about today?
Otherwise… Had a light… Attendance and light topics.
Alright.
See y'all.
**Armin (Dynatrace)** 27:48 See you.
