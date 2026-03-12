SIG: Service and Deployment SemConv
Date: 2026-02-05
Duration: 16 minutes
============================================================

## Zoom Recording Transcript

**Ayushi Asthana** 04:19 Hello.
I influence…
**Yoshi Yamaguchi** 04:22 A… Hi, Howie, is she?
**Ayushi Asthana** 04:25 I'm good, thank you. So… I'm here to fill in for Janvi. Unfortunately, she won't be able to join us today. I see.
**Yoshi Yamaguchi** 04:34 I see.
**Ayushi Asthana** 04:35 There is a conflict in a calendar.
So… I think, we can talk about the ongoings of last week.
If you have any questions about that. But we generally discussed about the open PRs for service, and some discussion about service.cost center proposal that we were in process of creating.
**Yoshi Yamaguchi** 05:03 Yeah, I… I… because I was pinged on a… CNCF Slack to review the standardization document for, environment.
a label.
So I made… I left some comment, and then I have one question, so… Are… are the… the most of the people Agreeing on standardizing all values for the environment label.
I mean… I mean, this document, the narrative on this doc… I mean… Let me share the document.
**Ayushi Asthana** 05:42 Yeah.
**Yoshi Yamaguchi** 05:44 Yeah, this one.
So, so I'm… Reviewing this, and then it seems like the narrative is to prepare a set of values for the environment label.
And if… Fixed… fixed values for the… Environment label, and then we don't allow the users to set their arbitrary values into that label.
Once we set… once we standardize the… the label.
Is this correct?
**Ayushi Asthana** 06:19 Yeah, I think that was the direction, but the point that you are mentioning, sort of, I kind of anticipate where this is going. There was also some discussion about, what if Users want to name their environment something custom, so it's not always going to be staging fraud, it could also be that they want to name their environments by region, maybe. So there was some discussion around that as well.
I'm sorry, but I'm forgetting if there was a conclusion on that discussion. I remember this point was raised.
But, yeah.
**Yoshi Yamaguchi** 06:55 Yeah, I would love to, emphasize that some companies I know of use… use their, like, arbitrary… arbitrary values for the environment label. Like, so in their case, they… for example, they have, multiple customers.
Of their service. And if they deploy the application or system.
To the… the multiple, so they, they have, they have the system per user.
per customer.
So they prepare one AWS account per customer.
So, even if it's in production.
From their point of view, it means… the production means the account name.
And then they… they have one, central… pipeline.
that… that is in charge of deploying the latest version of application to the respective AWS account from there.
And then, in that case, they put the label Like, they put the value of the account name into the label.
And then they collected the whole telemetry data from respective AWS account into one, telemetry endpoint.
So that they can filter out the telemetry data of specific customers later on.
So, in that case, Each of them are production.
**Ayushi Asthana** 08:36 But still, they need to have some label.
**Yoshi Yamaguchi** 08:39 And then if we force them to, like, change the value name, then they need to rewrite everything, and also there will be some gaps between the existing telemetry data And the… the military data, after we introduced the new, like, new… Standardized version of semantics. So…
**Ayushi Asthana** 09:03 Okay.
**Yoshi Yamaguchi** 09:04 It'll be great if he can have… even if we conclude to set the… fix the value of the environment value.
We'd like to have some, like, migration period for them to prepare for the migration to, like, you know, from existing value to the fixed value we prepare.
So that's the… my comments. Otherwise, it looks really, you know, looks great, so that's the… my… That's… that's my point, yeah.
**Ayushi Asthana** 09:35 Okay, I think I'll bring this up and discuss it, because I am also looking at the current registry, and over there as well, deployment.environment.name is a freeform, like, it's a string, it's a custom string.
**Yoshi Yamaguchi** 09:53 So… Right, right.
**Ayushi Asthana** 09:54 I don't believe we would want to change that when making it stable. That doesn't seem right, in any case. So, okay, I'll bring this up and discuss it, and we can probably talk more about it in the next, session.
their own group.
**Yoshi Yamaguchi** 10:13 You know, so I understand the narrative, and it makes really sense. You know, it makes perfect sense to me. So, my suggestion is to… raise a recommendation to the communities that, you know, OpenTementry recommends this set of values for this label, and then… like, other, like, the vendors, cloud providers or SaaS vendors, follow that kind of guidelines. For example, as named here, so Google Cloud and AWS and then, Agile.
Provide the values based on the suggested, recommended values.
**Ayushi Asthana** 10:53 Right.
**Yoshi Yamaguchi** 10:54 And then also, the SaaS vendors treat those You know… Recommended values, you know, to the… Well, I…
**Ayushi Asthana** 11:05 Like, functionality on top of it.
**Yoshi Yamaguchi** 11:07 Yeah, yeah, yeah. But still, like, they support… they support those values for a certain period, and then that would be… Yeah, that'd be better, I guess.
**Ayushi Asthana** 11:16 That makes sense. I believe you've already added a comment, so I will bring this up.
with, Arnav, and we'll work on this. Apart from this, I think we have two more proposals out this.
One is for introducing data entity.
in hotel. That proposal is… I think it's posted on Slack, already.
**Yoshi Yamaguchi** 11:40 Yeah, yeah.
I think it's, it's by the, JP, right?
**Ayushi Asthana** 11:47 Mmm…
**Yoshi Yamaguchi** 11:49 I think… I'm looking… I'm… Business one?
**Ayushi Asthana** 12:00 D… Oh, no, this is for service.oner, I didn't mean that.
**Yoshi Yamaguchi** 12:09 Oh, okay.
**Ayushi Asthana** 12:11 I think the last… Two messages on… Slack, at the moment.
**Yoshi Yamaguchi** 12:18 For service.
Let me see, going back to… Okay, so the one you posted this morning, or… Don't mean nighttime.
**Ayushi Asthana** 12:33 power.
**Yoshi Yamaguchi** 12:34 Yeah, yeah, yeah, yeah.
**Ayushi Asthana** 12:36 So these are the two proposals that are also up for discussion, that would be up for discussion.
**Yoshi Yamaguchi** 12:40 I see.
Yeah, I'd take a look at it, and then… What, what, what?
So, what's… what are the discussion points that I need to take a deeper look into?
**Ayushi Asthana** 12:54 So, right now, I think folks have not reviewed it, or we have not had a chance to discuss these proposals yet. So, the main, like, discussion points are going to be for introducing service.cost center, what is the recommendation that we have?
And, like, does it make sense? Do we need more data, more research for introducing this? Is, like, the group aligned at cost center?
or business unit, like, which of the two… so there was cost center, and there was also business unit. There were two fields that… roughly did the same thing, so is one better than the other? Like, those will be, like, the broader discussion points, I feel. For data as an entity, the discussion is going to be on… Most likely, the utility of tagging data, or introducing attributes specifically for data, and if there is, like, an actual observability use case for having data as an entity.
I have put in some research for observability platforms, but it is limited to Datadog and Splunk. I need to look at… A few more observability vendors to see what they're doing in security space, because both of the use cases of data are security and management.
So… There is also that. So the general direction of research, and if this makes sense as a proposal for introducing it in hotel.
**Yoshi Yamaguchi** 14:35 Right.
And then this is not the, the mandatory… mandatory attribute, right? This is… it's optional.
Yes. Optional, yeah, yeah. Then this all… all… all narratives in this document makes total sense.
**Ayushi Asthana** 14:53 Right.
**Yoshi Yamaguchi** 14:54 Yeah, yeah. And also, I'm just asking, I'm just wondering, have we, have we reached out to any FinOps community people for, for this level?
Already?
**Ayushi Asthana** 15:06 I am not aware of that. I think Janvi would be more aware if there's any outreach.
**Yoshi Yamaguchi** 15:10 Can I… can I… can I, can I share, can I share this document with the, the, the community, the Phoenops community I know, in Japan?
**Ayushi Asthana** 15:18 Yeah, totally.
**Yoshi Yamaguchi** 15:19 Yeah, you should do.
**Ayushi Asthana** 15:20 This is a public document, so yeah, surely I am.
**Yoshi Yamaguchi** 15:24 Awesome, awesome.
**Ayushi Asthana** 15:29 So, I'll note down the point that you'd shared about, Making the, deployment attribute… environment attribute.
**Yoshi Yamaguchi** 15:41 Yeah, yeah, yeah.
**Ayushi Asthana** 15:45 And…
**Yoshi Yamaguchi** 15:46 Thank you so much.
**Ayushi Asthana** 15:47 Pass this next time.
I'll add it in the notes. I think… I don't have any more discussion points, is there anything else we'd want to talk about?
**Yoshi Yamaguchi** 15:58 I see. Then I'll take a look at these documents this afternoon, and then we'll leave the comments if there are…
**Ayushi Asthana** 16:06 Yeah, sure.
**Yoshi Yamaguchi** 16:07 Yep, cool, cool.
**Ayushi Asthana** 16:09 Thank you!
Nice job.
**Yoshi Yamaguchi** 16:11 Thank you, alright, likewise, see you soon.
**Ayushi Asthana** 16:15 Yep, bye.
**Yoshi Yamaguchi** 16:17 by…
