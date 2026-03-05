SIG: Service and Deployment SemConv
Date: 2026-03-05
Duration: 19 minutes
Zoom Recording URL: https://zoom.us/rec/share/459TRsaSJML-ARI7hQZyhFR98FRh6yNBlYkoiqEBIH0Z-2IxChTfTUhL0A81SOTV.yzDustkDanefjoJ2
============================================================

## Zoom Recording Transcript

**Ayushi Asthana** 03:55 Hello.
**Yoshi Yamaguchi** 03:59 Hello.
How are you?
**Ayushi Asthana** 04:01 Hey, I'm good. Thanks, how are you?
**Yoshi Yamaguchi** 04:05 Yeah, I'm good. Sorry for being late.
**Ayushi Asthana** 04:08 What is… I think we also have Arnav with us today.
**Arnav Bansal** 04:14 And… Oh.
**Ayushi Asthana** 04:18 Okay?
**Yoshi Yamaguchi** 04:20 Yep.
**Ayushi Asthana** 04:21 I think there is two items on the agenda, this time around.
So, Arnak, would you like to discuss, yours first?
**Arnav Bansal** 04:35 Yeah, I think, in the last meet, we discussed that, we needed two separate pairs for, adding enum values, and,
stabilizing, the attribute. So, I've just, like, added the links to the PPS.
And, yeah, I think, maybe you guys can take a look.
**Ayushi Asthana** 05:04 Yoshi, I do recall you had some concerns about the enum. Were they resolved, and was that.
**Arnav Bansal** 05:09 Oh, yes. Yes, yes, I think in the last… Sorry, Yoshi, go ahead.
**Yoshi Yamaguchi** 05:13 I'm reading… I'm reading through the, the pull request.
for the… for the change, I mean, for the change for, a deployment environment name, and then I find some…
I find this sentence that's, that's saying.
Deployment environment name has the following list of well-known values. If one of them applies, then the respective value must be used. Otherwise, a custom value may be used.
So, yeah, I think this is… my opinion is… is…
**Ayushi Asthana** 05:51 hybrid.
**Yoshi Yamaguchi** 05:51 Accepted.
**Ayushi Asthana** 05:53 In, in.
**Yoshi Yamaguchi** 05:56 Yeah, in the proposal.
**Arnav Bansal** 06:00 Yes, yes, yes, Yoshi. I just saw your comment, and yeah. We discussed this in the last segment also, and we have added, these enum values.
**Yoshi Yamaguchi** 06:11 Awesome.
**Arnav Bansal** 06:12 Nope.
**Yoshi Yamaguchi** 06:13 Cop.
**Ayushi Asthana** 06:16 Okay, apart from that, I think we reviewed
the data entity proposal in the last meeting, last SIG meeting.
And, right now, there is a dock that is up.
that talks about, why we need, data as an entity in hotel. There were some questions in the last SIG meeting around, basically.
instrumentation of this entity and how this would look like in hotel. Also about the naming.
So, would it be data, or would it be data source?
So, there is some open questions right now. I would also request you, Yoshi, to review it offline. We can also discuss it right now, if needed, the approach. But basically, I would request your review as well on what we are trying to do with introducing this new entity.
**Yoshi Yamaguchi** 07:16 I see. I see.
**Ayushi Asthana** 07:19 So, I'll let me… Yeah, let me…
**Yoshi Yamaguchi** 07:22 And also, to…
**Ayushi Asthana** 07:23 Yep, sure, go ahead, sorry.
**Yoshi Yamaguchi** 07:25 I'm sorry, see, it looks like…
Okay, I see, I see. Yeah, because it looks like… The… The label, the entity, It's…
It's really relevant to the data platform, like…
Databricks, and then Snowflake, and so on.
And I was just wondering if we have reached out to those data…
Like, data lake or data platform companies for the reviews.
**Ayushi Asthana** 08:11 I don't think we've done that yet.
**Yoshi Yamaguchi** 08:14 Okay, yeah, because, if… so if it's okay that I can reach out to them, if they're interested in stabilizing this entity.
**Ayushi Asthana** 08:25 Okay.
**Yoshi Yamaguchi** 08:25 Well, because this… this is… this… this entry is really relevant to their business.
So…
And I just wondered. I'm not… I'm not, you know, accusing you, but I just… I just wondered if…
Yeah, if… if it's possible, like, if it's okay for me to, like, reach out to them
on my end.
**Ayushi Asthana** 08:46 Yeah, yeah, I think that would be helpful as well for them to have, like, put in their perspective on the utility.
And use cases that we have highlighted over here. So, I think, like, I have not covered the entire breadth of use cases that are possible. This is just some of them that I could think of from, like, a cloud platform versus observability perspective.
But they can provide a fresh perspective on what use cases are possible if this entity exists. So that would be very helpful, in fact.
**Yoshi Yamaguchi** 09:17 Okay, great.
**Ayushi Asthana** 09:20 So, yeah, that is, I think, the entire… so if there is… is there, like, a channel in, the CNCF workspace where we can post this,
Proposal to get the relevant reviews, or will you be reaching out to your contacts?
**Yoshi Yamaguchi** 09:38 So I'm… I… because, you know, the Japanese developer community is really small, and then I know a couple of folks who work for those companies, so I thought, you know, I can reach out to them
you know, in my channel, like, the expo… yeah. But, if you want me to post…
this kind of topics, I mean, this kind of communication in the official Slack, then I'd ask them to join.
the Slack channel.
**Ayushi Asthana** 10:09 I'm good either way, yeah, I'm good either way. I was just wondering if there exists a channel in CNCF right now that is, like, a platform for these discussions, but I'm good either way. I think there was some discussion to also propose it in the entities group.
In the entities SIG, so I will, like, work on refining the feedback that I've got from the last SIG meeting and this SIG meeting, and then we will probably propose it in the entities group as well for their feedback.
**Yoshi Yamaguchi** 10:44 I see.
Yeah, sounds good.
**Ayushi Asthana** 10:49 Cool.
So I think those were the two major items that were discussed last time around. Amikit is not here, but we do have proposals for business unit as well.
Just…
This is the PR, or business unit ID.
Not sure if you have already taken a look at it or not.
and…
Same for cost center ID as well. Like, both of those PRs are already raised in.
**Yoshi Yamaguchi** 11:42 Yeah, I have looked at it, and I'm totally supportive towards this direction.
**Ayushi Asthana** 11:48 Got it.
**Yoshi Yamaguchi** 11:49 Yeah.
So this is… this is different from the… the service owner or service groups, right? So this is the business unit, so that's… that should be, like.
I'm not sure who uses this, but I understand the intention for this proposal. So, say, for example, there are a couple of teams who develop on specific services.
To… that consists of, like, multiple… multiple microservices.
And then… all of those small teams are… if all of those
Small teams are under the one business unit, then
That business unit name should be
The value for this label, right?
**Ayushi Asthana** 12:36 Right. I think that, that is, that is the larger intent for business unit being separate from, like, service owner.
**Yoshi Yamaguchi** 12:43 Cool. Yeah.
Yeah, well, yeah, so, if I, if I, if I were a user.
then I will do that on the client side, I mean…
I don't put the business unit into… as a label for the metrics, and then I just do the query. I just do the aggregation on the query.
On the timing of quitting the data.
Because it reduces the dimensions, but still, it's all up to the user, so it's… I… I… I thought it's…
It's okay to standardize this kind of label on our side.
So, yeah, but I'm not… so in that… so, with that context, I'm not against setting this…
Label as a standard of the open telemetry.
So, yeah, that's my standpoint.
**Ayushi Asthana** 13:41 That's great, then I think you can plus one on the proposal itself.
**Yoshi Yamaguchi** 13:46 Oh, yeah.
**Ayushi Asthana** 13:46 That's needed. But, yeah, I think then… I think that was all of the topics that we had for last time, from our side for discussion.
**Yoshi Yamaguchi** 13:57 It's pretty much straightforward.
Cool.
And also, I know that, Cloud Next is approaching, so, your team or… or, like, product teams are so busy with releasing the new features by then, so,
Yeah. Good luck.
**Ayushi Asthana** 14:19 Thank you, thank you so much. Yeah, yeah.
Cool, okay, I think… and then that's it. Anav, did you have anything else?
**Yoshi Yamaguchi** 14:27 Not much. Yeah, not much.
**Ayushi Asthana** 14:31 Okay, cool. I think then you can wrap up.
**Yoshi Yamaguchi** 14:34 All right.
**Ayushi Asthana** 14:35 Thank you.
**Yoshi Yamaguchi** 14:36 Thanks, buddy.
Have a good day! Bye!
**Arnav Bansal** 14:39 Thanks, buddy.
**Yoshi Yamaguchi** 14:40 Right.
